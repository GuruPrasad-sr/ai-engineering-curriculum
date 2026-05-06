# Informal-to-Formal Concept Mapping

> **Generated:** 2026-04-29 | **Revised:** 2026-05-06
> **Purpose:** Map every informal concept used in the workspace to its formal AI engineering name, assess knowledge maturity, and map to career credentials
>
> **IMPORTANT — Scope Note:** This mapping was originally generated from WOSRI workspace analysis only (last ~4 months).
> It therefore misses 3 years of WOS work (2023–2025) which is the primary evidence for TypeScript, Playwright, BDD/Cucumber,
> accessibility, CI/CD, and POM skills. See `honest_assessment.md v2` for the corrected full-picture skill assessment.
>
> **Correction applied here:**
> - BDD/Cucumber and POM entries below now credit both WOSRI **and** 3 years of WOS output (80+ PRs, 6 E2E collections)
> - A new Section 0 (Accessibility Testing) has been added — this was entirely missing from the original
> - All other ratings from WOSRI remain unchanged

---

## 0. Accessibility Testing (WOS 2023–2025) — Missing from Original

> This section was absent from the original mapping because it only examined the WOSRI workspace.
> These skills were built over 3 years on `wos-e2e-smoketests` and `wos-nx-ui`.

| Informal (Your Usage) | Formal Name | Definition | Evidence | Maturity | Credential |
|---|---|---|---|---|---|
| "accessibility tests" / axe-core scans | **Automated Accessibility Testing (WCAG)** | Using tools like Playwright-axe or axe-core to detect WCAG violations automatically | `wos-e2e-smoketests` WPP accessibility suite — built from scratch | **Practitioner** — built the suite, knows violations by WCAG criterion number | ISTQB, CPACC |
| "WCAG fix" | **Web Content Accessibility Guidelines (WCAG) 2.1 Remediation** | Correcting code violations against specific WCAG success criteria | 9 production fixes in `wos-nx-ui` Angular/CSS — WOSAR tickets with real commit history | **Practitioner** — authored production code fixes, not just test code | CPACC, CPWA |
| "accessibility nightly build" | **Continuous Accessibility Testing / Automated Compliance Gate** | Scheduled CI/CD pipeline running accessibility validation on every build | Jenkins pipeline configured from scratch; failed builds trigger team alerts | **Practitioner** — designed and configured the pipeline end-to-end | ISTQB, DevOps certs |
| "WOSAR tickets" | **Accessibility Defect Taxonomy / Compliance Incident Management** | Tracking accessibility violations as production defects with severity classification | WOSAR-prefixed Jira tickets for each WCAG fix | **Practitioner** — raises, tracks, and closes accessibility defects | — |
| "2.4.4" / "4.1.2" / "1.3.1" | **WCAG Success Criteria** | The specific numbered requirements in WCAG 2.1 that define what is accessible | User knows criteria numbers from 3 years of remediation work | **Practitioner** — cites WCAG criteria by number in ticket descriptions | CPACC |

---

## 1. Testing Concepts

| Informal (Your Usage) | Formal Name | Definition | Workspace Evidence | Maturity | Credential |
|---|---|---|---|---|---|
| "gold questions" | **Gold Standard Evaluation Dataset** | Curated set of reference inputs with known-correct expected outputs used for regression | `Impact Assistant Gold Questions 2026.xlsx`, `test_files/impact/0_gold/gold_questions.yaml` | **Practitioner** — authored and maintained gold sets | ISTQB AI Testing, DeepLearning.AI Eval |
| "agent_must" | **Evaluation Rubric / Assertion Specification** | Declarative criteria defining what a correct agent response must contain | Every YAML test file: `agent_must: "show Organization(s) as primary focus..."` | **Practitioner** — authored hundreds of rubrics | — |
| "fractional scoring" | **Continuous Evaluation Metrics** | Scoring on a continuous scale (0.0–1.0) rather than binary pass/fail | `fractional_score_demo.yaml`, `--streamlined` flag, PASS ≥ 0.85 / PARTIAL 0.60–0.84 / FAIL < 0.60 | **Practitioner** — implemented and uses daily | DeepLearning.AI Eval |
| "LLM judge" | **LLM-as-Judge Evaluation Pattern** | Using a separate LLM to evaluate the quality of another LLM's output | `--enable-llm-judge` flag, `automated_testing/llm_judge/test_single.yaml` | **Practitioner** — runs routinely, understands limitations (clvt-hide blind spots) | DeepLearning.AI Eval, AI Safety cert |
| "regex_checks" | **Structural Assertion / Pattern Matching Validation** | Regex-based validation of response structure | `regex_checks: ["(?i)(stanford\|mit)", "\\d+\\.?\\d*%"]` in YAML files | **Practitioner** — writes complex regex patterns | ISTQB |
| "llm_validation" | **Multi-Criteria Semantic Evaluation** | Multiple semantic criteria evaluated by LLM judge in parallel | `comprehensive_showcase.yaml` → `llm_validation.criteria` list | **Practitioner** — authored multi-criteria evaluations | — |
| "multi-turn test" | **Stateful Dialogue Evaluation** | Testing agent behavior across a sequence of dependent conversational turns | `conversation:` blocks in YAML, `gold_questions_long_chats.yaml` | **Practitioner** — authored multi-turn suites | — |
| "depends_on" | **Test Dependency DAG (Directed Acyclic Graph)** | Test execution ordering based on dependency relationships | `depends_on: ["emerging_topics_foundation"]` in `comprehensive_showcase.yaml` | **Practitioner** — uses in test design | ISTQB Advanced |
| "retry_manager" | **Fault-Tolerant Test Execution / Retry Policy** | Automatic retry of failed tests to handle transient failures | `core/retry_manager.py`, `--max-retries 5` | **Practitioner** — configured and uses | — |
| "smoke test" | **Smoke Test / Build Verification Test (BVT)** | Minimal test subset to verify basic functionality | `tags: [smoke]`, `--test-index 1-3` on gold set | **Practitioner** | ISTQB |
| "test tags" | **Test Categorization / Test Taxonomy** | Metadata labels for filtering and organizing tests | `tags: [smoke, critical]`, `--tags smoke` | **Practitioner** | ISTQB |
| "HTML report" | **Test Reporting / Test Evidence Artifact** | Generated reports showing pass/fail, scores, response details | `reporters/html_reporter.py`, GitHub Pages publication | **Practitioner** | — |
| "guardrail tests" | **Safety Evaluation / Guardrail Validation** | Tests verifying agent refuses off-topic, harmful, or out-of-scope requests | `AGAI_3633_3396_guardrails.yaml` | **Practitioner** — but scored 53% (agent not reliably refusing) | AI Safety cert |
| "BFF adapter" / "legacy adapter" | **Test Adapter Pattern / Integration Level Selection** | Configurable adapter choosing between direct API and BFF-routed testing | `runners/bff_adapter.py`, `runners/legacy_adapter.py`, `--use-bff` | **Practitioner** | — |
| "Cucumber feature file" | **Behavior-Driven Development (BDD) Specification** | Gherkin-syntax specification connecting business requirements to test code | **WOS (primary):** Hundreds of feature files authored over 3 years across `wos-e2e-smoketests`, `wos-restapi-automation` — 6 full E2E collections, scenario outlines, backgrounds, tag strategies. **WOSRI:** all `.feature` files in `research-intelligence-ui-tests/` and `core-api-it-tests/` | **Practitioner (4/5)** — independent authorship across 3 years | ISTQB BDD |
| "page locator" | **Page Object Model (POM)** | Centralized locator management for UI test automation | **WOS (primary):** 3 years maintaining and refactoring page objects across `wos-e2e-smoketests` — standardised locator naming conventions across the entire suite. **WOSRI:** `WOSRI_RI_Assistant_Page.ts` | **Practitioner (4/5)** — 3 years independent POM authorship and refactoring | ISTQB Advanced Test Automation |
| "contract test" | **Consumer-Driven Contract Test** | API schema and behavior validation at the integration boundary | `RI_Assistant_BFF_API.feature` — WebSocket schema, REST endpoints | **Practitioner** | ISTQB API Testing |

---

## 2. AI / ML Concepts

| Informal (Your Usage) | Formal Name | Definition | Workspace Evidence | Maturity | Credential |
|---|---|---|---|---|---|
| "router agent" / "AppSelectorTool" | **Hierarchical Multi-Agent Orchestration (Router Pattern)** | A master agent that classifies intent and delegates to specialized sub-agents | `conductor.py` → AppSelectorTool → {OrganizationsApp, ResearchersApp, ...} | **Practitioner** — tests against it, understands routing chain | — |
| "conductor" | **Agent Orchestrator / Workflow Coordinator** | Central component managing the execution flow of multiple agents and tools | `wos-ri-conductor/app/conductor/conductor.py` | **Practitioner** — tests, reads code, writes conductor-level YAML tests | — |
| "agent 20, 30, 40, 90" | **Multi-Stage Agent Pipeline** | Sequential pipeline of specialized agents, each handling one phase | Impact agent: self_contained → strategy → search → help | **Practitioner** — tests each stage independently and end-to-end | — |
| "normalizer" | **Entity Resolution / Entity Linking** | Mapping ambiguous user-entered names to canonical database identifiers | `wos-ai-normalizer/` — candidate retrieval → LLM reranking → alternatives | **User** — tests against it, understands pipeline, doesn't implement | NLP specialization |
| "embedding search" | **Vector Similarity Search / Semantic Retrieval** | Using embeddings to find semantically similar entities | Normalizer candidate retrieval step | **User** — knows it's used, doesn't implement | — |
| "LLM reranking" | **Cross-Encoder Reranking / LLM-Assisted Reranking** | Using an LLM to reorder candidate results by relevance | `wos-ai-normalizer` uses AGAI API for LLM reranking | **User** — understands the pattern, doesn't implement | — |
| "tool call" / "tool use" | **Function Calling / Tool-Augmented LLM** | LLM invoking external functions (APIs, databases) as part of its reasoning | IncitesTool, NormalizerTool, VisualizerTool in conductor | **Practitioner** — validates tool invocation (AGAI-3783: 22 tests) | — |
| "SSE stream" | **Server-Sent Events / Token Streaming** | Progressive delivery of LLM output token-by-token | `wos-ri-conductor/app/routers/api.py` → SSE stream through BFF to UI | **User** — tests against it, understands protocol | — |
| "context window" / "history processor" | **Context Window Management / Conversation Compression** | Techniques to fit conversation history within LLM token limits | HistoryProcessorTool summarizes chat history | **User** — understands the need, tests behavior | — |
| "MCP" | **Model Context Protocol** | Anthropic's standard protocol for connecting LLMs to external tools and data | `agai-api` MCP server management | **Awareness** — knows it exists in AGAI, hasn't directly configured | — |
| "structured output" | **Constrained Decoding / JSON Schema Enforcement** | Forcing LLM output to conform to a specific JSON schema | AppSelectorTool returns structured App selection | **User** — tests structured outputs, doesn't implement | — |
| "prompt library" | **Prompt Template Repository** | Curated collection of reusable prompt templates | `prompts/` directory, agent_must rubric patterns | **Practitioner** — maintains prompt library | Prompt Engineering cert |
| "clvt-hide" | **Hidden Chain-of-Thought / Internal Reasoning Artifact** | Agent reasoning visible to developers but hidden from end users | `clvt-hide` blocks in agent responses, noted in QA_TESTING_REPORT.md | **Practitioner** — accounts for in test design | — |
| "AGAI / ClarivateAGAI" | **LLM Gateway / API Abstraction Layer** | Unified API layer abstracting multiple LLM providers | `agai-api/` — OpenAI-compat + Anthropic-compat endpoints | **User** — calls via conductor, understands capabilities | — |
| "Ray tasks" | **Distributed Task Execution (Ray)** | Using Ray framework for parallel/distributed LLM workloads | `agai-api/agai_ray/` | **Awareness** — knows it exists | — |
| "vector DB" | **Vector Database** | Specialized database for storing and querying embeddings | `agai-api` — Weaviate, AI21 integration | **Awareness** — knows it's used in the stack | — |
| "agent hub" | **Conversation Management Service** | Centralized service for managing agent conversations | `agai-api/agenthub/` | **Awareness** — knows it exists | — |

---

## 3. Software Engineering Concepts

| Informal (Your Usage) | Formal Name | Definition | Workspace Evidence | Maturity | Credential |
|---|---|---|---|---|---|
| "clock manipulation" / date range testing | **Time-Travel Testing / Temporal Boundary Testing** | Testing system behavior with manipulated time parameters | `impact_agent_date_range_testSuite.yaml`, date filter tests in gold questions | **Practitioner** | ISTQB Advanced |
| "BFF" | **Backend-for-Frontend Pattern** | Dedicated API layer customized for a specific frontend | `research-intelligence-core-api` (Java/Spring Boot) | **Practitioner** — writes contract tests against it | Software Architecture |
| "NgRx store" | **Redux Pattern / Unidirectional Data Flow** | Centralized state management with actions, reducers, effects | `research-intelligence-ui/src/app/pages/ask-ri/store/` | **User** — understands shape, tests effects | — |
| "WebSocket proxy" | **Protocol Bridge / Gateway Pattern** | Proxying WebSocket connections through an intermediary | BFF relays WebSocket to conductor SSE | **User** — tests against both paths | — |
| "feature toggle" | **Feature Flag / Feature Toggle** | Runtime configuration controlling feature visibility | `ask-ri.config.ts`, shared store feature toggles | **User** — checks toggles in tests | — |
| "GitHub Pages dashboard" | **Static Site Deployment / Test Reporting Portal** | Automated publishing of test reports to a web dashboard | `docs/` → GitHub Pages, `generate_structure.py` | **Practitioner** — built the pipeline | — |
| "GitHub Actions workflow" | **CI/CD Pipeline** | Automated build, test, deploy workflows | `.github/workflows/` in `wos-ri-conductor`, `platform-agent-testing` | **User** — triggers and monitors, doesn't author from scratch | DevOps/CI cert |
| "pull-all-repos" | **Multi-Repo Management / Mono-Workspace Script** | Script to synchronize multiple repositories | `pull-all-repos.ps1` | **Practitioner** — authored | — |
| "knowledge graph" (codebase) | **Static Code Analysis / Architectural Knowledge Extraction** | Automated extraction of code structure into graph representation | `graphify/` → `graphify-out/` (20,886 nodes, 52,533 edges) | **Practitioner** — runs tool, interprets results | — |
| "context file" / "workspace map" | **Context Engineering / Developer Experience (DX) Document** | Curated context document enabling AI agents to work effectively | `RI_ASSISTANT_WORKSPACE_MAP.md`, `agent-skills/CLAUDE.md` | **Practitioner** — authored multiple context files | — |
| "skill file" | **AI Agent Skill Definition** | Structured document defining a reusable AI agent capability | `Agai_testing_Skill.md`, `Ui_Test_Gen_Skill.md`, `agent-skills/` | **Practitioner** — authored skill definitions | — |

---

## 4. Knowledge Maturity Assessment Summary

### Maturity Levels Defined

| Level | Definition | Evidence Threshold |
|---|---|---|
| **Practitioner** | Can implement, debug, and teach. Has authored artifacts. | Created files, solved problems, authored tests |
| **User** | Can use effectively but hasn't built from scratch. | Configures, runs, interprets but doesn't implement |
| **Awareness** | Knows it exists, can describe at high level. | Mentioned in workspace but not directly used |
| **No Exposure** | Has not encountered in workspace. | Not present in any workspace artifact |

### Maturity by Category

| Category | Practitioner | User | Awareness | No Exposure |
|---|---|---|---|---|
| **Testing/Validation** | Gold datasets, LLM-as-judge, fractional scoring, YAML test DSL, BDD/Cucumber, POM, contract tests, guardrail tests, multi-turn eval, test DAGs, reporting | — | — | Formal metamorphic testing, mutation testing for LLMs |
| **AI Agent Patterns** | Router pattern testing, tool-use verification, multi-stage pipeline testing, prompt engineering | Entity resolution, LLM reranking, structured outputs, SSE streaming, context window mgmt | MCP, Ray distributed, vector DB, agent hub | RLHF, fine-tuning, model training, distillation |
| **Software Engineering** | Multi-repo management, CI triggers, BFF testing, GitHub Pages, context engineering | NgRx, feature flags, WebSocket protocol, GitHub Actions authoring | Docker/ECS, Terraform | Kubernetes, service mesh, observability (Datadog advanced) |

---

## 5. Career Credential Mapping

| Skill Cluster | Applicable Certifications | Your Readiness |
|---|---|---|
| AI/LLM Evaluation | **DeepLearning.AI: Evaluating and Debugging Generative AI**, **Weights & Biases: LLM Evaluation** | Ready — already practicing LLM-as-judge, fractional scoring, gold datasets |
| AI Safety & Guardrails | **Anthropic AI Safety Fundamentals**, **NIST AI RMF Practitioner** | Partial — has guardrail tests but scored 53% (agent issues, not knowledge gaps) |
| Prompt Engineering | **DeepLearning.AI: ChatGPT Prompt Engineering**, **Anthropic Prompt Engineering Guide** | Ready — maintains prompt library, writes evaluation rubrics |
| Test Automation (Traditional) | **ISTQB Advanced Test Automation Engineer**, **ISTQB AI Testing** | Ready — multi-layer test pyramid, BDD, POM, contract tests |
| Agent Systems | **DeepLearning.AI: Multi AI Agent Systems (CrewAI)**, **LangChain Certified Developer** | Partial — understands patterns from testing perspective, needs implementation depth |
| MLOps / LLMOps | **Google MLOps Certification**, **AWS ML Specialty** | Low — awareness of infrastructure, hasn't implemented pipelines |
| Software Architecture | **AWS Solutions Architect**, **System Design Interview** | Partial — understands BFF, microservices, event-driven from testing |

---

*Revised: 2026-05-06 | Added Section 0 (Accessibility Testing — WOS 2023–2025), corrected BDD/Cucumber and POM entries to credit primary WOS evidence, added scope note.*
*Original: 2026-04-29 | This mapping connects informal workspace terminology to formal AI engineering vocabulary. Maturity assessments are based on evidence from actual workspace artifacts.*
