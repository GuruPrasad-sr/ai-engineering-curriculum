"""LLM-as-Judge evaluator.

Uses a language model to evaluate responses against configurable rubrics.
Supports pointwise scoring (rate a single response) and pairwise comparison
(which of two responses is better).
"""

from __future__ import annotations

import json
import time
from typing import Any

from openai import AsyncOpenAI

from .base import BaseEvaluator, EvalContext, EvalResult


DEFAULT_POINTWISE_TEMPLATE = """You are an expert evaluator. Score the following response on a scale of 1 to 5.

## Evaluation Criteria
{criteria}

## Input
{prompt}

## Response to Evaluate
{response}

{reference_section}

## Instructions
Evaluate the response on each dimension listed below. For each dimension, provide:
1. A score from 1 (worst) to 5 (best)
2. A brief explanation

Then provide an overall score from 1 to 5.

## Dimensions to Evaluate
{dimensions}

Respond in this exact JSON format:
{{
  "dimensions": {{
    "<dimension_name>": {{"score": <1-5>, "explanation": "<brief explanation>"}},
    ...
  }},
  "overall_score": <1-5>,
  "overall_explanation": "<1-2 sentence summary>"
}}"""


DEFAULT_PAIRWISE_TEMPLATE = """You are an expert evaluator. Compare the following two responses and determine which is better.

## Evaluation Criteria
{criteria}

## Input
{prompt}

## Response A
{response_a}

## Response B
{response_b}

## Instructions
Compare the two responses on these dimensions: {dimensions}

Respond in this exact JSON format:
{{
  "winner": "A" | "B" | "tie",
  "explanation": "<1-2 sentence explanation>",
  "dimension_comparisons": {{
    "<dimension>": {{"winner": "A" | "B" | "tie", "explanation": "<brief>"}}
  }}
}}"""


class LLMJudgeEvaluator(BaseEvaluator):
    """Evaluator that uses an LLM as a judge.

    Supports two modes:
    - pointwise: Score a single response on configured dimensions
    - pairwise: Compare two responses

    Args:
        model: The judge model to use (default: gpt-4o-mini).
        criteria: The evaluation criteria description.
        dimensions: List of dimensions to evaluate on.
        prompt_template: Custom judge prompt template (optional).
        mode: "pointwise" or "pairwise".
        threshold: Minimum normalized score to pass (0.0–1.0).
    """

    name = "llm_judge"
    description = "Uses an LLM to judge response quality on configurable dimensions"

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        criteria: str = "Evaluate the response for accuracy, completeness, and helpfulness.",
        dimensions: list[str] | None = None,
        prompt_template: str | None = None,
        mode: str = "pointwise",
        threshold: float = 0.6,
        **kwargs: Any,
    ) -> None:
        super().__init__(threshold=threshold, **kwargs)
        self.model = model
        self.criteria = criteria
        self.dimensions = dimensions or ["accuracy", "completeness", "helpfulness"]
        self.supported_dimensions = self.dimensions
        self.prompt_template = prompt_template or DEFAULT_POINTWISE_TEMPLATE
        self.pairwise_template = DEFAULT_PAIRWISE_TEMPLATE
        self.mode = mode
        self._client = AsyncOpenAI()

    async def evaluate(self, context: EvalContext) -> EvalResult:
        """Run LLM judge evaluation."""
        if self.mode == "pairwise":
            return await self._evaluate_pairwise(context)
        return await self._evaluate_pointwise(context)

    async def _evaluate_pointwise(self, context: EvalContext) -> EvalResult:
        """Score a single response using the LLM judge."""
        prompt_text = context.prompt if isinstance(context.prompt, str) else json.dumps(context.prompt)

        reference_section = ""
        if context.reference:
            reference_section = f"## Reference Answer\n{context.reference}"

        judge_prompt = self.prompt_template.format(
            criteria=self.criteria,
            prompt=prompt_text,
            response=context.response,
            reference_section=reference_section,
            dimensions=", ".join(self.dimensions),
        )

        start = time.perf_counter()
        try:
            completion = await self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": judge_prompt}],
                temperature=0.0,
                response_format={"type": "json_object"},
            )
        except Exception as e:
            return self._make_error(f"LLM API call failed: {e}")

        latency_ms = (time.perf_counter() - start) * 1000
        tokens_used = completion.usage.total_tokens if completion.usage else 0

        raw = completion.choices[0].message.content or "{}"
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            return self._make_error(f"Failed to parse judge response as JSON: {raw[:200]}")

        return self._parse_pointwise_result(parsed, latency_ms, tokens_used)

    def _parse_pointwise_result(
        self, parsed: dict[str, Any], latency_ms: float, tokens_used: int
    ) -> EvalResult:
        """Parse the structured judge output into an EvalResult."""
        overall_score_raw = parsed.get("overall_score", 3)
        overall_score = (float(overall_score_raw) - 1) / 4  # Normalize 1-5 to 0-1

        dimensions: dict[str, float] = {}
        dim_data = parsed.get("dimensions", {})
        for dim_name, dim_info in dim_data.items():
            if isinstance(dim_info, dict) and "score" in dim_info:
                dimensions[dim_name] = (float(dim_info["score"]) - 1) / 4

        explanation = parsed.get("overall_explanation", "")

        return self._make_result(
            score=overall_score,
            explanation=explanation,
            dimensions=dimensions,
            latency_ms=latency_ms,
            tokens_used=tokens_used,
        )

    async def _evaluate_pairwise(self, context: EvalContext) -> EvalResult:
        """Compare the response against the reference (as response B)."""
        if not context.reference:
            return self._make_error("Pairwise evaluation requires a reference response")

        prompt_text = context.prompt if isinstance(context.prompt, str) else json.dumps(context.prompt)

        judge_prompt = self.pairwise_template.format(
            criteria=self.criteria,
            prompt=prompt_text,
            response_a=context.response,
            response_b=context.reference,
            dimensions=", ".join(self.dimensions),
        )

        start = time.perf_counter()
        try:
            completion = await self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": judge_prompt}],
                temperature=0.0,
                response_format={"type": "json_object"},
            )
        except Exception as e:
            return self._make_error(f"LLM API call failed: {e}")

        latency_ms = (time.perf_counter() - start) * 1000
        tokens_used = completion.usage.total_tokens if completion.usage else 0

        raw = completion.choices[0].message.content or "{}"
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            return self._make_error(f"Failed to parse judge response: {raw[:200]}")

        winner = parsed.get("winner", "tie")
        score = {"A": 1.0, "tie": 0.5, "B": 0.0}.get(winner, 0.5)
        explanation = parsed.get("explanation", "")

        return self._make_result(
            score=score,
            explanation=f"Winner: {winner}. {explanation}",
            latency_ms=latency_ms,
            tokens_used=tokens_used,
        )
