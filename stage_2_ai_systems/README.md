---
tags: [stage2, ai-systems, curriculum, rag, agents]
stage: 2
days: "15-22"
hours: 16
status: not-started
---

# Stage 2: AI Systems — RAG, Agents, Tool-Use, Memory, Orchestration

> **Days 15–22 of 30 | ~14–18 hours | Prerequisites: Stage 0 (LLM Fundamentals) + Stage 1 (AI Validation)**

---

## Why This Stage Exists

In Stage 0 you learned how LLMs work. In Stage 1 you learned how to validate them.
Now you learn how to **build** the systems you've been testing.

You already work with these systems daily — your conductor orchestrates agents, your normalizer is a RAG pipeline, your AGAI platform manages 37+ tools and MCP servers. This stage gives you the **first-principles understanding** of *why* those systems are designed the way they are, so you can reason about them, debug them, and improve them — not just test them.

---

## What You'll Learn

| Chapter | Core Concept | Your Workspace Connection |
|---------|-------------|--------------------------|
| 1 | **Retrieval-Augmented Generation (RAG)** | `wos-ai-normalizer` — Elasticsearch + LLM reranking |
| 2 | **Agent Architecture** | `wos-ri-conductor` — multi-agent orchestration with 7+ apps |
| 3 | **Orchestration Patterns** | `Conductor` class, SSE streaming, error handling |
| 4 | **Model Context Protocol (MCP)** | `agai-api` — MCP servers (Alma, Primo), OAuth, admin |
| 5 | **Prompt Engineering** | 14 persona files, AppSelectorTool, QueryParserTool |

---

## Time Budget

| Day | Hours | Focus |
|-----|-------|-------|
| 15 | 2h | Ch 1.1–1.3: RAG fundamentals + embeddings |
| 16 | 2h | Ch 1.4–1.6: Vector DBs, chunking, advanced RAG |
| 17 | 2h | Ch 2.1–2.2: Agent fundamentals + components |
| 18 | 2h | Ch 2.3–2.4: Tool use + multi-agent systems |
| 19 | 2h | Ch 2.5 + Ch 3: Agent memory + orchestration |
| 20 | 1.5h | Ch 4: MCP |
| 21 | 1.5h | Ch 5: Prompt engineering |
| 22 | 3–5h | Exercises + mini-project |

---

## Files in This Stage

| File | Purpose |
|------|---------|
| [`concepts.md`](concepts.md) | Comprehensive textbook — read cover-to-cover AND use as reference |
| [`live_examples.md`](live_examples.md) | Every concept mapped to specific workspace files with paths and line numbers |
| [`exercises/week3_exercises.md`](exercises/week3_exercises.md) | 10 hands-on exercises |
| [`resources.md`](resources.md) | Curated external learning resources (2024–2025) |
| [`mini_project/PROJECT.md`](mini_project/PROJECT.md) | Capstone: Build a RAG-Powered Research Assistant |

---

## How to Use This Material

1. **Read `concepts.md` sequentially** — it's designed as a textbook with each chapter building on the last
2. **Cross-reference `live_examples.md`** — after each section, open the linked files in your IDE and study the real code
3. **Do the exercises** — they're ordered by difficulty and map directly to your workspace
4. **Build the mini-project** — it synthesizes everything into one deployable system
5. **Items marked `[PARETO-20]`** are the critical 20% that drive 80% of your understanding — prioritize these if short on time

---

## The Mental Model Shift

```
Before this stage:  "I test AI systems"
After this stage:   "I understand how AI systems are built, so I test them better
                     AND I can build them myself"
```

The best SDETs don't just validate outputs — they understand the architecture deeply enough to predict *where* failures will occur and *why*.
