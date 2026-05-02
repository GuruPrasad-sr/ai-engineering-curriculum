"""Test runner — loads YAML configs and orchestrates evaluations.

Supports:
- YAML test suite loading
- Evaluator resolution by name
- Multi-turn conversation testing
- Parallel execution of independent evaluations
"""

from __future__ import annotations

import asyncio
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.table import Table

from ..evaluators.base import (
    BaseEvaluator,
    EvalContext,
    EvalResult,
    EvaluationRun,
    TestCase,
)
from ..evaluators.hallucination import HallucinationEvaluator
from ..evaluators.llm_judge import LLMJudgeEvaluator
from ..evaluators.safety import SafetyEvaluator
from ..evaluators.tool_use import ToolUseEvaluator

console = Console()

# Built-in evaluator registry
EVALUATOR_REGISTRY: dict[str, type[BaseEvaluator]] = {
    "llm_judge": LLMJudgeEvaluator,
    "hallucination": HallucinationEvaluator,
    "tool_use": ToolUseEvaluator,
    "safety": SafetyEvaluator,
}


def register_evaluator(name: str, evaluator_class: type[BaseEvaluator]) -> None:
    """Register a custom evaluator."""
    EVALUATOR_REGISTRY[name] = evaluator_class


def load_test_suite(path: str | Path) -> tuple[dict[str, Any], list[TestCase]]:
    """Load a YAML test suite and return config + test cases.

    Args:
        path: Path to the YAML test suite file.

    Returns:
        Tuple of (suite_config, list_of_test_cases).
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Test suite not found: {path}")

    with open(path) as f:
        raw = yaml.safe_load(f)

    suite_config = {
        "suite": raw.get("suite", path.stem),
        "model": raw.get("model", "gpt-4o-mini"),
        "evaluators": raw.get("evaluators", []),
        "threshold": raw.get("threshold", 0.5),
        "parallel": raw.get("parallel", True),
    }

    cases: list[TestCase] = []
    for case_data in raw.get("cases", []):
        # Merge suite-level evaluators with case-level
        case_evaluators = case_data.get("evaluators", []) or suite_config["evaluators"]
        cases.append(
            TestCase(
                name=case_data["name"],
                prompt=case_data["prompt"],
                response=case_data.get("response"),
                reference=case_data.get("reference"),
                context_documents=case_data.get("context_documents", []),
                metadata=case_data.get("metadata", {}),
                evaluators=case_evaluators,
                expected=case_data.get("expected", {}),
                tags=case_data.get("tags", []),
            )
        )

    return suite_config, cases


def resolve_evaluators(
    names: list[str], config: dict[str, Any]
) -> list[BaseEvaluator]:
    """Resolve evaluator names to instances.

    Args:
        names: List of evaluator names to resolve.
        config: Suite-level config (used for model name, threshold, etc.).

    Returns:
        List of evaluator instances.

    Raises:
        ValueError: If an evaluator name is not found in the registry.
    """
    evaluators: list[BaseEvaluator] = []
    for name in names:
        if name not in EVALUATOR_REGISTRY:
            raise ValueError(
                f"Unknown evaluator: '{name}'. "
                f"Available: {sorted(EVALUATOR_REGISTRY.keys())}"
            )
        evaluator_cls = EVALUATOR_REGISTRY[name]
        evaluators.append(
            evaluator_cls(
                model=config.get("model", "gpt-4o-mini"),
                threshold=config.get("threshold", 0.5),
            )
        )
    return evaluators


async def run_single_case(
    case: TestCase,
    evaluators: list[BaseEvaluator],
) -> list[tuple[str, EvalResult]]:
    """Run all evaluators against a single test case."""
    context = case.to_eval_context()
    results: list[tuple[str, EvalResult]] = []

    tasks = [evaluator.evaluate(context) for evaluator in evaluators]
    eval_results = await asyncio.gather(*tasks, return_exceptions=True)

    for evaluator, result in zip(evaluators, eval_results):
        if isinstance(result, Exception):
            results.append((
                case.name,
                EvalResult(
                    evaluator=evaluator.name,
                    error=f"Evaluator raised exception: {result}",
                    explanation="",
                ),
            ))
        else:
            results.append((case.name, result))

    return results


async def run_suite(
    path: str | Path,
    parallel: bool | None = None,
) -> EvaluationRun:
    """Run a full test suite from a YAML file.

    Args:
        path: Path to the YAML test suite file.
        parallel: Override suite-level parallel setting.

    Returns:
        An EvaluationRun with all results and summary.
    """
    config, cases = load_test_suite(path)
    use_parallel = parallel if parallel is not None else config.get("parallel", True)

    run = EvaluationRun(
        suite_name=config["suite"],
        config=config,
    )

    start = time.perf_counter()
    console.print(f"\n[bold]Running suite: {config['suite']}[/bold] ({len(cases)} cases)\n")

    if use_parallel:
        # Run all cases in parallel
        all_tasks = []
        for case in cases:
            evaluators = resolve_evaluators(case.evaluators, config)
            all_tasks.append(run_single_case(case, evaluators))

        all_results = await asyncio.gather(*all_tasks)
        for case_results in all_results:
            run.results.extend(case_results)
    else:
        # Run sequentially
        for case in cases:
            evaluators = resolve_evaluators(case.evaluators, config)
            case_results = await run_single_case(case, evaluators)
            run.results.extend(case_results)

    duration = time.perf_counter() - start
    run.compute_summary()
    run.summary.duration_seconds = duration

    _print_summary(run)
    return run


def _print_summary(run: EvaluationRun) -> None:
    """Print a rich-formatted summary to the terminal."""
    summary = run.summary
    table = Table(title=f"Results: {run.suite_name}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="bold")

    table.add_row("Total cases", str(summary.total_cases))
    table.add_row("Passed", f"[green]{summary.passed}[/green]")
    table.add_row("Failed", f"[red]{summary.failed}[/red]")
    table.add_row("Errors", f"[yellow]{summary.errored}[/yellow]")
    table.add_row(
        "Avg score",
        f"{summary.avg_score:.3f}" if summary.avg_score is not None else "N/A",
    )
    table.add_row("Duration", f"{summary.duration_seconds:.2f}s")
    table.add_row("Tokens used", str(summary.total_tokens))
    table.add_row("Cost", f"${summary.total_cost_usd:.4f}")

    console.print(table)

    if summary.dimension_averages:
        dim_table = Table(title="Dimension Averages")
        dim_table.add_column("Dimension", style="cyan")
        dim_table.add_column("Score", style="bold")
        for dim, score in sorted(summary.dimension_averages.items()):
            color = "green" if score >= 0.7 else "yellow" if score >= 0.5 else "red"
            dim_table.add_row(dim, f"[{color}]{score:.3f}[/{color}]")
        console.print(dim_table)


# CLI entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        console.print("[red]Usage: python -m src.runners.test_runner <suite.yaml>[/red]")
        sys.exit(1)

    suite_path = sys.argv[1]
    result = asyncio.run(run_suite(suite_path))

    # Exit with non-zero if any tests failed
    if result.summary.failed > 0 or result.summary.errored > 0:
        sys.exit(1)
