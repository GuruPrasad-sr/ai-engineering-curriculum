---
tags: [progress, tracker]
---

# Progress Tracker

> Check off each item as you complete it. Return to [[HOME]] after each session.
> See [[ROADMAP]] for the full day-by-day schedule with time estimates.

---

## Stage 0: Foundations (Days 1–3, ~7 hrs)

### Day 1 — How LLMs Work (~2.5 hrs)
- [ ] Read [[stage_0_foundations/concepts]] Ch 1.1: What is a Neural Network?
- [ ] Read Ch 1.2: What is a Transformer?
- [ ] Read Ch 1.3: Tokens and Tokenization
- [ ] Read Ch 1.4: Context Window
- [ ] Read Ch 1.5: Embeddings
- [ ] Read Ch 1.6: Inference Pipeline
- [ ] Exercise: Decode your conductor's config (30 min)
- [ ] Exercise: Temperature experiment (30 min)

### Day 2 — Inference Parameters & Prompting (~1.5 hrs)
- [ ] Read Ch 2: Temperature, Top-p, Top-k, Penalties
- [ ] Read Ch 2: System/User/Assistant roles
- [ ] Read Ch 2: Prompt engineering basics
- [ ] Exercise: Parameter sweep (temp 0 / 0.5 / 1.0 / 1.5)
- [ ] Exercise: Role comparison experiment

### Day 3 — Why AI Testing Is Different (~2.5 hrs)
- [ ] Read Ch 3: Non-determinism in AI systems
- [ ] Read Ch 3: The Oracle Problem
- [ ] Read Ch 3: Evaluation vs Testing distinction
- [ ] Read Ch 3: AI Testing Taxonomy
- [ ] Read Ch 4: Failure modes (hallucination, refusal, drift)
- [ ] Exercise: Run same prompt 20× at temp=0, measure variance
- [ ] **Mini-project: [[stage_0_foundations/mini_project/PROJECT|LLM Variance Analysis Report]]**
- [ ] Checklist in exercises/day1_to_day3.md: all 7 boxes green

**Stage 0 complete?** → Proceed to Stage 1

---

## Stage 1: AI Validation (Days 4–14, ~22 hrs) ⭐ CORE

### Day 4 — Evaluation Taxonomy (~1.5 hrs)
- [ ] Read [[stage_1_ai_validation/concepts]] Ch 1: The Evaluation Problem
- [ ] Read Ch 1: Evaluation dimensions (faithfulness, relevance, coherence, safety, helpfulness)
- [ ] Read Ch 1: Metric types (reference-based vs reference-free)
- [ ] Exercise 1.1: Taxonomy mapping (10 example outputs)

### Day 5 — LLM-as-a-Judge Pt 1 (~1.5 hrs)
- [ ] Read Ch 2: LLM-as-Judge patterns
- [ ] Read Ch 2: Pointwise scoring
- [ ] Read Ch 2: Rubric design
- [ ] Exercise 1.2: Build a 4-dimension rubric for your Impact Agent

### Day 6 — LLM-as-a-Judge Pt 2 + Frameworks intro (~2 hrs)
- [ ] Read Ch 2: Pairwise comparison
- [ ] Read Ch 2: Bias sources in LLM judges
- [ ] Read Ch 3: DeepEval setup
- [ ] Exercise 1.3: Run DeepEval on 5 of your gold questions

### Day 7 — Evaluation Frameworks (~2 hrs)
- [ ] Read Ch 3: G-Eval, RAGAS
- [ ] Read Ch 3: Promptfoo
- [ ] Read Ch 3: When to use which framework
- [ ] Exercise 1.4: Compare DeepEval vs RAGAS on the same test case

### Day 8 — Agent Testing Pt 1 (~1.5 hrs)
- [ ] Read Ch 4: The Agent Test Pyramid
- [ ] Read Ch 4: Tool invocation testing
- [ ] Read Ch 4: Unit tests for prompts
- [ ] Exercise 1.5: Write unit tests for 3 conductor tools

### Day 9 — Agent Testing Pt 2 (~1.5 hrs)
- [ ] Read Ch 4: Multi-agent handoff testing
- [ ] Read Ch 4: Integration testing patterns
- [ ] Read Ch 4: System-level evaluation
- [ ] Exercise 1.6: Write integration tests for conductor → app routing

### Day 10 — Structured Output Validation (~1.5 hrs)
- [ ] Read Ch 4: Structured output validation (Pydantic)
- [ ] Read Ch 4: JSON schema contracts
- [ ] Exercise 1.7: Write Pydantic validators for AppSelectorTool output

### Day 11 — Red Teaming (~2 hrs)
- [ ] Read Ch 5: Red teaming taxonomy
- [ ] Read Ch 5: Prompt injection, jailbreaks, off-topic
- [ ] Read Ch 5: Adversarial dataset design
- [ ] Exercise 1.8: Build 10-case red team suite for RI Assistant guardrails

### Day 12 — Evaluation Pipelines (~2 hrs)
- [ ] Read Ch 6: CI/CD evaluation pipelines
- [ ] Read Ch 6: Pass/fail gates and thresholds
- [ ] Read Ch 6: HTML reporting
- [ ] Exercise 1.9: Configure pipeline with GitHub Actions YAML

### Days 13–14 — Mini-Project (~4–6 hrs)
- [ ] Part 1: Custom DeepEval metrics (5 metrics for Impact Agent)
- [ ] Part 2: LLM-as-Judge rubric (4-dimension)
- [ ] Part 3: Red team test suite (10 cases)
- [ ] Part 4: HTML report generation
- [ ] Part 5: CI pass/fail gate
- [ ] **[[stage_1_ai_validation/mini_project/PROJECT|Mini-project complete]]**

**Stage 1 complete?** → Proceed to Stage 2

---

## Stage 2: AI Systems (Days 15–22, ~16 hrs)

### Day 15 — RAG Pt 1 (~2 hrs)
- [ ] Read [[stage_2_ai_systems/concepts]] Ch 1.1–1.3: RAG fundamentals + embeddings
- [ ] Exercise: Map normalizer architecture to RAG pattern

### Day 16 — RAG Pt 2 (~2 hrs)
- [ ] Read Ch 1.4–1.6: Vector DBs, chunking, advanced RAG
- [ ] Exercise: Implement basic vector search with ChromaDB

### Day 17 — Agent Architecture Pt 1 (~2 hrs)
- [ ] Read Ch 2.1–2.2: Agent fundamentals + components
- [ ] Exercise: Draw conductor architecture with ReAct pattern overlay

### Day 18 — Agent Architecture Pt 2 (~2 hrs)
- [ ] Read Ch 2.3–2.4: Tool use + multi-agent systems
- [ ] Exercise: Implement a 3-tool agent from scratch

### Day 19 — Orchestration (~2 hrs)
- [ ] Read Ch 2.5: Agent memory
- [ ] Read Ch 3: Orchestration patterns (sequential, parallel, hierarchical)
- [ ] Exercise: Trace a multi-agent conversation in conductor logs

### Day 20 — MCP (~1.5 hrs)
- [ ] Read Ch 4: Model Context Protocol
- [ ] Exercise: Inspect agai-api MCP server definitions

### Day 21 — Prompt Engineering (~1.5 hrs)
- [ ] Read Ch 5: Advanced prompt engineering
- [ ] Exercise: Refactor one conductor persona file using learned patterns

### Day 22 — Mini-Project (~3–5 hrs)
- [ ] **[[stage_2_ai_systems/mini_project/PROJECT|RAG-Powered Research Assistant complete]]**

**Stage 2 complete?** → Proceed to Stage 3

---

## Stage 3: AI Engineering (Days 23–28, ~13 hrs)

### Day 23 — MLOps (~2 hrs)
- [ ] Read [[stage_3_ai_engineering/concepts]] Ch 1: MLOps for LLM Systems
- [ ] Exercise 1: Set up MLflow experiment tracking

### Day 24 — Deployment (~2 hrs)
- [ ] Read Ch 2: Deployment patterns, caching, rate limiting
- [ ] Exercise 2: Implement semantic cache

### Day 25 — Cost & Latency (~1.5 hrs)
- [ ] Read Ch 2: Cost management and model routing
- [ ] Exercise 3: Calculate token cost for 5 conductor scenarios

### Day 26 — Fine-Tuning (~1.5 hrs)
- [ ] Read Ch 3: Fine-tuning overview
- [ ] Exercise 4: Evaluate whether fine-tuning vs prompting fits your use case

### Day 27 — Safety & Alignment (~2 hrs)
- [ ] Read Ch 4: AI Safety fundamentals
- [ ] Read Ch 4: Guardrails implementation
- [ ] Exercise 5: Audit RI Assistant guardrails against OWASP LLM Top 10

### Day 28 — Observability + Mini-Project (~3–5 hrs)
- [ ] Read Ch 5: Observability and monitoring
- [ ] Exercise 6: Add structured LLM logging to your RAG assistant
- [ ] **[[stage_3_ai_engineering/mini_project/PROJECT|Production AI Agent with Safety Guardrails complete]]**

**Stage 3 complete?** → Proceed to Stage 4

---

## Stage 4: Capstone (Days 29–30, ~5 hrs)

### Day 29 — Architecture & Design (~2.5 hrs)
- [ ] Read [[stage_4_expert_capstone/concepts]] — advanced patterns
- [ ] Exercise: Competitive analysis (3 existing eval frameworks)
- [ ] Exercise: Architecture decision record (ADR) for EvalForge
- [ ] Exercise: Component diagram

### Day 30 — MVP Plan (~2.5 hrs)
- [ ] Exercise: Define MVP scope (what's in v0.1)
- [ ] Exercise: Write Sprint 1 tickets (acceptance criteria)
- [ ] Exercise: Repository setup + CI skeleton
- [ ] **[[stage_4_expert_capstone/mini_project/CAPSTONE_SPEC|EvalForge capstone spec reviewed]]**
- [ ] GitHub repo initialized with README + CI

**30-day curriculum complete.**

---

## Completion Summary

| Stage | Complete? | Date | Notes |
|-------|-----------|------|-------|
| Stage 0 | | | |
| Stage 1 | | | |
| Stage 2 | | | |
| Stage 3 | | | |
| Stage 4 | | | |
