---
tags: [stage1, ai-validation, curriculum, core]
stage: 1
days: "4-14"
hours: 22
status: not-started
---

# Stage 1: AI Validation Engineering — Core Competency

> **This is the stage that makes you employable.** Everything here maps directly to
> what companies pay AI Validation Engineers to do every day.

---

## What This Stage Is

You already know how to test software. You write Playwright E2E tests, API contract
tests, and YAML-driven agent tests. You use LLM-as-judge and fractional scoring.

This stage takes those skills and builds the **theoretical foundation and industry
tooling** underneath them. When you finish, you won't just be someone who tests AI
systems — you'll be someone who can **design evaluation strategies** for any
LLM-powered product.

Think of it this way: right now you're a skilled carpenter who builds solid furniture.
This stage teaches you architecture — so you can design the whole building.

---

## Learning Outcomes

After completing this stage, you will be able to:

1. **Explain** why traditional testing breaks for LLM systems and what replaces it
2. **Design** LLM-as-a-Judge evaluations with multi-dimensional rubrics
3. **Use** industry-standard evaluation frameworks (DeepEval, RAGAS, Promptfoo)
4. **Test** agentic systems at every level — from prompts to multi-agent handoffs
5. **Build** red team test suites that find safety and security vulnerabilities
6. **Create** evaluation pipelines that run in CI/CD and produce actionable reports
7. **Speak the language** of AI evaluation in interviews and architecture discussions

---

## Time Commitment

| Item | Hours | Days |
|------|-------|------|
| Chapter 1: The Evaluation Problem | 2-3 | Day 4 |
| Chapter 2: LLM-as-a-Judge | 3-4 | Days 5-6 |
| Chapter 3: Evaluation Frameworks | 3-4 | Days 6-7 |
| Chapter 4: Testing Agentic Systems | 3-4 | Days 8-9 |
| Chapter 5: Prompt Testing & Red Teaming | 2-3 | Days 10-11 |
| Chapter 6: Building Evaluation Pipelines | 2-3 | Day 12 |
| Exercises (10 hands-on) | 4-6 | Days 4-13 (interleaved) |
| Mini-Project | 4-6 | Days 12-14 |
| **Total** | **~20-24** | **Days 4-14** |

---

## Structure

```
stage_1_ai_validation/
  README.md              ← You are here
  concepts.md            ← The textbook (6 chapters, read cover-to-cover)
  live_examples.md       ← Every concept mapped to YOUR workspace repos
  exercises/
    week1_exercises.md   ← 10 hands-on exercises
  mini_project/
    PROJECT.md           ← Capstone: full evaluation suite for Impact Agent
  resources.md           ← Papers, tools, courses, communities
```

---

## How to Use This

1. **Read one chapter per day** from `concepts.md`. Don't rush — the analogies and
   first principles matter more than memorizing tool APIs.
2. **Cross-reference** with `live_examples.md` as you read. Seeing concepts in YOUR
   codebase makes them stick.
3. **Do 1-2 exercises** from `exercises/week1_exercises.md` after each chapter pair.
4. **Start the mini-project** on Day 12. It synthesizes everything.
5. **Use `resources.md`** to go deeper on any topic that interests you.

---

## Prerequisites

- [x] You can write YAML test specs for platform-agent-testing
- [x] You understand `--enable-llm-judge` and `agent_must`
- [x] You can run Playwright and API tests
- [x] You've worked with the conductor, normalizer, and AGAI gateway
- [x] You understand fractional scoring

If any of these are shaky, review Stage 0 (Foundations) first.

---

## The One Sentence That Matters

> **AI Validation Engineering is the discipline of measuring whether an AI system
> is good enough — reliably, automatically, and at scale.**

Everything in this stage serves that sentence.
