# EvalForge — AI Validation Framework (Boilerplate)

A production-ready starter template for building an AI evaluation framework in Python.

## Architecture

```
src/
├── __init__.py                  # Package root, public API
├── evaluators/
│   ├── base.py                  # BaseEvaluator ABC + EvalResult model
│   ├── llm_judge.py             # LLM-as-judge (pointwise + pairwise)
│   ├── hallucination.py         # Hallucination detection pipeline
│   ├── tool_use.py              # Tool-use accuracy evaluator
│   └── safety.py                # Safety + prompt injection detection
├── runners/
│   └── test_runner.py           # YAML-driven test runner with parallel execution
└── reporters/
    └── html_reporter.py         # HTML report generation with Jinja2

tests/
├── test_config/
│   └── sample_tests.yaml        # Example test suite configuration
└── evaluators/
    └── test_llm_judge.py        # Unit tests for the LLM judge evaluator
```

## Quick Start

```bash
# Install in development mode
pip install -e ".[dev]"

# Run the sample test suite
python -m src.runners.test_runner tests/test_config/sample_tests.yaml

# Run framework tests
pytest tests/ -v
```

## Extending the Framework

### Adding a New Evaluator

1. Create a new file in `src/evaluators/`
2. Subclass `BaseEvaluator`:

```python
from src.evaluators.base import BaseEvaluator, EvalResult, EvalContext

class MyEvaluator(BaseEvaluator):
    name = "my_evaluator"

    async def evaluate(self, context: EvalContext) -> EvalResult:
        # Your evaluation logic here
        return EvalResult(
            evaluator=self.name,
            score=0.95,
            passed=True,
            explanation="Evaluation passed because ...",
        )
```

3. Add tests in `tests/evaluators/test_my_evaluator.py`
4. Register the evaluator in your test suite YAML

### Adding a New Reporter

Implement the reporter interface and transform `EvaluationRun` results into your desired output format.

## Configuration

Test suites are defined in YAML. See `tests/test_config/sample_tests.yaml` for the full schema.

```yaml
suite: my_tests
model: gpt-4o-mini
evaluators:
  - llm_judge
  - hallucination
cases:
  - name: "Basic QA check"
    prompt: "What is 2+2?"
    reference: "4"
```

## Dependencies

- `openai` — LLM API client
- `pydantic` — Data validation and serialization
- `pyyaml` — YAML configuration loading
- `jinja2` — HTML report templating
- `httpx` — Async HTTP client
- `rich` — Terminal output formatting
- `pytest` — Testing framework
