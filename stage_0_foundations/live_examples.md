# Stage 0: Live Examples — Concepts in Your Codebase

> Every concept from `concepts.md` mapped to real code you work with daily. Open these files side-by-side with the concepts chapter.

---

## Temperature = 0: Deterministic Inference

**Concept:** Temperature controls randomness. temp=0 = always pick the most likely token.

**Where to look:** `wos-ri-conductor/app/config.py`

**What you'll find:** The conductor sets `temperature=0` (or near-zero) for all LLM calls.

**Why it's there:** The conductor makes tool selection decisions, generates structured JSON, and routes user queries. If it used temp=0.8, the same question might select different tools on different runs. Your tests would be flaky — not because of a bug, but because of randomness. Setting temp=0 eliminates this source of non-determinism.

**What to notice:**
- Every tool call uses low/zero temperature
- Creative or user-facing text might use slightly higher temperature
- This is a deliberate engineering decision, not a default

**First principle connection:** When you need reliability, clamp down randomness. When you need creativity, open it up. The conductor needs reliability.

---

## Structured Outputs: JSON Schema Response Format

**Concept:** Structured outputs force the LLM to produce valid JSON matching a schema.

**Where to look:** `AppSelectorTool`'s configuration — find the `response_format` parameter with a JSON Schema definition.

**What you'll find:** A `response_format` parameter that specifies:
- The exact fields the LLM must return (e.g., `app_name`, `confidence`, `reasoning`)
- The types of each field (string, number, enum)
- Which fields are required

**Why it's there:** Without this, the LLM might return: `"I think you should use App1 because it handles order queries."` — valid text, but impossible to parse reliably. With the schema, it MUST return: `{"app_name": "App1", "confidence": 0.95, "reasoning": "Order-related query"}` — valid JSON that downstream code can consume.

**What to notice:**
- The schema acts as a contract between the LLM and the rest of the system
- Validation errors happen when the LLM can't fit its answer into the schema
- This is why your tests can assert on structure — the schema guarantees it

**Try this:** Look at 2-3 different tool configurations. Notice how each has a different JSON schema tailored to its specific output needs.

---

## Token Counting: Rate Limiter Estimates

**Concept:** Everything in LLM-land is measured in tokens. You pay per token, and there are limits per minute/day.

**Where to look:** `rate_limiter.py` — find the `request_tokens_estimate()` function.

**What you'll find:** A function that estimates how many tokens a request will consume BEFORE sending it to the API. It likely uses a rough formula (e.g., character count / 4) or a tokenizer library.

**Why it's there:** Without token estimation, you'd have no way to:
- Predict costs before making a call
- Stay within rate limits (tokens per minute)
- Budget for large test runs
- Decide whether a conversation has grown too large

**What to notice:**
- Input tokens and output tokens are counted separately
- The estimate is approximate — exact counting requires the model's actual tokenizer
- Rate limiting is about both cost control AND API stability

**Try this:** Take a prompt from one of your tools, count its characters, divide by 4 — that's a rough token estimate. Then compare with what `request_tokens_estimate()` returns.

---

## Embeddings: SentenceTransformerEmbeddingModel

**Concept:** Embeddings convert text into number-vectors where similar meanings are nearby.

**Where to look:** `SentenceTransformerEmbeddingModel` in the AGAI API codebase.

**What you'll find:** A model that takes text strings and outputs fixed-length vectors of floating-point numbers. These vectors are used for similarity comparisons — finding relevant context, matching queries to documents, or comparing expected vs actual outputs.

**Why it's there:** The platform needs to do things like:
- Find the most relevant documents for a user query (semantic search)
- Compare whether two responses mean the same thing (semantic similarity)
- Cluster similar user questions together

None of these work with exact string matching. "How do I cancel my order?" and "I want to return my purchase" mean similar things but share almost no words. Embeddings capture this semantic similarity.

**What to notice:**
- The embedding model is separate from the LLM — it's specialized for turning text into vectors
- Vector dimensions (e.g., 384, 768, 1536) represent how detailed the meaning representation is
- Cosine similarity between vectors gives a 0-to-1 similarity score

**Connection to your work:** When your normalizer compares expected and actual outputs, embeddings let it determine "these are saying the same thing differently" vs "these are completely different answers."

---

## Tool Use: The 37 AGAI Platform Tools

**Concept:** Function calling lets LLMs decide which function to invoke and with what arguments. Your code executes the actual function.

**Where to look:** The tool registry in the conductor. Each tool has:
1. A name and description (what the LLM sees)
2. A parameter schema (what arguments the LLM must provide)
3. An implementation (what your code actually does)

**What you'll find:** ~37 tools registered with the LLM. Each tool definition includes:
- `name`: "AppSelectorTool", "SearchTool", etc.
- `description`: Plain-English description of what the tool does
- `parameters`: JSON Schema for the expected input
- Implementation code that runs when the tool is selected

**Why it's there:** The LLM can think and reason, but it can't search databases, look up orders, or check system status. The tools give it "hands" — it decides what to do, and your code does it.

**What to notice:**
- The LLM only sees the name, description, and parameter schema — it never sees the implementation code
- Tool descriptions are critical — a bad description means the LLM won't select the tool correctly
- This is a key testing surface: does the LLM select the RIGHT tool with the RIGHT arguments?

**Try this:** Read 3 different tool definitions. For each, write down:
1. What the LLM sees (name + description + parameters)
2. What your code does (implementation)
3. How you would test "did the LLM use this tool correctly?"

---

## Streaming: SSE Pipeline from Conductor → BFF → UI

**Concept:** Streaming sends tokens to the user as they're generated, using Server-Sent Events (SSE).

**Where to look:** The SSE implementation in the conductor and BFF layers.

**What you'll find:** A pipeline:
```
LLM API (streaming) → Conductor (processes stream) → BFF (relays) → UI (renders)
```

Each layer receives token chunks via SSE and forwards them to the next layer.

**Why it's there:** Without streaming, the user waits 5-30 seconds for a complete response. With streaming, they see tokens appearing in real-time (like watching someone type). The perceived latency drops from seconds to milliseconds.

**What to notice:**
- The stream carries not just text tokens but also tool call events
- Error handling mid-stream is tricky — you might get 50% of a response and then an error
- Testing streaming requires consuming the stream and validating both individual chunks AND the assembled result

**Testing implication:** Your tests might need to handle both streaming and non-streaming response modes. A test that awaits the full response misses streaming-specific bugs (chunk ordering, incomplete tool calls, mid-stream errors).

---

## Non-Determinism: Structural Assertions in UI Tests

**Concept:** Because LLM outputs vary, tests assert structure and behavior rather than exact content.

**Where to look:** `Ui_Test_Gen_Skill.md` — the guidelines for generating UI tests.

**What you'll find:** Instructions that explicitly say to assert on structure, not content. For example:
- ✅ Assert the response contains a JSON object with specific keys
- ✅ Assert the selected tool matches the expected tool
- ✅ Assert the response length is within a reasonable range
- ❌ Do NOT assert the exact text of the response
- ❌ Do NOT assert specific wording in explanations

**Why it's there:** If you asserted `assert response.text == "The order status is: shipped"`, your test would fail every time the LLM phrases it differently: "Your order has been shipped", "Status: Shipped", "The order is currently in transit." All correct, all different. Structural assertions survive this variation.

**What to notice:**
- This is a paradigm shift from traditional testing where exact match is the default
- The trick is finding the boundary between "this must be exact" (tool name, schema fields) and "this can vary" (explanatory text, reasoning)
- Your gold questions define that boundary

---

## Context Window: HistoryProcessorTool

**Concept:** The context window is fixed-size. Multi-turn conversations accumulate tokens and eventually overflow it.

**Where to look:** `HistoryProcessorTool` in the conductor.

**What you'll find:** Logic that takes a multi-turn conversation history and compresses it to fit within the context window. This might include:
- Summarizing older messages
- Dropping messages beyond a certain age
- Keeping only the most recent N turns
- Preserving the system prompt and most recent user message at full fidelity

**Why it's there:** Consider a 20-turn conversation. Each turn has a user message (~100 tokens) and an assistant response (~500 tokens). That's 12,000 tokens of history alone, plus the system prompt (~500 tokens), plus the current user message, plus room for the response. Without compression, you'd hit the context window limit quickly.

**What to notice:**
- Compression is lossy — the model "forgets" details from older messages
- The compression strategy matters: dropping old messages is simple but loses context; summarizing preserves meaning but introduces errors
- This is a testable component: does the compression preserve the information the model needs?

**Try this:** Count the approximate tokens in a typical system prompt from one of your tools. Then calculate: how many conversation turns can fit in the remaining context window? This gives you a concrete feel for the constraint.

---

## Summary: Concept-to-Code Map

| Concept | Where in your workspace | Why it exists |
|---|---|---|
| Temperature=0 | `config.py` | Deterministic tool selection |
| Structured outputs | AppSelectorTool's response_format | Parseable, reliable JSON |
| Token counting | `rate_limiter.py` → `request_tokens_estimate()` | Cost control & rate limiting |
| Embeddings | `SentenceTransformerEmbeddingModel` | Semantic search & similarity |
| Tool use / Function calling | 37 AGAI tools in conductor | LLM ↔ real-world interaction |
| Streaming (SSE) | Conductor → BFF → UI pipeline | Real-time token delivery |
| Non-determinism | `Ui_Test_Gen_Skill.md` assertion patterns | Structure-based testing |
| Context window | `HistoryProcessorTool` | Conversation memory management |

Each of these is a concept you read about in `concepts.md` turned into a real engineering decision in your workspace. The theory isn't abstract — it's running in production.
