# Stage 2: Resources

> Curated external learning resources (2024–2025). Prioritized by value.

---

## Tier 1: Essential (Read/Watch These First)

### Papers

| Resource | Why | Time |
|----------|-----|------|
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020) | The foundational RAG paper. Read at least the abstract and Section 2. | 30 min |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (Yao et al., 2022) | The paper that formalized the agent reasoning loop your conductor uses. | 30 min |
| [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) (Schick et al., 2023) | How LLMs learn to use tools — the theoretical basis for function calling. | 30 min |

### Courses

| Resource | Why | Time |
|----------|-----|------|
| [Andrew Ng — Building Agentic AI](https://www.deeplearning.ai/courses/) (DeepLearning.AI) | Andrew Ng's course on agentic patterns: reflection, tool use, planning, multi-agent. Practical and concise. | 3–4 hours |
| [LangChain — Introduction to LangGraph](https://academy.langchain.com/) | Hands-on course on building agent workflows with LangGraph. Good complement to your conductor pattern understanding. | 2–3 hours |

### Blog Posts

| Resource | Why | Time |
|----------|-----|------|
| [Lilian Weng — LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) | The definitive blog post on agent architecture. Covers planning, memory, tools with excellent diagrams. | 45 min |
| [Lilian Weng — Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) | Systematic coverage of prompt engineering techniques with examples. | 30 min |
| [Anthropic — Model Context Protocol](https://modelcontextprotocol.io/) | Official MCP specification and documentation. Your agai-api implements this. | 30 min |

---

## Tier 2: Deep Dives (For Specific Topics)

### RAG

| Resource | Why |
|----------|-----|
| [LlamaIndex Documentation](https://docs.llamaindex.ai/) | The most comprehensive RAG framework. Excellent documentation on chunking, retrieval, reranking strategies. |
| [Pinecone — RAG Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/) | Practical guide to RAG with vector databases. Good diagrams. |
| [Jerry Liu — Building Production RAG](https://www.youtube.com/results?search_query=jerry+liu+production+rag) (YouTube talks) | LlamaIndex CEO on production RAG challenges: chunking, evaluation, hybrid search. |
| [RAGAS Documentation](https://docs.ragas.io/) | The framework for evaluating RAG systems. Your agai-api uses RAGAS (`test_rag_ragas.py`). |

### Agents

| Resource | Why |
|----------|-----|
| [LangChain Documentation](https://python.langchain.com/docs/) | Comprehensive agent framework. Study the agent types and tool integration patterns. |
| [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) | Graph-based agent orchestration — similar philosophy to your conductor pattern. |
| [Harrison Chase (LangChain CEO) — Talks on Agent Architecture](https://www.youtube.com/results?search_query=harrison+chase+agent+architecture) | Practical insights on building production agent systems. |
| [OpenAI — Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) | Official documentation on the function calling mechanism your platform uses. |
| [OpenAI — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) | The `strict: true` JSON Schema mode your workspace uses extensively. |

### Embeddings & Vector Databases

| Resource | Why |
|----------|-----|
| [OpenAI — Embeddings Guide](https://platform.openai.com/docs/guides/embeddings) | Official guide to OpenAI embeddings. |
| [Weaviate Documentation](https://weaviate.io/developers/weaviate) | Your workspace uses Weaviate. Study the HNSW index, hybrid search, and filtering. |
| [Jay Alammar — The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/) | Visual explanation of how embeddings capture meaning. Foundational understanding. |

### MCP

| Resource | Why |
|----------|-----|
| [MCP Specification](https://spec.modelcontextprotocol.io/) | The full protocol specification. |
| [MCP GitHub Repository](https://github.com/modelcontextprotocol) | Reference implementations, SDKs, examples. |
| [Anthropic — Introducing MCP](https://www.anthropic.com/news/model-context-protocol) | The announcement post explaining the "why" behind MCP. |

### Prompt Engineering

| Resource | Why |
|----------|-----|
| [OpenAI — Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | Official best practices from OpenAI. |
| [Anthropic — Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) | Anthropic's guide — different perspective, complementary to OpenAI's. |
| [DAIR.AI — Prompt Engineering Guide](https://www.promptingguide.ai/) | Community-maintained, comprehensive, well-organized. |

---

## Tier 3: Stay Current (Follow These)

| Resource | Type | Why |
|----------|------|-----|
| [Simon Willison's Blog](https://simonwillison.net/) | Blog | Tracks every development in LLM tooling. Particularly good on MCP and agent patterns. |
| [The Batch by Andrew Ng](https://www.deeplearning.ai/the-batch/) | Newsletter | Weekly AI news curated by Andrew Ng. |
| [Latent Space Podcast](https://www.latent.space/) | Podcast | Deep technical conversations with AI builders. |
| [AI Engineering subreddit](https://www.reddit.com/r/AIEngineering/) | Community | Practical discussions on building AI systems. |
| [LangChain Blog](https://blog.langchain.dev/) | Blog | Agent architecture patterns and case studies. |

---

## Recommended Reading Order

If you have limited time, read in this order:

1. **Lilian Weng — LLM Powered Autonomous Agents** (45 min) — gives you the full mental model
2. **Andrew Ng — Building Agentic AI course** (3 hrs) — hands-on understanding
3. **Lewis et al. RAG paper** (abstract + Section 2, 15 min) — foundational context
4. **OpenAI Function Calling + Structured Outputs guides** (30 min) — practical tool-use knowledge
5. **MCP specification overview** (20 min) — understand the standard your platform implements

Total: ~5 hours for the essential knowledge.
