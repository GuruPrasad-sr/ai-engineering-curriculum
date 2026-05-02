"""Tests for the LLM Judge evaluator.

These tests verify the evaluator's behavior without making real LLM API calls.
We mock the OpenAI client to return controlled responses.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch
import json
import pytest

from src.evaluators.base import EvalContext
from src.evaluators.llm_judge import LLMJudgeEvaluator


@pytest.fixture
def judge() -> LLMJudgeEvaluator:
    """Create an LLM judge evaluator with default settings."""
    return LLMJudgeEvaluator(
        model="gpt-4o-mini",
        dimensions=["accuracy", "completeness"],
        threshold=0.6,
    )


@pytest.fixture
def simple_context() -> EvalContext:
    """A simple evaluation context for testing."""
    return EvalContext(
        prompt="What is the capital of France?",
        response="The capital of France is Paris.",
        reference="Paris",
    )


def _mock_completion(content: str, tokens: int = 100) -> MagicMock:
    """Create a mock OpenAI completion response."""
    mock = MagicMock()
    mock.choices = [MagicMock()]
    mock.choices[0].message.content = content
    mock.usage = MagicMock()
    mock.usage.total_tokens = tokens
    return mock


class TestLLMJudgePointwise:
    """Tests for pointwise evaluation mode."""

    @pytest.mark.asyncio
    async def test_high_score_response(self, judge: LLMJudgeEvaluator, simple_context: EvalContext) -> None:
        """A correct response should receive a high score."""
        mock_response = json.dumps({
            "dimensions": {
                "accuracy": {"score": 5, "explanation": "Correct answer"},
                "completeness": {"score": 4, "explanation": "Concise but complete"},
            },
            "overall_score": 5,
            "overall_explanation": "Accurate and complete response.",
        })

        with patch.object(judge._client.chat.completions, "create", new_callable=AsyncMock) as mock_create:
            mock_create.return_value = _mock_completion(mock_response)
            result = await judge.evaluate(simple_context)

        assert result.score is not None
        assert result.score == 1.0  # (5-1)/4 = 1.0
        assert result.passed is True
        assert result.error is None
        assert "accuracy" in result.dimensions
        assert "completeness" in result.dimensions

    @pytest.mark.asyncio
    async def test_low_score_response(self, judge: LLMJudgeEvaluator) -> None:
        """An incorrect response should receive a low score."""
        context = EvalContext(
            prompt="What is the capital of France?",
            response="The capital of France is Berlin.",
            reference="Paris",
        )

        mock_response = json.dumps({
            "dimensions": {
                "accuracy": {"score": 1, "explanation": "Incorrect — Paris, not Berlin"},
                "completeness": {"score": 3, "explanation": "Response is complete but wrong"},
            },
            "overall_score": 1,
            "overall_explanation": "Factually incorrect.",
        })

        with patch.object(judge._client.chat.completions, "create", new_callable=AsyncMock) as mock_create:
            mock_create.return_value = _mock_completion(mock_response)
            result = await judge.evaluate(context)

        assert result.score is not None
        assert result.score == 0.0  # (1-1)/4 = 0.0
        assert result.passed is False

    @pytest.mark.asyncio
    async def test_mid_score_normalization(self, judge: LLMJudgeEvaluator, simple_context: EvalContext) -> None:
        """Score normalization from 1-5 scale to 0-1 should be correct."""
        mock_response = json.dumps({
            "dimensions": {},
            "overall_score": 3,
            "overall_explanation": "Average response.",
        })

        with patch.object(judge._client.chat.completions, "create", new_callable=AsyncMock) as mock_create:
            mock_create.return_value = _mock_completion(mock_response)
            result = await judge.evaluate(simple_context)

        assert result.score == pytest.approx(0.5, abs=0.01)  # (3-1)/4 = 0.5

    @pytest.mark.asyncio
    async def test_api_failure_returns_error(self, judge: LLMJudgeEvaluator, simple_context: EvalContext) -> None:
        """API failures should produce an error result, not raise exceptions."""
        with patch.object(judge._client.chat.completions, "create", new_callable=AsyncMock) as mock_create:
            mock_create.side_effect = Exception("API rate limit exceeded")
            result = await judge.evaluate(simple_context)

        assert result.score is None
        assert result.passed is None
        assert result.error is not None
        assert "API" in result.error

    @pytest.mark.asyncio
    async def test_malformed_json_returns_error(self, judge: LLMJudgeEvaluator, simple_context: EvalContext) -> None:
        """Malformed JSON from the judge should produce an error result."""
        with patch.object(judge._client.chat.completions, "create", new_callable=AsyncMock) as mock_create:
            mock_create.return_value = _mock_completion("not valid json {{{")
            result = await judge.evaluate(simple_context)

        assert result.error is not None
        assert "JSON" in result.error

    @pytest.mark.asyncio
    async def test_tokens_tracked(self, judge: LLMJudgeEvaluator, simple_context: EvalContext) -> None:
        """Token usage should be recorded in the result."""
        mock_response = json.dumps({
            "dimensions": {},
            "overall_score": 4,
            "overall_explanation": "Good.",
        })

        with patch.object(judge._client.chat.completions, "create", new_callable=AsyncMock) as mock_create:
            mock_create.return_value = _mock_completion(mock_response, tokens=250)
            result = await judge.evaluate(simple_context)

        assert result.tokens_used == 250


class TestLLMJudgePairwise:
    """Tests for pairwise comparison mode."""

    @pytest.fixture
    def pairwise_judge(self) -> LLMJudgeEvaluator:
        return LLMJudgeEvaluator(mode="pairwise", threshold=0.5)

    @pytest.mark.asyncio
    async def test_response_a_wins(self, pairwise_judge: LLMJudgeEvaluator) -> None:
        """When response A wins, score should be 1.0."""
        context = EvalContext(
            prompt="Explain gravity",
            response="Gravity is the force of attraction between objects with mass.",
            reference="Gravity is complicated.",
        )

        mock_response = json.dumps({
            "winner": "A",
            "explanation": "Response A is more informative.",
            "dimension_comparisons": {},
        })

        with patch.object(pairwise_judge._client.chat.completions, "create", new_callable=AsyncMock) as mock_create:
            mock_create.return_value = _mock_completion(mock_response)
            result = await pairwise_judge.evaluate(context)

        assert result.score == 1.0
        assert "Winner: A" in result.explanation

    @pytest.mark.asyncio
    async def test_pairwise_requires_reference(self, pairwise_judge: LLMJudgeEvaluator) -> None:
        """Pairwise mode should error when no reference is provided."""
        context = EvalContext(
            prompt="Explain gravity",
            response="Gravity pulls things down.",
        )

        result = await pairwise_judge.evaluate(context)
        assert result.error is not None
        assert "reference" in result.error.lower()


class TestLLMJudgeConfiguration:
    """Tests for evaluator configuration."""

    def test_default_dimensions(self) -> None:
        judge = LLMJudgeEvaluator()
        assert "accuracy" in judge.dimensions
        assert "completeness" in judge.dimensions
        assert "helpfulness" in judge.dimensions

    def test_custom_dimensions(self) -> None:
        judge = LLMJudgeEvaluator(dimensions=["tone", "brevity"])
        assert judge.dimensions == ["tone", "brevity"]

    def test_evaluator_name(self) -> None:
        judge = LLMJudgeEvaluator()
        assert judge.name == "llm_judge"

    def test_threshold_configuration(self) -> None:
        judge = LLMJudgeEvaluator(threshold=0.9)
        assert judge.threshold == 0.9
