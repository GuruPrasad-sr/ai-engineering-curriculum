"""Data models for the AI Evaluation Platform.

Uses Pydantic for API models and provides an async in-memory store
(replace with SQLModel + SQLite/Postgres for persistence).
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


# --- Enums ---

class RunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Severity(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


# --- Core Models ---

class EvaluationMetric(BaseModel):
    """A single metric/dimension score."""
    name: str
    score: float  # 0.0 to 1.0
    explanation: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)


class EvaluationResult(BaseModel):
    """Result of evaluating a single test case with a single evaluator."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    test_case_name: str
    evaluator_name: str
    score: float | None = None
    passed: bool | None = None
    explanation: str = ""
    metrics: list[EvaluationMetric] = Field(default_factory=list)
    error: str | None = None
    latency_ms: float = 0.0
    tokens_used: int = 0
    cost_usd: float = 0.0
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TestCase(BaseModel):
    """A test case definition."""
    name: str
    prompt: str | list[dict[str, str]]
    response: str | None = None
    reference: str | None = None
    evaluators: list[str] = Field(default_factory=list)
    expected: dict[str, Any] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class TestSuite(BaseModel):
    """A collection of test cases."""
    name: str
    description: str = ""
    model: str = "gpt-4o-mini"
    threshold: float = 0.6
    cases: list[TestCase] = Field(default_factory=list)
    evaluators: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


class RunSummary(BaseModel):
    """Aggregated metrics for an evaluation run."""
    total_cases: int = 0
    passed: int = 0
    failed: int = 0
    errored: int = 0
    avg_score: float | None = None
    dimension_averages: dict[str, float] = Field(default_factory=dict)
    total_tokens: int = 0
    total_cost_usd: float = 0.0
    duration_seconds: float = 0.0


class EvaluationRunDB(BaseModel):
    """A complete evaluation run with all results."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    suite_name: str
    status: RunStatus = RunStatus.PENDING
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
    results: list[EvaluationResult] = Field(default_factory=list)
    summary: RunSummary = Field(default_factory=RunSummary)
    config: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None

    def compute_summary(self) -> None:
        """Recompute summary from results."""
        scores = [r.score for r in self.results if r.score is not None]
        all_dims: dict[str, list[float]] = {}
        for r in self.results:
            for m in r.metrics:
                all_dims.setdefault(m.name, []).append(m.score)

        self.summary = RunSummary(
            total_cases=len(self.results),
            passed=sum(1 for r in self.results if r.passed is True),
            failed=sum(1 for r in self.results if r.passed is False),
            errored=sum(1 for r in self.results if r.error is not None),
            avg_score=sum(scores) / len(scores) if scores else None,
            dimension_averages={d: sum(v) / len(v) for d, v in all_dims.items()},
            total_tokens=sum(r.tokens_used for r in self.results),
            total_cost_usd=sum(r.cost_usd for r in self.results),
        )


class ComparisonReport(BaseModel):
    """Side-by-side comparison of two evaluation runs."""
    run_a_id: str
    run_b_id: str
    run_a_suite: str
    run_b_suite: str
    summary_comparison: dict[str, dict[str, Any]] = Field(default_factory=dict)
    dimension_comparison: dict[str, dict[str, float]] = Field(default_factory=dict)
    regressions: list[str] = Field(default_factory=list)
    improvements: list[str] = Field(default_factory=list)


# --- Request/Response Models ---

class RunEvaluationRequest(BaseModel):
    """Request to start a new evaluation run."""
    suite: TestSuite
    model: str = "gpt-4o-mini"


class CompareRequest(BaseModel):
    """Request to compare two runs."""
    run_a_id: str
    run_b_id: str


# --- In-Memory Store (replace with database) ---

_store: dict[str, EvaluationRunDB] = {}


async def init_db() -> None:
    """Initialize the database. Replace with actual DB init."""
    _store.clear()


async def save_run(run: EvaluationRunDB) -> None:
    _store[run.id] = run


async def get_run(run_id: str) -> EvaluationRunDB | None:
    return _store.get(run_id)


async def list_runs(limit: int = 50, offset: int = 0) -> list[EvaluationRunDB]:
    runs = sorted(_store.values(), key=lambda r: r.created_at, reverse=True)
    return runs[offset : offset + limit]


async def delete_run(run_id: str) -> bool:
    if run_id in _store:
        del _store[run_id]
        return True
    return False
