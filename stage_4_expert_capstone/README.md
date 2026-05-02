---
tags: [stage4, capstone, curriculum, evalforge]
stage: 4
days: "29-30"
hours: 5
status: not-started
---

# Stage 4: Expert Capstone — Production AI Validation Framework

## Overview

This is the culmination of your 30-day AI Engineering learning path. You will build a **production-grade AI Validation Framework** from scratch — an open-source tool that any team building LLM-powered products can use to evaluate, test, and monitor their AI systems.

This is your portfolio piece. It demonstrates mastery across every skill from Stages 0–3.

## Why This Capstone

| Stage | What You Learned | How the Capstone Uses It |
|-------|-----------------|--------------------------|
| 0 — LLM Fundamentals | Prompt engineering, tokenization, model behavior | Building configurable evaluation prompts, understanding model outputs |
| 1 — AI Validation | LLM-as-judge, hallucination detection, safety testing | Core evaluator implementations (the heart of the framework) |
| 2 — AI Systems | Multi-agent orchestration, RAG pipelines, tool use | Agent testing harness, multi-turn conversation evaluation |
| 3 — AI Engineering | Production patterns, CI/CD, observability | Framework architecture, pytest plugin, GitHub Actions integration |

## Timeline

| Phase | When | Deliverable |
|-------|------|-------------|
| **Planning** | Days 29–30 of the curriculum | Architecture doc, MVP scope, contribution guide |
| **MVP Build** | Week 1 post-curriculum | Core SDK: 3 evaluators + test runner + CLI |
| **Expansion** | Weeks 2–3 | Full evaluator suite, HTML reports, pytest plugin |
| **Polish** | Week 4 | Documentation, examples, CI/CD, first release |

## What "Production-Grade" Means

Your framework must meet these standards:

- **Typed**: Full type annotations, Pydantic models for all data structures
- **Tested**: The framework evaluates its own evaluation quality (self-referential testing)
- **Documented**: API reference, quickstart guide, architecture decision records
- **Packaged**: Installable via `pip install`, proper `pyproject.toml`
- **Extensible**: Plugin system for custom evaluators
- **Observable**: Structured logging, evaluation traces, performance metrics

## Portfolio Presentation

When showing this to employers, lead with:

1. **The problem it solves** — "Teams building with LLMs have no standardized way to evaluate quality"
2. **Architecture decisions** — Show you can design systems, not just write code
3. **Self-testing** — "The framework evaluates its own evaluations" is a compelling narrative
4. **Real metrics** — Run it against actual LLM outputs and show the results

## Getting Started

1. Read `concepts.md` for the theoretical foundation
2. Complete `exercises/capstone_planning.md` (days 29–30)
3. Review `mini_project/CAPSTONE_SPEC.md` for the full specification
4. Use `../boilerplate_python_validation/` as your starter template
5. Optionally extend with `../boilerplate_fullstack_ai_eval/` for the web dashboard

## Success Criteria

You are done when:

- [ ] Framework is installable via pip
- [ ] At least 5 evaluator types are implemented and tested
- [ ] Test runner loads YAML configs and produces reports
- [ ] pytest plugin allows `pytest --eval` workflow
- [ ] GitHub Actions workflow runs evaluations on PR
- [ ] README and docs are good enough for a stranger to use the tool
- [ ] You can demo it in a 10-minute technical interview presentation
