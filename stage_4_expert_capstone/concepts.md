# Stage 4: Advanced Concepts for Capstone-Level Work

## 1. Evaluation Framework Architecture Patterns

### The Pipeline Pattern

Every evaluation framework follows a variation of this pipeline:

```
Input → Preprocessing → Evaluation → Aggregation → Reporting
```

**Input layer**: Test cases (prompt + expected behavior), loaded from YAML/JSON/Python fixtures.

**Preprocessing**: Normalize inputs, extract claims from responses, parse tool calls, segment multi-turn conversations into evaluable units.

**Evaluation layer**: The core — where evaluators score outputs. This is where the framework's value lives. Key architectural decisions:

- **Evaluator registry**: Evaluators register themselves (plugin pattern). The framework discovers them at runtime.
- **Evaluation context**: Each evaluator receives a context object containing the input, output, reference, metadata, and configuration. This avoids parameter explosion.
- **Async-first**: LLM-based evaluators make API calls. The evaluation layer must be async to run evaluators concurrently.

**Aggregation**: Combine per-case scores into suite-level metrics. Support weighted aggregation, dimensional rollups, and statistical summaries (mean, p50, p95, std dev).

**Reporting**: Transform aggregated results into human-readable output (CLI tables, HTML reports, JSON for CI).

### Evaluator Taxonomy

Organize evaluators by what they measure:

| Category | Examples | Requires LLM Judge? |
|----------|----------|---------------------|
| **Correctness** | Exact match, semantic similarity, factual accuracy | Sometimes |
| **Quality** | Coherence, helpfulness, relevance | Yes |
| **Safety** | Toxicity, PII leakage, prompt injection resistance | Sometimes |
| **Behavioral** | Tool selection accuracy, instruction following, format compliance | No |
| **Performance** | Latency, token usage, cost per evaluation | No |

### Configuration Hierarchy

Good frameworks support configuration at multiple levels:

```
Global defaults → Suite-level overrides → Case-level overrides → Runtime flags
```

Use Pydantic `BaseSettings` with environment variable support for production deployment.

---

## 2. Building Evaluation SDKs

### API Design Principles for Evaluation Libraries

**Minimal surface area**: The 80% use case should require one import and one function call.

```python
# This is what good SDK design looks like
from evalforge import evaluate

results = evaluate(
    model="gpt-4o",
    test_suite="tests/my_suite.yaml",
)
```

**Progressive disclosure**: Simple things are simple, complex things are possible.

```python
# Simple: one-liner
score = evaluate_single(prompt="...", response="...", evaluator="hallucination")

# Medium: configured evaluator
evaluator = HallucinationDetector(consistency_samples=5, model="gpt-4o-mini")
result = evaluator.evaluate(prompt="...", response="...", reference="...")

# Advanced: custom pipeline
pipeline = EvaluationPipeline(
    evaluators=[HallucinationDetector(), SafetyEvaluator(), CustomMetric()],
    aggregator=WeightedAggregator(weights={"hallucination": 0.4, "safety": 0.3, "custom": 0.3}),
    reporter=HTMLReporter(output_dir="./reports"),
)
results = await pipeline.run(test_suite)
```

**Immutable results**: Evaluation results should be immutable data objects. Never allow mutation after creation.

**Serializable everything**: Every object in the SDK should be serializable to JSON. This enables storage, comparison, and debugging.

### Error Handling Strategy

Evaluations should never crash the pipeline. Use a result type that captures both success and failure:

```python
@dataclass(frozen=True)
class EvalResult:
    score: float | None        # None if evaluation failed
    passed: bool | None        # None if no threshold set
    explanation: str
    error: str | None = None   # Non-None if evaluation itself failed
    dimensions: dict[str, float] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
```

---

## 3. Benchmark Design Methodology

### What Makes a Good Benchmark

1. **Representative**: Test cases reflect real usage patterns, not just edge cases
2. **Discriminative**: The benchmark can distinguish between good and bad systems
3. **Stable**: Results are reproducible (control for temperature, seed, model version)
4. **Calibrated**: Human agreement on the benchmark scores is high

### Building Your Own Benchmarks

**Step 1 — Collect real examples**: Pull from production logs (anonymized), support tickets, or domain experts.

**Step 2 — Annotate**: For each example, define what "good" looks like. Use multiple annotators and measure inter-annotator agreement (Cohen's kappa ≥ 0.7).

**Step 3 — Stratify**: Ensure coverage across:
- Difficulty levels (easy / medium / hard)
- Input types (short / long / multi-turn / ambiguous)
- Expected behaviors (refusal, tool use, direct answer, clarifying question)

**Step 4 — Version**: Benchmarks are datasets. Version them. Track which benchmark version produced which results.

**Step 5 — Validate**: Run the benchmark against known-good and known-bad systems. Verify it ranks them correctly.

### Contamination Prevention

LLMs may have seen your benchmark data during training. Mitigations:
- Use private, non-public test cases for high-stakes evaluation
- Paraphrase public test cases
- Include temporal markers (questions about recent events)
- Canary strings to detect memorization

---

## 4. Evaluation-as-a-Service Architecture

### When You Need a Service (Not Just a Library)

- Multiple teams need to run evaluations against a shared benchmark
- You need persistent storage of evaluation results for trend analysis
- Evaluations are triggered by CI/CD pipelines across many repositories
- You want a web UI for non-technical stakeholders to review results

### Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  CLI / SDK  │────▶│  Eval API    │────▶│  Worker Pool │
│  (clients)  │◀────│  (FastAPI)   │◀────│  (async)     │
└─────────────┘     └──────┬───────┘     └──────┬──────┘
                           │                     │
                    ┌──────▼───────┐     ┌──────▼──────┐
                    │  Result DB   │     │  LLM APIs   │
                    │  (Postgres)  │     │  (OpenAI,   │
                    └──────────────┘     │   Anthropic) │
                                         └─────────────┘
```

### Key Design Decisions

**Async workers**: Evaluations are I/O-bound (waiting on LLM APIs). Use an async task queue (or just `asyncio.gather` for the MVP).

**Idempotent runs**: Every evaluation run gets a unique ID. Re-running the same config produces a new run, not an overwrite.

**Cost tracking**: Every LLM call during evaluation has a cost. Track tokens used per evaluator per run.

**Caching**: Cache LLM judge responses for identical (prompt, response, evaluator_config) tuples. This dramatically reduces cost during development.

---

## 5. Open-Source Project Management for AI Tools

### Repository Structure

```
evalforge/
├── src/evalforge/          # Source code
│   ├── evaluators/         # Built-in evaluators
│   ├── runners/            # Test runners
│   ├── reporters/          # Output formatters
│   └── plugins/            # Plugin system
├── tests/                  # Tests (self-evaluating!)
├── docs/                   # Documentation
├── examples/               # Usage examples
├── benchmarks/             # Built-in benchmark suites
├── pyproject.toml
├── CONTRIBUTING.md
├── CHANGELOG.md
└── .github/workflows/      # CI/CD
```

### Documentation Requirements

For an open-source AI tool, you need:

1. **README**: Problem statement, 30-second quickstart, installation, badges
2. **Architecture doc**: System design for contributors
3. **API reference**: Auto-generated from docstrings (use `mkdocs` + `mkdocstrings`)
4. **Tutorials**: Step-by-step guides for common workflows
5. **ADRs (Architecture Decision Records)**: Why you made key design choices

### Release Strategy

- **Semantic versioning**: `MAJOR.MINOR.PATCH`
- **Changelog**: Keep a `CHANGELOG.md` updated with every release
- **Pre-release testing**: Run the full benchmark suite before every release
- **Backward compatibility**: Evaluator interfaces are your public API — don't break them

### Community Building

- Write a compelling "Why this exists" blog post
- Submit to awesome-lists (awesome-llm, awesome-evaluation)
- Post in relevant communities (r/MachineLearning, HuggingFace forums)
- Provide comparison tables: "EvalForge vs DeepEval vs RAGAS vs Promptfoo"
