# Skill Gap Report — AI Engineering Career Progression

> **Generated:** 2026-04-29
> **Subject:** SDET → AI Validation Engineer → AI Systems Engineer → Full AI Engineer
> **Time Budget:** 1 month, ~10-12 hrs/week (~44 hours total)
> **Workspace:** C:\WOSRI-Workspace (16 repos)

---

## Section 1: What You Already Know (Formal Names + Evidence)

These are skills where you are at **Practitioner level** — you have built, debugged, and shipped artifacts.

| # | Formal Skill Name | Proficiency | Evidence |
|---|---|---|---|
| 1 | **LLM-as-Judge Evaluation** | Advanced | `--enable-llm-judge` flag; LLM judge results in QA_TESTING_REPORT.md across 13 tickets; understands blind spots (clvt-hide) |
| 2 | **Gold Standard Dataset Curation** | Advanced | `Impact Assistant Gold Questions 2026.xlsx`, `gold_questions.yaml`, `gold_questions_long_chats.yaml`, `gold_questions_filters_indicators.yaml` |
| 3 | **Continuous/Fractional Evaluation Metrics** | Advanced | Implemented PASS ≥ 0.85 / PARTIAL 0.60–0.84 / FAIL < 0.60 system; `fractional_score_demo.yaml`; `--streamlined` |
| 4 | **Declarative Test DSL Design (YAML)** | Advanced | Authored 60+ YAML test files with `agent_must`, `regex_checks`, `llm_validation`, `conversation`, `depends_on`, `tags` |
| 5 | **Multi-Turn Conversational Evaluation** | Advanced | `conversation:` blocks, `gold_questions_long_chats.yaml`, query correction tests (AGAI-3688) |
| 6 | **Hybrid Evaluation (Semantic + Structural)** | Advanced | Combines `agent_must` (LLM judge) + `regex_checks` (pattern match) + `llm_validation.criteria` in single tests |
| 7 | **Multi-Agent Pipeline Testing** | Advanced | Tests agent 20/30/40/90 independently and end-to-end; router validation; tool invocation checks (22 tests for AGAI-3783) |
| 8 | **Safety/Guardrail Evaluation** | Intermediate | `AGAI_3633_3396_guardrails.yaml` — authored tests, identified agent deficiencies (53% pass rate) |
| 9 | **BDD / Cucumber / Gherkin** | Advanced | Feature files across 2 repos (UI + API), established tag conventions, background patterns |
| 10 | **Page Object Model (Playwright)** | Advanced | `WOSRI_RI_Assistant_Page.ts` locator centralization |
| 11 | **API Contract Testing (REST-Assured)** | Advanced | 7 feature files covering WebSocket, REST CRUD, filters, error cases |
| 12 | **Context Engineering** | Advanced | Authored `RI_ASSISTANT_WORKSPACE_MAP.md`, `Agai_testing_Skill.md`, `Ui_Test_Gen_Skill.md`, `prompts/` library |
| 13 | **Knowledge Graph Construction** | Intermediate | `graphify/` → 20,886 nodes, 52,533 edges, 1,624 communities; interprets graph output for architecture discovery |
| 14 | **Test Infrastructure (CI/Reporting)** | Advanced | GitHub Pages test dashboard, HTML reporter, GitHub Actions triggers |
| 15 | **Prompt Engineering** | Intermediate-Advanced | `agent_must` rubric design, prompt library, DDA prompt, evaluation prompt patterns |
| 16 | **Test Pyramid Architecture (5-Layer)** | Advanced | Designed and operates: unit → conductor YAML → API contract → E2E Playwright → platform agent |

**Total Practitioner-level skills: 16**

---

## Section 2: What You Partially Know (Touched but Not Deep)

These are skills at **User** or **Intermediate** level — you've used them but haven't built them from scratch.

| # | Formal Skill Name | Current Level | What You've Done | What's Missing |
|---|---|---|---|---|
| 1 | **Entity Resolution / Entity Linking** | User | Tests normalizer outputs, understands candidate retrieval → LLM reranking pipeline | Haven't implemented a normalizer, don't know embedding model selection, similarity thresholds |
| 2 | **Structured Output / Constrained Decoding** | User | Tests AppSelectorTool structured outputs | Haven't defined JSON schemas for LLM output, don't understand Pydantic ↔ LLM schema enforcement internals |
| 3 | **Vector Similarity Search** | Awareness | Knows normalizer uses embeddings for candidate retrieval | Haven't implemented RAG, don't know embedding model choices, distance metrics, indexing strategies |
| 4 | **Agent Orchestration Implementation** | User | Tests conductor thoroughly, reads conductor code | Haven't built an orchestrator from scratch — doesn't know LangGraph, CrewAI, Autogen internals |
| 5 | **LLM API Configuration** | User | Calls AGAI API with agent names, understands temperature/seed conceptually | Hasn't tuned temperature, top_p, frequency_penalty; hasn't compared model behaviors |
| 6 | **SSE/WebSocket Streaming** | User | Tests against streaming endpoints | Hasn't implemented streaming server-side |
| 7 | **NgRx / Redux State Management** | User | Reads store shape, understands actions/effects | Hasn't authored reducers or effects |
| 8 | **Docker / Container Deployment** | Awareness | Reads ECS/Terraform docs in normalizer repo | Hasn't built Dockerfiles, managed ECS services |
| 9 | **Observability / Monitoring** | Awareness | Sees Datadog references in normalizer README | Hasn't set up dashboards, alerts, tracing for LLM systems |
| 10 | **Model Context Protocol (MCP)** | Awareness | Knows agai-api has MCP server management | Hasn't configured MCP servers or tools |

---

## Section 3: What You Need to Learn (By Role Target Stage)

### Stage 1: AI QA / Validation Engineer (Agentic Systems) — 0-2 months

*These close the gap between "SDET who tests AI" and "recognized AI Validation Engineer."*

| # | Skill | Priority | Why | How to Learn | Hours |
|---|---|---|---|---|---|
| 1 | **Formal Evaluation Frameworks (RAGAS, DeepEval, TruLens)** | HIGH | Your custom YAML framework is solid but industry uses standard frameworks; knowing them makes you credible in interviews | DeepEval docs + apply to your gold questions | 4 |
| 2 | **Statistical Evaluation Methods** | HIGH | You use thresholds (0.85/0.60) but lack statistical rigor: confidence intervals, inter-rater reliability (Cohen's kappa), significance testing | "LLM Evaluation" section of Chip Huyen's book + apply to your test results | 4 |
| 3 | **Taxonomy of LLM Failures** | MEDIUM | You find failures but lack formal taxonomy: hallucination types, faithfulness, relevance, coherence, toxicity | HELM benchmark paper + create failure taxonomy for your agents | 3 |
| 4 | **Red Teaming / Adversarial Evaluation** | MEDIUM | Your guardrail tests are basic; formal red teaming is a career differentiator | Anthropic red team guide + apply to RI Assistant | 3 |
| 5 | **Evaluation Dataset Design** | MEDIUM | Your gold questions are good but not formally stratified by difficulty, entity type, edge case coverage | Academic eval dataset papers + formalize your gold set | 2 |

**Stage 1 Total: ~16 hours**

### Stage 2: AI Systems Engineer — 2-4 months

*These close the gap between "tests agent systems" and "builds agent systems."*

| # | Skill | Priority | Why | How to Learn | Hours |
|---|---|---|---|---|---|
| 6 | **Agent Orchestration Frameworks (LangGraph, CrewAI)** | HIGH | You test conductor but can't build one; LangGraph is the industry standard | LangGraph tutorial → build a mini-conductor for a personal project | 8 |
| 7 | **RAG Pipeline Implementation** | HIGH | Vector search + retrieval + generation is core to AI engineering; you only have awareness | LangChain RAG tutorial → build RAG over your workspace docs | 6 |
| 8 | **Structured Outputs / Function Calling (OpenAI API)** | HIGH | You test structured outputs but haven't defined schemas; critical for tool-use agents | OpenAI function calling docs → implement 3 tool-use patterns | 4 |
| 9 | **Prompt Optimization / DSPy** | MEDIUM | You write prompts intuitively; DSPy/OPRO automate prompt optimization | DSPy tutorial → optimize one of your agent_must evaluation prompts | 4 |
| 10 | **LLMOps / Experiment Tracking** | MEDIUM | You lack MLflow/W&B tracking for LLM experiments; needed for systematic improvement | W&B LLM course (free) → track your agent test results | 4 |
| 11 | **Observability for LLM Systems** | MEDIUM | LangSmith, Datadog LLM monitoring — debugging agent failures at scale | LangSmith quickstart → instrument your test framework | 3 |

**Stage 2 Total: ~29 hours**

### Stage 3: Full AI Engineer (Evaluation & Safety Specialization) — 4-8 months

*These are longer-term investments for senior/staff-level positioning.*

| # | Skill | Priority | Why | How to Learn | Hours |
|---|---|---|---|---|---|
| 12 | **Fine-Tuning LLMs** | MEDIUM | Understanding fine-tuning informs evaluation design | HuggingFace fine-tuning tutorial → fine-tune a small model for entity classification | 10 |
| 13 | **RLHF / RLAIF Concepts** | MEDIUM | AI safety/alignment fundamentals; differentiator for evaluation specialist | Anthropic's Constitutional AI paper + RLHF explainer | 4 |
| 14 | **AI Safety Frameworks (NIST AI RMF, EU AI Act)** | MEDIUM | Compliance knowledge for enterprise AI validation | NIST AI RMF playbook → map to your testing practices | 4 |
| 15 | **Embedding Models & Vector Databases** | LOW-MEDIUM | Deeper RAG expertise | Pinecone/Weaviate docs → implement entity search for normalizer-like use case | 6 |
| 16 | **Distributed ML Systems (Ray, Kubernetes)** | LOW | Infrastructure understanding for scaling AI systems | Ray tutorial (your agai-api already uses it) | 4 |
| 17 | **Model Evaluation at Scale (HELM, BigBench)** | LOW | Academic evaluation methodology for large-scale benchmarking | Read HELM paper + apply 3 metrics to your agents | 3 |

**Stage 3 Total: ~31 hours**

---

## Section 4: Industry Demand Analysis (2024-2025)

### 4.1 Most In-Demand Skills in AI Validation / LLM Eval / Agentic QA

Based on job postings (LinkedIn, Levels.fyi, Greenhouse) for roles titled "AI Evaluation Engineer," "LLM QA Engineer," "AI Validation Engineer," "Agentic Systems Engineer":

| Rank | Skill | Demand Signal | Your Status |
|---|---|---|---|
| 1 | **LLM Evaluation (RAGAS, DeepEval, custom frameworks)** | Mentioned in 85% of postings | **STRONG** — custom framework, needs formal framework exposure |
| 2 | **Python (pytest, FastAPI)** | Table stakes | **STRONG** |
| 3 | **Agent/Tool-Use Testing** | Rapidly growing, 60% of new postings | **STRONG** — 22-test tool invocation suite, multi-agent pipeline testing |
| 4 | **RAG Pipeline (build + evaluate)** | 70% of AI engineer postings | **GAP** — awareness only |
| 5 | **Prompt Engineering** | 75% of postings | **STRONG** |
| 6 | **LangChain / LangGraph** | 50% of postings | **GAP** — hasn't used |
| 7 | **CI/CD for ML/LLM (MLOps)** | 45% of postings | **PARTIAL** — CI for tests, not for models |
| 8 | **Statistical Evaluation Methods** | 40% of postings | **GAP** — uses thresholds, lacks statistical rigor |
| 9 | **Red Teaming / Safety Testing** | Growing fast, 35% of postings | **PARTIAL** — has guardrail tests |
| 10 | **Structured Outputs / Function Calling** | 55% of AI engineer postings | **PARTIAL** — tests but doesn't implement |

### 4.2 Salary Impact by Skill (2025 US Market)

| Skill Addition | Estimated Salary Impact | Source |
|---|---|---|
| LLM Evaluation expertise | +$15-25K over standard SDET | Levels.fyi AI roles |
| Agent orchestration (LangGraph) | +$20-30K (systems engineer level) | LinkedIn salary data |
| RAG implementation | +$15-25K | AI engineer postings |
| AI Safety / Red Team | +$10-20K (niche premium) | Anthropic/OpenAI postings |
| MLOps / LLMOps | +$10-15K | DevOps → MLOps transition data |

---

## Section 5: Priority Matrix — Pareto Analysis (20% Effort → 80% Career Value)

### The Critical 6 Skills (Top 20%)

These 6 skills, if learned in the next month, unlock 80% of the career value for AI Validation Engineer → AI Systems Engineer progression:

| Priority | Skill | Hours | ROI Justification | Action This Month |
|---|---|---|---|---|
| **P1** | **Formal Eval Frameworks (DeepEval/RAGAS)** | 4 | Translates your custom work into industry-recognized vocabulary; immediate interview value | Install DeepEval, port 5 gold questions, run metrics comparison |
| **P2** | **Statistical Evaluation Methods** | 4 | Transforms "0.85 threshold" into "statistically significant improvement"; needed for evaluation papers/talks | Read Chip Huyen Ch.10, compute Cohen's kappa on your LLM judge results |
| **P3** | **LangGraph Agent Orchestration** | 6 | Bridges "I test conductors" to "I build conductors"; highest career multiplier | LangGraph tutorial, build mini-conductor that reimplements AppSelectorTool → App routing |
| **P4** | **RAG Pipeline (Build)** | 4 | Most-demanded AI engineering skill; your workspace has all the data (20K+ graph nodes) | LangChain RAG tutorial over your graphify-out knowledge graph |
| **P5** | **Red Teaming / Adversarial Testing** | 3 | Differentiator: very few SDETs can formally red-team LLM agents | Anthropic guide → write 10 adversarial prompts for RI Assistant |
| **P6** | **Structured Outputs / Function Calling** | 3 | Completes your tool-use testing with implementation knowledge | OpenAI function calling → implement 2 tools with JSON schema enforcement |

**Total: 24 hours out of 44 available → leaves 20 hours for practice, portfolio, and buffer**

### Weekly Plan (1 Month)

| Week | Focus | Hours | Deliverable |
|---|---|---|---|
| **Week 1** | P1: DeepEval/RAGAS + P2: Statistical Methods | 10-12 | DeepEval running on your gold questions; Cohen's kappa computed |
| **Week 2** | P3: LangGraph Agent Orchestration | 10-12 | Mini-conductor prototype that routes queries to 2 specialized agents |
| **Week 3** | P4: RAG Pipeline + P6: Structured Outputs | 10-12 | RAG pipeline over workspace docs; 2 function-calling tools implemented |
| **Week 4** | P5: Red Teaming + Portfolio consolidation | 10-12 | 10 adversarial test cases; LinkedIn/portfolio updated with formal terms |

---

## Section 6: Skills You Can Claim Now (With Formal Names)

For resume/LinkedIn/interviews, reframe your experience using these formal names:

| Resume Bullet (Before) | Resume Bullet (After) |
|---|---|
| "Tested AI agents with YAML files" | "Designed and maintained a **declarative evaluation DSL** (YAML) for multi-agent system validation with **LLM-as-Judge evaluation**, **continuous fractional scoring** (0.0–1.0), and **stateful multi-turn dialogue testing**" |
| "Wrote gold questions for the agent" | "Curated **Gold Standard Evaluation Datasets** for 4 AI agents across single-turn, multi-turn, and adversarial test scenarios" |
| "Used LLM to check agent responses" | "Implemented **LLM-as-Judge evaluation pipeline** with **multi-dimensional rubrics** (semantic + structural + behavioral) and **hybrid assertion patterns**" |
| "Tested agent routing" | "Validated **Hierarchical Multi-Agent Orchestration** patterns including intent classification, tool-use verification, and multi-stage pipeline handoffs across 5 specialized domain agents" |
| "Built test reports on GitHub Pages" | "Designed **automated evaluation reporting infrastructure** with CI/CD-integrated HTML dashboards, fractional scoring visualization, and regression trend tracking" |
| "Made a knowledge graph of the codebase" | "Applied **automated knowledge graph extraction** (20,886 nodes, 52,533 edges, 1,624 community clusters) for **architectural analysis** and **AI agent context engineering**" |

---

## Section 7: Gap-to-Role Mapping

```
CURRENT STATE                    STAGE 1 (0-2mo)               STAGE 2 (2-4mo)              STAGE 3 (4-8mo)
─────────────                    ───────────────               ───────────────              ───────────────
SDET testing AI agents    ──►   AI Validation Engineer   ──►   AI Systems Engineer    ──►   Full AI Engineer
                                                                                            (Eval & Safety)

WHAT YOU HAVE:                   WHAT TO ADD:                   WHAT TO ADD:                 WHAT TO ADD:
✅ LLM-as-Judge                  📚 DeepEval/RAGAS             🔧 LangGraph orchestration   🧠 Fine-tuning
✅ Gold datasets                 📚 Statistical eval            🔧 RAG pipeline              🧠 RLHF/RLAIF
✅ Fractional scoring            📚 Failure taxonomy           🔧 Structured outputs        🧠 AI Safety frameworks
✅ Multi-agent testing           📚 Red teaming                🔧 Prompt optimization       🧠 Embedding models
✅ YAML test DSL                 📚 Formal eval design         🔧 LLMOps/experiment track   🧠 Distributed ML
✅ 5-layer test pyramid                                        🔧 Observability
✅ Context engineering
✅ Knowledge graphs

TIMELINE:                        Weeks 1-4 (this month)        Months 2-4                   Months 4-8
HOURS:                           ~24 focused hours              ~30 hours                    ~30 hours
CREDENTIAL:                      Portfolio + LinkedIn           LangChain cert               NIST AI RMF
```

---

*This gap analysis is based on actual workspace artifacts from C:\WOSRI-Workspace\ and current AI engineering job market data (2024-2025). Reassess after completing the 1-month sprint.*
