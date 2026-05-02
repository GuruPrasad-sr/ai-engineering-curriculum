"""Tool-use accuracy evaluator.

Evaluates whether an AI agent:
1. Selected the correct tool(s)
2. Provided correct parameters
3. Used the tool results correctly in its response
"""

from __future__ import annotations

import json
from typing import Any

from .base import BaseEvaluator, EvalContext, EvalResult


class ToolUseEvaluator(BaseEvaluator):
    """Evaluates tool-use accuracy for AI agents.

    Compares actual tool calls against expected tool calls defined in
    the test case's `expected` field.

    Expected format in test case:
        expected:
          tools_called: ["search_flights", "book_flight"]
          tool_call_order: sequential  # or "any"
          tool_parameters:
            search_flights:
              destination: "London"
            book_flight:
              flight_id: "BA123"
          result_usage: "must_reference"  # or "optional"

    Args:
        strict_order: Whether tool call order must match exactly.
        strict_params: Whether tool parameters must match exactly (vs. subset).
        threshold: Minimum score to pass.
    """

    name = "tool_use"
    description = "Evaluates tool selection, parameter accuracy, and result usage"
    supported_dimensions = ["tool_selection", "parameter_accuracy", "result_usage"]

    def __init__(
        self,
        strict_order: bool = False,
        strict_params: bool = False,
        threshold: float = 0.7,
        **kwargs: Any,
    ) -> None:
        super().__init__(threshold=threshold, **kwargs)
        self.strict_order = strict_order
        self.strict_params = strict_params

    async def evaluate(self, context: EvalContext) -> EvalResult:
        """Evaluate tool-use accuracy."""
        expected = context.expected
        actual_calls = context.tool_calls

        if not expected.get("tools_called"):
            return self._make_error("No expected tool calls defined in test case")

        dimensions: dict[str, float] = {}
        explanations: list[str] = []

        # Dimension 1: Tool selection
        selection_score, selection_explanation = self._evaluate_tool_selection(
            expected_tools=expected["tools_called"],
            actual_calls=actual_calls,
            check_order=expected.get("tool_call_order") == "sequential" or self.strict_order,
        )
        dimensions["tool_selection"] = selection_score
        explanations.append(selection_explanation)

        # Dimension 2: Parameter accuracy
        expected_params = expected.get("tool_parameters", {})
        if expected_params:
            param_score, param_explanation = self._evaluate_parameters(
                expected_params=expected_params,
                actual_calls=actual_calls,
            )
            dimensions["parameter_accuracy"] = param_score
            explanations.append(param_explanation)

        # Dimension 3: Result usage
        if expected.get("result_usage") == "must_reference":
            usage_score, usage_explanation = self._evaluate_result_usage(
                actual_calls=actual_calls,
                response=context.response,
            )
            dimensions["result_usage"] = usage_score
            explanations.append(usage_explanation)

        avg_score = sum(dimensions.values()) / len(dimensions) if dimensions else 0.0

        return self._make_result(
            score=avg_score,
            explanation=" | ".join(explanations),
            dimensions=dimensions,
        )

    def _evaluate_tool_selection(
        self,
        expected_tools: list[str],
        actual_calls: list[dict[str, Any]],
        check_order: bool,
    ) -> tuple[float, str]:
        """Check if the correct tools were called."""
        actual_tool_names = [call.get("function", {}).get("name", call.get("name", "")) for call in actual_calls]

        expected_set = set(expected_tools)
        actual_set = set(actual_tool_names)

        # Correct tools called
        correct = expected_set & actual_set
        missing = expected_set - actual_set
        extra = actual_set - expected_set

        if not expected_set:
            return 1.0, "No tools expected, none called"

        # Base score: proportion of expected tools that were called
        score = len(correct) / len(expected_set)

        # Penalty for extra tools (0.1 per extra tool)
        score = max(0.0, score - len(extra) * 0.1)

        # Order check
        if check_order and score > 0:
            expected_order = [t for t in expected_tools if t in actual_set]
            actual_order = [t for t in actual_tool_names if t in expected_set]
            if expected_order != actual_order:
                score *= 0.8  # 20% penalty for wrong order

        parts = []
        if correct:
            parts.append(f"Correct: {sorted(correct)}")
        if missing:
            parts.append(f"Missing: {sorted(missing)}")
        if extra:
            parts.append(f"Unexpected: {sorted(extra)}")

        return score, "Tool selection — " + "; ".join(parts)

    def _evaluate_parameters(
        self,
        expected_params: dict[str, dict[str, Any]],
        actual_calls: list[dict[str, Any]],
    ) -> tuple[float, str]:
        """Check if tool parameters were correct."""
        actual_by_name: dict[str, dict[str, Any]] = {}
        for call in actual_calls:
            name = call.get("function", {}).get("name", call.get("name", ""))
            args = call.get("function", {}).get("arguments", call.get("arguments", {}))
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except json.JSONDecodeError:
                    args = {}
            actual_by_name[name] = args

        total_params = 0
        correct_params = 0
        issues: list[str] = []

        for tool_name, expected_args in expected_params.items():
            actual_args = actual_by_name.get(tool_name, {})
            for param_name, expected_value in expected_args.items():
                total_params += 1
                actual_value = actual_args.get(param_name)
                if actual_value == expected_value:
                    correct_params += 1
                elif str(actual_value).lower() == str(expected_value).lower():
                    correct_params += 0.5  # Partial credit for case-insensitive match
                else:
                    issues.append(
                        f"{tool_name}.{param_name}: expected={expected_value}, got={actual_value}"
                    )

        score = correct_params / total_params if total_params > 0 else 1.0
        explanation = f"Parameters — {correct_params}/{total_params} correct"
        if issues:
            explanation += f". Issues: {issues}"

        return score, explanation

    def _evaluate_result_usage(
        self,
        actual_calls: list[dict[str, Any]],
        response: str,
    ) -> tuple[float, str]:
        """Check if tool results were referenced in the final response."""
        results_referenced = 0
        total_results = 0

        for call in actual_calls:
            result = call.get("result", call.get("output", ""))
            if not result:
                continue
            total_results += 1
            result_str = str(result)
            # Simple heuristic: check if key parts of the result appear in the response
            # A more sophisticated version would use semantic similarity
            key_tokens = [t for t in result_str.split() if len(t) > 4][:5]
            if any(token.lower() in response.lower() for token in key_tokens):
                results_referenced += 1

        if total_results == 0:
            return 1.0, "Result usage — no tool results to verify"

        score = results_referenced / total_results
        return score, f"Result usage — {results_referenced}/{total_results} results referenced in response"
