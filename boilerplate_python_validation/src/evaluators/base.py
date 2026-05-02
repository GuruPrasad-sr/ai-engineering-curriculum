"""Base evaluator classes and core data models.

All evaluators inherit from BaseEvaluator. All evaluation results
use the EvalResult model for consistent serialization and aggregation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class EvalContext(BaseModel):
    """Everything an evaluator needs to perform its evaluation.

    Using a context object instead of individual parameters prevents
    interface bloat as we add more evaluation capabilities.
    """

    prompt: str | list[dict[str, str]]
    response: str
    reference: str | None = None
    context_documents: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    expected: dict[str, Any] = Field(default_factory=dict)
    conversation_history: list[dict[str, str]] = Field(default_factory=list)
    tool_calls: list[dict[str, Any]] = Field(default_factory=list)
    available_tools: list[dict[str, Any]] = Field(default_factory=list)


class EvalResult(BaseModel, frozen=True):
    """Immutable result of a single evaluation.

    Scores are normalized to 0.0–1.0. The `dimensions` dict holds
    sub-scores for multi-dimensional evaluation (e.g., correctness=0.9,
    completeness=0.7).
    """

    evaluator: str
    score: float | None = None
    passed: bool | None = None
    explanation: str = ""
    dimensions: dict[str, float] = Field(default_factory=dict)
    error: str | None = None
    latency_ms: float = 0.0
    tokens_used: int = 0
    cost_usd: float = 0.0
    metadata: dict[str, Any] = Field(default_factory=dict)


class TestCase(BaseModel):
    """A single test case loaded from YAML or constructed in Python."""

    name: str
    prompt: str | list[dict[str, str]]
    response: str | None = None
    reference: str | None = None
    context_documents: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    evaluators: list[str] = Field(default_factory=list)
    expected: dict[str, Any] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)

    def to_eval_context(self) -> EvalContext:
        """Convert this test case to an EvalContext for evaluators."""
        return EvalContext(
            prompt=self.prompt,
            response=self.response or "",
            reference=self.reference,
            context_documents=self.context_documents,
            metadata=self.metadata,
            expected=self.expected,
        )


class RunSummary(BaseModel):
    """Aggregated summary of an evaluation run."""

    total_cases: int = 0
    passed: int = 0
    failed: int = 0
    errored: int = 0
    avg_score: float | None = None
    dimension_averages: dict[str, float] = Field(default_factory=dict)
    total_tokens: int = 0
    total_cost_usd: float = 0.0
    duration_seconds: float = 0.0


class EvaluationRun(BaseModel):
    """A complete evaluation run — the top-level result object."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    suite_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    results: list[tuple[str, EvalResult]] = Field(default_factory=list)  # (case_name, result)
    summary: RunSummary = Field(default_factory=RunSummary)
    config: dict[str, Any] = Field(default_factory=dict)

    def compute_summary(self) -> None:
        """Recompute the summary from current results."""
        scores = [r.score for _, r in self.results if r.score is not None]
        all_dims: dict[str, list[float]] = {}
        for _, r in self.results:
            for dim, val in r.dimensions.items():
                all_dims.setdefault(dim, []).append(val)

        self.summary = RunSummary(
            total_cases=len(self.results),
            passed=sum(1 for _, r in self.results if r.passed is True),
            failed=sum(1 for _, r in self.results if r.passed is False),
            errored=sum(1 for _, r in self.results if r.error is not None),
            avg_score=sum(scores) / len(scores) if scores else None,
            dimension_averages={
                dim: sum(vals) / len(vals) for dim, vals in all_dims.items()
            },
            total_tokens=sum(r.tokens_used for _, r in self.results),
            total_cost_usd=sum(r.cost_usd for _, r in self.results),
        )


class BaseEvaluator(ABC):
    """Abstract base class for all evaluators.

    Subclasses must:
    1. Set the `name` class attribute
    2. Implement the `evaluate()` method

    Example:
        class MyEvaluator(BaseEvaluator):
            name = "my_evaluator"

            async def evaluate(self, context: EvalContext) -> EvalResult:
                ...
    """

    name: str = "base"
    description: str = ""
    supported_dimensions: list[str] = []

    def __init__(self, threshold: float = 0.5, **kwargs: Any) -> None:
        self.threshold = threshold
        self.config = kwargs

    @abstractmethod
    async def evaluate(self, context: EvalContext) -> EvalResult:
        """Run evaluation and return a result.

        Args:
            context: The evaluation context containing inputs and expected outputs.

        Returns:
            An immutable EvalResult with score, pass/fail, and explanation.
        """
        ...

    def _make_result(
        self,
        score: float,
        explanation: str,
        dimensions: dict[str, float] | None = None,
        **kwargs: Any,
    ) -> EvalResult:
        """Helper to construct an EvalResult with automatic pass/fail."""
        return EvalResult(
            evaluator=self.name,
            score=score,
            passed=score >= self.threshold,
            explanation=explanation,
            dimensions=dimensions or {},
            **kwargs,
        )

    def _make_error(self, error: str) -> EvalResult:
        """Helper to construct an error result."""
        return EvalResult(
            evaluator=self.name,
            score=None,
            passed=None,
            explanation="",
            error=error,
        )
