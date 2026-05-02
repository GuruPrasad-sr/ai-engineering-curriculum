"""Evaluation runner service.

Orchestrates the execution of evaluation runs. This service:
1. Resolves evaluators from the test suite config
2. Runs evaluators against each test case (with parallel execution)
3. Stores results and broadcasts progress via WebSocket
"""

from __future__ import annotations

import asyncio
import time
from datetime import datetime, timezone
from typing import Any

from ..models.evaluation import (
    EvaluationResult,
    EvaluationRunDB,
    RunEvaluationRequest,
    RunStatus,
    TestCase,
    get_run,
    save_run,
)


async def execute_evaluation_run(run_id: str, request: RunEvaluationRequest) -> None:
    """Execute an evaluation run in the background.

    This is the main entry point called by the API route via BackgroundTasks.
    It updates the run status and stores results as evaluations complete.

    Args:
        run_id: The ID of the evaluation run to execute.
        request: The original request containing the test suite.
    """
    run = await get_run(run_id)
    if not run:
        return

    run.status = RunStatus.RUNNING
    await save_run(run)

    start = time.perf_counter()

    try:
        suite = request.suite
        model = request.model

        # Process each test case
        tasks = [
            _evaluate_single_case(case, suite.evaluators or case.evaluators, model, suite.threshold)
            for case in suite.cases
        ]

        all_results = await asyncio.gather(*tasks, return_exceptions=True)

        for case, result_or_error in zip(suite.cases, all_results):
            if isinstance(result_or_error, Exception):
                run.results.append(
                    EvaluationResult(
                        test_case_name=case.name,
                        evaluator_name="error",
                        error=str(result_or_error),
                    )
                )
            elif isinstance(result_or_error, list):
                run.results.extend(result_or_error)

            # Broadcast progress
            await _broadcast_progress(run_id, {
                "type": "progress",
                "data": {
                    "completed": len(run.results),
                    "total": len(suite.cases) * max(len(suite.evaluators), 1),
                },
            })

        run.status = RunStatus.COMPLETED
        run.completed_at = datetime.now(timezone.utc)
        run.compute_summary()
        run.summary.duration_seconds = time.perf_counter() - start

        await _broadcast_progress(run_id, {
            "type": "complete",
            "data": run.summary.model_dump(),
        })

    except Exception as e:
        run.status = RunStatus.FAILED
        run.error = str(e)
        run.completed_at = datetime.now(timezone.utc)

        await _broadcast_progress(run_id, {
            "type": "error",
            "data": {"error": str(e)},
        })

    await save_run(run)


async def _evaluate_single_case(
    case: TestCase,
    evaluator_names: list[str],
    model: str,
    threshold: float,
) -> list[EvaluationResult]:
    """Evaluate a single test case with all specified evaluators.

    This is a stub implementation. In a real deployment, this would
    import and invoke the evaluators from the Python validation framework
    (boilerplate_python_validation).

    Args:
        case: The test case to evaluate.
        evaluator_names: Names of evaluators to run.
        model: The LLM model to use for evaluation.
        threshold: Score threshold for pass/fail.

    Returns:
        List of evaluation results, one per evaluator.
    """
    results: list[EvaluationResult] = []

    for evaluator_name in evaluator_names:
        start = time.perf_counter()

        try:
            # TODO: Replace with actual evaluator invocation.
            # This stub simulates an evaluation by returning a placeholder result.
            # In production, import from the evalforge SDK:
            #
            #   from evalforge.evaluators import EVALUATOR_REGISTRY
            #   evaluator = EVALUATOR_REGISTRY[evaluator_name](model=model, threshold=threshold)
            #   eval_context = EvalContext(prompt=case.prompt, response=case.response or "", ...)
            #   result = await evaluator.evaluate(eval_context)

            # Simulated delay for realistic async behavior
            await asyncio.sleep(0.1)

            latency_ms = (time.perf_counter() - start) * 1000

            results.append(
                EvaluationResult(
                    test_case_name=case.name,
                    evaluator_name=evaluator_name,
                    score=None,  # Replace with actual score
                    passed=None,
                    explanation=f"Stub: evaluator '{evaluator_name}' not yet connected. "
                                f"Wire up the evalforge SDK to enable real evaluations.",
                    latency_ms=latency_ms,
                )
            )

        except Exception as e:
            results.append(
                EvaluationResult(
                    test_case_name=case.name,
                    evaluator_name=evaluator_name,
                    error=f"Evaluator '{evaluator_name}' failed: {e}",
                )
            )

    return results


async def _broadcast_progress(run_id: str, message: dict[str, Any]) -> None:
    """Broadcast a progress message to WebSocket clients.

    Imports lazily to avoid circular imports with main.py.
    """
    try:
        from ..main import broadcast_to_run
        await broadcast_to_run(run_id, message)
    except Exception:
        pass  # WebSocket broadcast is best-effort
