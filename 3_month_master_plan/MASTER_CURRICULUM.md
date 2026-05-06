---
tags: [curriculum, master-plan, 12-week, schedule]
created: 2026-05-05
status: active
---

# 12-Week Master Curriculum

> **3 courses. 1 Python track. 4 projects. 84 days.**
> Every week has: a theme, a course section, a Python exercise, a WOSRI task, and a milestone.
> The 30-day curriculum in `/stage_*/` remains your deep-reference library. This plan is your schedule.

---

## At a Glance

| Weeks | Theme | Course | Python Phase | Project |
|-------|-------|--------|-------------|---------|
| 1–2 | LLM Foundations | Core Track — Fundamentals + Embeddings | Survival Python | — |
| 3–6 | Agent Architecture + Evaluation | Agentic Track — all of it (moved earlier) | AI Engineering Python | — |
| 7–8 | RAG + Prompting | Core Track — RAG + Prompting sections | AI Engineering Python | Project 4 starts |
| 9–12 | Production + Portfolio | Production Track | Independent Authorship | Projects 1–4 |

---

## MONTH 1 — LLM Foundations + Agent Architecture (Weeks 1–4)

### Week 1: How LLMs Work

| Element | Detail |
|---------|--------|
| **Course section** | Core Track: LLM Fundamentals (tokens, inference, temperature, context windows) |
| **Watch speed** | 1x on code sections, 1.5x on concept sections |
| **Python exercise** | Week 1: Text analysis function (word count, sentence count, avg word length) |
| **WOSRI task** | Find: where is the LLM called in `wos-ri-conductor`? What parameters are set? |
| **Build** | Script: count tokens in 5 sample WOSRI queries using `tiktoken` |
| **Friday integration** | Write 2 test cases that target context window edge cases |
| **Milestone** | Can explain token-level flow from WOSRI UI → LLM → response |
| **Stage 0 curriculum ref** | `stage_0_foundations/concepts.md` — read alongside |

**Confidence Checklist — Week 1:**
- [ ] L1: Can explain what a token is and why it matters for cost and quality
- [ ] L1: Can explain temperature and what happens at 0.0 vs 1.0
- [ ] L2: Can find where WOSRI sets LLM parameters (file path)
- [ ] L2: Can write a test case targeting context window limits
- [ ] L3: Can explain why two identical WOSRI queries return different responses (non-determinism)
- [ ] L3: Can identify which DDA findings were caused by LLM variance vs. true bugs

**3-Level Scenario Questions — Week 1:**

*Level 1 — Conceptual:*
"A user asks why the Impact Agent gives different answers to the same question.
Explain what is happening at the token and inference level. No jargon the user doesn't need."

*Level 2 — Applied:*
"Your WOSRI DDA test for the Impact Agent is failing intermittently — sometimes pass, sometimes fail for the same query.
Walk through your diagnostic process. What do you check first? What does it tell you?"

*Level 3 — Systems/Expert:*
"You need to make the Impact Agent's responses deterministic for compliance purposes.
What are the tradeoffs of setting temperature=0? What else affects non-determinism beyond temperature?
How would you test that you've actually achieved determinism vs. just reduced variance?"

---

### Week 2: Embeddings and Vector Search

| Element | Detail |
|---------|--------|
| **Course section** | Core Track: Embeddings, vector databases, semantic similarity |
| **Watch speed** | 1x — this is foundational, cannot be rushed |
| **Python exercise** | Week 2: Read a JSON file → process → write summary JSON |
| **WOSRI task** | Find the embedding endpoints in `agai-api/`. What model generates embeddings? |
| **Build** | Script: generate embeddings for 5 WOSRI queries, calculate pairwise cosine similarity |
| **Friday integration** | Write 2 test cases that test semantic equivalence (same query, different phrasing) |
| **Milestone** | Can explain how RI Assistant finds relevant research papers |
| **Stage 0 curriculum ref** | `stage_0_foundations/concepts.md` — embeddings chapter |

**Confidence Checklist — Week 2:**
- [ ] L1: Can explain what an embedding is using an analogy (not "a vector")
- [ ] L1: Can explain why cosine similarity is used instead of Euclidean distance
- [ ] L2: Can find where WOSRI generates embeddings and for what data
- [ ] L2: Can write a test that catches embedding quality degradation
- [ ] L3: Can explain the tradeoff between embedding model size and retrieval quality
- [ ] L3: Can design a test strategy for semantic search quality in RI Assistant

**3-Level Scenario Questions — Week 2:**

*Level 1 — Conceptual:*
"Why does RI Assistant return relevant results for 'leading scientists in ML' when the database
only has the phrase 'top researchers in machine learning'? Explain the mechanism."

*Level 2 — Applied:*
"The Impact Agent starts returning irrelevant papers after a model update.
Your existing keyword-match tests all pass. Why? What tests would catch this?"

*Level 3 — Systems/Expert:*
"RI Assistant's retrieval quality has degraded. You don't know if it's the embedding model,
the chunking strategy, the vector index, or the retrieval query. Design a diagnostic plan
that isolates which component is failing, with a test for each hypothesis."

---

### Week 3: Agent Architecture

| Element | Detail |
|---------|--------|
| **Course section** | Agentic Track: Agent fundamentals, tool calling, ReAct pattern |
| **Watch speed** | 1x — this maps directly to your daily WOSRI work |
| **Python exercise** | Week 3: Call an LLM API from scratch, print response + token count + time |
| **WOSRI task** | Trace 1 full agent execution from conductor → tool → LLM → response with file references |
| **Build** | Minimal tool-calling agent: 3 tools (search, calculate, format), 1 task |
| **Friday integration** | Catalogue all WOSRI tools: name, purpose, failure mode, missing test |
| **Milestone** | Can draw the execution trace of any WOSRI agent with formal tool-calling vocabulary |
| **Stage 2 curriculum ref** | `stage_2_ai_systems/concepts.md` — agents chapter |

**Confidence Checklist — Week 3:**
- [ ] L1: Can explain the ReAct pattern (Reason → Act → Observe loop)
- [ ] L1: Can explain what tool calling is and why it matters
- [ ] L2: Can trace any WOSRI agent's execution with file path references
- [ ] L2: Can write tests that validate tool selection, not just final output
- [ ] L3: Can explain what happens when AppSelectorTool selects the wrong agent
- [ ] L3: Can design a test strategy that covers agent decision-making, not just agent output

**3-Level Scenario Questions — Week 3:**

*Level 1 — Conceptual:*
"Explain the ReAct agent pattern. Why is 'Reason + Act' better than just 'Act'?
What does the Observe step add? Use the WOSRI conductor as your example."

*Level 2 — Applied:*
"The Impact Agent is calling the NormalizerTool repeatedly in a loop without making progress.
What is this failure mode called? What causes it? How do you test for it?
What is the production mitigation?"

*Level 3 — Systems/Expert:*
"You are designing a test strategy for the WOSRI conductor's agent selection logic.
The conductor must correctly route queries to Impact, Collaboration, Funding, or Emerging Topics.
Design: the test dataset, the evaluation criteria, the edge cases, and the monitoring strategy."

---

### Week 4: Multi-Agent Systems

| Element | Detail |
|---------|--------|
| **Course section** | Agentic Track: Multi-agent coordination, handoffs, parallel execution, shared state |
| **Watch speed** | 1x |
| **Python exercise** | Week 4: PromptTemplate class with .render() and .validate() methods |
| **WOSRI task** | Map the 4-agent coordination pattern: is it parallel, sequential, or conditional routing? |
| **Build** | 2-agent system with orchestrator: routes to Agent A (data) or Agent B (analysis) |
| **Friday integration** | Write 5 cross-agent test cases (routing correctness, not just output quality) |
| **Milestone** | Can explain WOSRI's multi-agent architecture using formal vocabulary |
| **Stage 2 curriculum ref** | `stage_2_ai_systems/concepts.md` — orchestration chapter |

**Confidence Checklist — Week 4:**
- [ ] L1: Can explain the difference between a coordinator and an executor agent
- [ ] L1: Can explain why multi-agent systems are harder to test than single-agent systems
- [ ] L2: Can explain which WOSRI agent is the orchestrator and which are executors
- [ ] L2: Can write tests that validate routing decisions, not just agent output
- [ ] L3: Can explain how shared state between agents can cause test flakiness
- [ ] L3: Can design a test suite that distinguishes routing failures from execution failures

---

## MONTH 2 — Agent Systems + RAG + Evaluation (Weeks 5–8)

### Week 5: MCP Protocol

| Element | Detail |
|---------|--------|
| **Course section** | Agentic Track: MCP (Model Context Protocol), servers, tool definitions |
| **Watch speed** | 1x — new protocol, technically dense |
| **Python exercise** | Week 5: AgentTestCase dataclass with all fields |
| **WOSRI task** | Find MCP-related code in `agai-api/`. Understand what tools are exposed. |
| **Build** | Minimal MCP server: search_papers tool + normalise_entity tool, 2 test calls |
| **Friday integration** | Write tool definition spec for the WOSRI NormalizerTool in MCP format |
| **Milestone** | Can explain MCP to a colleague and explain how `agai-api` uses it |
| **Stage 2 curriculum ref** | `stage_2_ai_systems/concepts.md` — tool protocols chapter |

**Confidence Checklist — Week 5:**
- [ ] L1: Can explain what MCP is and the problem it solves
- [ ] L1: Can explain the difference between direct API calls and MCP-mediated tool calls
- [ ] L2: Can find where MCP is used in `agai-api` and explain what it enables
- [ ] L2: Can write a tool definition spec for any WOSRI tool
- [ ] L3: Can explain the architectural tradeoffs of MCP vs. direct integration
- [ ] L3: Can design a test strategy for an MCP-connected tool that includes failure modes

---

### Week 6: Agent Evaluation — Formalise the DDA Framework

| Element | Detail |
|---------|--------|
| **Course section** | Agentic Track: Agent evaluation, LLM-as-judge, test oracles, human-in-the-loop |
| **Watch speed** | 1x — this is your core domain, maximum attention |
| **Python exercise** | Week 6: Error handling + retry logic (3 attempts, exponential backoff) |
| **WOSRI task** | Assign formal evaluation categories to all 7 DDA findings: faithfulness, relevance, correctness, safety, format |
| **Build** | LLM-as-judge prompt for Impact Agent. Test on 3 real DDA samples. |
| **Friday integration** | Define: when should a DDA result require human review? Build decision criteria. |
| **Milestone** | Can explain the DDA framework as a formal evaluation system with gaps identified |
| **Stage 1 curriculum ref** | `stage_1_ai_validation/concepts.md` — evaluation chapter |

**Confidence Checklist — Week 6:**
- [ ] L1: Can explain LLM-as-judge: what it is, when to use it, when not to
- [ ] L1: Can explain the 5 evaluation dimensions: faithfulness, relevance, correctness, safety, format
- [ ] L2: Can classify all 7 DDA findings using formal evaluation vocabulary
- [ ] L2: Can write an LLM-as-judge prompt for any WOSRI agent
- [ ] L3: Can explain what the DDA framework is missing and how to make it production-grade
- [ ] L3: Can design an evaluation rubric for a new WOSRI agent from first principles

**3-Level Scenario Questions — Week 6:**

*Level 1 — Conceptual:*
"Explain LLM-as-judge. Why would you use an LLM to evaluate another LLM's output?
What are the failure modes of this approach? When is human evaluation irreplaceable?"

*Level 2 — Applied:*
"The DDA framework currently compares agent outputs against a baseline.
A colleague argues this is not real evaluation because 'you're just comparing to an old wrong answer'.
They're partially right. What is the actual limitation? How would you extend the framework?"

*Level 3 — Systems/Expert:*
"You are designing the evaluation system for a new WOSRI agent that doesn't exist yet —
an Emerging Ethics agent that identifies ethical concerns in research papers.
There is no gold standard dataset. There is no baseline. How do you build an evaluation system
for an agent whose 'correct' output is partly subjective? What are the philosophical tradeoffs?"

---

### Week 7: RAG Pipeline Architecture

| Element | Detail |
|---------|--------|
| **Course section** | Core Track: RAG pipeline (retrieval → augmentation → generation) |
| **Watch speed** | 1x — build the code example as you watch |
| **Python exercise** | Week 7: Async concurrent API calls (5 parallel calls, measure time vs. sequential) |
| **WOSRI task** | Trace the full RI Assistant query flow. Label each step R, A, or G. |
| **Build** | Minimal RAG: 10 text "papers" → embed → store → query → generate answer |
| **Friday integration** | Write 3 test cases targeting RAG failure modes: irrelevant retrieval, empty retrieval, conflicting docs |
| **Milestone** | Can build a working (minimal) RAG system from scratch |
| **Stage 2 curriculum ref** | `stage_2_ai_systems/concepts.md` — RAG chapter |

**Confidence Checklist — Week 7:**
- [ ] L1: Can explain RAG in one sentence (what it solves, how it works)
- [ ] L1: Can explain why LLMs hallucinate less with RAG than without
- [ ] L2: Can label every component of RI Assistant as R, A, or G
- [ ] L2: Can write tests for all 3 RAG failure modes
- [ ] L3: Can explain the tradeoffs of different chunking strategies for research paper indexing
- [ ] L3: Can diagnose a "confidently wrong" RI Assistant answer at the RAG failure level

**3-Level Scenario Questions — Week 7:**

*Level 1 — Conceptual:*
"Explain RAG to a non-technical product manager who wants to know why RI Assistant
sometimes gives wrong answers even though it 'has access to the research database'."

*Level 2 — Applied:*
"The Funding Discovery agent is returning answers about author impact instead of funding.
Is this a retrieval failure, an augmentation failure, or a generation failure? How do you tell?"

*Level 3 — Systems/Expert:*
"You are designing the test strategy for a RAG system that will index 50 million research papers.
What are the 5 failure modes you must cover? For each: the test type, the expected behaviour,
and what it would cost the user if it fails silently."

---

### Week 8: Prompting Techniques

| Element | Detail |
|---------|--------|
| **Course section** | Core Track: Prompting (system prompts, few-shot, chain-of-thought, adversarial) |
| **Watch speed** | 1.5x for concepts, 1x for code examples |
| **Python exercise** | Week 8: pytest tests for PromptTemplate class |
| **WOSRI task** | Locate the 4 WOSRI agent system prompts. Rate each on: role clarity, constraint specificity, output format guidance |
| **Build** | 5 adversarial test queries designed to break each WOSRI agent out of scope |
| **Friday integration** | Review `DDA prompt.txt` with new vocabulary. Document: what it does well, what it would change |
| **Milestone** | Can review any system prompt and predict its failure modes |
| **Stage 1 curriculum ref** | `stage_1_ai_validation/concepts.md` — prompting chapter |

**Confidence Checklist — Week 8:**
- [ ] L1: Can explain the difference between zero-shot, few-shot, and chain-of-thought prompting
- [ ] L1: Can explain what prompt injection is and why it matters for AI testing
- [ ] L2: Can review any WOSRI system prompt and identify its weaknesses
- [ ] L2: Can write 5 adversarial inputs for any given agent scope
- [ ] L3: Can design a prompt robustness test suite (scope violations, injection attempts, conflicting instructions)
- [ ] L3: Can explain why the DDA prompt.txt works well and what structured prompt design principles it uses

**3-Level Scenario Questions — Week 8:**

*Level 1 — Conceptual:*
"What is chain-of-thought prompting, and under what circumstances does it improve
LLM output quality? When does it make things worse?"

*Level 2 — Applied:*
"A user discovers that if they include 'ignore your previous instructions' in a WOSRI query,
the agent changes its behaviour. What happened? What test should have caught this?
How would you fix it at the prompt level?"

*Level 3 — Systems/Expert:*
"You are designing a prompt robustness standard for all 4 WOSRI agents.
Define: what does 'robust' mean for a production AI agent's system prompt?
What are the 5 dimensions you would test? How would you score them?"

---

## MONTH 3 — Production + Portfolio

### Week 9: Production LLM Patterns

| Element | Detail |
|---------|--------|
| **Course section** | Production Track: API at scale, caching, rate limiting, cost management, retries |
| **Python exercise** | Week 9: Pydantic models for AgentTestCase |
| **WOSRI task** | Estimate monthly LLM cost of RI Assistant. Calculate using token counts from real DDA runs. |
| **Build** | Add to multi-agent system: retry logic, response caching, cost tracking, error alerting |
| **Friday integration** | Write reliability test cases: slow LLM, down LLM, malformed response |
| **Milestone** | Can explain the production reliability concerns of any LLM-powered service |

**Confidence Checklist — Week 9:**
- [ ] L1: Can explain exponential backoff and why it exists
- [ ] L1: Can explain the cost implications of context window size
- [ ] L2: Can estimate the LLM cost of a WOSRI query from token counts
- [ ] L2: Can write tests that target production reliability, not just correctness
- [ ] L3: Can design a cost and reliability strategy for a production AI service
- [ ] L3: Can explain why caching is architecturally complex for LLM responses

---

### Week 10: Deployment and Service Architecture

| Element | Detail |
|---------|--------|
| **Course section** | Production Track: FastAPI, Docker basics, environment management, service boundaries |
| **Python exercise** | Week 10: CLI tool (argparse or click) wrapping your API caller |
| **WOSRI task** | Read the WOSRI conductor Dockerfile and main entry point. Document what you find. |
| **Build** | Expose your multi-agent system as a FastAPI REST API |
| **Friday integration** | Write environment-specific test metadata for 5 existing WOSRI test cases |
| **Milestone** | Can read any FastAPI service file and explain its architecture |

**Confidence Checklist — Week 10:**
- [ ] L1: Can explain what FastAPI is and why it's used in AI services
- [ ] L1: Can explain what Docker does and why containerisation matters
- [ ] L2: Can read `wos-ri-conductor/` and explain its API surface
- [ ] L2: Can add a new endpoint to a FastAPI app
- [ ] L3: Can explain the service boundary decisions in WOSRI's 5-service architecture
- [ ] L3: Can explain what breaks first in each WOSRI service failure scenario

---

### Week 11: Monitoring, Observability, DDA Dashboard

| Element | Detail |
|---------|--------|
| **Course section** | Production Track: Monitoring, observability, evaluation in production |
| **Python exercise** | Week 11: Add proper logging to the DDA framework (replace print with logging) |
| **WOSRI task** | Design a production quality dashboard for WOSRI: 5 metrics, thresholds, alert conditions |
| **Build** | Project 3 (DDA Dashboard): minimal HTML/JS dashboard loading DDA report JSON |
| **Friday integration** | Propose 3 monitoring improvements to the DDA framework with implementation notes |
| **Milestone** | Can build a functional monitoring dashboard for AI system output |

**Confidence Checklist — Week 11:**
- [ ] L1: Can explain the difference between testing and monitoring
- [ ] L1: Can explain what observability means for an LLM system
- [ ] L2: Can define 5 meaningful metrics for the WOSRI RI Assistant
- [ ] L2: Can build a basic dashboard that visualises DDA report data
- [ ] L3: Can design a full monitoring + alerting strategy for a production AI system
- [ ] L3: Can explain what the DDA framework would need to become a monitoring system

---

### Week 12: Integration, Projects, Portfolio

| Element | Detail |
|---------|--------|
| **Course section** | Production Track: final sections + Core Track remainder (QLoRA optional) |
| **Python exercise** | Project 1: Ticket-to-Test Pipeline — write it independently |
| **WOSRI task** | Test Project 1 on 3 real WOSRI Jira tickets from your current sprint |
| **Build** | All 4 projects pushed to GitHub with READMEs |
| **Friday integration** | Write new honest assessment — same format as `honest_assessment.md`. What changed? |
| **Milestone** | Portfolio complete. 4 projects shipped. Can interview for AI Validation Engineer roles. |

**Confidence Checklist — Week 12:**
- [ ] L1: Can explain your entire 12-week learning arc in 2 minutes
- [ ] L2: Can demo at least 2 of your 4 projects to a technical interviewer
- [ ] L2: Can explain every design decision in the Ticket-to-Test Pipeline
- [ ] L3: Can answer "tell me about a time you found a production AI system failure" with full technical depth
- [ ] L3: Can explain the WOSRI architecture from token ingestion to UI render — without notes
- [ ] L3: Can accurately state your current skill level at every competency — no overclaiming, no underclaiming

---

## The 4 Projects

| # | Project | Weeks | What It Demonstrates |
|---|---------|-------|---------------------|
| 1 | **Ticket-to-Test Pipeline** | Wks 11–12 | Python authorship, prompt engineering, structured outputs |
| 2 | **RAG over Workspace Docs** | Wks 7–9 | Embeddings, retrieval, LLM integration |
| 3 | **DDA Dashboard** | Wk 11 | Data visualisation, web basics, monitoring concepts |
| 4 | **Eval Notebook** | Wks 7–9 | DeepEval/RAGAS, evaluation framework literacy |

Each project has a spec in `curriculum/projects/`.

---

## Milestone Tracker

```
Month 1 milestones:
  [ ] Week 1: Can explain WOSRI token-level flow
  [ ] Week 2: Can explain how RI Assistant finds relevant papers
  [ ] Week 3: Can draw execution trace of any WOSRI agent with formal vocabulary
  [ ] Week 4: Can explain WOSRI multi-agent architecture formally

Month 2 milestones:
  [ ] Week 5: Built a minimal MCP server
  [ ] Week 6: DDA framework formalised with evaluation vocabulary
  [ ] Week 7: Built a minimal working RAG system
  [ ] Week 8: Can review any system prompt and predict its failure modes

Month 3 milestones:
  [ ] Week 9: Can estimate WOSRI LLM costs from token counts
  [ ] Week 10: Built and deployed a FastAPI endpoint
  [ ] Week 11: DDA Dashboard shipped
  [ ] Week 12: 4 projects on GitHub, new honest assessment written
```

---

*Revised: 2026-05-06 | Course sequence corrected — Agentic Track moved to Weeks 3–6, Core Track RAG/Prompting deferred to Weeks 7–8*
*This schedule integrates with: WORK_INTEGRATION.md (daily tasks) | DAILY_TIMETABLE.md (session structure)*
*Reference library: stage_0/ through stage_4/ curriculum files*
*Source of truth for skill level: my_knowledge_map/honest_assessment.md*
