# Workspace Sessions Summary — Knowledge Extraction

> **Source:** C:\WOSRI-Workspace (16 repositories)
> **Generated:** 2026-04-29
> **Purpose:** Extract and formalize all knowledge demonstrated through workspace artifacts

---

## 1. Technology Proficiency Map

| Technology | Category | Proficiency | Evidence (Workspace Artifacts) |
|---|---|---|---|
| **Python** | Language | Advanced | `platform-agent-testing/automated_testing_v2/` (built entire test framework), `run_tests.py`, `final_tests.py`, `test_continue.py`, `test_full_conv.py` |
| **FastAPI** | Framework | Intermediate-Advanced | `wos-ri-conductor/app/main.py` (agent orchestrator), `wos-ai-normalizer/app/` (entity normalizer) — reads, configures, tests against both services |
| **pytest** | Testing | Advanced | `wos-ri-conductor/test/` (YAML-driven conductor tests), `platform-agent-testing/` (custom test runner) |
| **TypeScript** | Language | Intermediate | `research-intelligence-ui-tests/` (Playwright step defs), locator files (`WOSRI_RI_Assistant_Page.ts`) |
| **Playwright** | E2E Testing | Intermediate | `research-intelligence-ui-tests/features/WosRI_UI_Tests/Assistant/` — Impact, Collaboration, Funding, Emerging Topics agent E2E tests |
| **Cucumber/Gherkin** | BDD | Advanced | Feature files across `research-intelligence-ui-tests/` and `research-intelligence-core-api-it-tests/` — both UI and API layers |
| **Angular** | Frontend | Awareness-Intermediate | `research-intelligence-ui/src/app/pages/ask-ri/` — understands NgRx store shape, component structure, service layer |
| **Java / Spring Boot** | Backend | Intermediate | `research-intelligence-core-api/` (BFF), `research-intelligence-core-api-it-tests/` (REST-Assured contract tests) |
| **REST-Assured** | API Testing | Intermediate | `research-intelligence-core-api-it-tests/src/main/resources/features/RI_Assistant/` — 7 feature files covering WebSocket, REST, feedback, chat history, chart config |
| **YAML** | Config/DSL | Advanced | 60+ YAML test files authored in `platform-agent-testing/automated_testing_v2/test_files/` and `wos-ri-conductor/test/test_config/` |
| **WebSocket/SSE** | Protocol | Intermediate | Tests against `wss://api.dev-stable.clarivate.com/api/wosri/ws/askri`, understands streaming response schema |
| **Git/GitHub** | VCS | Advanced | Multi-repo workflow (16 repos), GitHub Pages deployment for test reports, GitHub Actions CI |
| **Knowledge Graphs** | AI/Data | Practitioner | `graphify/` tool (v0.3.20), `graphify-out/` — generated graph with 20,886 nodes, 52,533 edges, 1,624 communities across workspace |
| **LLM APIs (GPT-4.1)** | AI | Practitioner | Direct interaction via `agai-api`, `ClarivateAGAI` class; tests agent responses, understands temperature/seed/structured outputs |
| **Prompt Engineering** | AI | Intermediate-Advanced | `prompts/` library, `agent_must` evaluation prompts, `DDA prompt.txt`, `agent-skills/` skill definitions |
| **Docker/AWS ECS** | DevOps | Awareness | `wos-ai-normalizer/README-ecs.md`, `README-terraform.md` — infrastructure context |

---

## 2. Testing & Validation Tasks Performed

### 2.1 YAML-Driven Agent Testing (platform-agent-testing)

| Task | Files | Scope |
|---|---|---|
| Gold standard regression suite | `test_files/impact/0_gold/gold_questions.yaml` | Full impact agent single-question regression |
| Multi-turn conversation regression | `test_files/impact/0_gold/gold_questions_long_chats.yaml` | Context preservation across turns |
| Filter & indicator validation | `test_files/impact/0_gold/gold_questions_filters_indicators.yaml` | Date range, location, funder, topic filters |
| Entity broadening tests (AGAI-4078) | `test_files/impact/1st_agent__self_contained_(20)/AGAI_3767_supported_entities.yaml` | 20 tests: entity acceptance/rejection |
| Query correction tests (AGAI-3958) | `test_files/impact/across_agents/AGAI-3688_query_corrector.yaml` | Multi-turn query reformulation |
| Guardrail tests | `test_files/impact/across_agents/AGAI_3633_3396_guardrails.yaml` | Off-topic refusal validation |
| Strategy tool call tests (AGAI-3783) | `test_files/impact/2d_agent__search_strategy_(30)/AGAI_3783_strategy_tool_call_skipped.yaml` | 22 tests for tool invocation |
| Fractional scoring demos | `test_files/demo/fractional_score_demo.yaml`, `fractional_score_demo_basic.yaml` | Framework capability demonstration |
| Funding agent gold questions | `test_files/funding_agent/gold_questions/gold_questions.yaml` | Funding Discovery agent regression |
| Collaboration agent tests | `test_files/collaboration_agent/other/agent_completes_answers/` | Answer completion validation |

### 2.2 Conductor YAML Testing (wos-ri-conductor)

| Task | Files | Scope |
|---|---|---|
| Schema/level routing (WOSRI-15810) | `test/test_config/bug/wosri_tickets/WOSRI_15810/test{1-4}_*.yml` | Citation Topics Micro/Meso, WoS category routing |
| WoS categories precision (AGAI-4152) | `test/test_config/bug/wosri_tickets/AGAI_4152/test{1-4}_*.yml` | Schema default selection for well-known disciplines |
| Schema selection (WOSRI-15680) | `test/test_config/bug/wosri_tickets/WOSRI_15680/test{1-3}_*.yml` | Explicit level request routing |
| Fractional scoring comprehensive | `test/test_config/fractional_scoring_comprehensive/test_filters.yaml` | Multi-dimensional scoring |
| Custom filter tests | `test/test_config/custom/test_filters.yaml`, `test_filters_corrected.yaml` | Filter assertion patterns |

### 2.3 E2E UI Tests (Playwright + Cucumber)

| Task | Files | Scope |
|---|---|---|
| Assistant home page | `features/WosRI_UI_Tests/Assistant/Assistant_Home_page.feature` | Agent cards, navigation |
| Chat history | `features/WosRI_UI_Tests/Assistant/Chat_History.feature` | List, rename, delete |
| Feedback | `features/WosRI_UI_Tests/Assistant/Feedback.feature` | Thumbs up/down |
| Impact Agent E2E | `features/WosRI_UI_Tests/Assistant/Impact_Agent/` | Full agent flow |
| Collaboration Agent E2E | `features/WosRI_UI_Tests/Assistant/Collaboration_Agent/` | Full agent flow |
| Funding Agent E2E | `features/WosRI_UI_Tests/Assistant/Funding_Agent/` | Full agent flow |
| Emerging Topics Agent E2E | `features/WosRI_UI_Tests/Assistant/EmergingTopics_Agent/` | Full agent flow |
| Accessibility | `features/WosRI_UI_Tests/WosRI_Accessibility_Tests.feature` | `/wosri/ri-assistant` coverage |

### 2.4 API Contract Tests (REST-Assured + Cucumber)

| Task | Files | Scope |
|---|---|---|
| WebSocket streaming | `RI_Assistant_BFF_API.feature` | Connect, send question, validate SSE schema |
| Feedback API | `RI_Assistant_BFF_API_Feedback.feature` | PUT feedback — valid/invalid |
| Chat history CRUD | `RI_Assistant_Retrieve_Chat_History.feature`, `RI_Assistant_Edit_Chat_History.feature`, `RI_Assistant_Delete_Chat_History.feature` | Full CRUD |
| Chart config | `RI_Assistant_ChatConfigAPI.feature` | Multiple chart types |
| Filter verification | `RI_Assistant_BFF_API_Filter_Verification.feature` | Location, funder, topic filters |

---

## 3. AI Agents Evaluated

### 3.1 Primary Agents (User-Facing)

| Agent | `agentType` | Sub-Agents (Pipeline) | Tests Written |
|---|---|---|---|
| **Impact Evaluation** | `impact` | Agent 20 (self-contained question) → Agent 30 (search strategy) → Agent 40 (search execution) → Agent 90 (help/fallback) | 100+ YAML tests, E2E features, API contracts |
| **Collaboration Analysis** | `collaboration` | Similar pipeline via conductor | YAML tests, E2E features |
| **Funding Discovery** | `funding` | Funding Opp tools via conductor | Gold questions YAML, E2E features |
| **Emerging Topics** | `emerging_topics` | Emerging topic tools via conductor | E2E features, YAML tests |

### 3.2 Internal Agents / Tools (Backend)

| Agent/Tool | Location | Function |
|---|---|---|
| **AppSelectorTool** | `wos-ri-conductor/app/tools/llm/` | Classifies query → selects correct App (Organizations, Researchers, etc.) |
| **TranslatorTool** | `wos-ri-conductor/app/tools/llm/` | Translates non-English queries to English |
| **HistoryProcessorTool** | `wos-ri-conductor/app/tools/llm/` | Summarizes/processes chat history context |
| **VisualizerTool** | `wos-ri-conductor/app/tools/llm/` | Selects appropriate chart/visualization type |
| **HighlightsTool** | `wos-ri-conductor/app/tools/llm/` | Extracts key insights from data |
| **NormalizerTool** | `wos-ri-conductor/app/tools/remote/normalizer/` | Routes to `wos-ai-normalizer` for entity resolution |
| **IncitesTool** | `wos-ri-conductor/app/tools/remote/` | Calls InCites API for research metrics data |

### 3.3 Entity Normalizer Pipeline (wos-ai-normalizer)

| Entity Type | Router | Pipeline |
|---|---|---|
| Organization | `routers/incites.py` | Candidate retrieval → LLM reranking → alternatives |
| Author | `routers/incites.py` | Embedding search → LLM reranking |
| Department | `routers/incites.py` | Controlled list lookup → LLM match |
| Location | `routers/incites.py` | Controlled list → match |
| Journal | `routers/incites.py` | Embedding search → LLM reranking |
| Subject | `routers/incites.py` | Controlled list → match |
| Publisher | `routers/incites.py` | Controlled list → match |
| Funding Agency | `routers/incites.py` | Controlled list → LLM match |
| WoSRA Institution | `routers/wosra.py` | Separate normalization path |
| Funding Keyword/Sponsor | `routers/funding_opp.py` | Funding-specific normalization |

---

## 4. Problems Solved & Formal Approaches Used

| Problem | Approach | Formal Name | Files |
|---|---|---|---|
| Agent gives wrong results on follow-up queries | Multi-turn conversation testing with `agent_must` rubrics | **Conversational Regression Testing** | `AGAI-3688_query_corrector.yaml` |
| Agent rejects valid entities too aggressively | Boundary value entity tests (supported vs unsupported) | **Acceptance Boundary Testing** | `AGAI_3767_supported_entities.yaml` |
| Schema routing selects wrong category | Parameterized YAML tests with structural JSON assertions | **Structural Output Validation** | `WOSRI_15810/test{1-4}_*.yml` |
| Agent doesn't refuse off-topic requests | Guardrail tests with LLM-as-judge | **Safety/Guardrail Evaluation** | `AGAI_3633_3396_guardrails.yaml` |
| Test results are binary (pass/fail only) | Fractional scoring system (0.0–1.0) | **Continuous Evaluation Metrics** | `fractional_score_demo.yaml`, `--streamlined` flag |
| Non-technical users can't run agent tests | GitHub Pages dashboard + GitHub Actions workflow | **Test Democratization** | `USER_MANUAL_IMPACT_AGENT_TESTING.md` |
| Agent tool call skipped silently | 22-test suite validating tool invocation | **Tool-Use Verification** | `AGAI_3783_strategy_tool_call_skipped.yaml` |
| Need comprehensive codebase understanding | Knowledge graph extraction (20,886 nodes) | **Automated Knowledge Extraction** | `graphify/`, `graphify-out/GRAPH_REPORT.md` |
| Evaluating semantic correctness of agent output | LLM-as-judge with structured rubrics | **LLM-as-Judge Evaluation** | `--enable-llm-judge` flag, `agent_must` fields |
| Test environment flakiness (401 errors, DNS) | Retry logic + environment isolation | **Resilient Test Infrastructure** | `core/retry_manager.py`, VPN requirements |

---

## 5. Context Engineering Artifacts Created

| Artifact | File | Purpose |
|---|---|---|
| **Workspace context map** | `RI_ASSISTANT_WORKSPACE_MAP.md` | Zero-shot context for any AI agent — architecture, APIs, test locations |
| **Agent testing skill** | `Agai_testing_Skill.md` | Reusable skill definition for OpenCode to run AGAI tests |
| **UI test generation skill** | `Ui_Test_Gen_Skill.md` | Skill definition for generating Playwright tests |
| **Platform agent testing guide** | `platform-agent-testing-guide.md` | Complete tester onboarding document |
| **Conductor testing manual** | `wos-ri-conductor/USER_MANUAL_IMPACT_AGENT_TESTING.md` | Non-technical user manual for YAML test creation |
| **Testing dashboard guide** | `wos-ri-conductor/TESTING_DASHBOARD_GUIDE.md` | GitHub Pages results viewing guide |
| **QA testing report** | `QA_TESTING_REPORT.md` | Comprehensive test results across 13 AGAI tickets |
| **Agent skills library** | `agent-skills/CLAUDE.md` | OpenCode agent skill definitions |
| **Prompt library** | `prompts/` | Reusable prompts for agent tasks |
| **DDA prompt** | `DDA prompt.txt` | Data analytics agent prompt |
| **Gold questions dataset** | `Impact Assistant Gold Questions 2026.xlsx` | Curated reference questions with expected answers |
| **Knowledge graph report** | `graphify-out/GRAPH_REPORT.md` | 20,886 nodes, 52,533 edges, 1,624 communities |

---

## 6. Informal-to-Formal Terminology Quick Reference

| What You Called It | What It Actually Is (Formal Name) |
|---|---|
| "gold questions" | **Gold Standard Evaluation Dataset** |
| "agent_must" field | **Evaluation Rubric / Assertion Specification** |
| "fractional scoring" | **Continuous Evaluation Metrics (0.0–1.0 scoring)** |
| "LLM judge" | **LLM-as-Judge Evaluation Pattern** |
| "router agent" / "AppSelectorTool" | **Intent Classification / Query Router** |
| "conductor" | **Agent Orchestrator / Multi-Agent Coordinator** |
| "normalizer" | **Entity Resolution / Entity Linking Service** |
| "agent 20, 30, 40, 90" | **Hierarchical Multi-Agent Pipeline (numbered stages)** |
| "clvt-hide" blocks | **Hidden Reasoning / Chain-of-Thought Artifacts** |
| "agent_must" + regex_checks | **Hybrid Evaluation (Semantic + Structural Assertions)** |
| "YAML test file" | **Declarative Test Specification** |
| "streamlined mode" | **Enhanced Reporting with Fractional Scores** |
| "BFF adapter" | **Backend-for-Frontend Integration Test Adapter** |
| "graphify" | **Automated Knowledge Graph Extraction** |
| "multi-turn conversation test" | **Stateful Dialogue Evaluation** |
| "depends_on" in YAML | **Test Dependency Graph / DAG-Based Test Orchestration** |
| "retry_manager" | **Fault-Tolerant Test Execution** |

---

*This document extracts knowledge demonstrated through actual workspace artifacts. All file references are to real files in `C:\WOSRI-Workspace\`.*
