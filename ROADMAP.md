# 30-Day AI Engineering Curriculum — Master Roadmap

> **Start here. Return here daily.** This is your navigation document for the entire curriculum.
>
> **NOTE (2026-05-06):** This is the original 30-day sprint plan. The active schedule is now the
> 3-month master plan at `3_month_master_plan/MASTER_CURRICULUM.md`. These stage files remain
> your deep-reference library — use them for concepts and exercises, not as a day-by-day schedule.
>
> **You:** QA Engineer with 3 years TypeScript/Playwright + accessibility automation (WOS, 2023–2025),
> 4 months functional QA on production AI agents (WOSRI). Python is the primary skill gap.
> **Goal:** AI Validation Engineer → AI Systems Engineer → Full AI Engineer (evaluation & safety).
> **Active time budget:** 17 hrs/week × 12 weeks = 204 hrs (see 3-month master plan).

---

## 1. Visual Roadmap

```
YOU ARE HERE
    |
    v
┌─────────────────────────────────────────────────────────────────────────┐
│  STAGE 0: FOUNDATIONS (Days 1-3, ~7 hrs)                                │
│  ┌─────────────┐  ┌──────────────────┐  ┌────────────────────────────┐  │
│  │ Transformer  │  │ Tokens, Prompts, │  │ Why AI Testing !=          │  │
│  │ Architecture │->│ Temperature,     │->│ Traditional Testing        │  │
│  │ (mental      │  │ Sampling         │  │ (non-determinism,          │  │
│  │  model only) │  │                  │  │  stochastic outputs)       │  │
│  └─────────────┘  └──────────────────┘  └────────────────────────────┘  │
└──────────────────────────────┬──────────────────────────────────────────┘
                               |
                               v
┌─────────────────────────────────────────────────────────────────────────┐
│  STAGE 1: AI VALIDATION (Days 4-14, ~22 hrs)  *** CORE STAGE ***        │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │
│  │ Evaluation   │  │ LLM-as-Judge │  │ DeepEval &   │                   │
│  │ Taxonomy     │->│ Patterns     │->│ Frameworks   │                   │
│  │ (metrics,    │  │ (pointwise,  │  │ (setup, run, │                   │
│  │  dimensions) │  │  pairwise)   │  │  interpret)  │                   │
│  └──────┬───────┘  └──────────────┘  └──────┬───────┘                   │
│         |                                    |                           │
│         v                                    v                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │
│  │ Red Teaming  │  │ Agent Test   │  │ Structured   │                   │
│  │ & Adversarial│  │ Pyramid      │  │ Output       │                   │
│  │ Testing      │  │ (unit/integ/ │  │ Validation   │                   │
│  │              │  │  system)     │  │ (Pydantic)   │                   │
│  └──────────────┘  └──────────────┘  └──────────────┘                   │
└──────────────────────────────┬──────────────────────────────────────────┘
                               |
              ┌────────────────┼────────────────┐
              v                v                v
┌─────────────────────────────────────────────────────────────────────────┐
│  STAGE 2: AI SYSTEMS (Days 15-22, ~16 hrs)                              │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │
│  │ RAG Pipeline │  │ Function     │  │ Multi-Agent  │                   │
│  │ Design &     │  │ Calling &    │  │ Orchestration│                   │
│  │ Evaluation   │  │ Tool-Use     │  │ & MCP        │                   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                   │
│         |                 |                  |                           │
│         v                 v                  v                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │
│  │ Embedding &  │  │ Schema       │  │ Agent Comms  │                   │
│  │ Retrieval    │  │ Validation & │  │ Patterns &   │                   │
│  │ Metrics      │  │ Error Chains │  │ Failure Modes│                   │
│  └──────────────┘  └──────────────┘  └──────────────┘                   │
└──────────────────────────────┬──────────────────────────────────────────┘
                               |
                               v
┌─────────────────────────────────────────────────────────────────────────┐
│  STAGE 3: AI ENGINEERING (Days 23-28, ~13 hrs)                          │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │
│  │ Experiment   │  │ Cost Mgmt &  │  │ Safety       │                   │
│  │ Tracking &   │  │ Latency      │  │ Guardrails & │                   │
│  │ Observability│  │ Optimization │  │ Content      │                   │
│  │ (LangSmith,  │  │ (caching,    │  │ Filtering    │                   │
│  │  W&B)        │  │  model route)│  │              │                   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                   │
│         |                 |                  |                           │
│         v                 v                  v                           │
│  ┌──────────────────────────────────────────────────┐                   │
│  │        Evaluation CI/CD Pipeline Design          │                   │
│  │   (GitHub Actions + eval suite + gating logic)   │                   │
│  └──────────────────────────────────────────────────┘                   │
└──────────────────────────────┬──────────────────────────────────────────┘
                               |
                               v
┌─────────────────────────────────────────────────────────────────────────┐
│  STAGE 4: CAPSTONE PLANNING (Days 29-30, ~5 hrs)                        │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Architecture Document + MVP Plan + Implementation Roadmap       │   │
│  │  (Choose one capstone track below)                               │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│         ┌──────────────┐   ┌──────────────┐   ┌──────────────┐         │
│         │ TRACK A:     │   │ TRACK B:     │   │ TRACK C:     │         │
│         │ Eval         │   │ RAG Quality  │   │ Agent Safety │         │
│         │ Framework    │   │ System       │   │ Harness      │         │
│         │ (open-source │   │ (end-to-end  │   │ (red team +  │         │
│         │  eval tool)  │   │  RAG + eval) │   │  guardrails) │         │
│         └──────────────┘   └──────────────┘   └──────────────┘         │
└─────────────────────────────────────────────────────────────────────────┘
                               |
                               v
                    ┌─────────────────────┐
                    │  BEYOND 30 DAYS     │
                    │  Ship capstone,     │
                    │  open-source,       │
                    │  role transition    │
                    └─────────────────────┘
```

### Specialization Branches (Post-Curriculum)

```
                    After Stage 4, pick your lane:

    ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────────┐
    │  SAFETY &        │  │  AGENT           │  │  EVALUATION         │
    │  RED TEAMING     │  │  ENGINEERING      │  │  INFRASTRUCTURE     │
    │                  │  │                   │  │                     │
    │  - Adversarial   │  │  - Multi-agent    │  │  - Eval frameworks  │
    │    robustness    │  │    architectures  │  │  - CI/CD for LLMs   │
    │  - Alignment     │  │  - Tool ecosystems│  │  - Benchmarking     │
    │    testing       │  │  - MCP servers    │  │    infrastructure   │
    │  - Policy &      │  │  - Autonomous     │  │  - Dataset curation │
    │    compliance    │  │    workflows      │  │  - Regression       │
    │                  │  │                   │  │    detection        │
    │  Roles:          │  │  Roles:           │  │  Roles:             │
    │  AI Safety Eng   │  │  AI Systems Eng   │  │  ML/AI Test Eng     │
    │  Red Team Lead   │  │  Agent Developer  │  │  Eval Platform Eng  │
    └─────────────────┘  └──────────────────┘  └─────────────────────┘
```

---

## 2. 30-Day Schedule (Day-by-Day)

> **Legend:**
> - (W) = Weekday (~1.5 hrs)
> - (WE) = Weekend (~2.5 hrs)
> - `concepts.md#Section` = section of the concepts file to read
> - `exercises/` = hands-on exercises directory

---

### STAGE 0 — Foundations (Days 1-3, ~7 hrs)

#### Day 1 (W) — How LLMs Work | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 1: Transformer Architecture, Attention Mechanism, Tokenization |
| **Do** | Exercise 0.1: Token counting experiment — use `tiktoken` to tokenize 10 different prompts; observe how token counts differ between English, code, and multilingual text |
| **Time** | 0.75 hr reading, 0.75 hr exercise |
| **Checkpoint** | Can explain: "A transformer uses self-attention to weigh the relevance of every token against every other token. Tokens are sub-word units. GPT-4 uses BPE tokenization." |

#### Day 2 (W) — Inference Parameters & Prompting | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 2: Temperature, Top-p, Top-k, Frequency/Presence Penalties, System/User/Assistant roles, Prompt Engineering Basics |
| **Do** | Exercise 0.2: Parameter sweep — call the same prompt with temperature 0, 0.5, 1.0, 1.5; top_p 0.1 vs 0.9; log and compare outputs; write a 1-paragraph analysis |
| **Time** | 0.75 hr reading, 0.75 hr exercise |
| **Checkpoint** | Can explain: "Temperature controls randomness. At 0, output is deterministic. Top-p nucleus sampling truncates the probability distribution. For testing, temperature=0 reduces but does not eliminate non-determinism." |

#### Day 3 (WE) — Why AI Testing Is Different | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 3: Non-determinism in AI systems, Oracle Problem, Evaluation vs Testing distinction, AI Testing Taxonomy (unit/integration/system for AI), Shift from binary pass/fail to scored evaluation |
| **Do** | Exercise 0.3: Run the same prompt 20 times at temperature=0. Measure: exact match rate, semantic similarity (using an embedding model), BLEU/ROUGE scores. Write a short analysis of variance. |
| **Time** | 1 hr reading, 1.5 hrs exercise |
| **Checkpoint** | Can explain: "Traditional testing has deterministic oracles. AI testing requires statistical evaluation, reference-free metrics, and human-aligned scoring. The evaluation taxonomy includes faithfulness, relevance, coherence, harmlessness, and helpfulness." |

**Stage 0 Total: ~7 hrs** (3 hrs reading, 4 hrs exercises)

---

### STAGE 1 — AI Validation (Days 4-14, ~22 hrs) [CORE]

#### Day 4 (W) — Evaluation Taxonomy Deep Dive | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 4: Evaluation dimensions (faithfulness, relevance, coherence, safety, helpfulness), Metric types (reference-based vs reference-free), Human vs automated evaluation tradeoffs |
| **Do** | Exercise 1.1: Taxonomy mapping — given 10 example LLM outputs, manually classify evaluation failures by dimension. Create a decision tree: "Which metric do I use when?" |
| **Time** | 0.75 hr reading, 0.75 hr exercise |
| **Checkpoint** | Can draw the evaluation taxonomy from memory and pick the right metric for a given scenario. |

#### Day 5 (W) — LLM-as-Judge: Concept & Architecture | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 5: LLM-as-Judge pattern, Pointwise vs Pairwise vs Reference-based judging, Judge prompt design, Bias in LLM judges (position bias, verbosity bias, self-preference) |
| **Do** | Exercise 1.2: Build a minimal LLM-as-Judge — write a Python function that takes (question, answer, rubric) and returns a 1-5 score with reasoning, using OpenAI API. Test with 5 hand-crafted examples. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can explain pointwise vs pairwise judging and build a basic judge function from scratch. |

#### Day 6 (WE) — LLM-as-Judge: Advanced Patterns | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 5 continued: Multi-judge consensus, Calibration, Judge agreement metrics (Cohen's Kappa), Chain-of-thought judging, Cost optimization for judges |
| **Do** | Exercise 1.3: Extend your judge — implement pairwise comparison mode, add chain-of-thought reasoning extraction, measure inter-judge agreement by running 3 different judge prompts on the same 10 examples. Calculate Cohen's Kappa. |
| **Time** | 1 hr reading, 1.5 hrs exercise |
| **Checkpoint** | Can implement multi-judge consensus and calculate inter-judge reliability. |

#### Day 7 (WE) — DeepEval Framework Setup & Core Metrics | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 6: DeepEval overview, Metric types (G-Eval, faithfulness, answer relevancy, contextual precision/recall/relevancy, hallucination, toxicity, bias), Test case structure |
| **Do** | Exercise 1.4: Install DeepEval. Create a test suite with 15+ test cases covering at least 5 different metrics. Run against a real LLM. Analyze the results — which metrics correlate? Which are most sensitive? |
| **Time** | 0.75 hr reading, 1.75 hrs exercise |
| **Checkpoint** | Can set up DeepEval from scratch, configure metrics, run a test suite, and interpret metric scores. |

#### Day 8 (W) — Evaluation Datasets & Golden Sets | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 7: Golden dataset construction, Synthetic data generation for evals, Dataset versioning, Stratified sampling for eval sets, Edge case taxonomies |
| **Do** | Exercise 1.5: Build a golden evaluation dataset — 20 examples with human-annotated expected outputs, covering normal cases, edge cases, adversarial cases, and ambiguous cases. Store as structured JSON. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can design and construct a balanced evaluation dataset with proper coverage. |

#### Day 9 (W) — Red Teaming Fundamentals | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 8: Red teaming concepts, Attack taxonomies (prompt injection, jailbreaks, data extraction, goal hijacking), OWASP Top 10 for LLMs, Responsible disclosure |
| **Do** | Exercise 1.6: Create an attack taxonomy document — list 15 attack categories with 3 example prompts each. Test 5 attacks against a model and document results. |
| **Time** | 0.75 hr reading, 0.75 hr exercise |
| **Checkpoint** | Can name the OWASP Top 10 for LLMs and demonstrate 5 different attack categories. |

#### Day 10 (W) — Red Team Test Suite | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 8 continued: Automated red teaming, Garak framework, Red team evaluation metrics (attack success rate, defense bypass rate), Continuous red teaming in CI/CD |
| **Do** | Exercise 1.7: Build a red team test suite using your judge — automated prompt injection tests, jailbreak attempts, and content policy violations. Track attack success rate. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can run an automated red team suite and report attack success rates. |

#### Day 11 (W) — Agent Testing Pyramid | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 9: Agent testing pyramid (unit → integration → system), Testing tool calls in isolation, Mocking LLM responses, Testing agent loops and termination, State machine testing for agents |
| **Do** | Exercise 1.8: Build an agent test pyramid — write unit tests for a tool-calling agent (mock the LLM), integration tests (mock external tools, real LLM), and one system test (everything real). Use pytest. |
| **Time** | 0.75 hr reading, 0.75 hr exercise |
| **Checkpoint** | Can articulate the agent testing pyramid and write tests at each level. |

#### Day 12 (WE) — Structured Output Validation | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 10: Structured outputs (JSON mode, function calling schema enforcement), Pydantic validation for LLM outputs, Schema evolution and backward compatibility, Partial/streaming output validation |
| **Do** | Exercise 1.9: Build a structured output validation pipeline — define Pydantic models for 3 different LLM tasks, implement retry logic with schema repair, measure schema compliance rate across 50 calls. |
| **Time** | 0.75 hr reading, 1.75 hrs exercise |
| **Checkpoint** | Can enforce structured output via Pydantic, handle schema violations gracefully, and measure compliance rates. |

#### Day 13 (WE) — Stage 1 Mini-Project | 2.5 hrs
| | |
|---|---|
| **Read** | Review all Stage 1 notes |
| **Do** | **Mini-Project:** Build an "Eval-in-a-Box" — a self-contained evaluation toolkit that includes: (1) LLM-as-judge with configurable rubrics, (2) DeepEval integration with 5+ metrics, (3) Red team test suite with 10+ attacks, (4) Structured output validation, (5) HTML report generation. Run against a real use case (e.g., summarization or Q&A). |
| **Time** | 0.5 hr review, 2 hrs building |
| **Checkpoint** | Can demo a working evaluation toolkit end-to-end. |

#### Day 14 (W) — Stage 1 Review & Consolidation | 1.5 hrs
| | |
|---|---|
| **Read** | Re-read any weak areas from self-assessment |
| **Do** | Complete the Stage 1 Self-Assessment (see Section 3 milestones below). Write a 1-page summary: "What I learned in Stage 1 and how it applies to my current work." Identify 2 things you could apply at work immediately. |
| **Time** | 1.5 hrs |
| **Checkpoint** | Pass all Stage 1 milestone criteria (see Section 3). |

**Stage 1 Total: ~22 hrs** (7.5 hrs reading, 14.5 hrs exercises/projects)

---

### STAGE 2 — AI Systems (Days 15-22, ~16 hrs)

#### Day 15 (W) — RAG Architecture Fundamentals | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 11: RAG overview, Embedding models, Vector databases, Chunking strategies (fixed, semantic, recursive), Retrieval methods (dense, sparse, hybrid) |
| **Do** | Exercise 2.1: Build a minimal RAG pipeline — chunk 3 documents, embed with OpenAI embeddings, store in ChromaDB, query and generate answers. No frameworks — raw API calls only. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can explain RAG architecture and build a basic pipeline from scratch. |

#### Day 16 (W) — RAG Evaluation | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 12: RAG evaluation metrics (context precision, context recall, faithfulness, answer relevancy), RAGAS framework, Retrieval quality vs generation quality separation |
| **Do** | Exercise 2.2: Evaluate your RAG pipeline — use RAGAS metrics to score retrieval quality and generation quality separately. Create 10 test queries with ground truth. Identify the weakest component. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can evaluate a RAG system across retrieval and generation dimensions independently. |

#### Day 17 (W) — Advanced RAG Patterns | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 12 continued: Query rewriting, Re-ranking, Hypothetical Document Embeddings (HyDE), Multi-step retrieval, Metadata filtering, RAG failure modes |
| **Do** | Exercise 2.3: Implement query rewriting and re-ranking on top of your Day 15 pipeline. Measure improvement using the same RAGAS evaluation from Day 16. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can implement and measure the impact of advanced RAG techniques. |

#### Day 18 (WE) — Function Calling & Tool Use | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 13: Function calling mechanics (OpenAI, Anthropic), Tool definition schemas, Parallel function calls, Error handling in tool chains, Tool-use evaluation |
| **Do** | Exercise 2.4: Build an agent with 5 tools (web search, calculator, file reader, database query, API caller — can be mocked). Write tests for: correct tool selection, correct parameter extraction, error handling when tools fail, multi-step tool chains. |
| **Time** | 0.75 hr reading, 1.75 hrs exercise |
| **Checkpoint** | Can implement function calling with proper error handling and write tests for tool selection accuracy. |

#### Day 19 (WE) — Multi-Agent Systems | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 14: Multi-agent architectures (supervisor, peer-to-peer, hierarchical), Agent communication protocols, State management, Failure modes (infinite loops, deadlocks, cascading failures), Testing strategies for multi-agent systems |
| **Do** | Exercise 2.5: Design and implement a 3-agent system (researcher, writer, reviewer) using LangGraph or AutoGen. Test: Does the system converge? Does the reviewer actually improve outputs? Measure quality delta between 1 pass and 3 passes. |
| **Time** | 0.75 hr reading, 1.75 hrs exercise |
| **Checkpoint** | Can design a multi-agent system and test for convergence and quality improvement. |

#### Day 20 (W) — MCP (Model Context Protocol) | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 15: MCP specification, MCP servers and clients, Resource types, Tool exposure via MCP, Testing MCP integrations, MCP vs direct function calling tradeoffs |
| **Do** | Exercise 2.6: Build a simple MCP server that exposes 2-3 tools. Connect it to Claude Desktop or another MCP client. Write integration tests that validate the tool contracts through MCP. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can explain MCP, build a basic MCP server, and test tool contracts. |

#### Day 21 (W) — Stage 2 Mini-Project | 1.5 hrs
| | |
|---|---|
| **Read** | Review Stage 2 notes |
| **Do** | **Mini-Project:** Build a "RAG Quality Dashboard" — a RAG pipeline with: (1) configurable chunking, (2) RAGAS evaluation suite, (3) tool-calling agent for queries, (4) automated quality regression tests. Generate a quality report comparing 2 different chunking strategies. |
| **Time** | 0.25 hr review, 1.25 hrs building |
| **Checkpoint** | Can demo a RAG system with integrated quality evaluation. |

#### Day 22 (W) — Stage 2 Review & Consolidation | 1.5 hrs
| | |
|---|---|
| **Read** | Re-read weak areas |
| **Do** | Complete Stage 2 Self-Assessment. Write: "How RAG evaluation differs from general LLM evaluation." Identify 1 thing you could apply at work immediately. |
| **Time** | 1.5 hrs |
| **Checkpoint** | Pass all Stage 2 milestone criteria (see Section 3). |

**Stage 2 Total: ~16 hrs** (4.25 hrs reading, 11.75 hrs exercises/projects)

---

### STAGE 3 — AI Engineering (Days 23-28, ~13 hrs)

#### Day 23 (W) — Experiment Tracking & Observability | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 16: Experiment tracking (LangSmith, Weights & Biases, MLflow), Trace logging, Prompt versioning, A/B testing for prompts, Observability dashboards |
| **Do** | Exercise 3.1: Set up LangSmith (free tier). Instrument your Stage 1 eval toolkit with traces. Run 3 prompt variants through your eval suite. Compare results in the LangSmith dashboard. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can set up experiment tracking, log traces, and compare prompt variants systematically. |

#### Day 24 (W) — Cost Management & Optimization | 1.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 17: Token cost calculation, Caching strategies (semantic cache, exact cache), Model routing (cheap model for easy tasks, expensive for hard), Batching, Context window optimization, Cost monitoring and alerting |
| **Do** | Exercise 3.2: Implement a cost tracker — wrap your LLM calls to log token usage and cost. Implement semantic caching using embeddings. Measure: cache hit rate, cost savings, latency improvement. Implement model routing: use GPT-4o-mini for classification, GPT-4o for generation. |
| **Time** | 0.5 hr reading, 1 hr exercise |
| **Checkpoint** | Can implement caching, model routing, and measure cost impact. |

#### Day 25 (WE) — Safety Guardrails | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 18: Input guardrails (content filtering, PII detection, injection detection), Output guardrails (toxicity filtering, hallucination detection, format enforcement), Guardrail frameworks (Guardrails AI, NeMo Guardrails), Layered defense architecture |
| **Do** | Exercise 3.3: Build a guardrail pipeline — implement 3 input guards (PII detection, prompt injection detection, topic restriction) and 3 output guards (toxicity check, hallucination flag via NLI, schema enforcement). Measure false positive rate on 50 benign inputs. |
| **Time** | 0.75 hr reading, 1.75 hrs exercise |
| **Checkpoint** | Can build a multi-layer guardrail system and measure its precision/recall. |

#### Day 26 (WE) — Evaluation CI/CD Pipeline | 2.5 hrs
| | |
|---|---|
| **Read** | `concepts.md` Section 19: Eval-driven development, Evaluation in CI/CD (GitHub Actions), Gating logic (fail build if eval score drops), Regression detection, Eval dataset management in CI, Cost budgets for CI evals |
| **Do** | Exercise 3.4: Build a GitHub Actions workflow that: (1) runs your eval suite on every PR, (2) compares scores against a baseline, (3) fails the build if faithfulness drops >5%, (4) posts a quality report as a PR comment. Use a mock or cheap model to keep costs low. |
| **Time** | 0.75 hr reading, 1.75 hrs exercise |
| **Checkpoint** | Can design and implement an eval-gated CI/CD pipeline. |

#### Day 27 (W) — Stage 3 Mini-Project | 1.5 hrs
| | |
|---|---|
| **Read** | Review Stage 3 notes |
| **Do** | **Mini-Project:** Build an "LLM Production Readiness Checker" — a tool that evaluates an LLM application across: (1) quality (eval scores), (2) safety (guardrail pass rates), (3) cost (per-query cost estimate), (4) latency (p50/p95/p99). Outputs a go/no-go report. |
| **Time** | 0.25 hr review, 1.25 hrs building |
| **Checkpoint** | Can demo a production readiness assessment tool. |

#### Day 28 (W) — Stage 3 Review & Consolidation | 1.5 hrs
| | |
|---|---|
| **Read** | Re-read weak areas |
| **Do** | Complete Stage 3 Self-Assessment. Write: "My LLM production checklist" — a 1-page operational runbook. |
| **Time** | 1.5 hrs |
| **Checkpoint** | Pass all Stage 3 milestone criteria (see Section 3). |

**Stage 3 Total: ~13 hrs** (3.25 hrs reading, 9.75 hrs exercises/projects)

---

### STAGE 4 — Capstone Planning (Days 29-30, ~5 hrs)

#### Day 29 (WE) — Capstone Architecture | 2.5 hrs
| | |
|---|---|
| **Read** | Review all mini-project code and notes from Stages 1-3 |
| **Do** | Choose a capstone track (A, B, or C from the visual roadmap). Write an Architecture Decision Record (ADR): problem statement, chosen approach, alternatives considered, component diagram, tech stack, evaluation strategy. |
| **Time** | 0.5 hr review, 2 hrs architecture work |
| **Checkpoint** | Has a complete architecture document with clear component boundaries. |

#### Day 30 (WE) — MVP Plan & Implementation Start | 2.5 hrs
| | |
|---|---|
| **Read** | N/A |
| **Do** | Break capstone into 2-week sprints. Define Sprint 1 stories with acceptance criteria. Set up the repo (README, CI, project structure). Write the first integration test (test-first). Start building the core module. |
| **Time** | 2.5 hrs |
| **Checkpoint** | Has a GitHub repo with project structure, CI pipeline, first failing test, and a 2-week sprint plan. |

**Stage 4 Total: ~5 hrs**

---

## 3. Milestone Checkpoints with Pass Criteria

### Stage Gates

| Milestone | Day | Pass Criteria | Self-Test |
|-----------|-----|---------------|-----------|
| **M0: Foundations** | Day 3 | Can explain what a transformer is, how tokens work, why temperature matters, and what makes AI testing fundamentally different from traditional software testing. | Write a 1-paragraph explanation of each without looking at notes. If you can't, re-read. |
| **M1: AI Validation** | Day 14 | Can build an LLM-as-judge evaluator from scratch, run a DeepEval test suite with 5+ metrics, create and execute a red team test suite with 10+ attacks, explain the evaluation taxonomy, and validate structured outputs with Pydantic. | Demo your Eval-in-a-Box mini-project to someone (or rubber duck). If any component doesn't work end-to-end, fix it. |
| **M2: AI Systems** | Day 22 | Can build a RAG pipeline with evaluation, implement function calling with test coverage, design a multi-agent system, explain MCP, and measure retrieval quality separately from generation quality. | Given a new domain (e.g., legal docs), could you stand up a RAG + eval system in 4 hours? If not, review. |
| **M3: AI Engineering** | Day 28 | Can set up experiment tracking with LangSmith, implement semantic caching and model routing for cost control, build input/output safety guardrails, and design an evaluation-gated CI/CD pipeline. | Walk through your production readiness checker. Does it cover quality, safety, cost, and latency? |
| **M4: Capstone** | Day 30 | Has a capstone architecture document with component diagram, tech stack decisions, evaluation strategy, and a Sprint 1 plan with acceptance criteria. GitHub repo is initialized with CI. | Could a senior engineer read your ADR and understand what you're building and why? |

### Detailed Pass Criteria per Stage

**Stage 0 — You should be able to:**
- [ ] Sketch the transformer architecture (encoder-decoder, self-attention, feed-forward, positional encoding)
- [ ] Explain BPE tokenization and why "token" != "word"
- [ ] Explain temperature, top-p, top-k and when to use each
- [ ] List 3 reasons why AI testing is harder than traditional testing
- [ ] Define the difference between "evaluation" and "testing" for AI systems

**Stage 1 — You should be able to:**
- [ ] Build an LLM-as-judge with pointwise scoring from scratch (no framework)
- [ ] Explain and mitigate judge biases (position, verbosity, self-preference)
- [ ] Set up and run DeepEval with faithfulness, relevancy, hallucination, toxicity, and G-Eval metrics
- [ ] Construct a golden evaluation dataset with proper stratification
- [ ] Name and demonstrate 5 categories from OWASP Top 10 for LLMs
- [ ] Run automated red team attacks and measure attack success rate
- [ ] Draw the agent testing pyramid and explain each level
- [ ] Validate structured LLM outputs using Pydantic with retry and repair logic
- [ ] Explain when to use reference-based vs reference-free evaluation

**Stage 2 — You should be able to:**
- [ ] Build a RAG pipeline (chunk, embed, store, retrieve, generate) without frameworks
- [ ] Evaluate RAG with RAGAS metrics (context precision, recall, faithfulness, relevancy)
- [ ] Implement query rewriting and re-ranking; measure their impact
- [ ] Implement function calling with 5+ tools and write tests for tool selection accuracy
- [ ] Design a 3-agent system with defined communication protocol
- [ ] Build an MCP server and test tool contracts
- [ ] Explain failure modes of multi-agent systems (loops, deadlocks, cascading failures)

**Stage 3 — You should be able to:**
- [ ] Set up LangSmith for experiment tracking and prompt comparison
- [ ] Implement semantic caching and measure cache hit rate
- [ ] Implement model routing (cheap/expensive) based on task complexity
- [ ] Build 3 input guardrails and 3 output guardrails
- [ ] Measure guardrail false positive rate
- [ ] Build an eval-gated CI/CD pipeline in GitHub Actions
- [ ] Define gating thresholds and regression detection logic
- [ ] Write an LLM production readiness checklist

**Stage 4 — You should be able to:**
- [ ] Present a clear capstone architecture with component diagram
- [ ] Justify your tech stack choices with tradeoffs
- [ ] Define an evaluation strategy for your capstone
- [ ] Have a Sprint 1 plan with testable acceptance criteria
- [ ] Have a GitHub repo with CI, project structure, and first failing test

---

## 4. Top 5 Most In-Demand Skills (2024-2025)

### 1. LLM Evaluation & Testing
| | |
|---|---|
| **Where in curriculum** | Stage 1 (Days 4-14): evaluation taxonomy, LLM-as-judge, DeepEval, golden datasets |
| **Job titles** | AI Evaluation Engineer, LLM Quality Engineer, AI Test Architect |
| **Companies hiring** | Anthropic, OpenAI, Google DeepMind, Scale AI, Patronus AI, Braintrust, Arize AI, Weights & Biases |
| **Salary range (US)** | $150K-$250K base (IC), $180K-$300K+ total comp (senior) |
| **Why hot** | Every company deploying LLMs needs evaluation. Massive undersupply of engineers who understand both testing and LLMs. |

### 2. Agent / Tool-Use Testing
| | |
|---|---|
| **Where in curriculum** | Stage 1 (Day 11): agent testing pyramid; Stage 2 (Days 18-20): function calling, multi-agent, MCP |
| **Job titles** | AI Agent Engineer, Agent Reliability Engineer, Tool-Use Platform Engineer |
| **Companies hiring** | LangChain, CrewAI, Microsoft (AutoGen), Anthropic (MCP), Cognition (Devin), Adept AI |
| **Salary range (US)** | $160K-$260K base, $200K-$350K+ total comp |
| **Why hot** | 2024-2025 is the "year of agents." Every agent platform needs testing infrastructure. Almost no one has built this yet. |

### 3. RAG System Design & Evaluation
| | |
|---|---|
| **Where in curriculum** | Stage 2 (Days 15-17): RAG architecture, RAGAS evaluation, advanced RAG patterns |
| **Job titles** | RAG Engineer, AI Search Engineer, Knowledge System Engineer |
| **Companies hiring** | Pinecone, Weaviate, Cohere, Databricks, most enterprises deploying AI (financial services, legal tech, healthcare) |
| **Salary range (US)** | $140K-$230K base, $170K-$280K total comp |
| **Why hot** | RAG is the #1 pattern for enterprise LLM deployment. Quality evaluation of RAG systems is the bottleneck. |

### 4. AI Safety & Red Teaming
| | |
|---|---|
| **Where in curriculum** | Stage 1 (Days 9-10): red teaming; Stage 3 (Day 25): safety guardrails |
| **Job titles** | AI Red Team Engineer, AI Safety Engineer, Trust & Safety Engineer (AI), LLM Security Researcher |
| **Companies hiring** | Anthropic, OpenAI, Google DeepMind, Meta FAIR, RAND Corporation, NIST, HackerOne (AI), Trail of Bits |
| **Salary range (US)** | $160K-$280K base, $200K-$400K+ total comp (safety orgs pay premiums) |
| **Why hot** | Regulatory pressure (EU AI Act, Biden EO), increasing attack surface, executive/board-level visibility. Very few qualified practitioners. |

### 5. MLOps / LLMOps
| | |
|---|---|
| **Where in curriculum** | Stage 3 (Days 23-28): experiment tracking, cost management, CI/CD, guardrails, observability |
| **Job titles** | LLMOps Engineer, AI Platform Engineer, ML Infrastructure Engineer |
| **Companies hiring** | Datadog, New Relic, Arize AI, LangSmith, Humanloop, every large enterprise with AI teams |
| **Salary range (US)** | $150K-$240K base, $180K-$300K total comp |
| **Why hot** | The gap between "demo" and "production" for LLM apps is enormous. LLMOps is the bridge. |

> **Note on salary data:** Ranges are approximations based on publicly available data from Levels.fyi, Glassdoor, LinkedIn, and public postings as of early 2025. Actual compensation varies significantly by location, company stage, and experience level. Remote roles in this space are common, which compresses geographic differentials somewhat.

---

## 5. Recommended Certifications & Portfolio Projects

### Stage 1 — AI Validation

| Type | Recommendation |
|------|---------------|
| **Certificate** | DeepLearning.AI — "Building and Evaluating Advanced RAG Applications" (includes eval concepts); Coursera — "Generative AI with Large Language Models" by AWS + DeepLearning.AI |
| **Portfolio Project** | **Eval-in-a-Box** (your Stage 1 mini-project, polished): Open-source your LLM evaluation toolkit on GitHub. Include: README with architecture diagram, example usage, metric explanations, and CI. Target: 50+ stars demonstrates domain expertise. |
| **Stretch** | Contribute a new metric or judge prompt to the DeepEval open-source project. |

### Stage 2 — AI Systems

| Type | Recommendation |
|------|---------------|
| **Certificate** | LangChain Academy — "Introduction to LangGraph" (free); DeepLearning.AI — "LangChain for LLM Application Development"; DeepLearning.AI — "Building Agentic RAG with LlamaIndex" |
| **Portfolio Project** | **RAG Quality Benchmark**: Build and publish a RAG evaluation benchmark for a specific domain (e.g., technical documentation). Include multiple chunking strategies, retrieval methods, and quality comparisons. Publish results as a blog post or arXiv preprint. |
| **Stretch** | Build and publish an MCP server for a useful tool integration. The MCP ecosystem is young — early contributions get visibility. |

### Stage 3 — AI Engineering

| Type | Recommendation |
|------|---------------|
| **Certificate** | AWS Certified Machine Learning — Specialty (relevant portions on deployment, monitoring, cost); Google Cloud Professional Machine Learning Engineer; Weights & Biases "Effective MLOps" course (free) |
| **Portfolio Project** | **LLM Production Readiness Framework**: Package your Stage 3 mini-project as a reusable GitHub Action or Python package. "Run this on any LLM app to get a production readiness score." |
| **Stretch** | Write a technical blog post: "How We Evaluate LLMs in CI/CD" — practical content like this gets massive reach in 2024-2025. |

### Stage 4 — Capstone

| Type | Recommendation |
|------|---------------|
| **Portfolio Project** | Your capstone, polished and shipped. See the three tracks in the visual roadmap. Whichever you choose, ensure it has: (1) clear README, (2) working CI/CD, (3) eval suite, (4) demo/screenshots, (5) architecture documentation. |
| **Stretch** | Present your capstone at a local meetup or submit a talk proposal to a conference (AI Engineer Summit, MLOps Community, PyData). A 15-minute talk about your evaluation framework is more valuable than any certificate. |

---

## 6. Pareto Analysis — The Critical 20%

> **If you only have time for 20% of this curriculum, learn these 8 things. They deliver ~80% of the career value.**

### The Essential 8

| # | Concept | Why It Matters | Where to Learn | Time Investment |
|---|---------|---------------|----------------|-----------------|
| 1 | **LLM-as-a-Judge Evaluation** | The foundational pattern for automated LLM quality assessment. Used everywhere. You cannot do AI engineering without this. | Days 5-6, Exercises 1.2-1.3 | 4 hrs |
| 2 | **Agent Testing Pyramid** | Defines how to systematically test AI agents at every level. Your existing testing expertise makes this your highest-leverage skill. | Day 11, Exercise 1.8 | 1.5 hrs |
| 3 | **RAG Architecture + Evaluation** | RAG is the dominant enterprise AI pattern. Knowing how to build AND evaluate it makes you rare. | Days 15-17, Exercises 2.1-2.3 | 4.5 hrs |
| 4 | **Tool-Use / Function Calling Validation** | Agents are only as reliable as their tool calls. Testing tool selection, parameter extraction, and error handling is critical. | Day 18, Exercise 2.4 | 2.5 hrs |
| 5 | **Safety & Red Teaming** | The only skill on this list with regulatory drivers (EU AI Act). Demand will only increase. Hardest to hire for. | Days 9-10 + Day 25, Exercises 1.6-1.7 + 3.3 | 5.5 hrs |
| 6 | **Structured Output Validation** | Every production LLM app needs reliable structured outputs. Pydantic + schema enforcement is the standard pattern. | Day 12, Exercise 1.9 | 2.5 hrs |
| 7 | **Evaluation Pipeline Design (CI/CD)** | The bridge between "we test manually" and "quality is automated." This is what makes you an engineer, not just a tester. | Day 26, Exercise 3.4 | 2.5 hrs |
| 8 | **Cost Management** | Real-world constraint that determines if an AI project ships or gets cancelled. Caching + routing = immediate production impact. | Day 24, Exercise 3.2 | 1.5 hrs |

**Total for the Essential 8: ~24 hrs** (about half the total curriculum time)

### How to Prioritize If Time Is Short

```
If you have 1 week:   Learn #1 (LLM-as-Judge) and #2 (Agent Testing Pyramid)
If you have 2 weeks:  Add #3 (RAG) and #5 (Red Teaming)
If you have 3 weeks:  Add #4 (Tool-Use), #6 (Structured Outputs), #7 (CI/CD)
If you have 4 weeks:  Complete all 8 + mini-projects + capstone planning
```

---

## 7. Beyond 30 Days — Continuing Education Path

### Month 2-3: Build & Ship the Capstone

- **Week 5-6:** Implement core functionality (Sprint 1 from Day 30 plan)
- **Week 7-8:** Add evaluation suite, CI/CD, documentation
- **Week 9-10:** Polish, write a README that sells the project, deploy a demo
- **Week 11-12:** Write a blog post or create a short demo video
- **Goal:** A GitHub repo with 50+ stars or a blog post with 1000+ reads

### Month 3-6: Contribute to Open Source

Target one of these projects based on your specialization:
- **Evaluation:** DeepEval, RAGAS, Braintrust, Promptfoo
- **Agents:** LangGraph, CrewAI, AutoGen, Semantic Kernel
- **Safety:** Garak, NeMo Guardrails, Guardrails AI, LLM Guard
- **Infrastructure:** LiteLLM, LangFuse, OpenLLMetry

Contribution strategy:
1. Start with documentation improvements and bug fixes (week 1-2)
2. Add test coverage — your unique skill set makes this high-value (week 3-4)
3. Propose and implement a small feature (month 2+)
4. Aim for "contributor" status in at least one project

### Month 6+: Specialize

Pick one lane and go deep:

| Specialization | What to Do | Target Outcome |
|---------------|-----------|----------------|
| **Safety & Red Teaming** | Study alignment research, take Anthropic's safety courses, practice on HackAPrompt challenges, build a red team automation tool | Apply to AI Safety roles at Anthropic, OpenAI, Google DeepMind, or start an AI red team consultancy |
| **Agent Engineering** | Build increasingly complex agent systems, contribute to agent frameworks, study planning and reasoning architectures | Apply to agent platform teams or start building commercial agents |
| **Evaluation Infrastructure** | Build evaluation frameworks, study psychometrics (how to measure things reliably), contribute to benchmarking efforts | Apply to eval platform companies (Scale AI, Braintrust, Patronus) or build internal eval platforms |

### Year 1: Role Transition

Timeline for moving from SDET to AI Engineer:

```
Month 1:     Complete this curriculum (you are here)
Month 2-3:   Ship capstone, start contributing to open source
Month 4-5:   Apply internal transfer or start interviewing
              - Update resume: lead with AI evaluation + testing
              - LinkedIn: publish 2-3 posts about your projects
              - Target roles: "AI Evaluation Engineer," "AI Quality Engineer"
Month 6-8:   Land the role (internal transfer is faster)
Month 9-12:  Establish yourself in the new role, specialize further
```

**Key insight:** You don't need to wait until you're "ready." Your existing SDET experience + this curriculum makes you more qualified than most applicants for AI evaluation roles. The supply-demand gap is massive.

---

## 8. How to Use This Curriculum

### Read Order

For each day, follow this sequence:

```
1. ROADMAP.md    → Check today's plan (you're here)
2. concepts.md   → Read the assigned sections
3. live_examples/→ Study the code examples for today's topic
4. exercises/    → Do the hands-on exercise
5. ROADMAP.md    → Check off today's checkpoint
```

### Daily Routine (Weekdays, ~1.5 hrs)

```
[0:00 - 0:05]  Open ROADMAP.md, read today's plan
[0:05 - 0:35]  Read the concepts section (~30 min)
[0:35 - 1:20]  Do the exercise (~45 min)
[1:20 - 1:30]  Write 3 bullet points: what I learned, what confused me, what to review
```

### Daily Routine (Weekends, ~2.5 hrs)

```
[0:00 - 0:05]  Open ROADMAP.md, read today's plan
[0:05 - 0:50]  Read the concepts section (~45 min)
[0:50 - 2:20]  Do the exercise or mini-project (~90 min)
[2:20 - 2:30]  Write summary + update checklist
```

### When You're Stuck

Try these in order:

1. **Re-read the concepts.md section** — most confusion comes from skimming
2. **Look at live_examples/** — working code often clarifies what prose cannot
3. **Ask an LLM** — "Explain [concept] as if I'm an experienced software tester learning AI. Give me a concrete testing analogy."
4. **Search for the concept + "for engineers"** — skip the academic papers, find the practitioner blog posts
5. **Move on and come back** — some things click after you see them applied in a later exercise

### How to Know You're Ready to Move On

At the end of each stage, ask yourself these questions. If you can answer all of them without notes, move on. If not, spend 30 more minutes reviewing.

**Stage 0 self-test:**
- What is self-attention and why does it matter?
- Why does the same prompt sometimes give different results at temperature=0?
- Name 3 ways AI testing differs from REST API testing.

**Stage 1 self-test:**
- Build an LLM-as-judge from scratch in 15 minutes (timed).
- Given a new LLM use case, which 3 DeepEval metrics would you choose and why?
- Describe 5 attacks from the OWASP LLM Top 10.
- What's the difference between faithfulness and relevance?

**Stage 2 self-test:**
- Explain RAG to a non-technical PM in 2 minutes.
- What's the difference between context precision and context recall?
- When would you use MCP instead of direct function calling?
- Name 3 failure modes of multi-agent systems.

**Stage 3 self-test:**
- Design a cost-optimization strategy for an LLM app doing 10K queries/day.
- What guardrails would you put on a customer-facing chatbot? (Name 5+)
- Sketch the GitHub Actions workflow for eval-gated deployment.

### Progress Tracking

Copy this checklist into a file and check items as you complete them:

```
## Daily Progress

### Stage 0: Foundations
- [ ] Day 1: Transformers & Tokenization
- [ ] Day 2: Inference Parameters & Prompting
- [ ] Day 3: Why AI Testing Is Different
- [ ] **MILESTONE M0 PASSED**

### Stage 1: AI Validation [CORE]
- [ ] Day 4: Evaluation Taxonomy
- [ ] Day 5: LLM-as-Judge Concept
- [ ] Day 6: LLM-as-Judge Advanced
- [ ] Day 7: DeepEval Setup
- [ ] Day 8: Evaluation Datasets
- [ ] Day 9: Red Teaming Fundamentals
- [ ] Day 10: Red Team Test Suite
- [ ] Day 11: Agent Testing Pyramid
- [ ] Day 12: Structured Output Validation
- [ ] Day 13: Stage 1 Mini-Project
- [ ] Day 14: Stage 1 Review
- [ ] **MILESTONE M1 PASSED**

### Stage 2: AI Systems
- [ ] Day 15: RAG Fundamentals
- [ ] Day 16: RAG Evaluation
- [ ] Day 17: Advanced RAG
- [ ] Day 18: Function Calling & Tool Use
- [ ] Day 19: Multi-Agent Systems
- [ ] Day 20: MCP
- [ ] Day 21: Stage 2 Mini-Project
- [ ] Day 22: Stage 2 Review
- [ ] **MILESTONE M2 PASSED**

### Stage 3: AI Engineering
- [ ] Day 23: Experiment Tracking
- [ ] Day 24: Cost Management
- [ ] Day 25: Safety Guardrails
- [ ] Day 26: Evaluation CI/CD
- [ ] Day 27: Stage 3 Mini-Project
- [ ] Day 28: Stage 3 Review
- [ ] **MILESTONE M3 PASSED**

### Stage 4: Capstone Planning
- [ ] Day 29: Architecture Document
- [ ] Day 30: MVP Plan & Repo Setup
- [ ] **MILESTONE M4 PASSED**
```

---

> **You already know how to test software. Now you're learning how to test intelligence.**
> **That's one of the most valuable skills in the industry right now. Trust the process.**
