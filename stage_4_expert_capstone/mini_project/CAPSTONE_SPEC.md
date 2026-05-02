# Capstone Specification: EvalForge

> An AI Evaluation Framework for teams building LLM-powered products.

---

## 1. Project Identity

| Field | Value |
|-------|-------|
| **Name** | EvalForge (or learner's choice) |
| **Tagline** | "Test your AI like you test your code" |
| **Type** | Python SDK + CLI + optional web dashboard |
| **License** | MIT |
| **Target audience** | SDETs, QA engineers, and ML engineers working on AI products |

---

## 2. Core Features

### 2.1 Custom Metric Builders

Users define evaluation metrics in Python or YAML:

```python
from evalforge import metric

@metric(name="tone_check", dimensions=["formality", "empathy"])
def tone_check(response: str, expected_tone: str) -> EvalResult:
    """Evaluates whether the response matches the expected tone."""
    ...
```

```yaml
# metrics/custom_tone.yaml
name: tone_check
type: llm_judge
prompt_template: |
  Rate the following response for {dimension}.
  Response: {response}
  Score 1-5 and explain.
dimensions:
  - formality
  - empathy
threshold: 0.7
```

### 2.2 LLM-Judge Templates

Pre-built, configurable judge prompts for common evaluation tasks:

| Template | What it evaluates |
|----------|-------------------|
| `correctness` | Is the answer factually correct? |
| `relevance` | Does the response address the question? |
| `helpfulness` | Would a user find this response useful? |
| `coherence` | Is the response well-structured and logical? |
| `safety` | Is the response free from harmful content? |
| `instruction_following` | Did the model follow the given instructions? |

Each template supports:
- **Pointwise mode**: Score a single response (1–5 or 0–1)
- **Pairwise mode**: Compare two responses ("A is better / B is better / tie")
- **Reference-based**: Compare against a gold-standard answer
- **Reference-free**: Evaluate without a reference

### 2.3 Agent Testing Harness

For multi-agent systems and tool-using agents:

```yaml
# test_suites/agent_booking.yaml
suite: booking_agent
type: agent
setup:
  available_tools:
    - search_flights
    - book_flight
    - get_user_preferences

cases:
  - name: "Simple booking request"
    conversation:
      - role: user
        content: "Book me a flight to London next Tuesday"
    expected:
      tools_called: ["get_user_preferences", "search_flights", "book_flight"]
      tool_call_order: sequential
      final_response_contains: ["confirmation", "London", "Tuesday"]
    evaluators:
      - tool_selection_accuracy
      - tool_parameter_correctness
      - response_completeness
```

### 2.4 Report Generation

Multiple output formats:

- **CLI**: Rich-formatted terminal output with pass/fail indicators
- **JSON**: Machine-readable for CI/CD pipelines
- **HTML**: Visual report with charts, drill-down, and failure analysis
- **Markdown**: For GitHub PR comments

---

## 3. Architecture

### 3.1 High-Level Components

```
┌─────────────────────────────────────────────────────┐
│                     EvalForge                        │
├──────────┬──────────┬───────────┬───────────────────┤
│  CLI     │  SDK     │  pytest   │  GitHub Action     │
│ (typer)  │ (Python) │  plugin   │  (YAML workflow)   │
├──────────┴──────────┴───────────┴───────────────────┤
│                  Core Engine                          │
├──────────┬──────────┬───────────┬───────────────────┤
│ Config   │ Runner   │ Evaluator │ Aggregator         │
│ Loader   │          │ Registry  │                     │
├──────────┴──────────┴───────────┴───────────────────┤
│                  Evaluators                           │
├──────────┬──────────┬───────────┬───────────────────┤
│ LLM      │ Halluci- │ Tool Use  │ Safety             │
│ Judge    │ nation   │           │                     │
├──────────┴──────────┴───────────┴───────────────────┤
│                  Reporters                            │
├──────────┬──────────┬───────────┬───────────────────┤
│ CLI      │ HTML     │ JSON      │ Markdown            │
└──────────┴──────────┴───────────┴───────────────────┘
```

### 3.2 Package Structure

```
src/evalforge/
├── __init__.py              # Public API
├── cli.py                   # CLI entry point (typer)
├── config.py                # Configuration management
├── models.py                # Core data models (Pydantic)
├── evaluators/
│   ├── __init__.py          # Evaluator registry
│   ├── base.py              # BaseEvaluator ABC
│   ├── llm_judge.py         # LLM-as-judge evaluator
│   ├── hallucination.py     # Hallucination detector
│   ├── tool_use.py          # Tool-use accuracy
│   ├── safety.py            # Safety evaluator
│   └── composite.py         # Combines multiple evaluators
├── runners/
│   ├── __init__.py
│   ├── test_runner.py       # Orchestrates evaluation runs
│   └── parallel.py          # Parallel execution engine
├── reporters/
│   ├── __init__.py
│   ├── base.py              # Reporter ABC
│   ├── cli_reporter.py      # Terminal output (rich)
│   ├── html_reporter.py     # HTML report (jinja2)
│   ├── json_reporter.py     # JSON output
│   └── templates/           # Jinja2 HTML templates
├── plugins/
│   ├── pytest_plugin.py     # pytest integration
│   └── github_action/       # GitHub Action files
└── utils/
    ├── llm_client.py        # Unified LLM API client
    ├── caching.py           # Response caching
    └── cost_tracker.py      # Token/cost accounting
```

### 3.3 Data Models

```python
class TestCase(BaseModel):
    name: str
    prompt: str | list[dict]          # Single turn or conversation
    response: str | None = None       # Pre-generated, or generate at runtime
    reference: str | None = None      # Gold-standard answer
    context: list[str] | None = None  # RAG context documents
    metadata: dict[str, Any] = {}
    evaluators: list[str] = []        # Evaluator names to run
    expected: dict[str, Any] = {}     # Expected outcomes

class EvalResult(BaseModel, frozen=True):
    evaluator: str
    score: float | None               # 0.0 to 1.0, None on error
    passed: bool | None
    explanation: str
    dimensions: dict[str, float] = {}
    error: str | None = None
    latency_ms: float = 0.0
    tokens_used: int = 0
    cost_usd: float = 0.0

class EvaluationRun(BaseModel):
    id: str                            # UUID
    suite_name: str
    timestamp: datetime
    results: list[EvalResult]
    summary: RunSummary
    config: dict[str, Any]
```

---

## 4. Self-Evaluating Framework

This is the flagship feature. EvalForge evaluates the quality of its own evaluations.

### How It Works

1. **Calibration dataset**: A curated set of (prompt, response, human_score) tuples where human scores are ground truth.

2. **Meta-evaluation**: Run EvalForge's evaluators on the calibration dataset. Compare evaluator scores against human scores.

3. **Metrics on metrics**:
   - **Agreement rate**: How often does the evaluator agree with humans (within threshold)?
   - **Correlation**: Spearman/Pearson correlation between evaluator and human scores
   - **Bias detection**: Does the evaluator systematically over- or under-score?
   - **Consistency**: Given the same input twice, does the evaluator produce the same score?

4. **Report**: A "calibration report" showing how trustworthy each evaluator is.

```bash
evalforge calibrate --dataset calibration/v1.yaml --evaluators all
```

---

## 5. Integration Points

### 5.1 pytest Plugin

```python
# conftest.py
import evalforge

evalforge.configure(
    model="gpt-4o-mini",
    test_suite="tests/eval_suite.yaml",
)

# test_evaluations.py
@evalforge.test
def test_booking_agent_accuracy():
    """Runs the booking agent evaluation suite."""
    pass  # Framework handles execution
```

```bash
pytest --eval --eval-suite tests/eval_suite.yaml --eval-model gpt-4o-mini
```

### 5.2 CI/CD Integration

```yaml
# .github/workflows/eval.yml
name: AI Evaluation
on: [pull_request]

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: evalforge/action@v1
        with:
          suite: tests/eval_suite.yaml
          model: gpt-4o-mini
          threshold: 0.8
          comment-on-pr: true
```

### 5.3 Python SDK

```python
from evalforge import EvalForge

forge = EvalForge(model="gpt-4o-mini")

# Quick single evaluation
result = forge.evaluate(
    prompt="What is the capital of France?",
    response="The capital of France is Paris.",
    evaluator="correctness",
)
print(result.score, result.explanation)

# Full suite run
run = await forge.run_suite("tests/eval_suite.yaml")
run.to_html("reports/latest.html")
```

---

## 6. Portfolio Value

### What to Showcase

| Audience | Emphasize |
|----------|-----------|
| **Hiring managers** | "I built a production tool, not a tutorial project" |
| **Technical interviewers** | Architecture decisions, trade-offs, testing strategy |
| **AI/ML teams** | Evaluator accuracy, benchmark methodology, self-calibration |
| **Open-source community** | Documentation quality, contribution guide, extensibility |

### How to Present

**GitHub README**: Professional, with badges, quickstart, and screenshots of reports.

**Demo script** (10 minutes):
1. (1 min) "Here's the problem: teams building with LLMs can't test quality systematically"
2. (2 min) Install and run a sample evaluation from the CLI
3. (2 min) Show the HTML report — drill into a failure
4. (2 min) Walk through the architecture — show how evaluators are pluggable
5. (2 min) Show the self-calibration feature — "the framework tests itself"
6. (1 min) Show CI integration — evaluation runs on every PR

**Blog post**: "Why I Built an AI Evaluation Framework (and What I Learned)" — publish on dev.to or your personal blog.

**LinkedIn/Resume line**: "Built EvalForge, an open-source AI evaluation framework with N evaluator types, self-calibration, and CI/CD integration. Used by [yourself / your team / N GitHub stars]."

---

## 7. Development Milestones

| Week | Milestone | Deliverables |
|------|-----------|-------------|
| 1 | **MVP** | `BaseEvaluator`, `LLMJudge`, `HallucinationDetector`, YAML loader, CLI `run` command, JSON output |
| 2 | **Expand** | `ToolUseEvaluator`, `SafetyEvaluator`, HTML reporter, multi-turn support |
| 3 | **Integrate** | pytest plugin, GitHub Action, cost tracking, caching |
| 4 | **Polish** | Self-calibration, documentation site, examples, first tagged release |
| 5+ | **Grow** | Web dashboard (see `boilerplate_fullstack_ai_eval`), community feedback, additional evaluators |
