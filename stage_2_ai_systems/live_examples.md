# Stage 2: Live Examples — Workspace File Mapping

> Every concept from `concepts.md` mapped to specific files and line numbers in your workspace.
> Open these files alongside the textbook to see the theory in production code.

---

## Chapter 1: RAG

### 1.1 The Hallucination Problem / Your Normalizer as RAG

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| RAG pipeline entry point | `wos-ai-normalizer/app/util/normalizer.py` | 9–32 | `run_normalizer()` — the full retrieve→generate cycle in 32 lines |
| Elasticsearch retrieval base | `wos-ai-normalizer/app/tools/__init__.py` | 19–235 | `ElasticsearchNormalizerTool` — abstract RAG retriever |
| OrgName RAG pipeline | `wos-ai-normalizer/app/tools/incites/incites_orgname_normalizer.py` | 14–88 | Full pipeline: alternatives → ES search → LLM reranking |
| Router (incites endpoints) | `wos-ai-normalizer/app/routers/incites.py` | — | HTTP endpoints that trigger normalization |

### 1.2 RAG Architecture — The 3 Stages

| Stage | File | Lines | What to Look At |
|-------|------|-------|-----------------|
| **Retrieval:** ES query builder | `wos-ai-normalizer/app/tools/__init__.py` | 73–115 | `_query_without_ranker()` — builds boost + constant_score queries |
| **Retrieval:** ES execution | `wos-ai-normalizer/app/tools/__init__.py` | 150+ | The `_run()` method executes ES queries and collects results |
| **Retrieval:** Index selection | `wos-ai-normalizer/app/tools/incites/incites_orgname_normalizer.py` | 50–56 | Dynamic index selection with environment suffix |
| **Generation:** Reranker | `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py` | 59–176 | LLM-based reranking of ES candidates |
| **Generation:** Response format | `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py` | 10–52 | JSON Schema for structured reranker output |

### 1.3 Embeddings

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Base embedding interface | `agai-api/api/embeddingfunctions/baseembedfunction.py` | 1–10 | `get_embedding()` and `embedding_openaicompat()` abstract methods |
| OpenAI embeddings | `agai-api/api/embeddingfunctions/openaiembedmodel.py` | — | Production embedding with OpenAI API |
| In-house embeddings | `agai-api/api/embeddingfunctions/inhouseembedmodel.py` | — | Self-hosted embedding model |
| CLIP (multimodal) | `agai-api/api/embeddingfunctions/clipembedmodel.py` | — | Text + image embeddings |
| Factory pattern | `agai-api/api/embeddingfunctions/embedfunctionfactory.py` | — | Selects the right embedding model |
| Embedding router | `agai-api/api/routers/embeddingfunctions.py` | — | HTTP endpoints for embedding requests |
| Embedding config model | `agai-api/api/models.py` | 64–84 | `EmbeddingConfig` — model, cost, deployment |
| Embedding tests | `agai-api/tests/unittests/test_embed_st.py` | — | SentenceTransformer embedding tests |

### 1.4 Vector Databases

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Base vector store | `agai-api/api/vectordatabases/basevectorstore.py` | — | Abstract interface for vector operations |
| Weaviate implementation | `agai-api/api/vectordatabases/weaviatevectorstore.py` | — | Weaviate-specific search, indexing, deletion |
| AI21 implementation | `agai-api/api/vectordatabases/ai21vectorstore.py` | — | AI21-specific vector store |
| Factory | `agai-api/api/vectordatabases/vectorstorefactory.py` | — | Vector DB selection logic |
| Collection model | `agai-api/api/models.py` | 211–218 | `Collection` ties vector DB + embedding config |
| Vector DB config | `agai-api/api/models.py` | — | `VectorDatabaseConfig` model |
| Vector DB tests | `agai-api/tests/unittests/test_vecdb_wv.py` | — | Weaviate vector store tests |
| Vector DB tests (AI21) | `agai-api/tests/unittests/test_vecdb_ai21.py` | — | AI21 vector store tests |

### 1.5 Chunking

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| DocumentChunk model | `agai-api/api/models.py` | 835+ | `DocumentChunk` — chunk storage model |
| Document processing | `agai-api/api/agenthub/utils/conversation.py` | — | `process_document_chunks()` — how uploaded docs become chunks |

### 1.6 Advanced RAG Patterns

| Pattern | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| **Hybrid search** (sparse+dense) | `wos-ai-normalizer/app/tools/__init__.py` | 73–115 | Constant score (exact) + match (fuzzy) in one ES query |
| **Reranking** — OrgName | `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py` | 59+ | Full LLM reranker with structured output |
| **Reranking** — Location | `wos-ai-normalizer/app/tools/incites/llm/incites_location_reranker.py` | — | Location-specific reranking |
| **Reranking** — Author | `wos-ai-normalizer/app/tools/incites/llm/incites_author_reranker.py` | — | Author-specific reranking |
| **Reranking** — Journal | `wos-ai-normalizer/app/tools/incites/llm/incites_journal_reranker.py` | — | Journal-specific reranking |
| **Query expansion** — Org | `wos-ai-normalizer/app/tools/common/llm/incites_orgname_alternatives.py` | — | Generates org name alternatives |
| **Query expansion** — Location | `wos-ai-normalizer/app/tools/incites/llm/incites_location_alternatives.py` | 16–74 | Generates location name alternatives with rules |
| **Query expansion** — Journal | `wos-ai-normalizer/app/tools/incites/llm/incites_journal_alternatives.py` | — | Journal name alternatives |
| **Query expansion** — Funding | `wos-ai-normalizer/app/tools/incites/llm/incites_funding_agency_alternatives.py` | — | Funding agency alternatives |
| **Query expansion** — Conductor | `wos-ri-conductor/app/tools/local/normalizer/alternatives/alternatives_generator.py` | — | Conductor-side alternative generation |
| **RAGAS evaluation** | `agai-api/tests/unittests/test_rag_ragas.py` | — | RAG evaluation with RAGAS metrics |
| **RAG classification** | `agai-api/tests/unittests/test_rag_classifier.py` | — | RAG query classification |

---

## Chapter 2: Agent Architecture

### 2.1 What Is an Agent?

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| App (agent) base class | `wos-ri-conductor/app/apps/__init__.py` | 63–67 | `App(ABC)` with `name` and `description` |
| App.run() orchestration | `wos-ri-conductor/app/apps/__init__.py` | 78–80 | Streaming setup, error handling wrapper |
| OrganizationsApp | `wos-ri-conductor/app/apps/organizations_app.py` | — | A complete specialized agent |
| ResearchersApp | `wos-ri-conductor/app/apps/researchers_app.py` | — | Another specialized agent |
| LocationsApp | `wos-ri-conductor/app/apps/locations_app.py` | — | Location-focused agent |
| NotUnderstandableApp | `wos-ri-conductor/app/apps/not_understandable_app.py` | 8–28 | Fallback agent — graceful degradation |

### 2.2 Agent Components

| Component | File | Lines | What to Look At |
|-----------|------|-------|-----------------|
| **Brain:** BaseAgent init | `agai-api/api/agenthub/agents/baseagent.py` | 59–100 | Agent initialization with LLM config |
| **Brain:** Config loading | `agai-api/api/agenthub/agents/baseagent.py` | 102–145 | `load_config()` — prompt, tools, memory settings, MCP |
| **Brain:** AgentConfig model | `agai-api/api/models.py` | 500–549 | Full agent configuration with all fields |
| **Brain:** System prompt + date | `agai-api/api/agenthub/agents/baseagent.py` | 121–123 | Prompt augmentation with handoff instructions and date |
| **Tools:** ToolConfig model | `agai-api/api/models.py` | 372–428 | Tool definition with description, params, class |
| **Tools:** ToolParameter model | `agai-api/api/models.py` | 430–462 | Parameter schema for LLM tool calls |
| **Tools:** BaseTool runtime | `agai-api/api/agenthub/tools/basetool.py` | 6–114 | Runtime tool initialization from config |
| **Tools:** Tool factory | `agai-api/api/agenthub/tools/toolfactory.py` | — | Creates correct tool class from config |
| **Tools:** LocalTool | `agai-api/api/agenthub/tools/localtool.py` | — | Python function execution |
| **Tools:** HTTPTool | `agai-api/api/agenthub/tools/httptool.py` | — | External API calls |
| **Tools:** HandoffTool | `agai-api/api/agenthub/tools/handofftool.py` | — | Agent-to-agent handoff |
| **Tools:** AgentAsTool | `agai-api/api/agenthub/tools/agentastool.py` | — | Nested agent execution |
| **Memory:** Conversation model | `agai-api/api/models.py` | 616+ | Full conversation with messages and state |
| **Planner:** Agent factory | `agai-api/api/agenthub/agents/agentfactory.py` | — | Creates agents from config |
| **Planner:** SinglePromptAgent | `agai-api/api/agenthub/agents/singlepromptagent.py` | — | Simplest agent type |

### 2.3 Tool Use (Function Calling)

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Tool description as prompt | `agai-api/api/models.py` | 376 | `description: str` — the LLM reads this |
| Tool parameter types | `agai-api/api/models.py` | 446–450 | Allowed types: number, string, array, object |
| `send_result_to` | `agai-api/api/models.py` | 388, 400–413 | Where tool results go: conversation, client |
| `tool_class` validation | `agai-api/api/models.py` | 393–398 | Allowed: LocalTool, HTTPTool, HandoffTool, AgentAsTool |
| Tool init from config | `agai-api/api/agenthub/tools/basetool.py` | 16–60 | Config values → instance attributes, parameter building |
| Internal state params | `agai-api/api/models.py` | 472–481 | `ToolInternalStateParameter` — state propagation |
| Internal state in tool | `agai-api/api/agenthub/tools/basetool.py` | 48–54 | Internal state parameter mapping |

### 2.4 Multi-Agent Systems

| Pattern | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| **Router:** Conductor | `wos-ri-conductor/app/conductor/conductor.py` | 29–44 | App list + AppSelector setup |
| **Router:** AppSelectorTool | `wos-ri-conductor/app/tools/llm/app_selector.py` | 9–97 | Routing LLM prompt + structured output |
| **Router:** App descriptions | `wos-ri-conductor/app/apps/not_understandable_app.py` | 10–20 | Description as routing hint |
| **Router:** Conduct flow | `wos-ri-conductor/app/conductor/conductor.py` | 51–108 | Full orchestration: validate→translate→route→execute |
| **Handoff:** Config | `agai-api/api/models.py` | 520–533 | `handoffs`, `handoff_description`, `handoff_input_type`, `handoff_input_filter` |
| **Handoff:** Tool | `agai-api/api/agenthub/tools/handofftool.py` | — | HandoffTool implementation |
| **Handoff:** Filter logic | `agai-api/api/agenthub/agents/baseagent.py` | 157–159 | `handoff_filter_tools()` |
| **Agent-as-Tool** | `agai-api/api/agenthub/tools/agentastool.py` | — | Agent wrapped as callable tool |
| **Traversal link** | `agai-api/api/models.py` | 495–498 | `AgentConfigTraversalLink` — agent graph edges |

### 2.5 Agent Memory

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Memory truncation | `agai-api/api/agenthub/agents/memorymanagement/truncatemessages.py` | — | `truncate_messages()`, `fix_tool_calls()` |
| Memory swap (archive) | `agai-api/api/agenthub/agents/memorymanagement/swapmemory.py` | 25–52 | `archive()` — replace content with retrieval instruction |
| Swap placeholder text | `agai-api/api/agenthub/agents/memorymanagement/swapmemory.py` | 38–42 | The archived message placeholder |
| nth user message index | `agai-api/api/agenthub/agents/memorymanagement/swapmemory.py` | 9–23 | Logic for deciding what to archive |
| Internal state init | `agai-api/api/agenthub/agents/baseagent.py` | 84–85 | `conversation.init_internal_state()` |
| hide_above config | `agai-api/api/models.py` | 534 | When to hide large messages |
| hide_older_tool_messages | `agai-api/api/models.py` | 535 | Age threshold for tool message hiding |
| hide_older_assistant | `agai-api/api/models.py` | 536 | Age threshold for assistant message hiding |
| repeat_system_prompt | `agai-api/api/models.py` | 537 | System prompt reinforcement frequency |
| continue_message | `agai-api/api/models.py` | 538 | Message to append when continuing |

---

## Chapter 3: Orchestration Patterns

### 3.1 The Conductor Pattern

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Conductor class | `wos-ri-conductor/app/conductor/conductor.py` | 29–44 | Class-level app registry and LLM engines |
| conduct() method | `wos-ri-conductor/app/conductor/conductor.py` | 51–108 | Full pipeline: validate → translate → route → execute |
| Input validation | `wos-ri-conductor/app/conductor/conductor.py` | 59 | `in_understandable_input()` check |
| Translation step | `wos-ri-conductor/app/conductor/conductor.py` | 66–80 | Translate non-English queries |
| Config | `wos-ri-conductor/app/config.py` | — | All conductor configuration |

### 3.2 Streaming

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Streaming class | `wos-ri-conductor/app/util/sse.py` | 11–58 | Full SSE implementation |
| Message format | `wos-ri-conductor/app/util/sse.py` | 19–38 | SSE event structure with id, retry, data |
| Disconnect detection | `wos-ri-conductor/app/util/sse.py` | 20–21 | `request.is_disconnected()` check |
| Exception streaming | `wos-ri-conductor/app/util/sse.py` | 40–58 | Error events with type-based codes |
| App streaming (yield) | `wos-ri-conductor/app/apps/not_understandable_app.py` | 28 | `yield streaming.message(data)` pattern |

### 3.3 Error Handling

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Graceful degradation | `wos-ri-conductor/app/apps/not_understandable_app.py` | 8–28 | Dedicated fallback handler |
| Input validation | `wos-ri-conductor/app/conductor/conductor.py` | 59–64 | Character ratio check |
| Error streaming | `wos-ri-conductor/app/util/sse.py` | 40–58 | SSE error events |
| Normalizer error handling | `wos-ai-normalizer/app/util/normalizer.py` | 24–29 | Try/except with error codes |
| Retry manager | `platform-agent-testing/automated_testing_v2/core/retry_manager.py` | — | Systematic retry logic |
| Retry utils (v1) | `platform-agent-testing/automated_testing/retry_utils.py` | — | Earlier retry utilities |

---

## Chapter 4: MCP

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| Alma MCP Server | `agai-api/api/routers/mcp/alma/server.py` | 16 | `AlmaMcpServer(MCPServer)` |
| Primo MCP Server | `agai-api/api/routers/mcp/primo/server.py` | 16 | `PrimoMcpServer(MCPServer)` |
| MCP Server base | `agai-api/api/routers/mcp/servers/base.py` | 70, 186 | `MCPServerConfig`, `MCPServer` base class |
| MCP Servers Manager | `agai-api/api/routers/mcp/servers/manager.py` | 60, 73 | `MCPAppState`, `MCPServersManager` |
| MCP Config Parser | `agai-api/api/routers/mcp/servers/config_parser.py` | 18–153 | SSM + PostgreSQL config backends |
| MCP Middleware | `agai-api/api/routers/mcp/servers/middleware.py` | 42 | `MCPComponentsFilteringMiddleware` |
| MCP List Cache | `agai-api/api/models.py` | 483–489 | Cache MCP tool lists per agent |
| MCP OAuth | `agai-api/api/routers/mcp/oauth/oauth_manager.py` | 41 | `MCPOAuthManager` |
| MCP Admin router | `agai-api/api/routers/mcp_admin.py` | — | Administration endpoints |
| MCP Docs router | `agai-api/api/routers/mcp_docs.py` | — | Documentation endpoints |
| MCP Service Settings | `agai-api/api/models.py` | 850+ | Per-service configuration model |
| MCP Institution Settings | `agai-api/api/models.py` | 884+ | Per-institution overrides |
| MCP Errors | `agai-api/api/routers/mcp/utils/mcp_errors.py` | 1–34 | Error hierarchy: MCPError → ValidationError, AuthError, ApiHTTPError |
| Agent MCP config loading | `agai-api/api/agenthub/agents/baseagent.py` | 137 | `self.mcp_servers` loaded from agent config |
| Responses API trigger | `agai-api/api/agenthub/agents/baseagent.py` | 144 | MCP forces use of Responses API |
| MCP cache utils | `agai-api/api/agenthub/utils/openai.py` | — | `get_mcp_list_cache`, `update_mcp_list_cache` |
| MCP tests | `agai-api/tests/unittests/test_mcp_servers_manager.py` | — | Server manager unit tests |
| MCP config tests | `agai-api/tests/unittests/test_mcp_config_parsing.py` | — | Config parsing tests |
| MCP admin tests | `agai-api/tests/unittests/test_mcp_admin.py` | — | Admin endpoint tests |
| MCP middleware tests | `agai-api/tests/unittests/test_mcp_servers_manager_middlewares.py` | — | Middleware filtering tests |
| Primo MCP integration | `agai-api/tests/integrationtests/test_primo_mcp_server.py` | — | End-to-end Primo MCP test |

---

## Chapter 5: Prompt Engineering

| Concept | File | Lines | What to Look At |
|---------|------|-------|-----------------|
| **Role prompting:** AppSelector | `wos-ri-conductor/app/tools/llm/app_selector.py` | 66–97 | Full router prompt with role, context, task |
| **Role prompting:** Reranker | `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py` | 59+ | Reranking prompt |
| **Role prompting:** Alternatives | `wos-ai-normalizer/app/tools/incites/llm/incites_location_alternatives.py` | 29–48 | Location alternatives prompt with rules |
| **Structured output:** AppSelector | `wos-ri-conductor/app/tools/llm/app_selector.py` | 12–44 | JSON Schema with strict mode |
| **Structured output:** Reranker | `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py` | 10–52 | Schema with enum constraints |
| **System prompt:** Agent config | `agai-api/api/models.py` | 504 | `system_prompt: str` on AgentConfig |
| **Prompt augmentation** | `agai-api/api/agenthub/agents/baseagent.py` | 121–123 | Handoff instructions + date appended |
| **Query parsing** | `wos-ri-conductor/app/tools/llm/incites/query_parser.py` | — | NL query → structured entities |
| **Query correction** | `wos-ri-conductor/app/tools/llm/incites/query_corrector.py` | — | Post-parse correction prompts |
| **Translation prompt** | `wos-ri-conductor/app/tools/llm/translator.py` | — | Translation system prompt |
| **Visualizer prompt** | `wos-ri-conductor/app/tools/llm/visualizer.py` | — | Chart recommendation prompt |
| **Input sanitization** | `wos-ri-conductor/app/tools/llm/app_selector.py` | 5–6 | `_sanitize_input()` — remove backticks |
| **Input sanitization** | `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py` | 55–56 | Same pattern in normalizer |

---

## Cross-Cutting: Testing

| Concept | File | What to Look At |
|---------|------|-----------------|
| Conductor regression tests | `wos-ri-conductor/test/regression_test.py` | End-to-end pipeline tests |
| Parser test runner | `wos-ri-conductor/test/parser_test_runner.py` | NL parsing accuracy tests |
| Impact agent tests | `wos-ri-conductor/test/impact_agent_test.py` | Agent flow tests |
| AGAI unit tests | `agai-api/tests/unittests/` | ~40 test files covering all components |
| AGAI integration tests | `agai-api/tests/integrationtests/` | End-to-end tests |
| Agent integration test | `agai-api/tests/integrationtests/test_agents.py` | Full agent execution tests |
| Swap agent test | `agai-api/tests/integrationtests/test_swap_agent.py` | Memory swap integration test |
| Platform agent testing | `platform-agent-testing/automated_testing_v2/` | Systematic agent validation framework |
