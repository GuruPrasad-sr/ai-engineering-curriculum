# Stage 2: Exercises — Week 3

> 10 hands-on exercises, ordered by difficulty.
> Each exercise maps to specific concepts from `concepts.md` and workspace patterns from `live_examples.md`.

---

## Exercise 1: Build a Simple RAG Pipeline

**Concepts:** Ch 1.1–1.2 | **Time:** 90 min | **Difficulty:** ★★☆☆☆

### Goal
Build a minimal RAG pipeline that indexes markdown files and answers questions about them.

### Steps

1. **Index:** Read 5–10 markdown files from your workspace (e.g., from `curriculum/`). Split each into chunks of ~500 characters with 50-character overlap.

2. **Embed:** Use OpenAI's embedding API to convert each chunk into a vector. Store in a simple Python dict.

```python
# starter code
import openai

def embed(text: str) -> list[float]:
    response = openai.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding

index = {}  # {chunk_id: {"text": str, "embedding": list[float]}}
```

3. **Retrieve:** Given a user question, embed it and find the top-3 most similar chunks (cosine similarity).

4. **Generate:** Send the top-3 chunks + question to GPT-4 and generate an answer.

5. **Test:** Ask 5 questions and evaluate whether the answers are grounded in the retrieved chunks.

### Reflection
- Compare your pipeline to `wos-ai-normalizer/app/tools/__init__.py:19` (ElasticsearchNormalizerTool). What stages are the same? What's different?
- What happens when you ask a question that ISN'T in your indexed docs?

---

## Exercise 2: Custom Embedding Search Over Your Notes

**Concepts:** Ch 1.3–1.4 | **Time:** 90 min | **Difficulty:** ★★☆☆☆

### Goal
Build a semantic search engine over your Obsidian notes or workspace markdown files using embeddings.

### Steps

1. Collect all `.md` files from a directory (use `glob`).

2. For each file, create embeddings at the paragraph level.

3. Build a search function:
```python
def search(query: str, top_k: int = 5) -> list[dict]:
    """Returns top-k most relevant paragraphs with file path and similarity score."""
    pass
```

4. Compare results for:
   - Exact keyword query: `"ElasticsearchNormalizerTool"`
   - Semantic query: `"how does the system find matching organizations?"`
   - Both should return relevant results if your embeddings are working.

5. **Bonus:** Store embeddings in a JSON file so you don't re-embed every time.

### Deliverable
A Python script that takes a search query as input and prints the top-5 most relevant paragraphs with their source files and similarity scores.

---

## Exercise 3: Build a Single Agent with 3 Tools

**Concepts:** Ch 2.1–2.3 | **Time:** 2 hours | **Difficulty:** ★★★☆☆

### Goal
Build an agent using the OpenAI function calling API with 3 custom tools.

### Steps

1. Define 3 tools:
   - `search_files(query: str)` — searches your workspace files by name
   - `read_file(path: str)` — reads a file and returns its content
   - `count_lines(path: str)` — counts lines in a file

2. Implement the ReAct loop:
```python
import openai

tools = [
    {"type": "function", "function": {
        "name": "search_files",
        "description": "Search workspace files by name pattern. Use when the user asks to find files.",
        "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
    }},
    # ... define read_file and count_lines similarly
]

messages = [{"role": "system", "content": "You are a workspace assistant. Use tools to answer questions about files."}]

def run_agent(user_message: str):
    messages.append({"role": "user", "content": user_message})
    while True:
        response = openai.chat.completions.create(model="gpt-4", messages=messages, tools=tools)
        choice = response.choices[0]
        if choice.finish_reason == "tool_calls":
            # Execute each tool call, append results, continue loop
            pass
        else:
            # Final answer
            return choice.message.content
```

3. Test with queries:
   - "How many Python files are in the conductor project?"
   - "Find the file that defines the Streaming class and show me its first 20 lines"
   - "Compare the number of lines in conductor.py vs normalizer.py"

### Reflection
- Compare your tool descriptions to `ToolConfig.description` at `agai-api/api/models.py:376`. How does quality of description affect tool selection?
- Try making one tool description intentionally vague. What happens?

---

## Exercise 4: Design a Multi-Agent System

**Concepts:** Ch 2.4 | **Time:** 2 hours | **Difficulty:** ★★★☆☆

### Goal
Design and implement a mini multi-agent system with a router and 2 specialist agents, modeled on your WOSRI architecture.

### Steps

1. **Define 2 specialist agents:**
   - `CodeAnalystAgent` — answers questions about code structure, classes, functions
   - `DocAnalystAgent` — answers questions about documentation, README files, markdown

2. **Define a router agent** that reads the user's question and dispatches to the right specialist. Model it on `AppSelectorTool` at `wos-ri-conductor/app/tools/llm/app_selector.py:66`.

3. **Implement routing with structured output:**
```python
router_response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "routing",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "agent": {"type": "string", "enum": ["code_analyst", "doc_analyst"]},
                "reason": {"type": "string"}
            },
            "required": ["agent", "reason"],
            "additionalProperties": False
        }
    }
}
```

4. **Test with 10 queries** — 5 that should go to each agent, verify correct routing.

5. **Add a fallback** — model it on `NotUnderstandableApp`. What happens when the query doesn't match either agent?

### Deliverable
A working multi-agent system where: user query → router → specialist → answer.

---

## Exercise 5: Implement the Conductor Pattern

**Concepts:** Ch 3.1 | **Time:** 90 min | **Difficulty:** ★★★☆☆

### Goal
Build a simplified version of `wos-ri-conductor`'s Conductor class for a simple workflow.

### Steps

1. Define a `Conductor` class with:
   - A list of "apps" (simple classes with `name`, `description`, and `run()`)
   - An `AppSelector` that uses an LLM to route
   - A `conduct()` method that: validates input → routes → executes

2. Create 3 simple apps:
   - `CalculatorApp` — does math
   - `TranslatorApp` — translates text
   - `SummarizerApp` — summarizes text

3. Implement `conduct()` following the pattern in `wos-ri-conductor/app/conductor/conductor.py:51`:
   - Input validation (reject empty or gibberish input)
   - App selection (LLM-based routing)
   - Execution (delegate to selected app)

4. Test with 6 queries (2 per app).

---

## Exercise 6: Add SSE Streaming to a FastAPI Endpoint

**Concepts:** Ch 3.2 | **Time:** 60 min | **Difficulty:** ★★☆☆☆

### Goal
Build a FastAPI endpoint that streams results using Server-Sent Events.

### Steps

1. Create a FastAPI app with an SSE endpoint:

```python
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import asyncio, json

app = FastAPI()

async def event_generator(request: Request):
    for i in range(10):
        if await request.is_disconnected():
            break
        data = json.dumps({"event": "progress", "id": i, "data": f"Step {i} complete"})
        yield f"data: {data}\n\n"
        await asyncio.sleep(0.5)

@app.get("/stream")
async def stream(request: Request):
    return StreamingResponse(event_generator(request), media_type="text/event-stream")
```

2. Add a `/stream-llm` endpoint that streams an LLM response token-by-token.

3. Add disconnect detection — model it on `wos-ri-conductor/app/util/sse.py:20`.

4. Add error streaming — model it on `wos-ri-conductor/app/util/sse.py:40`.

5. Test with `curl` or a simple JavaScript client.

### Deliverable
A FastAPI app with working SSE streaming, disconnect handling, and error streaming.

---

## Exercise 7: Build and Test an MCP Server

**Concepts:** Ch 4 | **Time:** 90 min | **Difficulty:** ★★★☆☆

### Goal
Build a simple MCP server that exposes one tool, and connect it to an LLM client.

### Steps

1. Install the MCP SDK:
```bash
pip install mcp
```

2. Create a simple MCP server with one tool:
```python
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("my-workspace-server")

@server.list_tools()
async def list_tools():
    return [Tool(
        name="count_files",
        description="Count the number of files matching a pattern in the workspace",
        inputSchema={"type": "object", "properties": {"pattern": {"type": "string"}}, "required": ["pattern"]}
    )]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "count_files":
        import glob
        files = glob.glob(arguments["pattern"], recursive=True)
        return [TextContent(type="text", text=f"Found {len(files)} files")]
```

3. Test the server standalone.

4. **Reflection:** Compare your server to `AlmaMcpServer` at `agai-api/api/routers/mcp/alma/server.py:16`. What production concerns does the AGAI implementation handle that yours doesn't? (Hint: look at middleware, caching, OAuth, error handling.)

---

## Exercise 8: Write and Evaluate a System Prompt

**Concepts:** Ch 5 | **Time:** 90 min | **Difficulty:** ★★★☆☆

### Goal
Write a system prompt for a new domain agent, then systematically evaluate it.

### Steps

1. Pick a domain you know well (e.g., "test automation advisor", "code review assistant").

2. Write a system prompt following the 5-part structure from Ch 5.2:
   - Role → Context → Task → Constraints → Output Format

3. Create 10 test queries spanning:
   - 3 straightforward queries (should work perfectly)
   - 3 edge cases (ambiguous, partial information)
   - 2 out-of-scope queries (should be rejected gracefully)
   - 2 adversarial queries (prompt injection attempts)

4. Run all 10 queries against your prompt. For each, record:
   - Did it follow the role? (Y/N)
   - Did it respect constraints? (Y/N)
   - Was the output format correct? (Y/N)
   - Quality score (1–5)

5. Iterate: improve the prompt based on failures and re-test.

### Deliverable
- The final system prompt
- A test matrix (10 queries × 4 criteria)
- A brief report: what failed, what you changed, and why

---

## Exercise 9: Implement Memory Swap

**Concepts:** Ch 2.5 | **Time:** 2 hours | **Difficulty:** ★★★★☆

### Goal
Implement the memory swap pattern from `agai-api/api/agenthub/agents/memorymanagement/swapmemory.py`.

### Steps

1. Build an agent that accumulates conversation history.

2. After 5 user turns, implement the archive logic:
   - Identify messages longer than a threshold
   - Replace their content with: `"This message was archived. Retrieve it with retrieve_memory(id={msg_id})"`
   - Store the original content in a separate dict (simulating a database)

3. Implement a `retrieve_memory` tool that the agent can call to retrieve archived messages.

4. Test the full flow:
   - Have a conversation with 10+ turns including some long tool results
   - Verify that old messages get archived
   - Verify that the agent can retrieve archived content when needed
   - Verify that the agent doesn't mention the archival mechanism to the user (see `swapmemory.py:42`)

### Reflection
- Compare your implementation to `swapmemory.py:25–52`. What edge cases does the production code handle?
- Why does the production code check `hide_above` (character count) rather than archiving all old messages?

---

## Exercise 10: Build a Tool-Use Accuracy Evaluator

**Concepts:** Ch 2.3 + Stage 1 (AI Validation) | **Time:** 2 hours | **Difficulty:** ★★★★☆

### Goal
Build an evaluator that measures how accurately an agent selects and uses tools.

### Steps

1. Define a test suite of 20 queries with expected tool calls:
```python
test_cases = [
    {
        "query": "What's the weather in London?",
        "expected_tool": "get_weather",
        "expected_params": {"location": "London"},
    },
    {
        "query": "Convert 100 USD to EUR",
        "expected_tool": "convert_currency",
        "expected_params": {"amount": 100, "from": "USD", "to": "EUR"},
    },
    # ... 18 more
]
```

2. Run each query through your agent (from Exercise 3 or 4) and capture:
   - Which tool was selected
   - What parameters were extracted
   - Whether the tool was called at all (vs. direct answer)

3. Calculate metrics:
   - **Tool selection accuracy:** % of queries where the correct tool was selected
   - **Parameter extraction accuracy:** % of parameters correctly extracted
   - **False tool calls:** % of queries where a tool was called unnecessarily
   - **Missed tool calls:** % of queries where a tool should have been called but wasn't

4. Create a report:
```
Tool Selection Accuracy: 85% (17/20)
Parameter Extraction: 90% (36/40 params correct)
False Tool Calls: 5% (1/20)
Missed Tool Calls: 10% (2/20)

Failures:
- Query 7: Selected "search_files" instead of "read_file" — description ambiguity
- Query 14: Missed "count" param — vague phrasing in query
```

5. **Iterate:** Improve tool descriptions based on failures and re-evaluate.

### Deliverable
- The evaluator script
- A test suite of 20+ queries
- Before/after results showing improvement from description tuning

### Connection to Your Work
This is exactly what `platform-agent-testing` does at scale. Your evaluator is a simplified version of the regression testing framework at `platform-agent-testing/automated_testing_v2/`.
