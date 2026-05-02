---
tags: [stage0, foundations, curriculum]
stage: 0
days: "1-3"
hours: 7
status: not-started
---

# Stage 0: Foundations — Bridging from SDET to AI Engineer

## What This Stage Is (and Isn't)

You already know how to build and test software. You write Python, TypeScript, Playwright tests, BDD scenarios, FastAPI services, and API tests daily. **This stage does NOT re-teach any of that.**

Instead, this stage fills the *specific gaps* between "experienced SDET" and "someone who understands AI systems well enough to test, build, and reason about them." Think of it as upgrading your mental model — you already have the engine, we're adding a new transmission.

---

## Prerequisites (Your Skip List)

You already know these — we won't cover them:

| Skill | Status |
|---|---|
| Python (intermediate+) | You write it daily |
| TypeScript | Playwright, BFF work |
| REST APIs & HTTP | You test them constantly |
| pytest, Playwright, Cucumber BDD | Your testing toolkit |
| FastAPI | You build services with it |
| REST-Assured / API testing | Core competency |
| Elasticsearch basics | You query it for test data |
| Git, CI/CD, Docker basics | Standard dev workflow |

---

## What You'll Be Able to DO After This Stage

By the end of Day 3, you will:

1. **Explain how an LLM works** to a colleague — from tokens to transformer to output — without hand-waving
2. **Read any LLM API call** in your conductor codebase and understand every parameter (temperature, max_tokens, response_format, tools, etc.)
3. **Identify why AI testing is fundamentally different** from traditional testing and articulate the 3 core challenges (non-determinism, evaluation, prompt sensitivity)
4. **Map your existing work** to the AI testing landscape — you'll see that you're already further along than you think
5. **Send raw LLM API calls** yourself and predict how parameter changes affect output
6. **Count tokens and estimate costs** for any prompt

---

## Time Estimate

| Day | Focus | Time |
|---|---|---|
| Day 1 | Chapter 1 — How LLMs Work | ~2.5 hours |
| Day 2 | Chapter 2 & 3 — LLM APIs + AI System Differences | ~2.5 hours |
| Day 3 | Chapter 4 + Exercises + Mini-project | ~2.5 hours |

**Total: 6–8 hours over 3 days**

---

## How to Use This Stage

### The Learning Loop

```
1. READ concepts.md     → Understand the "why" and "what"
2. READ live_examples.md → See it in YOUR workspace code
3. DO exercises          → Build muscle memory
4. CHECK resources.md    → Go deeper on anything that clicked
```

### Reading Strategy

- **First pass:** Read concepts.md straight through like a textbook. Don't worry about memorizing — focus on the analogies and first principles.
- **Second pass:** Open live_examples.md side-by-side with your actual codebase. Find each concept in real code.
- **Third pass:** Do the exercises. This is where learning actually happens.

### Look for These Markers

- **[PARETO 80/20]** — These concepts give you outsized returns. Learn these deeply.
- **"What problem does this solve?"** — The WHY before the HOW.
- **"Connection to your workspace"** — Bridges to code you already work with.
- **"First principle to remember"** — The one sentence to tattoo on your brain.

---

## Files in This Stage

| File | Purpose |
|---|---|
| `concepts.md` | The textbook — all 4 chapters of foundational knowledge |
| `live_examples.md` | Every concept mapped to real code in your workspace |
| `exercises/day1_to_day3.md` | Hands-on exercises for each day |
| `resources.md` | Curated external learning resources (2024–2025) |
| `mini_project/PROJECT.md` | Day 3 capstone — LLM variance analysis report |

---

## A Note on Mindset

The biggest shift in moving from traditional software to AI systems isn't technical — it's philosophical. In traditional software, we expect **determinism**: same input, same output, every time. In AI systems, **non-determinism is a feature, not a bug.** Your job isn't to eliminate it — it's to understand it, bound it, and test within those bounds.

You're already doing this in your workspace. This stage just gives you the vocabulary and mental models to do it deliberately.

Let's begin.
