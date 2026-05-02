# Stage 2: AI Systems — Concepts

> A comprehensive textbook on RAG, agents, tool-use, memory, orchestration, and prompt engineering.
> Designed to read cover-to-cover AND use as a reference.

---

# Chapter 1: Retrieval-Augmented Generation (RAG) [PARETO-20]

## 1.1 The Hallucination Problem (Why RAG Was Invented)

### What Problem Does RAG Solve?

LLMs make things up. That's not a bug — it's how they work.

An LLM is a next-token predictor. Given some text, it predicts the most probable next word. It doesn't "know" facts — it learned patterns from training data. When it encounters a question where the patterns in its training data don't clearly point to one answer, it generates the *most probable-sounding* answer. That answer might be correct. It might be completely fabricated. The LLM doesn't know the difference — it has no concept of truth, only of probability.

**Analogy:** Imagine a brilliant medical expert who studied exhaustively 10 years ago but hasn't read a single paper since. When you ask about a treatment approved last year, they don't say "I don't know." They confidently describe something *plausible-sounding* based on their old knowledge. That's hallucination.

### The Core Insight

The LLM is good at *reasoning about text* but unreliable at *remembering specific facts*. What if we separated those two jobs?

- **The LLM's job:** Reason, synthesize, explain, compare
- **Something else's job:** Find the right information

This is Retrieval-Augmented Generation:

```
User Question → RETRIEVE relevant documents → GIVE documents to LLM → LLM GENERATES answer using those documents
```

Instead of asking the LLM "What is X?" (relying on its memory), you:
1. Search a database for documents about X
2. Hand those documents to the LLM
3. Ask: "Based on THESE documents, what is X?"

Now the LLM reasons over *provided evidence* rather than *recalled training data*. Hallucination drops dramatically.

### Your Workspace IS a RAG Pipeline

Your `wos-ai-normalizer` is a RAG system, even though nobody calls it that:

| RAG Component | Your Normalizer Equivalent |
|---------------|---------------------------|
| User query | Entity to normalize (e.g., "MIT") |
| Retrieval | Elasticsearch query (`ElasticsearchNormalizerTool`) |
| Retrieved docs | Candidate organizations from the index |
| Generation | LLM reranker picks the best match (`IncitesOrgNameReranker`) |

When someone types "MIT" and the system needs to map it to the correct InCites organization, it doesn't ask the LLM "What is MIT's official name?" (hallucination risk). It retrieves candidates from Elasticsearch, then asks the LLM "Which of THESE candidates best matches MIT?" That's RAG.

### First Principle

> **RAG = Don't trust the LLM's memory. Give it the answers and let it reason.**

The Lewis et al. 2020 paper ("Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks") formalized this, but the intuition is ancient: open-book exams beat closed-book exams for factual accuracy.

---

## 1.2 RAG Architecture (First Principles)

### The 3 Stages

Every RAG system has three stages. No exceptions. If you understand these three stages, you understand RAG.

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  INDEXING    │ →   │  RETRIEVAL   │ →   │  GENERATION  │
│ (offline)    │     │  (at query   │     │  (at query   │
│              │     │   time)      │     │   time)      │
└─────────────┘     └──────────────┘     └──────────────┘
```

### Stage 1: Indexing (Offline — Done Once or Periodically)

**What problem?** You have a mountain of documents. You need to make them *searchable* in a way that captures *meaning*, not just keywords.

**Steps:**
1. **Collect** your source documents (PDFs, web pages, databases, markdown files)
2. **Split** them into chunks (more on this in §1.5)
3. **Embed** each chunk — convert it into a vector (more on this in §1.3)
4. **Store** the vectors in a vector database (more on this in §1.4)

```
Documents → Split into chunks → Convert to vectors → Store in vector DB
```

**Analogy:** Building the index at the back of a textbook. You read the entire book once, identify key topics in each section, and create a lookup system. The index itself is not the book — it's a map to find things quickly.

### Stage 2: Retrieval (Online — At Query Time)

**What problem?** The user asks a question. You need to find the most relevant chunks from your indexed documents.

**Steps:**
1. **Embed** the user's query (same embedding model as indexing)
2. **Search** the vector database for chunks closest to the query
3. **Optionally rerank** the results with a more sophisticated model

```
User Query → Convert to vector → Find nearest vectors in DB → Return top-k chunks
```

**Your workspace:** The normalizer does this in `ElasticsearchNormalizerTool`:
- The user input ("Massachusetts Institute of Technology") gets converted to a search query
- Elasticsearch finds candidate matches using both exact matching and fuzzy matching
- See `wos-ai-normalizer/app/tools/__init__.py:73` — the `_query_without_ranker` method builds the Elasticsearch query with boosted exact matches and fuzzy alternatives

### Stage 3: Generation (Online — At Query Time)

**What problem?** You have relevant chunks. Now you need to synthesize a coherent answer.

**Steps:**
1. **Construct** a prompt with: system instructions + retrieved chunks + user question
2. **Send** to the LLM
3. **Parse** the response

```
System Prompt + Retrieved Chunks + User Question → LLM → Answer
```

**Your workspace:** The reranker does this — `IncitesOrgNameReranker` at `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py:59` takes the Elasticsearch candidates and asks the LLM to rank them.

### The Key Insight About RAG Architecture

The three stages have *different optimization strategies*:

| Stage | Optimize for | Trade-offs |
|-------|-------------|-----------|
| Indexing | Recall (don't miss anything relevant) | More chunks = more storage & cost |
| Retrieval | Precision + speed | Faster search ≠ better results |
| Generation | Accuracy + groundedness | More context = better answers but higher cost & latency |

---

## 1.3 Embeddings Deep Dive [PARETO-20]

### What Problem Do Embeddings Solve?

Computers don't understand meaning. They understand numbers. Embeddings are the bridge.

An **embedding** is a way to represent the *meaning* of text as a list of numbers (a vector). Similar meanings produce similar numbers.

### The Intuition

**Analogy:** Imagine you could put every concept in the universe on a map. Similar concepts would be close together, different concepts would be far apart.

```
                    "machine learning"
                          ●
              "deep learning" ●
                                    ● "neural networks"
  
  "cooking recipes" ●
          ● "baking"
                                              ● "data science"
```

An embedding converts text into coordinates on this map. The map has many more dimensions than two (typically 384 to 3072 dimensions), but the principle is the same: **meaning becomes position**.

### How Embeddings Work (Simplified)

1. An embedding model (itself a neural network) was trained on massive text data
2. During training, it learned to put semantically similar text close together
3. You give it text, it gives you back a vector (list of floats)

```python
# Conceptual example
embed("king") →   [0.21, -0.45, 0.89, 0.12, ...]  # 384+ numbers
embed("queen") →  [0.22, -0.43, 0.87, 0.15, ...]  # Very similar!
embed("pizza") →  [-0.67, 0.31, -0.12, 0.55, ...]  # Very different!
```

### Cosine Similarity

**What problem?** You have two vectors. How do you measure if they're similar?

Cosine similarity measures the angle between two vectors:
- **1.0** = identical meaning (same direction)
- **0.0** = unrelated (perpendicular)
- **-1.0** = opposite meaning

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

You don't need to memorize the formula. The intuition: **are these two arrows pointing in the same direction?**

```python
from numpy import dot
from numpy.linalg import norm

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

# similarity("king", "queen") → ~0.85 (very similar)
# similarity("king", "pizza") → ~0.05 (unrelated)
```

### Your Workspace: Embedding Models

Your `agai-api` has multiple embedding implementations:

- **`BaseEmbedFunction`** at `agai-api/api/embeddingfunctions/baseembedfunction.py:1` — the abstract base class
- **`OpenAIEmbedModel`** at `agai-api/api/embeddingfunctions/openaiembedmodel.py` — uses OpenAI's embedding API
- **`InhouseEmbedModel`** at `agai-api/api/embeddingfunctions/inhouseembedmodel.py` — uses in-house models
- **`CLIPEmbedModel`** at `agai-api/api/embeddingfunctions/clipembedmodel.py` — multimodal (text + images)

The factory pattern at `agai-api/api/embeddingfunctions/embedfunctionfactory.py` selects the right model based on configuration.

### Why This Matters [PARETO-20]

Understanding embeddings unlocks:
- **RAG** (this chapter) — finding relevant documents
- **Semantic search** — searching by meaning, not keywords
- **Clustering** — grouping similar items
- **Classification** — categorizing text
- **Anomaly detection** — finding things that don't belong
- **Your normalizer** — matching "MIT" to "Massachusetts Institute of Technology" *by meaning*

### First Principle

> **An embedding converts meaning into geometry. Similar meanings → nearby points in space.**

---

## 1.4 Vector Databases

### What Problem Do They Solve?

You have millions of embeddings. When a user query comes in, you need to find the nearest ones *fast*. Regular databases can't do this efficiently.

A SQL database is built for exact matching: "find all rows where `name = 'MIT'`". A vector database is built for approximate matching: "find the 10 vectors closest to this query vector in 768-dimensional space."

### Why Regular Databases Can't Do This

If you have 1 million vectors with 768 dimensions each:
- **Brute force:** Compare the query to all 1M vectors. Works but O(n) — too slow at scale.
- **SQL index (B-tree):** Designed for ordered data in 1 dimension. Useless for 768 dimensions.
- **Vector DB index (HNSW, IVF, etc.):** Uses clever data structures to find *approximate* nearest neighbors in sub-linear time.

**Analogy:** Finding your friend in a city.
- Brute force: Walk to every house and check.
- B-tree: Works great for addresses (ordered, 1D). Useless for "find the house nearest to GPS coordinates."
- Vector index: Divide the city into neighborhoods. Check only the relevant neighborhoods.

### Common Vector Database Index Types

| Algorithm | How It Works | Trade-off |
|-----------|-------------|-----------|
| **HNSW** (Hierarchical Navigable Small World) | Graph-based; walks through a hierarchy of connections | Fast queries, high memory usage |
| **IVF** (Inverted File Index) | Clusters vectors, searches only relevant clusters | Good balance of speed and memory |
| **PQ** (Product Quantization) | Compresses vectors to reduce memory | Lower accuracy, much less memory |

### Your Workspace: Vector Stores

`agai-api` has a vector store abstraction:

- **`BaseVectorStore`** at `agai-api/api/vectordatabases/basevectorstore.py` — abstract interface
- **`WeaviateVectorStore`** at `agai-api/api/vectordatabases/weaviatevectorstore.py` — Weaviate implementation
- **`AI21VectorStore`** at `agai-api/api/vectordatabases/ai21vectorstore.py` — AI21 implementation
- **`VectorStoreFactory`** at `agai-api/api/vectordatabases/vectorstorefactory.py` — factory pattern for selecting the backend

The `Collection` model at `agai-api/api/models.py:211` ties a vector store configuration to an embedding configuration, ensuring that vectors stored in a collection were all embedded with the same model.

### The Trade-offs: Speed vs Accuracy vs Cost

| Factor | Optimize for speed | Optimize for accuracy | Optimize for cost |
|--------|-------------------|---------------------|------------------|
| Index type | HNSW | Flat (brute force) | IVF + PQ |
| Recall | ~95% | 100% | ~90% |
| Query latency | <10ms | Seconds | <50ms |
| Memory | High | Very high | Low |

For most applications: **HNSW gives you 95%+ recall with millisecond latency.** That's why it's the default in Weaviate, Pinecone, and most vector databases.

---

## 1.5 Chunking Strategies

### What Problem Does Chunking Solve?

LLMs have context windows (maximum input size). Your documents might be much larger. Even if they fit, stuffing an entire document into the context is wasteful — the LLM performs better with *focused, relevant* snippets.

Chunking is the art of splitting documents into pieces that are:
- **Small enough** to fit in context and reduce noise
- **Large enough** to preserve meaning and context
- **Aligned** to natural boundaries (sentences, paragraphs, sections)

### Why Chunking Matters

**Too big (e.g., entire documents):**
- Lots of irrelevant content dilutes the signal
- Uses expensive context window space
- Embedding quality degrades (one vector can't capture a whole book)

**Too small (e.g., individual sentences):**
- Loses context ("it" refers to what?)
- Retrieval returns disconnected fragments
- User gets incoherent answers

### Common Chunking Strategies

#### 1. Fixed-Size Chunking
Split every N tokens (or characters).

```python
# Simple fixed-size chunking
def fixed_chunk(text, size=512, overlap=50):
    chunks = []
    for i in range(0, len(text), size - overlap):
        chunks.append(text[i:i + size])
    return chunks
```

**Pros:** Simple, predictable chunk sizes.
**Cons:** Cuts mid-sentence, mid-paragraph, mid-thought.

#### 2. Sentence-Based Chunking
Group sentences until you hit a size limit.

```python
# Sentence-based chunking (conceptual)
def sentence_chunk(text, max_tokens=512):
    sentences = split_into_sentences(text)
    chunks, current = [], []
    for s in sentences:
        if token_count(current + [s]) > max_tokens:
            chunks.append(" ".join(current))
            current = [s]
        else:
            current.append(s)
    chunks.append(" ".join(current))
    return chunks
```

**Pros:** Respects sentence boundaries.
**Cons:** Sentences can still be out of context.

#### 3. Semantic Chunking
Use embeddings to detect *topic shifts*. Start a new chunk when the meaning changes significantly.

**Pros:** Each chunk is a coherent unit of meaning.
**Cons:** More complex, requires embedding calls during indexing.

#### 4. Structural Chunking
Use document structure (headers, sections, paragraphs) as boundaries.

**Pros:** Respects the author's intended organization.
**Cons:** Only works for well-structured documents.

### Overlap Strategies

Chunks should overlap slightly to avoid losing context at boundaries.

```
Document: [AAAAAA|BBBBB|CCCCCC|DDDDD]

Without overlap:  [AAAAAA] [BBBBBB] [CCCCCC]
With overlap:     [AAAAAA BB] [BB BBBBB CC] [CC CCCCC]
                        ^^              ^^
                     overlap          overlap
```

Typical overlap: 10–20% of chunk size.

### Your Workspace: Document Chunks

The `DocumentChunk` model at `agai-api/api/models.py:835` represents a chunk in the AGAI platform:

```python
class DocumentChunk(SQLModel, table=True):
    # Each chunk belongs to a document, has text content and an embedding
```

This is used for the document tools — when users upload documents to an agent, they get chunked and embedded for retrieval during conversation.

---

## 1.6 Advanced RAG Patterns

### Hybrid Search (Sparse + Dense) [PARETO-20]

**What problem?** Pure vector search (dense retrieval) sometimes misses exact keyword matches. Pure keyword search (sparse retrieval) misses semantic matches.

**Solution:** Combine both.

| Search Type | Finds "MIT" → "Massachusetts Institute of Technology" | Finds "college in Boston" → "MIT" |
|-------------|------------------------------------------------------|-----------------------------------|
| **Sparse** (keyword/BM25) | Yes (exact match) | No (no keyword overlap) |
| **Dense** (vector/embedding) | Maybe (depends on embedding) | Yes (semantic similarity) |
| **Hybrid** (both) | Yes | Yes |

**Your normalizer does exactly this!** The `ElasticsearchNormalizerTool` in `wos-ai-normalizer/app/tools/__init__.py:19` builds queries that combine:
- **Constant score** (exact match on `name_variation.norm`) — see line 78
- **Match query** (fuzzy/keyword on `name_variation`) — this uses Elasticsearch's built-in BM25

This is hybrid search: exact matching + text similarity, all in one Elasticsearch query.

### Reranking [PARETO-20]

**What problem?** The retrieval step returns "good enough" candidates, but the order might not be optimal. A lightweight retriever (Elasticsearch) is fast but not as smart as an LLM.

**Solution:** Use a cheap retriever to get candidates, then an expensive model to rerank them.

```
Query → Retriever (fast, gets 25 candidates) → Reranker (slow, picks top 3) → Answer
```

**Your workspace is a textbook example:**

1. `ElasticsearchNormalizerTool` retrieves up to 25 candidates (line 47: `results_size`)
2. `IncitesOrgNameReranker` at `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py:59` uses an LLM to rerank them
3. The reranker returns candidates ordered by probability with `is_top_choice` flags and optional reasons (line 30–31)
4. The structured output uses `json_schema` with the candidate list as an `enum` (line 27) — constraining the LLM to only select from actual candidates

This two-stage pattern (cheap retrieval → expensive reranking) is one of the most important patterns in production RAG systems.

### Query Expansion / Alternatives Generation

**What problem?** The user's query might not match the indexed terms. "MIT" won't match "Massachusetts Institute of Technology" in a keyword search.

**Solution:** Generate alternative forms of the query before searching.

**Your workspace:** Multiple alternatives tools:
- `OrganizationNameAlternativesTool` — generates org name variations
- `IncitesLocationAlternativesTool` at `wos-ai-normalizer/app/tools/incites/llm/incites_location_alternatives.py:16` — generates location name variations ("Germany" → ["GERMANY (FED REP GER)", "Federal Republic of Germany", "Deutschland", ...])
- `IncitesJournalAlternativesTool` — journal name variations

The pattern: ask an LLM to generate N alternative names, then search for ALL of them.

```
"MIT" → LLM generates → ["Massachusetts Institute of Technology", "M.I.T.", "Mass Inst Tech"]
     → Search for all 4 → More candidates → Better results
```

### Multi-Step Retrieval

**What problem?** Some questions require information from multiple documents.

"Compare MIT's publication output with Stanford's" requires:
1. Retrieve MIT's data
2. Retrieve Stanford's data
3. Synthesize both

**Solution:** Break the query into sub-queries, retrieve for each, then combine.

Your conductor does a version of this — the `QueryParserTool` at `wos-ri-conductor/app/tools/llm/parser/` extracts multiple entities from a query, and each entity goes through its own normalization pipeline.

### Contextual Compression

**What problem?** Retrieved chunks contain irrelevant information alongside relevant information.

**Solution:** After retrieval, use an LLM to extract only the relevant portions of each chunk.

```
Retrieved chunk (500 tokens, 30% relevant) → Compressor → Compressed chunk (150 tokens, 90% relevant)
```

This reduces noise and saves context window space.

---

# Chapter 2: Agent Architecture [PARETO-20]

## 2.1 What Is an Agent? (First Principles)

### The Core Idea

An LLM generates text. An **agent** generates text AND takes actions based on that text.

**Analogy:** A textbook vs an employee.
- A textbook contains knowledge. You ask it a question, it gives you information. It doesn't DO anything.
- An employee has knowledge AND can take actions: search a database, send an email, update a spreadsheet, ask a colleague.

An agent is an LLM with the ability to call functions (tools). Instead of just answering "you should search the database for X", an agent *actually searches the database for X*, looks at the results, and then answers.

### The ReAct Pattern

Most agents follow the **ReAct** (Reasoning + Acting) pattern:

```
1. REASON: "The user wants to know MIT's publication count. I need to search the database."
2. ACT:    Call search_database(org="MIT")
3. OBSERVE: Got result: {publications: 45,231, year: 2024}
4. REASON: "I have the data. I can now answer the user."
5. ACT:    Return answer to user
```

This loop repeats until the agent has enough information to answer, or hits a limit.

```
         ┌──────────┐
         │  REASON   │ ← What should I do next?
         └────┬─────┘
              │
              ▼
         ┌──────────┐
         │   ACT     │ ← Call a tool
         └────┬─────┘
              │
              ▼
         ┌──────────┐
         │  OBSERVE  │ ← See the result
         └────┬─────┘
              │
              ▼
         ┌──────────┐
         │ DONE?     │ ──No──→ Back to REASON
         └────┬─────┘
              │ Yes
              ▼
         ┌──────────┐
         │  ANSWER   │
         └──────────┘
```

### Your Workspace: Every App Is an Agent

In `wos-ri-conductor`, every `App` subclass is an agent:

- `OrganizationsApp` — specialized for organization queries
- `ResearchersApp` — specialized for researcher queries
- `LocationsApp` — specialized for location queries
- `NotUnderstandableApp` — the fallback agent

Each one follows a similar pattern:
1. Receive a parsed query
2. Normalize entities (tool calls to the normalizer)
3. Execute InCites queries (tool calls to the API)
4. Generate visualizations (LLM calls)
5. Stream results back

The `App` base class at `wos-ri-conductor/app/apps/__init__.py:63` defines the contract:
```python
class App(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description
```

The `description` field is crucial — it's what the `AppSelectorTool` (the router) reads to decide which agent to dispatch to.

### First Principle

> **An agent = LLM + Tools + Loop. It reasons about what to do, does it, observes the result, and repeats.**

---

## 2.2 Agent Components

### The Four Components

Every agent has four essential components:

```
┌──────────────────────────────────────┐
│              AGENT                    │
│                                      │
│  ┌─────────┐     ┌──────────────┐   │
│  │  BRAIN   │     │    TOOLS     │   │
│  │  (LLM +  │     │ (functions   │   │
│  │  prompt)  │     │  it can call)│   │
│  └─────────┘     └──────────────┘   │
│                                      │
│  ┌─────────┐     ┌──────────────┐   │
│  │ MEMORY   │     │   PLANNER    │   │
│  │ (history │     │ (how it      │   │
│  │  + state) │     │  decides)    │   │
│  └─────────┘     └──────────────┘   │
│                                      │
└──────────────────────────────────────┘
```

### 1. The Brain (LLM + System Prompt)

The LLM is the reasoning engine. The system prompt shapes its behavior.

**Your workspace:**
- `AgentConfig.system_prompt` at `agai-api/api/models.py:504` — every agent has a system prompt
- `AgentConfig.to_llm_config` — links to a specific LLM configuration
- `BaseAgent.load_config()` at `agai-api/api/agenthub/agents/baseagent.py:102` — loads the prompt and appends the current date

Notice line 122–123:
```python
self.system_prompt = agentconfig.system_prompt
self.system_prompt = self.prompt_with_handoff_instructions()
```
The system prompt is *augmented* with handoff instructions — the agent needs to know about other agents it can delegate to.

### 2. The Tools (Functions the Agent Can Call)

Tools are the agent's hands. Each tool is a function with a name, description, and parameters.

**Your workspace:**
- `ToolConfig` at `agai-api/api/models.py:372` — the database model for a tool
  - `name` — human-readable name
  - `description` — **this is a prompt to the LLM** (the LLM reads this to decide when to use the tool)
  - `tool_class` — one of `['LocalTool', 'HTTPTool', 'HandoffTool', 'AgentAsTool']`
  - `parameters` — list of `ToolParameter` objects
  - `send_result_to` — where the result goes: `["conversation", "client", "client_no_assistant"]`

- `ToolParameter` at `agai-api/api/models.py:430` — describes each parameter the LLM must extract
  - `name`, `type`, `description`, `required`

- `BaseTool` at `agai-api/api/agenthub/tools/basetool.py:6` — runtime tool base class

The tool types in your platform:
- **LocalTool** — runs Python code locally
- **HTTPTool** — calls an external API
- **HandoffTool** — transfers control to another agent
- **AgentAsTool** — uses another agent as a tool (agent-as-a-tool pattern!)

### 3. The Memory (Conversation History + State)

Memory is what the agent remembers between turns and between tool calls.

**Your workspace:**
- `Conversation` at `agai-api/api/models.py:616` — the full conversation record
- `Message` — individual messages with roles (user, assistant, tool)
- `AgentConfig.hide_above` — memory management: hide large old messages from the LLM (line 534)

### 4. The Planner (How the Agent Decides)

The planner is *implicit* in the LLM's reasoning. The system prompt, tool descriptions, and conversation history collectively guide the LLM's decision-making.

In simple agents, the planner is just the ReAct loop. In complex systems (like your conductor), explicit routing logic supplements the LLM's planning.

---

## 2.3 Tool Use (Function Calling) [PARETO-20]

### How Function Calling Works Under the Hood

This is one of the most important concepts in modern AI systems. Let's build up from first principles.

**Step 1: You describe tools to the LLM.**

When you send a request to the OpenAI API (or equivalent), you include a `tools` parameter:

```json
{
  "messages": [{"role": "user", "content": "What's the weather in London?"}],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "City name"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
          },
          "required": ["location"]
        }
      }
    }
  ]
}
```

**Step 2: The LLM decides whether to call a tool.**

The LLM doesn't *execute* anything. It generates a special response:

```json
{
  "choices": [{
    "message": {
      "role": "assistant",
      "tool_calls": [{
        "id": "call_abc123",
        "function": {
          "name": "get_weather",
          "arguments": "{\"location\": \"London\", \"unit\": \"celsius\"}"
        }
      }]
    }
  }]
}
```

The LLM is saying: "I think you should call `get_weather` with `location='London'`." It's generating *text* that happens to be structured as a function call.

**Step 3: YOUR CODE executes the tool.**

The LLM never runs code. Your application parses the tool call, executes the actual function, and sends the result back:

```json
{
  "role": "tool",
  "tool_call_id": "call_abc123",
  "content": "{\"temperature\": 15, \"condition\": \"cloudy\"}"
}
```

**Step 4: The LLM generates a final answer using the tool result.**

"The current weather in London is 15°C and cloudy."

### Critical Insight: The Tool Description Is a Prompt

The `description` field in a tool definition is literally a prompt to the LLM. The LLM reads it to decide *when* to call the tool and *how* to fill in the parameters.

Bad description → wrong tool selection → broken agent.

```python
# Bad: Vague, the LLM won't know when to use it
"description": "Does stuff with data"

# Good: Specific, the LLM knows exactly when to use it
"description": "Search the InCites database for publication metrics. Use this when the user asks about citation counts, h-index, or publication output for a researcher or institution."
```

**Your workspace:** Look at `ToolConfig.description` at `agai-api/api/models.py:376` — every one of your 37+ tools has a description that the LLM reads.

### Tool Selection, Parameter Extraction, Result Handling

The LLM does three things during a tool call:

1. **Selection:** "Which tool should I use?" (based on tool descriptions vs user intent)
2. **Parameter extraction:** "What arguments does this tool need?" (based on parameter descriptions + user message)
3. **Result interpretation:** "What does this result mean? Do I need another tool call?" (based on tool result + original question)

**Your workspace flow:**

```
User message → BaseAgent processes → LLM sees tool descriptions → 
LLM generates tool_call → BaseAgent dispatches to BaseTool subclass → 
Tool executes (HTTP call, local function, or agent handoff) → 
Result sent back to LLM → LLM generates response or another tool call
```

### The `send_result_to` Pattern

Your platform has a sophisticated pattern for where tool results go. At `agai-api/api/models.py:388`:

```python
send_result_to: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
# Valid values: ["conversation", "client", "client_no_assistant"]
```

- **`"conversation"`** — result goes back to the LLM (standard: the LLM sees the result and reasons about it)
- **`"client"`** — result goes directly to the user (bypass: for structured data the user needs immediately)
- **`"client_no_assistant"`** — result goes to user without creating an assistant message

This is a production-grade pattern you won't find in tutorials.

### Building Your Own Tool (Conceptual)

```python
# 1. Define the tool in the database (ToolConfig)
tool = ToolConfig(
    name="Search Publications",
    description="Search for academic publications by author, topic, or institution. Use when the user asks about research papers or publication metrics.",
    tool_class="HTTPTool",
    parameters=[
        ToolParameter(name="query", type="string", description="The search query", required=True),
        ToolParameter(name="limit", type="number", description="Max results to return", required=False),
    ]
)

# 2. The platform handles the rest:
#    - Converts ToolConfig to OpenAI function schema
#    - Sends to LLM with user message
#    - Parses LLM's tool_call response
#    - Dispatches to the correct tool class (HTTPTool makes an HTTP request)
#    - Sends result back to LLM or client
```

---

## 2.4 Multi-Agent Systems [PARETO-20]

### Why One Agent Isn't Enough

**The problem:** A single agent with 37 tools is overwhelmed. The LLM's context window fills up with tool descriptions. Tool selection accuracy drops. The system prompt becomes a novel.

**The solution:** Specialize. Give each agent a focused job with a small set of tools, and use a router to dispatch to the right specialist.

**Analogy:** A hospital.
- **Bad design:** One doctor handles everything — surgery, psychiatry, radiology, pharmacy
- **Good design:** A triage nurse (router) evaluates the patient and sends them to the right specialist

### Pattern 1: The Router Pattern

```
User → Router Agent → decides which specialist → Specialist Agent → answers
```

**Your workspace implements this exactly:**

The `Conductor` at `wos-ri-conductor/app/conductor/conductor.py:29` is the router:

```python
class Conductor:
    apps = [
        OrganizationsApp(),     # Handles org queries
        ResearchersApp(),       # Handles researcher queries  
        FundingAgenciesApp(),   # Handles funding queries
        ResearchAreasApp(),     # Handles research area queries
        LocationsApp(),         # Handles location queries
        PublicationSourceApp(), # Handles publication source queries
        NotUnderstandableApp()  # Fallback
    ]
    app_selector = AppSelectorTool(*apps, engine=app_selector_engine)
```

The `AppSelectorTool` at `wos-ri-conductor/app/tools/llm/app_selector.py:9` is the routing logic:
- It receives the user query
- It reads all app descriptions (line 47: `self.apps = dict([(app.name, app.description) for app in apps])`)
- It asks the LLM: "Given this query and these app descriptions, which app should handle it?"
- It returns structured output: `{app, info, userquery_segment}` (line 13–44)

### Pattern 2: The Chain Pattern

```
Agent A → passes result to → Agent B → passes result to → Agent C
```

Each agent in the chain performs one step of a pipeline. The output of one becomes the input of the next.

**Your workspace:** The InCites flow is a chain:
1. `QueryParserTool` parses the user's natural language into structured entities
2. Entity normalizers map raw entities to database keys
3. `IncitesChampTool` / `IncitesBFFTool` executes the actual data queries
4. `Visualizer` generates chart recommendations

### Pattern 3: Agent-as-a-Tool

One agent calls another agent as if it were a tool. The parent agent doesn't know (or care) that a tool is actually another agent with its own reasoning loop.

**Your workspace:** `AgentAsTool` at `agai-api/api/agenthub/tools/agentastool.py` — literally an agent wrapped as a tool. The `tool_class='AgentAsTool'` in `ToolConfig` (line 395) enables this pattern.

### Pattern 4: Handoff

An agent transfers the entire conversation to another agent, including all context and state.

**Your workspace:**
- `AgentConfig.handoffs` at `agai-api/api/models.py:521` — list of agents this agent can hand off to
- `AgentConfig.handoff_description` — description shown to the LLM about what this agent handles when receiving handoffs
- `AgentConfig.handoff_input_type` — schema validation for data passed during handoff
- `AgentConfig.handoff_input_filter` at line 533 — strategy for filtering conversation history during handoff: `'default'`, `'remove_unrelated_tools'`, or `'remove_all_tools'`
- `HandoffTool` at `agai-api/api/agenthub/tools/handofftool.py` — the tool that triggers handoff

### State Propagation

When agents hand off or chain, state must flow correctly. Your workspace handles this through:

- `ToolInternalStateParameter` at `agai-api/api/models.py:472` — maps internal state keys to tool parameters
  - `internal_state_key` — where to read the value from
  - `post_body_key` — where to put it in the outgoing request
  - `pass_as_header` / `pass_as_cookie` — alternative transport mechanisms

This is a production concern that tutorials rarely cover: how does Agent B know what Agent A already figured out?

---

## 2.5 Agent Memory

### The Three Types of Memory

```
┌──────────────────────────────────────────────────┐
│                  AGENT MEMORY                     │
│                                                   │
│  SHORT-TERM          WORKING              LONG    │
│  (conversation)     (internal state)     -TERM    │
│                                         (vector   │
│  "What was said"   "What I'm tracking"   store)   │
│  this session       between tool calls            │
│                                         "Past     │
│                                          sessions │
│                                          + docs"  │
└──────────────────────────────────────────────────┘
```

### Short-Term Memory (Conversation Context)

**What:** The conversation history — all user messages, assistant responses, and tool results.

**The problem:** LLMs have finite context windows. Long conversations overflow.

**Your workspace solutions:**

1. **Truncation** at `agai-api/api/agenthub/agents/memorymanagement/truncatemessages.py` — when the conversation exceeds the token limit, older messages are removed

2. **Memory swap** at `agai-api/api/agenthub/agents/memorymanagement/swapmemory.py` — instead of deleting old messages, *archive* them and leave a retrieval instruction:

```python
# From swapmemory.py:38-42
placeholder = (
    'This message was archived. If there is the slightest chance it might be useful...'
    'retrieve it proactively without asking the user, using the '
    + agai_retrieve_swapped_memory_tool_name + ' tool and '
    + str(messages[idx]['id']) + ' as id input argument.'
)
```

This is elegant: instead of losing information, the agent gets a note saying "this was archived, here's how to retrieve it." The agent can then selectively retrieve old information when needed.

The `archive()` function at line 25 decides what to archive based on:
- `hide_above` — messages longer than N characters are candidates
- `hide_older_messages` — only archive if the message is older than N user turns

### Working Memory (Internal State Between Tool Calls)

**What:** Data the agent accumulates during a single processing run — partial results, flags, intermediate computations.

**Your workspace:**
- `Conversation.internal_state` — a JSON dict that persists between turns
- The `BaseAgent.__init__()` at `agai-api/api/agenthub/agents/baseagent.py:84`:
  ```python
  if not isinstance(self.conversation.internal_state, dict) or "states" not in self.conversation.internal_state.keys():
      self.conversation.init_internal_state()
  ```
- `ToolInternalStateParameter` allows tools to read from and write to this state

Example flow:
1. User asks a complex question
2. Tool A runs and stores `session_id` in internal state
3. Tool B reads `session_id` from internal state to make an authenticated API call
4. Tool C reads both previous results from internal state to generate the final answer

### Long-Term Memory (Vector Store / Knowledge Base)

**What:** Information that persists across conversations — uploaded documents, learned preferences, accumulated knowledge.

**Your workspace:**
- Document uploads → chunks → embeddings → vector store (the `DocumentChunk` model at line 835)
- `ConversationDocument` — links documents to conversations
- When a user uploads a PDF, it gets chunked and embedded. In future conversations, the agent can retrieve relevant chunks.

### The Memory Hierarchy Design Pattern

```
Fastest/Cheapest → System prompt (always present, never changes)
                 → Recent conversation (last few turns)
                 → Older conversation (truncated or swapped)
                 → Retrieved from long-term store (on demand)
Slowest/Most Expensive
```

Good agents minimize what's in context while maximizing what's *accessible*.

---

# Chapter 3: Orchestration Patterns

## 3.1 The Conductor Pattern

### What Problem Does It Solve?

When you have multiple agents, multiple tools, and complex pipelines, something needs to coordinate it all. The conductor pattern puts a central orchestrator in charge.

**Analogy:** An orchestra conductor doesn't play any instrument. They decide when each section plays, how loud, how fast. Without a conductor, you get noise. With one, you get a symphony.

### Your Workspace: `wos-ri-conductor`

Your `Conductor` class at `wos-ri-conductor/app/conductor/conductor.py:29` is a textbook implementation:

```python
class Conductor:
    # 1. Initialize all available agents (apps)
    apps = [OrganizationsApp(), ResearchersApp(), ...]
    
    # 2. Set up the routing LLM
    app_selector = AppSelectorTool(*apps, engine=app_selector_engine)
    
    # 3. Set up translation
    translator_tool = TranslatorTool(translator_engine)
```

The `conduct()` method at line 51 orchestrates the full pipeline:

1. **Input validation** — check if the input is understandable (line 59: `in_understandable_input()`)
2. **Translation** — translate to English if needed (line 70)
3. **Routing** — use `AppSelectorTool` to pick the right specialist
4. **Execution** — delegate to the selected app
5. **Streaming** — results flow back as SSE events

### When to Use the Conductor Pattern

| Use When | Don't Use When |
|----------|---------------|
| Multiple specialized agents | Single simple agent |
| Complex pipelines with stages | Simple request→response |
| Need central logging/monitoring | Each agent is independent |
| Need translation, auth, validation | No cross-cutting concerns |
| Results need to be streamed progressively | Simple batch responses |

---

## 3.2 Streaming Architectures

### Why Streaming Matters

LLMs are slow. A complex query through your conductor might take 10–30 seconds. Without streaming, the user stares at a blank screen. With streaming, they see progressive results.

### SSE (Server-Sent Events)

**What:** A simple HTTP protocol where the server pushes events to the client over a long-lived connection.

**Your workspace:** `Streaming` class at `wos-ri-conductor/app/util/sse.py:11`:

```python
class Streaming(object):
    def __init__(self, request, start_time, app_name, request_id):
        self.id = 0  # Event counter
        
    async def message(self, data, encoder=None):
        if await self.request.is_disconnected():
            raise DisconnectedStreamingException()
        self.id += 1
        return json.dumps({
            'event': self.app_name,
            'id': self.id,
            'retry': 15000,
            'data': { ... }
        })
```

Key details:
- Each message has an incrementing `id` (line 23)
- Disconnection is checked before each send (line 20)
- The `retry` field tells the client to reconnect after 15 seconds if disconnected (line 27)
- Each app yields multiple streaming messages as results become available

### The Full Streaming Path

```
User → Angular UI → BFF (WebSocket) → Conductor (SSE) → Agent → Tools → Results
                                                                          │
Results stream back: ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←┘
```

Your architecture bridges two streaming protocols:
1. **SSE** between conductor and BFF (simple, HTTP-based)
2. **WebSocket** between BFF and Angular UI (bidirectional, real-time)

---

## 3.3 Error Handling in Agent Systems

### Why Agent Error Handling Is Different

Traditional error handling: catch exception → return error message. Done.

Agent error handling is harder because:
- The LLM might generate invalid tool calls
- External APIs might fail
- The agent might enter infinite loops
- The user might ask something impossible
- One step in a multi-step pipeline might fail

### Graceful Degradation

**Your workspace:** `NotUnderstandableApp` at `wos-ri-conductor/app/apps/not_understandable_app.py:8`:

```python
class NotUnderstandableApp(App):
    def __init__(self):
        super().__init__('Not Understandable Input',
                         '''This app should be used when
    1 - The user input does not make any sense at all.
    2 - The answer to the user question cannot be obtained through an analytics query.
    ...''')
```

This is graceful degradation: instead of crashing, the system has a dedicated handler for "I can't help with this." The `Conductor` routes to this app when:
- The input fails the understandable-input check (line 59 in conductor.py)
- The `AppSelectorTool` selects it because no other app matches

### Retry Strategies

**Your workspace:** `platform-agent-testing/automated_testing_v2/core/retry_manager.py` — a dedicated retry manager for handling transient failures.

Common patterns:
- **Exponential backoff** — wait longer between each retry
- **Circuit breaker** — stop retrying after N failures
- **Fallback** — try an alternative approach if retries fail

### Error Streaming

Your `Streaming.exception_message()` at `wos-ri-conductor/app/util/sse.py:40` streams errors the same way it streams results:

```python
async def exception_message(self, e, encoder=None):
    return json.dumps({
        'event': 'error',
        'data': {
            'status': {'code': f'ERROR:{type(e).__name__}'},
            'errormessage': str(e)
        }
    })
```

This ensures the client always gets notified, even when things go wrong.

---

# Chapter 4: Model Context Protocol (MCP)

## 4.1 What MCP Is and Why It Matters

### The Problem

Every AI tool integration is custom. Connecting an agent to a calendar requires one integration. Connecting to email requires another. To a database, another. Each with its own API, auth, data format.

If you have 10 agents and 20 tools, you potentially need 200 custom integrations.

### The Solution: MCP

**Analogy:** USB-C for AI tools.

Before USB-C, every device had a different charger. USB-C created one standard plug that works for everything. MCP does the same for AI tool integrations.

**MCP (Model Context Protocol)** is an open standard (created by Anthropic) that defines how AI models interact with external tools and data sources through a universal interface.

```
Before MCP:                          After MCP:
Agent A ──custom──→ Tool 1          Agent A ──┐
Agent A ──custom──→ Tool 2                     │
Agent B ──custom──→ Tool 1          Agent B ──┤── MCP ──→ Any MCP Server
Agent B ──custom──→ Tool 2                     │
Agent C ──custom──→ Tool 1          Agent C ──┘
...                                  (one standard interface)
```

### Your Workspace: MCP Implementation

Your `agai-api` has a full MCP infrastructure:

- **MCP Servers:** `AlmaMcpServer` at `agai-api/api/routers/mcp/alma/server.py:16`, `PrimoMcpServer` at `agai-api/api/routers/mcp/primo/server.py:16`
- **MCP Server Manager:** `MCPServersManager` at `agai-api/api/routers/mcp/servers/manager.py:73` — manages server lifecycle
- **MCP Config:** `MCPServerConfig` at `agai-api/api/routers/mcp/servers/base.py:70` — configuration model
- **MCP List Cache:** `MCPListCache` at `agai-api/api/models.py:483` — caches available MCP tools per agent
- **MCP OAuth:** `MCPOAuthManager` at `agai-api/api/routers/mcp/oauth/oauth_manager.py:41` — handles authentication
- **MCP Admin:** `agai-api/api/routers/mcp_admin.py` — administration endpoints
- **MCP Service Settings:** `MCPServiceSettings` at `agai-api/api/models.py:850` — per-service configuration
- **MCP Institution Settings:** `MCPInstitutionSettings` at `agai-api/api/models.py:884` — per-institution overrides

---

## 4.2 MCP Architecture

### Core Concepts

| MCP Concept | What It Is | Your Workspace Example |
|-------------|-----------|----------------------|
| **Server** | Exposes tools/resources via MCP protocol | `AlmaMcpServer`, `PrimoMcpServer` |
| **Client** | Connects to MCP servers and uses their tools | `BaseAgent` with `mcp_servers` list |
| **Tool** | A function the server exposes | Primo search, Alma catalog lookup |
| **Resource** | Data the server exposes (read-only) | Database records, file contents |
| **Prompt** | Pre-built prompt templates the server provides | Search instructions |

### Transport

MCP supports multiple transport mechanisms:

- **stdio** — standard input/output (local tools, subprocess communication)
- **HTTP/SSE** — server-sent events over HTTP (remote tools)

### How Your Agents Use MCP

At `agai-api/api/agenthub/agents/baseagent.py:137`:
```python
self.mcp_servers = agentconfig.mcp_servers if agentconfig.mcp_servers else []
```

And at line 144:
```python
self.use_responses_api = bool(self.mcp_servers or self.web_search_enabled or ...)
```

When an agent has MCP servers configured, the platform:
1. Fetches available tools from each MCP server (cached in `MCPListCache`)
2. Includes those tools alongside regular tools in the LLM request
3. Uses the OpenAI Responses API (required for MCP) instead of the Chat Completions API
4. Routes tool calls to the appropriate MCP server

### The Middleware Pattern

`MCPComponentsFilteringMiddleware` at `agai-api/api/routers/mcp/servers/middleware.py:42` — filters which MCP components are available to which agents. This is a production concern: not every agent should see every MCP tool.

---

# Chapter 5: Prompt Engineering (Systematic Approach)

## 5.1 Prompt Design Patterns

### Why Systematic Prompt Engineering?

Prompts are the "source code" of AI systems. A well-designed prompt is the difference between an agent that works reliably and one that fails unpredictably.

Unlike traditional code, prompts are:
- **Probabilistic** — the same prompt can produce different outputs
- **Fragile** — small wording changes can dramatically change behavior
- **Opaque** — hard to debug why a prompt produces a particular output

But like traditional code, prompts can be **designed systematically**.

### Pattern 1: Role Prompting

Tell the LLM *who it is* and *what its job is*.

**Your workspace example** — `AppSelectorTool.prompt()` at `wos-ri-conductor/app/tools/llm/app_selector.py:66`:

```python
def prompt(self):
    return """
You are an AI bot implemented to provide help to the users of the InCites tool.
A research analytics tool from Clarivate that allows users to evaluate the impact
and performance of institutions, researchers, and journals using citation data...
"""
```

This establishes:
1. **Identity:** "You are an AI bot"
2. **Domain:** "InCites tool... research analytics... Clarivate"
3. **Capability:** "evaluate the impact and performance..."

### Pattern 2: Few-Shot Learning

Provide examples of the desired input→output mapping.

```
Example 1:
User: "Show me MIT's publications"
Output: {"app": "Organizations", "info": "..."}

Example 2:
User: "What are the trending topics in biology?"
Output: {"app": "Research Areas", "info": "..."}

Now handle this:
User: "{actual_query}"
```

The LLM learns the *pattern* from examples and applies it to new inputs.

### Pattern 3: Chain-of-Thought

Ask the LLM to show its reasoning before giving the final answer.

```
Think step by step:
1. What entity type is the user asking about?
2. What specific entity are they referring to?
3. What metric or data point do they want?

Then provide your structured output.
```

This dramatically improves accuracy on complex tasks because it forces the LLM to *reason* rather than pattern-match.

### Pattern 4: Output Formatting (Structured Outputs)

Constrain the LLM to produce output in a specific format.

**Your workspace uses this extensively:**

- `AppSelectorTool.response_format()` at `wos-ri-conductor/app/tools/llm/app_selector.py:12` — JSON Schema with `"strict": True`
- `orgname_reranker_response_format()` at `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py:10` — uses `enum` to constrain choices to actual candidates

The `"strict": True` flag enables Structured Outputs mode — the LLM is *guaranteed* to produce valid JSON matching the schema. No parsing errors. No hallucinated fields.

---

## 5.2 System Prompt Architecture

### The Five-Part Structure

A well-designed system prompt has five parts:

```
1. ROLE         → Who is the LLM?
2. CONTEXT      → What domain/situation?
3. TASK         → What should it do?
4. CONSTRAINTS  → What should it NOT do?
5. OUTPUT FORMAT → What shape should the response take?
```

### Case Study: AppSelectorTool

Let's analyze the `AppSelectorTool` prompt at `wos-ri-conductor/app/tools/llm/app_selector.py:66`:

```
ROLE:    "You are an AI bot implemented to provide help to the users of the InCites tool"
CONTEXT: "A research analytics tool from Clarivate that allows users to evaluate..."
TASK:    "Select an appropriate app from the dictionary below"
         "Justify your selection by providing a brief explanation"
CONSTRAINTS: "For each query, you should only use one app"
OUTPUT:  Enforced via json_schema response_format (strict: true)
```

### Case Study: Reranker Prompt

The `IncitesOrgNameReranker` at `wos-ai-normalizer/app/tools/common/llm/incites_orgname_reranker.py:59` demonstrates:

```
ROLE:    Entity matching expert
CONTEXT: User query + list of candidate organizations
TASK:    Rank candidates by probability of being the user's intent
CONSTRAINTS: Only select from provided candidates (enforced by enum in schema)
OUTPUT:  JSON array with entity, is_top_choice, and optional reason
```

The `enum` constraint at line 27 is particularly elegant:
```python
"entity": {
    "enum": candidates,  # LLM can ONLY output one of these exact strings
    "description": "The name of the organization."
}
```

This makes hallucination *impossible* for the entity selection — the LLM literally cannot output a string that isn't in the candidate list.

### Prompt Versioning and Testing

Prompts are code. They should be:
- **Version controlled** — track changes, review diffs
- **Tested** — run the same queries against old and new prompts
- **Measured** — quantify accuracy, latency, cost

Your `platform-agent-testing` project exists precisely for this purpose — systematically testing prompt changes against regression suites.

### Best Practices Summary

| Practice | Why | Example |
|----------|-----|---------|
| Be specific about the role | Reduces off-topic responses | "You are a bibliometric analyst" not "You are helpful" |
| Provide context about the domain | The LLM needs to know the rules | "InCites uses Web of Science data..." |
| Use delimiters for variable input | Prevents prompt injection | ` ```{query}``` ` |
| Constrain outputs structurally | Eliminates parsing errors | `json_schema` with `strict: true` |
| Include negative examples | "Do NOT" is as important as "DO" | "Do not include historical territories" |
| Order instructions by priority | LLMs attend more to beginning/end | Critical rules first and last |

---

# Summary: The 20% That Matters Most

If you're short on time, focus on these [PARETO-20] concepts:

1. **RAG = Retrieve relevant documents, then let the LLM reason over them** (Ch 1.1)
2. **Embeddings = Meaning as geometry** (Ch 1.3)
3. **Hybrid search + Reranking = Production RAG** (Ch 1.6)
4. **Agent = LLM + Tools + Loop** (Ch 2.1)
5. **Tool descriptions are prompts** — the quality of your tool descriptions determines agent reliability (Ch 2.3)
6. **Multi-agent routing** — specialize agents, route with an LLM (Ch 2.4)
7. **Structured outputs with strict JSON Schema** — eliminates an entire class of failures (Ch 5.1)

Everything else in this textbook builds on or refines these seven core ideas.
