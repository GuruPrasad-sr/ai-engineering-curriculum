# Capstone Planning Exercises (Days 29–30)

These exercises produce the artifacts you need before writing any code. By the end, you will have an architecture document, an MVP scope, and a contribution guide.

---

## Exercise 1: Competitive Landscape Survey

**Time**: 3–4 hours

Survey these five evaluation frameworks. For each one, complete the table below.

### Frameworks to Survey

1. **DeepEval** — https://github.com/confident-ai/deepeval
2. **RAGAS** — https://github.com/explodinggradients/ragas
3. **Promptfoo** — https://github.com/promptfoo/promptfoo
4. **OpenAI Evals** — https://github.com/openai/evals
5. **Garak** — https://github.com/NVIDIA/garak

### Survey Template

For each framework, document:

| Dimension | Notes |
|-----------|-------|
| **Primary focus** | (e.g., RAG evaluation, red-teaming, general LLM testing) |
| **Language / Runtime** | |
| **Installation experience** | Install it. How long from `pip install` to first result? |
| **Evaluator types** | List every built-in evaluator/metric |
| **Configuration format** | YAML? Python? JSON? CLI flags? |
| **Extensibility** | How do you add a custom evaluator? How many lines of code? |
| **Output formats** | CLI, HTML, JSON, dashboard? |
| **CI/CD integration** | pytest plugin? GitHub Action? Exit codes? |
| **Documentation quality** | Rate 1–5, note what's missing |
| **Community** | GitHub stars, last commit date, open issues, responsiveness |
| **Pricing / Limitations** | Open-source? Freemium? Cloud-only features? |

### Deliverable

A markdown file: `research/competitive_analysis.md` with all five frameworks compared side-by-side.

---

## Exercise 2: Gap Analysis

**Time**: 1–2 hours

Using your survey from Exercise 1, identify gaps across the ecosystem.

### Guiding Questions

1. **Agent testing**: Which frameworks handle multi-step agent evaluation well? (Tool selection accuracy, multi-turn coherence, plan execution quality)

2. **Self-hosted simplicity**: Which frameworks require cloud accounts or external services? What if a team wants 100% local evaluation?

3. **Testing the tester**: Do any frameworks evaluate the quality of their own evaluators? (Meta-evaluation / calibration)

4. **YAML-native workflow**: Which frameworks let SDETs define test suites in YAML with minimal Python? (Important for your background — you know how powerful declarative test configs are.)

5. **Multi-dimensional scoring**: Which frameworks support evaluating a single response on multiple dimensions simultaneously (correctness AND safety AND helpfulness)?

6. **Regression detection**: Which frameworks track scores over time and alert on regressions?

7. **Cost awareness**: Which frameworks track and report the cost of running evaluations?

### Deliverable

A markdown file: `research/gap_analysis.md` with a ranked list of the top 5 gaps you plan to address.

---

## Exercise 3: Unique Value Proposition

**Time**: 1 hour

Based on your gap analysis, define what makes your framework different.

### Framework

Complete this template:

```markdown
# [Framework Name] — One-Line Description

## The Problem
[2-3 sentences: What pain do AI teams feel today?]

## Existing Solutions Fall Short Because
1. [Gap 1 from your analysis]
2. [Gap 2]
3. [Gap 3]

## Our Approach
[Framework Name] is a [type of tool] that [key differentiator].

Unlike [competitor A], we [difference].
Unlike [competitor B], we [difference].

## Core Principles
1. [Principle 1 — e.g., "Declarative first: define evaluations in YAML, extend in Python"]
2. [Principle 2 — e.g., "Self-calibrating: the framework measures its own evaluation quality"]
3. [Principle 3 — e.g., "Cost-aware: every evaluation reports its LLM API cost"]
4. [Principle 4]

## Target Users
- Primary: [e.g., SDETs and QA engineers working on AI products]
- Secondary: [e.g., ML engineers validating model changes]
- Tertiary: [e.g., Product managers reviewing evaluation reports]
```

### Deliverable

A markdown file: `research/value_proposition.md`

---

## Exercise 4: Architecture Document

**Time**: 2–3 hours

Design the system architecture. This document is both your build plan and a portfolio artifact.

### Required Sections

**4.1 — System Context Diagram**

Draw (ASCII or Mermaid) showing: your framework, the LLM APIs it calls, the test suites it reads, the reports it produces, and the CI/CD systems it integrates with.

**4.2 — Component Diagram**

Show the major components and their relationships:
- Evaluator registry
- Test runner
- Configuration loader
- Result aggregator
- Reporter
- Plugin system
- CLI interface

**4.3 — Data Flow**

Trace a single evaluation from YAML test case to HTML report. Show every transformation.

**4.4 — Key Interfaces**

Define the Python interfaces (abstract base classes) for:
- `BaseEvaluator` — the contract every evaluator must implement
- `EvalResult` — the standard result object
- `TestCase` — the standard test case object
- `Reporter` — the contract for output formatters

**4.5 — Extension Points**

Where can users plug in custom behavior?
- Custom evaluators (implement `BaseEvaluator`)
- Custom reporters (implement `Reporter`)
- Custom loaders (new test case formats)
- Middleware (pre/post evaluation hooks)

**4.6 — Technology Decisions**

For each technology choice, document the decision and the alternative you considered:

| Decision | Choice | Alternative | Why |
|----------|--------|-------------|-----|
| Async runtime | `asyncio` | `threading` | LLM calls are I/O-bound |
| Data validation | `pydantic` | `dataclasses` | Need serialization + validation |
| CLI | `click` or `typer` | `argparse` | Better DX |
| Templating | `jinja2` | `string.Template` | Need complex report templates |
| Config format | YAML | TOML | Familiar to QA/SDET teams |

### Deliverable

A markdown file: `docs/architecture.md`

---

## Exercise 5: MVP Scope Definition

**Time**: 1–2 hours

Define exactly what ships in the first week. Resist scope creep.

### MVP Must Include

Categorize every feature as MVP (week 1), v0.2 (week 2–3), or Future.

| Feature | Priority | Rationale |
|---------|----------|-----------|
| `BaseEvaluator` abstract class | MVP | Foundation for everything |
| `LLMJudgeEvaluator` | MVP | Most-used evaluator type |
| `HallucinationEvaluator` | MVP | High-value, demonstrates claim extraction |
| YAML test case loader | MVP | Core workflow |
| CLI `run` command | MVP | Primary interface |
| JSON result output | MVP | Machine-readable for CI |
| `ToolUseEvaluator` | v0.2 | |
| `SafetyEvaluator` | v0.2 | |
| HTML report | v0.2 | |
| pytest plugin | v0.2 | |
| Web dashboard | Future | |
| GitHub Action | Future | |
| Caching layer | Future | |
| Cost tracking | Future | |

### Definition of Done for MVP

- [ ] `pip install -e .` works
- [ ] `evalforge run tests/sample.yaml` produces JSON output
- [ ] At least 2 evaluators work end-to-end
- [ ] `pytest` passes with >90% coverage on core modules
- [ ] README has a 5-minute quickstart

### Deliverable

A markdown file: `docs/mvp_scope.md` and a GitHub project board (or markdown checklist) tracking each item.

---

## Exercise 6: Contribution Guide

**Time**: 1 hour

Write a `CONTRIBUTING.md` that makes it easy for others (or future-you) to contribute.

### Required Sections

1. **Development Setup**: Clone, install, run tests
2. **Adding a New Evaluator**: Step-by-step (create file, implement interface, register, add tests, add docs)
3. **Adding a New Reporter**: Step-by-step
4. **Code Style**: Formatting (ruff), type checking (mypy), docstring format
5. **Testing Standards**: Every evaluator must have unit tests AND integration tests. Integration tests can be marked `@pytest.mark.llm` and skipped without API keys.
6. **PR Process**: Branch naming, commit message format, review checklist

### Deliverable

A file: `CONTRIBUTING.md` in the project root.

---

## Submission Checklist

By end of Day 30, you should have:

- [ ] `research/competitive_analysis.md` — Five frameworks surveyed
- [ ] `research/gap_analysis.md` — Top gaps identified
- [ ] `research/value_proposition.md` — Your framework's unique angle
- [ ] `docs/architecture.md` — Full system design
- [ ] `docs/mvp_scope.md` — Week 1 deliverables defined
- [ ] `CONTRIBUTING.md` — Ready for contributors
- [ ] Boilerplate project cloned and building locally

You are now ready to build.
