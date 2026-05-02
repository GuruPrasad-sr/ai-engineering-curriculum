"""Hallucination detection evaluator.

Three detection strategies:
1. Self-consistency: Ask the same question N times, compare answers
2. Factual grounding: Compare claims against a reference document
3. Claim extraction + verification: Extract individual claims, verify each
"""

from __future__ import annotations

import json
import time
from typing import Any

from openai import AsyncOpenAI

from .base import BaseEvaluator, EvalContext, EvalResult


CLAIM_EXTRACTION_PROMPT = """Extract all factual claims from the following text.
Return a JSON array of strings, each being one atomic factual claim.

Text:
{response}

Respond with only a JSON array:
["claim 1", "claim 2", ...]"""


CLAIM_VERIFICATION_PROMPT = """You are a fact-checker. Determine if the following claim is supported by the reference text.

Claim: {claim}

Reference text:
{reference}

Respond in JSON:
{{
  "supported": true | false,
  "explanation": "<brief explanation>"
}}"""


CONSISTENCY_COMPARISON_PROMPT = """Compare these {n} responses to the same question. Are they consistent with each other?

Question: {prompt}

{responses_section}

Respond in JSON:
{{
  "consistent": true | false,
  "consistency_score": <0.0 to 1.0>,
  "contradictions": ["<contradiction 1>", ...],
  "explanation": "<brief summary>"
}}"""


class HallucinationEvaluator(BaseEvaluator):
    """Detects hallucinations using multiple strategies.

    Args:
        model: LLM model for analysis.
        strategy: "consistency", "grounding", "claims", or "all".
        consistency_samples: Number of times to re-ask for consistency check.
        threshold: Minimum score to pass (0.0–1.0).
    """

    name = "hallucination"
    description = "Detects hallucinations via self-consistency, grounding, and claim verification"
    supported_dimensions = ["consistency", "grounding", "claim_accuracy"]

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        strategy: str = "all",
        consistency_samples: int = 3,
        threshold: float = 0.7,
        **kwargs: Any,
    ) -> None:
        super().__init__(threshold=threshold, **kwargs)
        self.model = model
        self.strategy = strategy
        self.consistency_samples = consistency_samples
        self._client = AsyncOpenAI()

    async def evaluate(self, context: EvalContext) -> EvalResult:
        """Run hallucination detection using configured strategies."""
        start = time.perf_counter()
        dimensions: dict[str, float] = {}
        explanations: list[str] = []
        total_tokens = 0
        errors: list[str] = []

        strategies = (
            ["consistency", "grounding", "claims"]
            if self.strategy == "all"
            else [self.strategy]
        )

        if "consistency" in strategies:
            result = await self._check_consistency(context)
            if result.error:
                errors.append(result.error)
            else:
                dimensions["consistency"] = result.score or 0.0
                explanations.append(f"Consistency: {result.explanation}")
                total_tokens += result.tokens_used

        if "grounding" in strategies and context.reference:
            result = await self._check_grounding(context)
            if result.error:
                errors.append(result.error)
            else:
                dimensions["grounding"] = result.score or 0.0
                explanations.append(f"Grounding: {result.explanation}")
                total_tokens += result.tokens_used

        if "claims" in strategies and context.reference:
            result = await self._check_claims(context)
            if result.error:
                errors.append(result.error)
            else:
                dimensions["claim_accuracy"] = result.score or 0.0
                explanations.append(f"Claims: {result.explanation}")
                total_tokens += result.tokens_used

        if not dimensions:
            error_msg = "; ".join(errors) if errors else "No strategies could be executed"
            return self._make_error(error_msg)

        avg_score = sum(dimensions.values()) / len(dimensions)
        latency_ms = (time.perf_counter() - start) * 1000

        return self._make_result(
            score=avg_score,
            explanation=" | ".join(explanations),
            dimensions=dimensions,
            latency_ms=latency_ms,
            tokens_used=total_tokens,
        )

    async def _check_consistency(self, context: EvalContext) -> EvalResult:
        """Ask the same question N times and compare answers."""
        prompt_text = context.prompt if isinstance(context.prompt, str) else json.dumps(context.prompt)
        total_tokens = 0

        try:
            responses: list[str] = [context.response]
            for _ in range(self.consistency_samples):
                completion = await self._client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt_text}],
                    temperature=0.7,  # Some variation to test consistency
                )
                responses.append(completion.choices[0].message.content or "")
                total_tokens += completion.usage.total_tokens if completion.usage else 0

            # Use LLM to compare responses
            responses_section = "\n".join(
                f"Response {i+1}:\n{r}" for i, r in enumerate(responses)
            )
            comparison_prompt = CONSISTENCY_COMPARISON_PROMPT.format(
                n=len(responses),
                prompt=prompt_text,
                responses_section=responses_section,
            )
            comparison = await self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": comparison_prompt}],
                temperature=0.0,
                response_format={"type": "json_object"},
            )
            total_tokens += comparison.usage.total_tokens if comparison.usage else 0

            parsed = json.loads(comparison.choices[0].message.content or "{}")
            score = float(parsed.get("consistency_score", 0.5))
            explanation = parsed.get("explanation", "")

            return self._make_result(
                score=score, explanation=explanation, tokens_used=total_tokens
            )
        except Exception as e:
            return self._make_error(f"Consistency check failed: {e}")

    async def _check_grounding(self, context: EvalContext) -> EvalResult:
        """Check if the response is grounded in the reference text."""
        if not context.reference:
            return self._make_error("Grounding check requires a reference")

        grounding_prompt = f"""Rate how well the response is grounded in the reference text.
A score of 1.0 means every statement is supported. A score of 0.0 means nothing is supported.

Reference:
{context.reference}

Response:
{context.response}

Respond in JSON:
{{"grounding_score": <0.0-1.0>, "unsupported_statements": ["..."], "explanation": "..."}}"""

        try:
            completion = await self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": grounding_prompt}],
                temperature=0.0,
                response_format={"type": "json_object"},
            )
            tokens = completion.usage.total_tokens if completion.usage else 0
            parsed = json.loads(completion.choices[0].message.content or "{}")
            score = float(parsed.get("grounding_score", 0.5))
            explanation = parsed.get("explanation", "")

            return self._make_result(
                score=score, explanation=explanation, tokens_used=tokens
            )
        except Exception as e:
            return self._make_error(f"Grounding check failed: {e}")

    async def _check_claims(self, context: EvalContext) -> EvalResult:
        """Extract claims from the response and verify each against the reference."""
        if not context.reference:
            return self._make_error("Claim verification requires a reference")

        total_tokens = 0
        try:
            # Step 1: Extract claims
            extract_prompt = CLAIM_EXTRACTION_PROMPT.format(response=context.response)
            extraction = await self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": extract_prompt}],
                temperature=0.0,
            )
            total_tokens += extraction.usage.total_tokens if extraction.usage else 0
            claims = json.loads(extraction.choices[0].message.content or "[]")

            if not claims:
                return self._make_result(
                    score=1.0,
                    explanation="No factual claims found to verify",
                    tokens_used=total_tokens,
                )

            # Step 2: Verify each claim
            supported_count = 0
            unsupported: list[str] = []

            for claim in claims:
                verify_prompt = CLAIM_VERIFICATION_PROMPT.format(
                    claim=claim, reference=context.reference
                )
                verification = await self._client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": verify_prompt}],
                    temperature=0.0,
                    response_format={"type": "json_object"},
                )
                total_tokens += verification.usage.total_tokens if verification.usage else 0
                parsed = json.loads(verification.choices[0].message.content or "{}")

                if parsed.get("supported", False):
                    supported_count += 1
                else:
                    unsupported.append(claim)

            score = supported_count / len(claims)
            explanation = (
                f"{supported_count}/{len(claims)} claims supported."
                + (f" Unsupported: {unsupported}" if unsupported else "")
            )

            return self._make_result(
                score=score, explanation=explanation, tokens_used=total_tokens
            )
        except Exception as e:
            return self._make_error(f"Claim verification failed: {e}")
