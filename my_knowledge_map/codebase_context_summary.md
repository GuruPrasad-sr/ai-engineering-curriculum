# Codebase Context Summary — AI Engineering Perspective

> **Workspace:** C:\WOSRI-Workspace (16 repositories)
> **Generated:** 2026-04-29
> **Purpose:** Summarize the codebase from an AI systems engineering perspective

---

## 1. Multi-Agent System Architecture

### 1.1 System-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  USER LAYER                                                         │
│  research-intelligence-ui (Angular SPA)                             │
│  ├── ask-ri.component → NgRx Store → AskRiService                  │
│  └── WebSocket (SSE streaming)                                      │
├─────────────────────────────────────────────────────────────────────┤
│  BFF LAYER                                                          │
│  research-intelligence-core-api (Java / Spring Boot)                │
│  ├── REST endpoints (chat history CRUD, feedback, chart config)     │
│  └── WebSocket proxy → SSE stream relay                             │
├─────────────────────────────────────────────────────────────────────┤
│  ORCHESTRATION LAYER                                                │
│  wos-ri-conductor (Python / FastAPI) — "Conductor"                  │
│  ├── TranslatorTool (non-English → English)                         │
│  ├── AppSelectorTool (intent classification → App routing)          │
│  ├── HistoryProcessorTool (chat context summarization)              │
│  └── App (domain-specific agent)                                    │
│       ├── NormalizerTool → wos-ai-normalizer                        │
│       ├── IncitesTool → InCites API                                 │
│       ├── VisualizerTool → ClarivateAGAI                            │
│       └── HighlightsTool → ClarivateAGAI                            │
├─────────────────────────────────────────────────────────────────────┤
│  ENTITY RESOLUTION LAYER                                            │
│  wos-ai-normalizer (Python / FastAPI)                               │
│  ├── Candidate retrieval (embedding search / controlled lists)      │
│  ├── LLM reranking (via agai-api)                                   │
│  └── Alternatives generation (fallback)                             │
├─────────────────────────────────────────────────────────────────────┤
│  LLM GATEWAY LAYER                                                  │
│  agai-api (Python / FastAPI / Ray)                                  │
│  ├── OpenAI-compatible completion & embedding endpoints              │
│  ├── Anthropic-compatible endpoints                                 │
│  ├── Vector DB integration (Weaviate, AI21)                         │
│  ├── MCP (Model Context Protocol) server management                 │
│  ├── Agent hub (conversation management)                            │
│  ├── Ray-based distributed tasks                                    │
│  └── Caching (memcache, S3), rate limiting                          │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Agent Routing Chain (Router → Specialized → Sub-Agent)

```
User Query
    │
    ▼
[TranslatorTool] ──── if non-English ───► translate to English
    │
    ▼
[AppSelectorTool] ──── intent classification
    │
    ├── OrganizationsApp        (research orgs)
    ├── ResearchersApp          (individual researchers)
    ├── FundingAgenciesApp      (funding bodies)
    ├── ResearchAreasApp        (subject areas)
    ├── LocationsApp            (geographic)
    ├── PublicationSourceApp    (journals)
    ├── DepartmentsApp          (university departments)
    └── NotUnderstandableApp    (fallback/refusal)
          │
          ▼
    [Sub-Agent Pipeline for Impact Agent]
    Agent 20 (self_contained_question) → Entity extraction, query interpretation
        │
        ▼
    Agent 30 (strategy) → Search strategy formulation
        │
        ▼
    Agent 40 (search) → InCites query execution
        │
        ▼
    Agent 90 (help) → Fallback / help responses
```

### 1.3 All User-Facing Agents

| Agent | agentType | Router Endpoint | Specialized Apps |
|---|---|---|---|
| Impact Evaluation | `impact` | `wos-ri-conductor/app/routers/api.py` | OrganizationsApp, ResearchersApp, ResearchAreasApp, LocationsApp, etc. |
| Collaboration Analysis | `collaboration` | `wos-ri-conductor/app/routers/api.py` | Similar app routing |
| Funding Discovery | `funding` | `wos-ri-conductor/app/routers/funding_opp_tools.py` | Funding-specific apps |
| Emerging Topics | `emerging_topics` | `wos-ri-conductor/app/routers/emerging_topic_tools.py` | Topic discovery apps |
| Custom Agent | user-defined | `wos-ri-conductor/app/routers/api.py` | User-specified behavior |

---

## 2. Five-Layer Test Pyramid

```
                    ┌───────────┐
                    │  Platform  │  platform-agent-testing/automated_testing_v2/
                    │   Agent    │  YAML-driven, LLM-as-judge, fractional scoring
                    │   Tests    │  60+ test files, multi-turn, dependency chains
                    ├───────────┤
                  ┌─┤    E2E    ├─┐  research-intelligence-ui-tests/
                  │ │ Playwright │ │  Cucumber + Playwright, @uismokescenarios
                  │ │ + Cucumber │ │  7 feature file groups (per agent + cross-cutting)
                  │ ├───────────┤ │
                ┌─┤ │    API    │ ├─┐  research-intelligence-core-api-it-tests/
                │ │ │ Contract  │ │ │  REST-Assured + Cucumber (Java)
                │ │ │   Tests   │ │ │  7 feature files: WebSocket, REST CRUD, filters
                │ │ ├───────────┤ │ │
              ┌─┤ │ │ Conductor │ │ ├─┐  wos-ri-conductor/test/test_config/
              │ │ │ │   YAML    │ │ │ │  pytest + YAML, structural JSON assertions
              │ │ │ │   Tests   │ │ │ │  Schema routing, filter validation, scoring
              │ │ │ ├───────────┤ │ │ │
            ┌─┤ │ │ │   Unit    │ │ │ ├─┐
            │ │ │ │ │   Tests   │ │ │ │ │  Angular: *.spec.ts
            │ │ │ │ │           │ │ │ │ │  Python: pytest (conductor, normalizer, agai)
            │ │ │ │ │           │ │ │ │ │  Java: JUnit (core-api)
            └─┴─┴─┴─┴───────────┴─┴─┴─┴─┘
```

### Layer Details

| Layer | Repo | Language | Runner | Test Count (Est.) | Scope |
|---|---|---|---|---|---|
| **Platform Agent** | `platform-agent-testing` | Python | `run_tests_v2.py` | 60+ YAML files | Agent behavior: what the agent says, tool calls, multi-turn context |
| **E2E (Playwright)** | `research-intelligence-ui-tests` | TypeScript | Playwright + Cucumber | 7 feature groups | Browser-level user flows: navigation, agent interaction, chat history |
| **API Contract** | `research-intelligence-core-api-it-tests` | Java | REST-Assured + Cucumber | 7 feature files | HTTP/WebSocket schema validation, CRUD operations, error cases |
| **Conductor YAML** | `wos-ri-conductor/test/` | Python | pytest + custom runner | 15+ YAML configs | Conductor-level structural assertions on JSON response fields |
| **Unit** | Multiple repos | TS/Python/Java | Jest/pytest/JUnit | Hundreds | Component isolation: Angular components, Python functions, Java services |

---

## 3. Evaluation Approaches in Use

### 3.1 LLM-as-Judge

| Aspect | Implementation |
|---|---|
| **Trigger** | `--enable-llm-judge` flag in `run_tests_v2.py` |
| **Input** | Agent response text + `agent_must` rubric (free-text evaluation criteria) |
| **Judge Model** | GPT-4.1 via `agai-api` |
| **Output** | Per-criterion pass/fail + overall fractional score |
| **Example rubric** | `agent_must: "show Organization(s) as primary focus, Organization Name: University of Oxford, Research area: PSYCHOLOGY, CLINICAL"` |
| **File ref** | `platform-agent-testing/automated_testing_v2/test_files/demo/basic_llm_demo.yaml` |

### 3.2 Fractional Scoring

| Aspect | Implementation |
|---|---|
| **Scale** | 0.0 – 1.0 continuous |
| **Thresholds** | PASS ≥ 0.85, PARTIAL 0.60–0.84, FAIL < 0.60 |
| **Granularity** | Per-check score contributing to test-level aggregate |
| **Trigger** | `--streamlined` flag |
| **Report** | HTML report with per-test fractional scores |
| **File ref** | `platform-agent-testing/automated_testing_v2/test_files/demo/fractional_score_demo.yaml` |

### 3.3 Multi-Dimensional Evaluation (Hybrid)

| Dimension | Method | Example |
|---|---|---|
| **Structural** | `regex_checks` — regex patterns on raw response | `"(?i)(stanford\|mit)"`, `"\\d+\\.?\\d*%"` |
| **Semantic** | `agent_must` — LLM-as-judge evaluation | "Response should compare MIT to Stanford" |
| **LLM Validation** | `llm_validation.criteria` — list of criteria | "Response contains specific institution names" |
| **Expected Behavior** | `llm_validation.expected_behavior` — free-text | "Should list top institutions with citation impact metrics" |
| **Error Checks** | Absence validation | "Must not contain 'Error:'" |
| **File ref** | `platform-agent-testing/automated_testing_v2/test_files/demo/comprehensive_showcase.yaml` |

### 3.4 Structural Assertions (Conductor Layer)

| Assertion Type | Conductor Field | Example |
|---|---|---|
| Schema routing | `data.response.incites_query.parsed_query.filters.schema.is` | `"Citation Topics"` vs `"Web of Science"` |
| Level routing | `data.response.incites_query.parsed_query.filters.schemalevel.is` | `"Micro"` vs `"Meso"` |
| Subject matching | `data.response.incites_query.parsed_query.filters.sbjname.is` | `"ZOOLOGY"`, `"ONCOLOGY"` |
| Compare functions | `==`, `contains`, `regex`, `iregex` | Used in `quick_yaml_runner.py` |

---

## 4. Agentic Workflow Patterns

### 4.1 Handoff Patterns

| Pattern | Implementation | Location |
|---|---|---|
| **Router → Specialist** | AppSelectorTool classifies query → routes to domain App | `wos-ri-conductor/app/conductor/conductor.py` |
| **Pipeline (Sequential)** | Agent 20 → 30 → 40 → 90 (numbered stage handoff) | `wos-ri-conductor/app/apps/` |
| **Fallback** | NotUnderstandableApp catches unclassifiable queries | `wos-ri-conductor/app/apps/` |
| **Tool Delegation** | Agent delegates to NormalizerTool, IncitesTool, VisualizerTool | `wos-ri-conductor/app/tools/` |
| **Cross-Service** | Conductor → Normalizer → AGAI API (3-hop tool call) | Conductor calls normalizer which calls agai-api for LLM reranking |

### 4.2 Tool-Use Patterns

| Pattern | Tool | Description |
|---|---|---|
| **LLM-as-classifier** | AppSelectorTool | LLM call to classify intent |
| **LLM-as-translator** | TranslatorTool | LLM call to translate query |
| **LLM-as-summarizer** | HistoryProcessorTool | LLM call to compress chat history |
| **LLM-as-reranker** | NormalizerTool pipeline | LLM reranks entity candidates |
| **LLM-as-visualizer** | VisualizerTool | LLM selects chart type |
| **LLM-as-analyst** | HighlightsTool | LLM extracts key insights |
| **API-as-tool** | IncitesTool | External API call for research data |
| **Embedding-search-as-tool** | Normalizer candidate retrieval | Vector search for entity candidates |

### 4.3 State Management

| Mechanism | Location | Description |
|---|---|---|
| **Chat history (persistent)** | `research-intelligence-core-api` | REST CRUD for chat sessions |
| **Conversation context** | `AskRequestBody.context.userquery_list` | Prior questions passed with each request |
| **NgRx store** | `research-intelligence-ui/src/app/pages/ask-ri/store/` | Frontend state: chatHistory, activeChat, activeChatId |
| **HistoryProcessorTool** | `wos-ri-conductor/app/tools/llm/` | Server-side context compression |
| **Session cookies** | `WOSRISID` | Authentication state across requests |

---

## 5. LLM Configuration Patterns

| Parameter | Usage | Location |
|---|---|---|
| **Model** | GPT-4.1 (via ClarivateAGAI) | `wos-ri-conductor/app/config.py` — `AG_ENDPOINT`, model name |
| **Temperature** | Low (deterministic for classification/routing), variable for generation | Configured per tool call in conductor |
| **Seed** | Used for reproducible test runs | AGAI API supports seed parameter |
| **Structured Outputs** | JSON schema enforcement for tool outputs | AppSelectorTool returns structured App selection |
| **Streaming (SSE)** | Token-by-token streaming to UI | `wos-ri-conductor/app/routers/api.py` → SSE stream |
| **Prompt Patterns** | System prompts per tool, `agent_must` evaluation prompts | `wos-ri-conductor/app/tools/llm/`, `prompts/` library |
| **Context Window** | Chat history compression via HistoryProcessorTool | Prevents context overflow in multi-turn conversations |
| **OpenAI-compat API** | `agai-api` exposes OpenAI-compatible endpoints | `agai-api/api/` — completions, embeddings |
| **Anthropic-compat API** | `agai-api` also exposes Anthropic endpoints | Multi-provider abstraction |
| **Caching** | Memcache + S3 for repeated LLM calls | `agai-api` caching layer |
| **Rate Limiting** | Built into agai-api | Prevents LLM API overload |

---

## 6. Knowledge Graph Statistics

| Metric | Value | Source |
|---|---|---|
| **Nodes** | 20,886 | `graphify-out/GRAPH_REPORT.md` |
| **Edges** | 52,533 | `graphify-out/GRAPH_REPORT.md` |
| **Communities** | 1,624 | `graphify-out/GRAPH_REPORT.md` |
| **Source files** | 103 files, ~32,264 words | `graphify-out/GRAPH_REPORT.md` |
| **Extraction split** | 47% EXTRACTED, 53% INFERRED | `graphify-out/GRAPH_REPORT.md` |
| **Inferred edge confidence** | avg 0.76 | 27,965 inferred edges |
| **Repos covered** | 10+ (all major repos in workspace) | Workspace-level extraction |
| **Output format** | HTML visualization + JSON graph + Obsidian vault | `graphify-out/` directory |
| **Tool** | `graphify` v0.3.20 (Python) | `graphify/` local install |

### Knowledge Graph Use Cases Demonstrated

1. **Codebase comprehension** — Visualizing relationships between 16 repos
2. **Architecture discovery** — Identifying community clusters (1,624 communities)
3. **Dependency mapping** — Understanding service-to-service relationships
4. **Context engineering** — Using graph output to build AI agent context files
5. **Audit trail** — Graph report as evidence of codebase coverage analysis

---

## 7. Repository-Level Summary

| Repo | Language | Lines of Code (Est.) | AI Components | Test Assets |
|---|---|---|---|---|
| `wos-ri-conductor` | Python | 10K+ | Agent orchestrator, 5 LLM tools, 8 domain Apps | pytest + YAML, fractional scoring |
| `wos-ai-normalizer` | Python | 5K+ | Entity resolution, LLM reranking, embedding search | Inline tests |
| `agai-api` | Python | 20K+ | LLM gateway, vector DB, MCP, Ray tasks, agent hub | pytest unit + integration |
| `platform-agent-testing` | Python | 5K+ | Test framework: LLM-as-judge, fractional scoring | 60+ YAML test files |
| `research-intelligence-ui` | TypeScript | 50K+ | Angular SPA, NgRx, WebSocket client | Jest unit tests |
| `research-intelligence-ui-tests` | TypeScript | 5K+ | Playwright + Cucumber E2E | 7 feature file groups |
| `research-intelligence-core-api` | Java | 30K+ | Spring Boot BFF, WebSocket proxy | JUnit |
| `research-intelligence-core-api-it-tests` | Java | 3K+ | REST-Assured contract tests | 7 Cucumber features |
| `research-intelligence-1pca` | Groovy | 10K+ | Analytics backend | Gradle tests |
| `graphify` | Python | 2K+ | Knowledge graph extraction | — |

---

*This document provides an AI engineering perspective on the WOSRI codebase. All references point to actual repository paths within `C:\WOSRI-Workspace\`.*
