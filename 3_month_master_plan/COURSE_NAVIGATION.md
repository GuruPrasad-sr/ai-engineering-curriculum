---
tags: [navigation, courses, strategy, udemy]
created: 2026-05-05
status: active
---

# Course Navigation Guide — 3 Udemy Courses, 3 Months

> **The one rule before you start:** Never watch a lecture passively.
> Every lecture must produce a written output — a note, a code file, or an Obsidian entry.
> If you watched it but wrote nothing, you did not learn it. You entertained yourself.

---

## The 3 Courses: What They Are and What They Are Not

| Course | Hours | Your Use | Risk |
|--------|-------|----------|------|
| **Core Track** — LLM Engineering, RAG, QLoRA, Agents | 33.5 hrs | Foundation vocabulary + RAG architecture | Broad — will tempt you to watch everything; don't |
| **Agentic Track** — Agents & MCP (Ed Donner) | 17 hrs | Most directly maps to your WOSRI work | Intermediate-labelled but manageable with context you already have |
| **Production Track** — Deploy LLMs & Agents at Scale | 18.5 hrs | Monitoring, observability, deployment patterns | Premature if done first; powerful if done after Month 2 |

**Total:** 69 hrs video → ~46 hrs at 1.5x → ~140 hrs with hands-on practice.
**Your budget:** 17 hrs/week × 12 weeks = 204 hrs. It fits.

---

## Master Watch Order

Do not watch the courses in Udemy's default order. Watch them in this sequence:

```
Month 1 (Weeks 1–4):  Core Track — selected sections only (see below)
Month 2 (Weeks 5–8):  Agentic Track — all of it
Month 3 (Weeks 9–12): Production Track + Core Track remainder
```

---

## Month 1 — Core Track Navigation (Weeks 1–4)

### What to watch (in this order):
1. **LLM Fundamentals section** — tokens, context windows, temperature, top_p, inference
2. **Embeddings section** — what they are, why they exist, vector space intuition
3. **RAG pipeline section** — the full retrieval → augmentation → generation loop
4. **Prompting techniques section** — zero-shot, few-shot, chain-of-thought, system prompts
5. **Agents basics section** — tool calling, ReAct pattern, agent loops

### What to skip in Month 1:
- ❌ QLoRA / fine-tuning sections → defer to Month 3 or skip entirely if AI Validation is your path
- ❌ Advanced model training / PEFT → not relevant to your role at this stage
- ❌ Deep infrastructure sections → skim at 2x, take 1 note max

### Deep dive (watch twice, then build):
- ✅ RAG pipeline — the most foundational concept for your current work
- ✅ Prompting techniques — directly improves your daily WOSRI test prompt design

### Month 1 target: By Week 4, you can explain what happens between a user typing a query into RI Assistant and the response appearing. Not in vague terms — at the token level.

---

## Month 2 — Agentic Track Navigation (Weeks 5–8)

### Watch all of it. No skip list.

**Prioritisation within the course:**

| Section | Priority | Why |
|---------|----------|-----|
| Tool calling and function calling | ★★★★★ | This is exactly how WOSRI's AppSelectorTool, NormalizerTool, etc. work |
| ReAct agent pattern | ★★★★★ | This is the orchestration pattern in `wos-ri-conductor` |
| Multi-agent coordination | ★★★★★ | The 4 WOSRI agents coordinated by the conductor — this is your daily work |
| MCP (Model Context Protocol) | ★★★★★ | `agai-api` has MCP endpoints. Understand what they do and why |
| Agent memory and state | ★★★★☆ | WOSRI chat history is an agent memory implementation |
| Agent failure modes | ★★★★★ | You've already seen these in production — now you'll have names for them |
| Human-in-the-loop patterns | ★★★☆☆ | Useful for AI Validation role specifically |
| Agent evaluation | ★★★★★ | This is what the DDA framework does — now formalise it |

### Deep dive (watch twice, then build):
- ✅ Tool calling section — open `wos-ri-conductor/app/conductor/conductor.py` while watching
- ✅ MCP protocol section — open `agai-api/api/` while watching
- ✅ Agent evaluation section — open `platform-agent-testing/dda_framework/` while watching

### Month 2 target: By Week 8, you can look at any agent in WOSRI and describe its architecture using formal terms: tools, state, memory, handoff pattern, failure mode surface.

---

## Month 3 — Production Track + Core Track Remainder (Weeks 9–12)

### Production Track navigation:

| Section | Priority | Why |
|---------|----------|-----|
| LLM API integration at scale | ★★★★★ | How to call LLMs reliably (retries, rate limits, cost) |
| Monitoring and observability | ★★★★★ | What the DDA framework measures — and what it's missing |
| Caching strategies | ★★★★☆ | Cost and latency optimisation — real production concerns |
| Deployment basics (FastAPI, Docker) | ★★★☆☆ | Enough to understand what your team ships |
| Evaluation in production | ★★★★★ | Connects directly to DDA dashboard and eval notebook projects |
| Deep Kubernetes / infra sections | ★☆☆☆☆ | Skim only — not your domain yet |
| CI/CD for ML | ★★★☆☆ | Understand patterns, don't build from scratch yet |

### Core Track remainder (QLoRA etc.):
- QLoRA / fine-tuning: watch only if time permits, this is an optional stretch
- Treat it as background knowledge, not required for your 3-month target

### Month 3 target: By Week 12, you can look at the DDA framework and describe what it measures, what it's missing, what a production-grade monitoring system would add, and how you'd extend it.

---

## The Note-Taking Pattern That Actually Works

For every lecture section (not every video — every section):

```
BEFORE watching:
  Write 2 questions you expect the section to answer.

DURING watching:
  Pause every 10 minutes.
  Write 1-2 sentences on what was just covered in your own words.
  Do not copy the slide. Translate it.

AFTER watching:
  Close the laptop.
  Open a terminal or text editor.
  Re-type the code shown — WITHOUT looking.
  Failed? Glance briefly, close it, try again.
  Succeeded? Add one modification. Change one parameter. Break it deliberately.

OBSIDIAN ENTRY:
  Add one daily note entry:
    - Concept name
    - What it is (1 sentence)
    - Where it appears in WOSRI (1 sentence + file reference)
    - One question it raises
```

This process takes more time than passive watching. It also produces actual retention.

---

## The Speed Rule

| Content type | Watch speed |
|-------------|-------------|
| Introduction / overview sections | 1.75x – 2x |
| Concept explanation (no code) | 1.5x |
| Code walkthrough | 1x — pause and type |
| Theory you've already seen | 2x |
| Anything about agents, evaluation, or MCP | 1x — this is your core domain |

---

## What "Completing a Section" Means

A section is complete when ALL of the following are true:

- [ ] You watched it (at appropriate speed)
- [ ] You typed out the code from memory
- [ ] You can explain the concept out loud in 60 seconds without notes
- [ ] You made one Obsidian entry connecting it to WOSRI
- [ ] You added one item to your confidence checklist

Finishing the video is not completing the section.

---

## Weekly Course Rhythm

Each week, complete:
- **3–4 course sections** (not individual videos — sections)
- **1 Python accelerator exercise** (separate from course material)
- **1 WOSRI connection note** in Obsidian
- **1 project milestone** (Weeks 5–12)

If you fall behind on video content, that is recoverable.
If you fall behind on practice and notes, that is not. The video is useless without the output.

---

## Section Completion Log (use in Obsidian or PROGRESS.md)

```
Core Track:
  [ ] LLM Fundamentals
  [ ] Embeddings
  [ ] RAG Pipeline
  [ ] Prompting Techniques
  [ ] Agents Basics
  [ ] QLoRA / Fine-tuning (optional)
  [ ] Advanced Agents

Agentic Track:
  [ ] Agent Foundations
  [ ] Tool Calling
  [ ] ReAct Pattern
  [ ] Multi-Agent Systems
  [ ] MCP Protocol
  [ ] Agent Memory & State
  [ ] Agent Evaluation
  [ ] Human-in-the-Loop
  [ ] Production Agents

Production Track:
  [ ] LLM API at Scale
  [ ] Caching Strategies
  [ ] Deployment Basics
  [ ] Monitoring & Observability
  [ ] Evaluation in Production
  [ ] Cost Optimisation
```

---

*Source: Honest Assessment → curriculum/my_knowledge_map/honest_assessment.md*
*WOSRI Architecture → RI_ASSISTANT_WORKSPACE_MAP.md*
