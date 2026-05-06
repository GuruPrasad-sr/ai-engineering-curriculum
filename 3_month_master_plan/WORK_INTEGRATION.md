---
tags: [integration, work, daily-plan, wosri, learning]
created: 2026-05-05
status: active
---

# Work–Learning Integration: Day-by-Day Plan

> **The core insight:** You work on a production multi-agent AI system every day.
> Every concept in the 3 Udemy courses exists, live and observable, in the WOSRI codebase.
> This is an extraordinary advantage that most learners don't have.
> The plan below turns every study session into something that makes your work better,
> and every work task into something that deepens what you just studied.
> Learning and work do not go in separate directions. They are the same direction.

---

## The WOSRI Concept Map

Before anything else, understand that every abstract concept you will study has a physical home in your workspace.

| Concept You'll Study | Where It Lives in WOSRI | File / Component |
|---------------------|------------------------|-----------------|
| Tokens & context windows | How queries to the conductor are sized and passed to the LLM | `wos-ri-conductor/app/conductor/conductor.py` |
| Temperature & inference params | LLM call configuration per agent | `agai-api/api/` + conductor config |
| Embeddings | How research papers are indexed and semantically searched | `agai-api/` (vector DB endpoints) |
| RAG pipeline | The full RI Assistant query → retrieval → augmentation → generation flow | Conductor → IncitesTool → VisualizerTool |
| Agent architecture | The 4 WOSRI agents (Impact, Collaboration, Funding, Emerging Topics) | `wos-ri-conductor/app/conductor/` |
| Tool calling | AppSelectorTool, NormalizerTool, IncitesTool, HighlightsTool | `wos-ri-conductor/app/conductor/conductor.py` |
| Multi-agent orchestration | The conductor routing queries to the correct App | `wos-ri-conductor/` |
| Entity normalisation | Resolving ambiguous author/institution names | `wos-ai-normalizer/app/tools/incites/` |
| MCP (Model Context Protocol) | `agai-api` MCP endpoints — external tool connectivity | `agai-api/api/` |
| LLM gateway | The internal Clarivate LLM API layer | `agai-api/` |
| Streaming responses | SSE token stream from BFF to Angular UI | `research-intelligence-core-api` + WebSocket |
| Evaluation framework | DDA framework measuring agent output quality | `platform-agent-testing/dda_framework/` |
| Hallucination / LLM variance | The findings in your DDA validation report | `platform-agent-testing/reports/` |
| Prompt templates | System prompts per agent in the conductor | `wos-ri-conductor/app/conductor/` |
| Vector databases | Where WOSRI stores indexed research data | `agai-api/` |
| BFF API pattern | Java layer between UI and Python services | `research-intelligence-core-api/` |
| E2E test automation | Playwright + Cucumber test suite | `research-intelligence-ui-tests/` |

---

## The Daily Integration Rule

For every study session, do this at the end:

```
1. Name the concept you studied today (1 sentence)
2. Find where it lives in WOSRI (file path or service name)
3. Write 1 test case that specifically targets this concept
4. Add a note: "What would break in WOSRI if this concept was implemented incorrectly?"
```

If you can't do step 2, you don't understand it well enough yet. Go back.
If you can do all 4 steps, you understood it well enough to apply it.

---

## Week-by-Week Integration Plan

---

### WEEK 1 — LLM Fundamentals → WOSRI Query Pipeline

**Concept:** Tokens, temperature, inference parameters, context windows

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Core Track: LLM fundamentals (tokens, how LLMs generate text) | Look up: where in the conductor is the LLM called? What parameters are set? Print the call signature. |
| **Tue** | Core Track: Temperature, top_p, and inference parameters | Find: does WOSRI use temperature=0 (deterministic) or temperature>0 (creative)? What would happen if you changed it? Write a test case: "low temperature query should return consistent response." |
| **Wed** | Python: Week 1 exercises (text analysis function) | Apply Python: write a small script that counts tokens in a sample WOSRI query using `tiktoken`. How many tokens is your longest test query? |
| **Thu** | Core Track: Context windows and prompt length limits | Investigate: what is the maximum query length WOSRI accepts? Test the boundary. What happens when you exceed it? This is a real test case. |
| **Fri** | Review + Obsidian note | Write in Obsidian: "5 things I now understand about WOSRI that I didn't know Monday." File reference for each one. |
| **Sat** | Deep dive: rewatch LLM fundamentals at 1x, type out all code | Build: a script that takes a WOSRI query and logs its token count, estimated cost, and expected inference time |
| **Sun** | Project: annotate the DDA report with token-level explanations | Which DDA findings can be explained by context window issues vs. temperature variance? Add "root cause at LLM level" to 3 findings. |

**Confidence check by end of Week 1:**
- [ ] Can explain the path from "user types query" to "LLM receives tokens" in WOSRI
- [ ] Can explain why two identical queries to the same agent return different answers
- [ ] Can write a test that specifically targets context window edge cases

---

### WEEK 2 — Embeddings → WOSRI Search and Retrieval

**Concept:** Embeddings, vector search, semantic similarity, vector databases

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Core Track: What embeddings are and why they exist | Find: where does WOSRI convert search queries into vectors? Look in `agai-api/` for embedding endpoints. |
| **Tue** | Core Track: Vector databases and similarity search | Investigate: how does RI Assistant find relevant research papers? Is it keyword search or semantic search? What's the difference in test terms? |
| **Wed** | Python: Week 2 exercises (JSON file processing) | Apply Python: parse one of your DDA report JSON files and extract all "similarity score" or "relevance" fields if they exist |
| **Thu** | Core Track: How semantic search differs from keyword search | Write test cases: "query using synonyms should return the same results as query using exact terms" — this tests embedding quality |
| **Fri** | Review + Obsidian | Obsidian entry: draw the query → embedding → vector search → result flow for WOSRI. Add file references. |
| **Sat** | Deep dive: embeddings section at 1x, build the code example | Project: write a Python script that generates embeddings for 5 sample WOSRI queries and calculates pairwise similarity |
| **Sun** | Work application: use embedding concepts to improve 2 existing test cases | Review your current test suite: which tests could be improved by testing semantic equivalence rather than exact string match? |

**Confidence check by end of Week 2:**
- [ ] Can explain why "who are the top researchers in ML" and "leading scientists in machine learning" should return similar results
- [ ] Can explain what a vector database is and why a relational database can't do the same job
- [ ] Can write a test that catches embedding quality degradation

---

### WEEK 3 — Agent Architecture → WOSRI Conductor Architecture

**Concept:** Agent loops, tool calling, ReAct pattern, agent decision making

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Agentic Track: What an agent is vs. a simple LLM call | Map: open `wos-ri-conductor/app/conductor/conductor.py`. Identify: where is the agent loop? Where does the conductor decide which tool to call next? |
| **Tue** | Agentic Track: Tool calling (function calling) in detail | Catalogue: list every tool in the WOSRI conductor. For each tool: what does it do, what can go wrong, what does a test for it look like? |
| **Wed** | Python: Week 3 exercises (LLM API call) | Apply Python: write a script that calls the conductor API directly (bypassing the UI), send a test query, print response + token count + time |
| **Thu** | Agentic Track: ReAct pattern (Reason + Act loops) | Trace: for a sample Impact Agent query, trace the full ReAct loop. Reason: what does the agent think? Act: what tool does it call? Observe: what does it get back? |
| **Fri** | Review + Obsidian | Obsidian entry: document one full agent execution trace with file references for every step |
| **Sat** | Deep dive: build a minimal tool-calling agent | Build an agent that has 3 tools: search, calculate, format. Give it a task. Watch how it decides which tool to use. |
| **Sun** | Work application: improve 3 WOSRI test cases using agent loop knowledge | Which test cases currently only test the final output? Add intermediate checks: did the agent call the right tool? In the right order? |

**Confidence check by end of Week 3:**
- [ ] Can draw the execution trace of any WOSRI agent query from input to output
- [ ] Can explain what happens when the AppSelectorTool selects the wrong agent
- [ ] Can design tests that validate tool selection, not just final output

---

### WEEK 4 — Multi-Agent Systems → WOSRI 4-Agent Coordination

**Concept:** Agent orchestration, handoffs, parallel execution, shared state

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Agentic Track: Multi-agent coordination patterns | Map: how does the WOSRI conductor decide between the 4 agents? Is this sequential, parallel, or conditional routing? |
| **Tue** | Agentic Track: Agent handoffs and shared state | Test: write a test case that requires handoff between agents — a query that involves both Impact (author performance) and Collaboration (co-authorship). What should happen? What actually happens? |
| **Wed** | Python: Week 4 exercises (PromptTemplate class) | Apply Python: build a PromptTemplate class that can render any of the 4 WOSRI system prompts with variable substitution |
| **Thu** | Agentic Track: Failure modes in multi-agent systems | Failure catalogue: for each of the 4 WOSRI agents, identify: what is the most common failure mode you've seen in 4 months? Now name it formally using agent vocabulary. |
| **Fri** | Review + Obsidian | Obsidian entry: the 4 WOSRI agents as a formal multi-agent system. Diagram: which agent is the orchestrator? Which are the executors? |
| **Sat** | Deep dive: build a minimal multi-agent system (2 agents + orchestrator) | Build an orchestrator that routes a query to either Agent A (data lookup) or Agent B (analysis), based on the query type. |
| **Sun** | Work application: design a cross-agent test suite | Write 5 test cases that test agent routing correctness, not just individual agent output quality |

**Confidence check by end of Week 4:**
- [ ] Can explain how the conductor decides which of the 4 agents handles a query
- [ ] Can identify when a WOSRI failure is a routing failure vs. an agent execution failure
- [ ] Can design a test suite that covers agent orchestration, not just agent output

---

### WEEK 5 — MCP Protocol → WOSRI External Tool Connectivity

**Concept:** Model Context Protocol, MCP servers, tool definitions, context injection

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Agentic Track: What MCP is and why Anthropic created it | Find: open `agai-api/api/`. Does WOSRI already use MCP? What external tools are connected through it? |
| **Tue** | Agentic Track: MCP server and client architecture | Map: if WOSRI exposed a new data source (e.g., grant databases) via MCP, where would the change be made? Which tests would need updating? |
| **Wed** | Python: Week 5 exercises (AgentTestCase dataclass) | Apply Python: build the `AgentTestCase` dataclass modelled on WOSRI's actual test structure |
| **Thu** | Agentic Track: Writing tool definitions for MCP | Write: define an MCP tool specification for the WOSRI NormalizerTool. What are its inputs, outputs, and error cases? |
| **Fri** | Review + Obsidian | Obsidian entry: MCP as an architectural pattern. How does it compare to how WOSRI currently connects tools? |
| **Sat** | Deep dive: build a minimal MCP server with 2 tools | Use the MCP Python SDK. Build a server with a search_papers tool and a normalise_entity tool. Test it. |
| **Sun** | Work application: write MCP-aware test cases | How would your existing WOSRI tests need to change if external tools were exposed via MCP instead of direct HTTP calls? |

**Confidence check by end of Week 5:**
- [ ] Can explain what MCP is to a non-technical colleague in 60 seconds
- [ ] Can explain why MCP exists instead of just using direct API calls
- [ ] Can write a tool definition specification for any WOSRI tool

---

### WEEK 6 — Agent Evaluation → DDA Framework Formalisation

**Concept:** LLM-as-judge, evaluation metrics, test oracles, failure classification

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Agentic Track: Agent evaluation patterns and test oracles | Review: open your DDA validation report. For each of the 7 findings, assign a formal evaluation category: faithfulness, relevance, correctness, safety, format. |
| **Tue** | Agentic Track: LLM-as-judge pattern | Build: write a simple LLM-as-judge prompt that evaluates an Impact Agent response. Input: query + response. Output: score 1–5 + reasoning. Test it on 3 real DDA samples. |
| **Wed** | Python: Week 6 exercises (error handling + retry) | Apply Python: upgrade your Week 3 API caller — retry 3 times on failure with exponential backoff, log every attempt |
| **Thu** | Agentic Track: Human-in-the-loop evaluation | Document: in the DDA framework, when should a human review be required? Build the decision criteria as a flowchart. |
| **Fri** | Review + Obsidian | Obsidian entry: the DDA framework as a formal evaluation system. What category of evaluation framework is it? What is missing? |
| **Sat** | Deep dive: implement DeepEval for 3 WOSRI test cases | Use DeepEval (from Stage 1 curriculum). Run faithfulness, answer relevancy, and hallucination metrics on 3 real agent responses. |
| **Sun** | Work application: extend the DDA framework | Add one new evaluation dimension to the framework that wasn't there before. Write the prompt, add the check, run it. |

**Confidence check by end of Week 6:**
- [ ] Can explain the difference between deterministic tests (exact match) and LLM-judge tests (semantic evaluation)
- [ ] Can design a complete evaluation rubric for any of the 4 WOSRI agents
- [ ] Can explain why the DDA framework alone is insufficient and what it needs to be complete

---

### WEEK 7 — RAG Pipeline → RI Assistant Full Flow

**Concept:** Retrieval-Augmented Generation — the architecture behind every answer RI Assistant gives

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Core Track: RAG pipeline architecture (retrieval → augmentation → generation) | Trace: map the full RI Assistant query flow using `RI_ASSISTANT_WORKSPACE_MAP.md`. Label each step as Retrieval, Augmentation, or Generation. |
| **Tue** | Core Track: Chunking strategies and document indexing | Investigate: how are research papers chunked and indexed in WOSRI's vector store? What chunk size is used? Does it matter for your test results? |
| **Wed** | Python: Week 7 exercises (async concurrent API calls) | Apply Python: make 5 concurrent LLM API calls with the same prompt; measure response time vs sequential. Compare the 5 responses — this demonstrates non-determinism. |
| **Thu** | Core Track: Retrieval quality and relevance scoring | Write test cases targeting retrieval quality: "query about funding should return funding-related papers, not author impact papers" |
| **Fri** | Review + Obsidian | Obsidian entry: diagram the RAG pipeline for one specific WOSRI agent. Which step is most likely to fail? |
| **Sat** | Deep dive: build a minimal RAG from scratch | Use a sample set of 10 "research papers" (text files you create). Build: embed them, store them, query them, generate an answer. This demystifies what WOSRI does. |
| **Sun** | Work application: write 3 tests targeting RAG failure modes | Failure modes to test: irrelevant retrieval, no retrieval (empty corpus), conflicting retrieved documents |

**Confidence check by end of Week 7:**
- [ ] Can explain why RI Assistant sometimes gives confident but wrong answers (retrieval failure → hallucination)
- [ ] Can explain what "grounding" means and why it matters for research intelligence
- [ ] Can design a test suite that covers all 3 RAG failure modes

---

### WEEK 8 — Prompting Techniques → WOSRI Agent Prompt Analysis

**Concept:** System prompts, few-shot examples, chain-of-thought, prompt engineering patterns

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Core Track: System prompts and their role in agent behaviour | Find: locate the system prompts used by each of the 4 WOSRI agents in the conductor. What role does each one define? |
| **Tue** | Core Track: Few-shot prompting and chain-of-thought | Analyse: do the WOSRI agent prompts use few-shot examples? Should they? Write a test that validates the agent follows its system prompt correctly. |
| **Wed** | Python: Week 8 exercises (pytest) | Apply Python: write pytest tests for the DDA framework's comparison logic |
| **Thu** | Core Track: Prompt injection and adversarial inputs | Security testing: write 5 adversarial test queries designed to make the WOSRI agents ignore their system prompts or behave outside their intended scope |
| **Fri** | Review + Obsidian | Obsidian entry: rate the 4 WOSRI system prompts (if accessible) on: clarity, role definition, constraint specificity, output format guidance |
| **Sat** | Deep dive: prompt engineering section at 1x, apply to your DDA prompt | Review your own `DDA prompt.txt` using what you've learned. What would you change? Document the improvements. |
| **Sun** | Work application: rewrite 2 weak test cases using prompt engineering insights | Which of your existing Cucumber test cases would be stronger if they included adversarial inputs or edge case prompts? |

**Confidence check by end of Week 8:**
- [ ] Can review a system prompt and identify: what it will do well, what it will do badly, what adversarial input could break it
- [ ] Can explain why the Emerging Topics agent sometimes goes off-topic (likely a prompt scope issue)
- [ ] Can write a structured system prompt for a new agent from scratch

---

### WEEK 9 — Production Patterns → WOSRI Reliability

**Concept:** Caching, rate limiting, cost management, retries, production API patterns

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Production Track: LLM API at scale (retries, rate limits, cost) | Investigate: does WOSRI cache any LLM responses? If it does, how does caching affect your test results? If it doesn't, why not? |
| **Tue** | Production Track: Cost estimation and token budgets | Calculate: estimate the monthly LLM API cost of the WOSRI RI Assistant based on average query length and response length. Use `tiktoken` for token counts. |
| **Wed** | Python: Week 9 exercises (Pydantic models) | Apply Python: rewrite one section of the DDA framework's data models using Pydantic |
| **Thu** | Production Track: Monitoring what matters in production | Define: what 5 metrics would you add to the DDA dashboard if you were building a production monitoring system? For each: why it matters, how to measure it. |
| **Fri** | Review + Obsidian | Obsidian entry: WOSRI as a production AI system. What production concerns are well-addressed? What is missing? |
| **Sat** | Deep dive: instrument your minimal agent with production patterns | Add to your Week 6 multi-agent system: retry logic, response caching, cost tracking, error alerting |
| **Sun** | Work application: write reliability test cases | Write test cases that target production reliability: what happens when the LLM gateway is slow? When it's down? When it returns a malformed response? |

**Confidence check by end of Week 9:**
- [ ] Can explain the cost implications of different context window sizes
- [ ] Can design a monitoring strategy for a production AI system
- [ ] Can write tests that target reliability, not just correctness

---

### WEEK 10 — Deployment Basics → WOSRI Service Architecture

**Concept:** FastAPI, Docker, environment management, service boundaries

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Production Track: FastAPI basics | Open: `wos-ri-conductor/` is a FastAPI service. Read its main entry point. Identify: endpoints, middleware, startup events. |
| **Tue** | Production Track: Docker and containerisation basics | Investigate: does the WOSRI conductor have a Dockerfile? What is its base image? What does the startup command do? |
| **Wed** | Python: Week 10 exercises (CLI tool) | Apply Python: build the CLI tool that wraps your API caller — this is the foundation of Project 1 |
| **Thu** | Production Track: Environment management | Review: how does WOSRI manage different environments (dev, stable, prod)? Where are environment variables set? What breaks when they're wrong? |
| **Fri** | Review + Obsidian | Obsidian entry: the WOSRI service mesh. Draw which services talk to which, what protocol they use, and what breaks first in each failure scenario. |
| **Sat** | Deep dive: add a FastAPI endpoint to your multi-agent system | Expose your Week 6 agent as a REST API. Test it with curl and with pytest. |
| **Sun** | Work application: write environment-specific test cases | Which of your WOSRI test cases behave differently in dev vs. stable? Why? Document the expected differences as explicit test metadata. |

**Confidence check by end of Week 10:**
- [ ] Can read any FastAPI service file and explain its endpoints and middleware
- [ ] Can explain the purpose of each WOSRI service and what breaks if it goes down
- [ ] Can write tests that are environment-aware (not brittle to env differences)

---

### WEEK 11 — Monitoring and Observability → DDA Dashboard

**Concept:** Logging, metrics, dashboards, evaluation in production

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Production Track: Monitoring and observability fundamentals | Review: what does the DDA HTML report currently show? What is missing? List 5 metrics you wish it showed. |
| **Tue** | Production Track: Evaluation in production (not just in testing) | Design: what would a live WOSRI quality dashboard show? What metrics, at what frequency, with what alerting thresholds? |
| **Wed** | Python: Week 11 exercises (integrate everything) | Apply Python: add proper `logging` to the DDA framework. Replace any `print()` statements with structured log calls. |
| **Thu** | Production Track: Alerting and anomaly detection | Write: what anomalies in WOSRI agent output should trigger an alert? Define thresholds for: response time, error rate, semantic similarity drift. |
| **Fri** | Review + Obsidian | Obsidian entry: the DDA framework as a monitoring system. What is it? What should it become? |
| **Sat** | Deep dive: build a minimal dashboard for DDA results | Use Python + HTML/JS. Load a DDA report JSON. Show: pass rate, failure categories, trend over 5 runs. This is Project 3 (DDA Dashboard). |
| **Sun** | Work application: propose 3 monitoring improvements to the DDA framework | For each: what it measures, why it matters, how to implement it, what action it triggers |

**Confidence check by end of Week 11:**
- [ ] Can design a production monitoring system for any AI service
- [ ] Can explain the difference between testing (pre-deployment) and monitoring (post-deployment)
- [ ] Can build a basic dashboard for AI system output metrics

---

### WEEK 12 — Integration Week → Portfolio and Interview Prep

**Concept:** Everything comes together. Projects ship. Interview answers are sharpened.

| Day | Study | Work Integration Task |
|-----|-------|----------------------|
| **Mon** | Project 1: Ticket-to-Test Pipeline — build it | Write the tool from scratch using Python weeks 1–11. No AI writing the code. |
| **Tue** | Project 1: Test it on 3 real WOSRI Jira tickets | Run the tool on real tickets from your current sprint. Does the output match what you'd generate manually? |
| **Wed** | Production Track: final sections (any remaining) | Apply: does anything in the final sections connect to a WOSRI gap you've identified? |
| **Thu** | CV and interview prep | Apply the honest assessment framing. For each project you've built in 12 weeks, write 1 interview answer using the format: "I built X, it does Y, I made design decision Z because…" |
| **Fri** | Review: what have you actually learned? | Write a new honest assessment — same format as `honest_assessment.md`. What changed in 12 weeks? What is your new Python rating? What gaps remain? |
| **Sat** | Portfolio: push all 4 projects to GitHub | Each project: README, what it does, how to run it, what you learned building it |
| **Sun** | Retrospective: what is the 3-month plan for Month 4–6? | You now have an accurate picture of where you are. Plan the next 90 days. |

**Confidence check by end of Week 12:**
- [ ] Can build a working Python tool from requirements to shipped script without AI writing the code
- [ ] Can explain the entire WOSRI system from token ingestion to response streaming — at the architecture level
- [ ] Can answer "tell me about a time you identified a failure in a production AI system" with a specific, technical, honest story
- [ ] Can explain your own skill level accurately and without false modesty or overclaiming

---

## The Integration Checklist (use this every Friday)

```
Weekly Integration Review — Friday Obsidian Entry

1. What concept did I study this week?
2. Where does this concept exist in WOSRI? (file path)
3. What WOSRI behaviour can I now explain that I couldn't explain last week?
4. What test case did I write (or improve) because of what I learned?
5. What question do I still have? (Write it down — you'll answer it next week)
6. Python: what did I write this week without AI help?
7. One thing I want to build with what I learned
```

---

## What "Seamless Integration" Actually Means

It means that when you get a new WOSRI ticket on Monday morning, you ask:
- **Which concept from last week's study does this ticket relate to?**
- **What would an AI engineer know about this system that would make me test it better?**
- **What is the formal name for the failure mode I'm testing for?**

It also means that when you finish a study session, you ask:
- **Which open WOSRI ticket can I test differently because of what I just learned?**
- **Which DDA finding can I now explain at a deeper level?**
- **What would I add to the DDA framework based on what I just studied?**

These are not extra tasks. They are the same task seen from two angles.
The person who can see from both angles is the person who gets promoted.

---

*Revised: 2026-05-06 | Weeks 3–8 reordered — Agentic Track moved to Weeks 3–6, Core Track RAG/Prompting to Weeks 7–8*
*WOSRI Architecture ref: RI_ASSISTANT_WORKSPACE_MAP.md*
*Honest Assessment ref: curriculum/my_knowledge_map/honest_assessment.md*
*DDA Framework ref: platform-agent-testing/dda_framework/*
