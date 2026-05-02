# Mini-Project: Build a RAG-Powered Research Assistant

> Synthesizes everything from Stage 2 into one deployable system.
> **Time:** 3–5 hours | **Difficulty:** ★★★★☆

---

## Overview

You will build a RAG-powered assistant that can answer questions about your workspace codebase. It mirrors the architecture of your production systems:

| Your Production System | Your Mini-Project |
|----------------------|-------------------|
| `wos-ai-normalizer` (Elasticsearch + LLM reranking) | Vector store + LLM reranking |
| `wos-ri-conductor` (multi-agent orchestration + SSE) | Agent with tools + SSE streaming |
| `agai-api` (tools, memory, evaluation) | 3 tools + evaluation |

---

## Architecture

```
┌──────────────────────────────────────────────────┐
│                 FastAPI Service                    │
│                                                    │
│  POST /index     → Index workspace markdown files  │
│  POST /ask       → Ask a question (SSE stream)     │
│  GET  /health    → Health check                    │
│                                                    │
│  ┌────────────────────────────────────────────┐   │
│  │            Agent (3 tools)                  │   │
│  │                                             │   │
│  │  🔍 search_docs(query)                     │   │
│  │     → embed query → vector search → rerank  │   │
│  │                                             │   │
│  │  📝 summarize(doc_ids)                     │   │
│  │     → fetch chunks → LLM summarization      │   │
│  │                                             │   │
│  │  ⚖️ compare(query_a, query_b)              │   │
│  │     → search both → LLM comparison          │   │
│  └────────────────────────────────────────────┘   │
│                                                    │
│  ┌─────────────┐  ┌──────────────┐                │
│  │ Vector Store │  │ LLM Client   │                │
│  │ (ChromaDB    │  │ (OpenAI)     │                │
│  │  or in-memory)│  │              │                │
│  └─────────────┘  └──────────────┘                │
└──────────────────────────────────────────────────┘
```

---

## Phase 1: Indexing Pipeline (60 min)

### Goal
Index your workspace's markdown files into a vector store, mirroring the `wos-ai-normalizer` pattern.

### Steps

1. **Collect documents:**
```python
from pathlib import Path

def collect_documents(root_dir: str, pattern: str = "**/*.md") -> list[dict]:
    docs = []
    for path in Path(root_dir).glob(pattern):
        docs.append({
            "id": str(path),
            "content": path.read_text(encoding="utf-8", errors="ignore"),
            "metadata": {"filename": path.name, "directory": str(path.parent)}
        })
    return docs
```

2. **Chunk documents** (sentence-based with overlap):
```python
def chunk_document(doc: dict, max_chars: int = 1000, overlap: int = 200) -> list[dict]:
    text = doc["content"]
    chunks = []
    start = 0
    chunk_id = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        # Try to break at a sentence boundary
        if end < len(text):
            last_period = text[start:end].rfind(".")
            if last_period > max_chars // 2:
                end = start + last_period + 1
        chunks.append({
            "chunk_id": f"{doc['id']}::{chunk_id}",
            "text": text[start:end],
            "source": doc["id"],
            "metadata": doc["metadata"]
        })
        start = end - overlap
        chunk_id += 1
    return chunks
```

3. **Embed and store:**
```python
import openai

def embed_chunks(chunks: list[dict]) -> list[dict]:
    texts = [c["text"] for c in chunks]
    # Batch embed (OpenAI supports up to 2048 inputs)
    response = openai.embeddings.create(model="text-embedding-3-small", input=texts)
    for i, chunk in enumerate(chunks):
        chunk["embedding"] = response.data[i].embedding
    return chunks
```

4. **Vector store** (use ChromaDB for simplicity, or build in-memory):
```python
# Option A: ChromaDB (pip install chromadb)
import chromadb

client = chromadb.Client()
collection = client.create_collection("workspace_docs")

for chunk in embedded_chunks:
    collection.add(
        ids=[chunk["chunk_id"]],
        embeddings=[chunk["embedding"]],
        documents=[chunk["text"]],
        metadatas=[chunk["metadata"]]
    )

# Option B: In-memory with numpy
import numpy as np

class SimpleVectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = None
    
    def add(self, chunks):
        self.chunks.extend(chunks)
        self.embeddings = np.array([c["embedding"] for c in self.chunks])
    
    def search(self, query_embedding, top_k=5):
        query = np.array(query_embedding)
        similarities = np.dot(self.embeddings, query) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query)
        )
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [(self.chunks[i], float(similarities[i])) for i in top_indices]
```

### Connection to Your Workspace
- Your chunking mirrors `DocumentChunk` at `agai-api/api/models.py:835`
- Your embedding mirrors `BaseEmbedFunction` at `agai-api/api/embeddingfunctions/baseembedfunction.py`
- Your vector store mirrors `BaseVectorStore` at `agai-api/api/vectordatabases/basevectorstore.py`

---

## Phase 2: Retrieval + Reranking (45 min)

### Goal
Build retrieval with LLM-based reranking, mirroring the `IncitesOrgNameReranker` pattern.

### Steps

1. **Basic retrieval:**
```python
def retrieve(query: str, top_k: int = 10) -> list[dict]:
    query_embedding = embed_chunks([{"text": query}])[0]["embedding"]
    return vector_store.search(query_embedding, top_k=top_k)
```

2. **LLM reranking** (modeled on `incites_orgname_reranker.py:10`):
```python
def rerank(query: str, candidates: list[dict], top_k: int = 3) -> list[dict]:
    # Build candidate list for the LLM
    candidate_texts = [f"[{i}] {c['text'][:200]}..." for i, (c, score) in enumerate(candidates)]
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "system",
            "content": "You are a relevance judge. Given a query and candidate text passages, rank them by relevance."
        }, {
            "role": "user",
            "content": f"Query: {query}\n\nCandidates:\n" + "\n".join(candidate_texts)
        }],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "reranking",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "ranked_indices": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Candidate indices ordered by relevance (most relevant first)"
                        }
                    },
                    "required": ["ranked_indices"],
                    "additionalProperties": False
                }
            }
        }
    )
    
    import json
    result = json.loads(response.choices[0].message.content)
    return [candidates[i] for i in result["ranked_indices"][:top_k]]
```

### Connection to Your Workspace
- Two-stage retrieval (cheap→expensive) matches `ElasticsearchNormalizerTool` → `IncitesOrgNameReranker`
- JSON Schema with `strict: True` matches `orgname_reranker_response_format()` at `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py:10`

---

## Phase 3: Agent Layer (60 min)

### Goal
Build an agent with 3 tools using OpenAI function calling.

### Steps

1. **Define tools:**
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": "Search the workspace documentation for relevant passages. Use when the user asks a question about the codebase, architecture, or any topic covered in the docs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "summarize",
            "description": "Summarize specific documents or search results. Use when the user asks for a summary or overview of a topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "The text to summarize"},
                    "style": {"type": "string", "enum": ["brief", "detailed"], "description": "Summary style"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "compare",
            "description": "Compare two topics, approaches, or code patterns. Use when the user asks to compare or contrast things.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic_a": {"type": "string", "description": "First topic to search for"},
                    "topic_b": {"type": "string", "description": "Second topic to search for"}
                },
                "required": ["topic_a", "topic_b"]
            }
        }
    }
]
```

2. **Implement the agent loop:**
```python
def execute_tool(name: str, args: dict) -> str:
    if name == "search_docs":
        results = retrieve(args["query"])
        reranked = rerank(args["query"], results)
        return "\n\n".join([f"[Source: {c['source']}]\n{c['text']}" for c, score in reranked])
    elif name == "summarize":
        # Direct LLM call for summarization
        resp = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Summarize ({args.get('style', 'brief')}):\n{args['text']}"}]
        )
        return resp.choices[0].message.content
    elif name == "compare":
        results_a = retrieve(args["topic_a"])
        results_b = retrieve(args["topic_b"])
        context_a = "\n".join([c["text"] for c, _ in results_a[:3]])
        context_b = "\n".join([c["text"] for c, _ in results_b[:3]])
        resp = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Compare:\n\nTopic A ({args['topic_a']}):\n{context_a}\n\nTopic B ({args['topic_b']}):\n{context_b}"}]
        )
        return resp.choices[0].message.content

async def run_agent(query: str, messages: list = None):
    if messages is None:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.append({"role": "user", "content": query})
    
    while True:
        response = openai.chat.completions.create(
            model="gpt-4o", messages=messages, tools=tools
        )
        msg = response.choices[0].message
        
        if msg.tool_calls:
            messages.append(msg.model_dump())
            for tc in msg.tool_calls:
                import json
                args = json.loads(tc.function.arguments)
                result = execute_tool(tc.function.name, args)
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
                yield {"type": "tool_call", "name": tc.function.name, "result_preview": result[:200]}
        else:
            yield {"type": "answer", "content": msg.content}
            break
```

---

## Phase 4: RAGAS Evaluation (45 min)

### Goal
Evaluate your RAG pipeline using RAGAS metrics.

### Steps

1. **Install RAGAS:**
```bash
pip install ragas
```

2. **Create a test dataset:**
```python
test_cases = [
    {
        "question": "What is the conductor pattern?",
        "ground_truth": "A central orchestrator that routes and manages agent execution, implemented in the Conductor class.",
        "contexts": []  # Will be filled by your retriever
    },
    {
        "question": "How does memory swap work in agents?",
        "ground_truth": "Old large messages are archived with a retrieval placeholder. The agent can retrieve them on demand using a tool.",
        "contexts": []
    },
    # Add 8-10 more test cases
]
```

3. **Run evaluation:**
```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

# For each test case, run your pipeline and collect:
# - The retrieved contexts
# - The generated answer
# Then evaluate with RAGAS

results = evaluate(
    dataset=your_dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)
print(results)
```

4. **Interpret results:**

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| Faithfulness | Is the answer supported by the retrieved context? | >0.8 |
| Answer Relevancy | Does the answer actually address the question? | >0.8 |
| Context Precision | Are the retrieved contexts actually relevant? | >0.7 |
| Context Recall | Did retrieval find all the relevant information? | >0.7 |

### Connection to Your Workspace
- RAGAS is already used in your platform: `agai-api/tests/unittests/test_rag_ragas.py`

---

## Phase 5: FastAPI Service with SSE (45 min)

### Goal
Deploy as a FastAPI service with SSE streaming, mirroring `wos-ri-conductor`.

```python
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import json, asyncio

app = FastAPI(title="RAG Research Assistant")

@app.post("/index")
async def index_docs(root_dir: str = "./"):
    docs = collect_documents(root_dir)
    chunks = []
    for doc in docs:
        chunks.extend(chunk_document(doc))
    embedded = embed_chunks(chunks)
    vector_store.add(embedded)
    return {"indexed": len(embedded), "documents": len(docs)}

@app.post("/ask")
async def ask(request: Request, query: str):
    async def stream():
        async for event in run_agent(query):
            if await request.is_disconnected():
                break
            yield f"data: {json.dumps(event)}\n\n"
            await asyncio.sleep(0)  # yield control
        yield f"data: {json.dumps({'type': 'done'})}\n\n"
    
    return StreamingResponse(stream(), media_type="text/event-stream")

@app.get("/health")
async def health():
    return {"status": "ok", "indexed_chunks": len(vector_store.chunks)}
```

### Connection to Your Workspace
- SSE pattern matches `Streaming` at `wos-ri-conductor/app/util/sse.py:11`
- Disconnect detection matches line 20: `request.is_disconnected()`

---

## Deliverables Checklist

- [ ] Indexing pipeline: collect → chunk → embed → store
- [ ] Retrieval: vector search → LLM reranking
- [ ] Agent: 3 tools (search, summarize, compare) with function calling
- [ ] RAGAS evaluation: 10+ test cases, 4 metrics, all >0.7
- [ ] FastAPI service: `/index`, `/ask` (SSE), `/health`
- [ ] Test with 10 diverse questions about your workspace

---

## Stretch Goals

1. **Hybrid search:** Add keyword matching alongside vector search (like your normalizer's constant_score + match)
2. **Query expansion:** Before searching, generate alternative phrasings (like `IncitesLocationAlternativesTool`)
3. **Memory:** Add conversation history so the agent can handle follow-up questions
4. **Multi-agent:** Add a router that dispatches to different specialist agents (code vs docs)
5. **MCP server:** Expose your search tool as an MCP server
