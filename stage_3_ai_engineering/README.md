---
tags: [stage3, ai-engineering, curriculum, mlops, safety]
stage: 3
days: "23-28"
hours: 13
status: not-started
---

# Stage 3: Production AI Engineering

## From Testing AI Systems to Engineering Them for Production

**Days 23-28 of 30** | **~12-14 hours** | **Prerequisite: Stages 0-2 completed**

---

## What This Stage Is About

In Stages 0-2, you learned what LLMs are, how to validate them, and how AI systems (RAG, agents, multi-agent orchestration) work. You can now *test* AI systems. In Stage 3, you cross the line from testing to **engineering**: the practices, patterns, and principles that keep AI systems alive, safe, and cost-effective in production.

Think of it this way: Stage 2 taught you how a car engine works. Stage 3 teaches you how to build the factory, the quality inspection line, and the safety systems around it.

## What You Will Learn

| Chapter | Topic | Hours | Priority |
|---------|-------|-------|----------|
| 1 | MLOps for LLM Systems | 3 | [PARETO-20] |
| 2 | Deployment Patterns | 2.5 | |
| 3 | Fine-Tuning (Understanding the Option) | 1.5 | |
| 4 | AI Safety and Alignment | 3 | [PARETO-20] |
| 5 | Observability and Monitoring | 2 | |

## How This Connects to Your Workspace

You are not starting from zero. Your production system already has pieces of every chapter:

| Concept | Already in Your Workspace |
|---------|--------------------------|
| Rate limiting & cost control | `agai-api/api/rate_limiter.py` — application-level and model-level token limits |
| Caching | `agai-api/api/cache/` — S3 and local cache abstractions |
| Distributed computing | `agai-api/api/tasks/ray_driver.py` — Ray for batch tasks |
| Model versioning | `wos-ri-conductor/app/config.py` line 265: `AG_MODEL_NAME = 'gpt_41_2025_04_14'` |
| Guardrail testing | `platform-agent-testing/.../AGAI_3633_3396_guardrails.yaml` — prompt injection, off-topic, safety |
| Mini model routing | `agai-api` uses `gpt_41_mini` for lightweight tasks, full models for complex ones |
| Monitoring hooks | Datadog tracing stubs in `agai-api/api/main.py` |

## Files in This Stage

```
stage_3_ai_engineering/
  README.md               <- You are here
  concepts.md             <- Comprehensive textbook (5 chapters)
  live_examples.md        <- Every concept mapped to workspace files
  resources.md            <- Curated 2024-2025 learning resources
  exercises/
    week4_exercises.md    <- 8 hands-on exercises
  mini_project/
    PROJECT.md            <- Capstone: Production-Ready AI Agent with Safety Guardrails
```

## Suggested Schedule

| Day | Focus | Hours |
|-----|-------|-------|
| 23 | Chapter 1: MLOps for LLM Systems | 2.5 |
| 24 | Chapter 2: Deployment Patterns | 2.5 |
| 25 | Chapter 3: Fine-Tuning + Chapter 4 start | 2.5 |
| 26 | Chapter 4: AI Safety (finish) + Exercises 1-4 | 2.5 |
| 27 | Chapter 5: Observability + Exercises 5-8 | 2.5 |
| 28 | Mini-project | 2.0 |

## Key Principle for This Stage

> **"Every LLM call costs money, takes time, and can produce harm. Engineer accordingly."**

This single principle drives every topic in Stage 3: cost control (MLOps), latency optimization (deployment), knowing when fine-tuning is worth it, preventing harm (safety), and knowing when things go wrong (observability).
