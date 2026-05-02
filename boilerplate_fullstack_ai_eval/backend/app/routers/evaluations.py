"""API routes for evaluation management.

All routes are prefixed with /api/evaluations (set in main.py).
"""

from __future__ import annotations

from fastapi import APIRouter, BackgroundTasks, HTTPException

from ..models.evaluation import (
    CompareRequest,
    ComparisonReport,
    EvaluationRunDB,
    RunEvaluationRequest,
    RunStatus,
    delete_run,
    get_run,
    list_runs,
    save_run,
)
from ..services.eval_runner import execute_evaluation_run

router = APIRouter()


@router.post("/run", response_model=EvaluationRunDB)
async def start_evaluation(
    request: RunEvaluationRequest,
    background_tasks: BackgroundTasks,
) -> EvaluationRunDB:
    """Start a new evaluation run.

    The evaluation executes in the background. Use the WebSocket endpoint
    or poll GET /{id} to track progress.
    """
    run = EvaluationRunDB(
        suite_name=request.suite.name,
        status=RunStatus.PENDING,
        config={
            "model": request.model,
            "threshold": request.suite.threshold,
            "evaluators": request.suite.evaluators,
            "num_cases": len(request.suite.cases),
        },
    )
    await save_run(run)

    # Execute in background
    background_tasks.add_task(execute_evaluation_run, run.id, request)
    return run


@router.get("/", response_model=list[EvaluationRunDB])
async def get_evaluations(limit: int = 50, offset: int = 0) -> list[EvaluationRunDB]:
    """List all evaluation runs, most recent first."""
    return await list_runs(limit=limit, offset=offset)


@router.get("/{run_id}", response_model=EvaluationRunDB)
async def get_evaluation(run_id: str) -> EvaluationRunDB:
    """Get details of a specific evaluation run."""
    run = await get_run(run_id)
    if not run:
        raise HTTPException(status_code=404, detail=f"Evaluation run {run_id} not found")
    return run


@router.get("/{run_id}/results")
async def get_evaluation_results(run_id: str) -> dict:
    """Get detailed results for an evaluation run."""
    run = await get_run(run_id)
    if not run:
        raise HTTPException(status_code=404, detail=f"Evaluation run {run_id} not found")
    return {
        "run_id": run.id,
        "status": run.status,
        "summary": run.summary,
        "results": run.results,
    }


@router.delete("/{run_id}")
async def remove_evaluation(run_id: str) -> dict[str, str]:
    """Delete an evaluation run."""
    deleted = await delete_run(run_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Evaluation run {run_id} not found")
    return {"status": "deleted", "run_id": run_id}


@router.post("/compare", response_model=ComparisonReport)
async def compare_evaluations(request: CompareRequest) -> ComparisonReport:
    """Compare two evaluation runs side-by-side.

    Returns dimension-level comparisons, regressions, and improvements.
    """
    run_a = await get_run(request.run_a_id)
    run_b = await get_run(request.run_b_id)

    if not run_a:
        raise HTTPException(status_code=404, detail=f"Run {request.run_a_id} not found")
    if not run_b:
        raise HTTPException(status_code=404, detail=f"Run {request.run_b_id} not found")

    # Build comparison
    regressions: list[str] = []
    improvements: list[str] = []
    dimension_comparison: dict[str, dict[str, float]] = {}

    all_dims = set(run_a.summary.dimension_averages.keys()) | set(run_b.summary.dimension_averages.keys())
    for dim in all_dims:
        score_a = run_a.summary.dimension_averages.get(dim, 0.0)
        score_b = run_b.summary.dimension_averages.get(dim, 0.0)
        delta = score_b - score_a
        dimension_comparison[dim] = {"run_a": score_a, "run_b": score_b, "delta": delta}

        if delta < -0.05:
            regressions.append(f"{dim}: {score_a:.3f} → {score_b:.3f} ({delta:+.3f})")
        elif delta > 0.05:
            improvements.append(f"{dim}: {score_a:.3f} → {score_b:.3f} ({delta:+.3f})")

    summary_comparison = {
        "avg_score": {
            "run_a": run_a.summary.avg_score,
            "run_b": run_b.summary.avg_score,
        },
        "pass_rate": {
            "run_a": run_a.summary.passed / max(run_a.summary.total_cases, 1),
            "run_b": run_b.summary.passed / max(run_b.summary.total_cases, 1),
        },
        "total_cost": {
            "run_a": run_a.summary.total_cost_usd,
            "run_b": run_b.summary.total_cost_usd,
        },
    }

    return ComparisonReport(
        run_a_id=request.run_a_id,
        run_b_id=request.run_b_id,
        run_a_suite=run_a.suite_name,
        run_b_suite=run_b.suite_name,
        summary_comparison=summary_comparison,
        dimension_comparison=dimension_comparison,
        regressions=regressions,
        improvements=improvements,
    )
