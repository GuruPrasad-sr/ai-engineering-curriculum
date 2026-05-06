---
tags: [gap-analysis, skills, career, updated]
generated: 2026-04-29
revised: 2026-05-06
source: honest_assessment.md v2 + impact reports 2023-2025 + 3-month master plan
---

# Skill Gap Report — AI Engineering Career Progression

> **Revision notice (2026-05-06):** This report was originally generated on 2026-04-29
> based on WOSRI context only. It has been fully rewritten to reflect:
> 1. Three years of WOS work (2023–2025) that was absent from the original
> 2. The corrected skill ratings in `honest_assessment.md` v2
> 3. The 3-month master plan (not the original 1-month sprint)
>
> The original report listed Python as "STRONG — table stakes" and TypeScript as
> a practitioner skill based on wrong evidence. Both have been corrected.
>
> **Primary source of truth:** `my_knowledge_map/honest_assessment.md`
> **Active learning plan:** `3_month_master_plan/MASTER_CURRICULUM.md`

---

## Section 1: What You Already Know (Honest Ratings + Evidence)

These are skills where evidence exists from actual work output.

| # | Skill | Rating | Evidence |
|---|-------|--------|---------|
| 1 | **E2E Test Automation (Playwright + Cucumber)** | 4/5 | 3 years, `wos-e2e-smoketests`, 6 collections built from zero, 80+ PRs |
| 2 | **BDD / Gherkin / Cucumber authorship** | 4/5 | Hundreds of feature files authored independently across 3 repos |
| 3 | **Accessibility testing (WCAG)** | 4/5 | 9 WCAG violations fixed in production Angular/CSS; nightly build configured; WPP suite built from scratch |
| 4 | **Page Object Model** | 4/5 | Full locator standardisation across `wos-e2e-smoketests` page objects — user's own work |
| 5 | **Manual AI agent testing** | 4/5 | 4 months, 4 WOSRI agents (Impact, Collaboration, Funding, Emerging Topics) |
| 6 | **LLM non-determinism (understanding)** | 4/5 | DDA findings 1 & 5 — correct distinction between reproducible bugs and LLM variance |
| 7 | **AI-assisted system design** | 4/5 | Playwright Agents POC (3-agent architecture), DDA framework (222-line prompt), Copilot Healer |
| 8 | **CI/CD (configuration)** | 3.5/5 | Accessibility Nightly Build set up; Jenkins hang fixed; error handling added; email routing configured |
| 9 | **Git** | 3.5/5 | 80+ PRs merged across 3 repos over 3 years |
| 10 | **Functional QA / ticket execution** | 4.5/5 | 3 years WOS + 4 months WOSRI — consistent ticket-to-done workflow across both products |
| 11 | **TypeScript** | 3.5/5 | 3 years independent Playwright authorship; CSS/Angular fixes shipped to production |
| 12 | **Structured prompt design** | 3.5/5 | `DDA prompt.txt` — 222 lines, role/tasks/constraints/format. Above-average prompt engineering. |
| 13 | **Context provision for AI tools** | 3.5/5 | `RI_ASSISTANT_WORKSPACE_MAP.md`, skill files, prompt library, DDA framework context |
| 14 | **Documentation** | 3.5/5 | Impact reports, workspace map, DDA prompt, architecture comparisons, Jira tickets |
| 15 | **Exploratory testing of AI systems** | 3.5/5 | 4 months of WOSRI agent failure pattern knowledge |
| 16 | **REST API testing** | 2.5/5 | ListBLC API automation built from scratch; delete search history bug fixed |

**Total: 16 skills with evidence. Python and formal AI evaluation frameworks are the primary gaps.**

---

## Section 2: What You Partially Know (Real Gaps)

| # | Skill | Current Level | What You've Done | What's Missing |
|---|-------|--------------|-----------------|----------------|
| 1 | **Python** | 1.5/5 | Reads AI-generated Python, directed DDA framework build | Cannot author Python scripts independently. All DDA code was AI-generated. WOS work was TypeScript. **This is the #1 gap.** |
| 2 | **Formal LLM Evaluation Frameworks** | 1.5/5 | Built DDA (custom), aware of DeepEval/RAGAS names | Has not installed or run DeepEval, RAGAS, or TruLens |
| 3 | **Agent orchestration (implementation)** | 2/5 | Tests conductor thoroughly, reads conductor code | Has not built an orchestrator — doesn't know LangGraph internals |
| 4 | **RAG pipeline (implementation)** | 2/5 | Understands RAG conceptually from WOSRI testing | Has not built a retrieval + augmentation + generation system |
| 5 | **Statistical evaluation methods** | 1.5/5 | Uses pass/fail thresholds | No confidence intervals, Cohen's kappa, or significance testing |
| 6 | **MCP (Model Context Protocol)** | 2/5 | Knows `agai-api` uses MCP, has not configured it | Has not built an MCP server or defined tool schemas |
| 7 | **LLM API configuration** | 2/5 | Calls agents via existing interfaces | Has not directly tuned temperature, top_p, or compared model behaviours |
| 8 | **Vector databases** | 1.5/5 | Knows they exist in WOSRI stack | No hands-on implementation |
| 9 | **Structured outputs / Pydantic** | 2/5 | Tests structured outputs from agents | Has not defined JSON schemas or Pydantic models from scratch |
| 10 | **Observability / monitoring for LLMs** | 2/5 | Built DDA reports, aware of monitoring concepts | Has not instrumented an LLM system with production-grade metrics |

---

## Section 3: What to Learn (By Role Target)

### Stage 1: AI Validation Engineer — Months 1–2 (Weeks 1–8)

| # | Skill | Priority | Why | Course/Resource | Weeks |
|---|-------|----------|-----|-----------------|-------|
| 0 | **Python 1.5 → 3.5/5** | CRITICAL | Gates every other skill. Every AI framework is Python. | `PYTHON_ACCELERATOR.md` — parallel track | 1–12 |
| 1 | **LLM Fundamentals (tokens, inference, temperature)** | HIGH | Formal vocabulary for things you already see in WOSRI daily | Core Track — Section 1 (Weeks 1–2) | 1–2 |
| 2 | **Agent architecture + tool calling + MCP** | HIGH | Direct clarity on what you test every day | Agentic Track — all of it (Weeks 3–6) | 3–6 |
| 3 | **Formal Evaluation Frameworks (DeepEval/RAGAS)** | HIGH | Translates DDA custom work into industry vocabulary | Agentic Track eval sections + Stage 1 curriculum | 7–8 |
| 4 | **Red teaming / adversarial evaluation** | MEDIUM | Career differentiator; extends your existing guardrail testing | Core Track prompting sections + Anthropic guide | 7–8 |

**Stage 1 total: ~Weeks 1–8**

### Stage 2: AI Systems Engineer — Months 2–3 (Weeks 7–12)

| # | Skill | Priority | Why | Course/Resource | Weeks |
|---|-------|----------|-----|-----------------|-------|
| 5 | **RAG pipeline (build one)** | HIGH | Most-demanded AI engineering skill; you only test it now | Core Track RAG sections (Weeks 7–9) | 7–9 |
| 6 | **Structured outputs / Pydantic** | HIGH | Language of all AI frameworks; needed for Python track | Python Accelerator Week 9 + Core Track | 9–10 |
| 7 | **LLMOps / production patterns** | MEDIUM | Cost, reliability, monitoring — needed for senior roles | Production Track (Weeks 10–12) | 10–12 |
| 8 | **Observability for LLM systems** | MEDIUM | Extends DDA dashboard work; directly applicable | Production Track monitoring sections | 11–12 |

**Stage 2 total: ~Weeks 7–12**

### Stage 3: Full AI Engineer — Months 4–8 (After this curriculum)

| # | Skill | Priority | Why | Resource |
|---|-------|----------|-----|---------|
| 9 | **LangGraph / agent orchestration frameworks** | HIGH | Builds what you currently only test | LangGraph tutorial |
| 10 | **Statistical evaluation methods** | MEDIUM | Rigour beyond thresholds | Chip Huyen — Designing ML Systems |
| 11 | **Fine-tuning LLMs (QLoRA)** | MEDIUM | Core Track remainder | Core Track QLoRA sections |
| 12 | **AI Safety frameworks (NIST AI RMF)** | MEDIUM | Enterprise AI compliance | NIST AI RMF playbook |
| 13 | **Embedding models + vector DBs** | LOW-MEDIUM | Deeper RAG expertise | Pinecone/Weaviate docs |

---

## Section 4: Industry Demand Analysis (2025–2026)

| Rank | Skill | Demand Signal | Your Status |
|------|-------|--------------|-------------|
| 1 | **LLM Evaluation (RAGAS, DeepEval, custom)** | 85% of postings | **STRONG foundation** — DDA framework; needs formal framework exposure |
| 2 | **Python (pytest, FastAPI)** | Table stakes | **GAP — developing. Currently 1.5/5, target 3.5/5 by Month 3** |
| 3 | **Agent/Tool-Use Testing** | 60% of new postings | **STRONG** — 4 months WOSRI, daily agent testing |
| 4 | **RAG Pipeline (build + evaluate)** | 70% of AI engineer postings | **GAP** — conceptual only, needs implementation |
| 5 | **Playwright / E2E automation** | 45% of QA-adjacent AI roles | **STRONG** — 3 years, 6 collections, independent authorship |
| 6 | **Accessibility (WCAG)** | Growing compliance requirement | **STRONG and rare** — 9 production fixes, nightly build, WCAG by number |
| 7 | **LangChain / LangGraph** | 50% of AI engineer postings | **GAP** — not yet used |
| 8 | **CI/CD for test automation** | 45% of postings | **STRONG** — nightly builds, Jenkins configuration, GitHub Actions |
| 9 | **Prompt Engineering** | 75% of postings | **STRONG** — DDA prompt, prompt library, context engineering |
| 10 | **Statistical Evaluation Methods** | 40% of postings | **GAP** — thresholds only |

---

## Section 5: Priority Matrix — What Unlocks the Most Career Value

### The 3-Month Pareto

| Priority | Skill | Weeks | Why This First | Owner Doc |
|----------|-------|-------|---------------|-----------|
| **P0** | Python 1.5 → 3.5/5 | 1–12 (parallel) | Without Python, every AI engineering tool is inaccessible. You have the programming instincts from TypeScript — transfer them. | `PYTHON_ACCELERATOR.md` |
| **P1** | LLM Fundamentals + Agent Architecture | 1–6 | Foundation vocabulary + immediate WOSRI clarity. The Agentic Track alone is worth the 3 courses. | `MASTER_CURRICULUM.md` Weeks 1–6 |
| **P2** | Formal Evaluation Frameworks | 7–8 | Translates what DDA does informally into what interviewers recognise. | `MASTER_CURRICULUM.md` Week 8 |
| **P3** | RAG Pipeline (build it) | 7–9 | Most-demanded missing skill. The understanding is there from testing — now build one. | `MASTER_CURRICULUM.md` Weeks 7–9 |
| **P4** | Production patterns (cost, monitoring) | 10–12 | Rounds out the AI Validation → AI Systems gap. | `MASTER_CURRICULUM.md` Weeks 10–12 |

**The honest 3-month outcome:** You will not be an AI Engineer. You will be a credible,
interview-ready AI Validation Engineer with a Python foundation and 4 shipped projects.
That is the correct and realistic target.

---

## Section 6: What You Can Claim Now (Honest Interview Framing)

| Claim | Honest Framing |
|-------|---------------|
| E2E automation | "3 years Playwright + Cucumber on Web of Science — 6 collections built from scratch, 80+ PRs, independent authorship" |
| Accessibility | "Built and maintained accessibility automation for WOS; shipped 9 WCAG fixes directly to production in Angular/CSS; established nightly accessibility pipeline" |
| AI agent testing | "4 months functional QA on a production multi-agent AI system — 4 agents, daily ticket flow. I understand LLM non-determinism in ways most QA engineers don't." |
| DDA framework | "Designed requirements for a data validation framework via a 222-line structured prompt, directed AI to build it, validated the output, used it to produce root cause analysis with 7 findings" |
| AI tooling | "Designed a 3-agent Playwright system (Planner → Generator → Healer) and a standalone Copilot locator healer utility — AI-assisted builds I planned and directed" |
| Python | "Python is a current growth area. I am building it alongside AI engineering study." (Do not claim more.) |

---

## Section 7: Gap-to-Role Map

```
CURRENT STATE                  MONTH 1-2                    MONTH 3                      MONTHS 4-8
─────────────                  ─────────                    ───────                      ──────────
QA Engineer                    AI Validation                AI Systems                   Full AI Engineer
(WOS + WOSRI)          ──►     Engineer              ──►    Engineer              ──►    (Eval & Safety)

STRONG NOW:                    ADD:                         ADD:                         ADD:
✅ Playwright/TS 3.5/5         📚 LLM vocabulary            🔧 RAG (build)               🧠 LangGraph
✅ BDD/Cucumber 4/5            📚 Agent architecture        🔧 Pydantic/structured out   🧠 Statistical eval
✅ Accessibility 4/5           📚 MCP protocol              🔧 Production patterns       🧠 Fine-tuning
✅ AI agent testing 4/5        📚 DeepEval/RAGAS             🔧 LLMOps basics             🧠 AI Safety
✅ CI/CD config 3.5/5          🐍 Python: 1.5→2.5/5         🐍 Python: 2.5→3.5/5        🐍 Python: 3.5→4/5
✅ Prompt design 3.5/5

GAP:                           Active plan:
❌ Python 1.5/5                3_month_master_plan/
❌ Formal eval frameworks      MASTER_CURRICULUM.md
❌ RAG implementation
❌ LangGraph/LLMOps
```

---

*Revised: 2026-05-06 | Source: honest_assessment.md v2 + IMPACT_REPORT_2023_2025.md*
*Active learning plan: curriculum/3_month_master_plan/MASTER_CURRICULUM.md*
*Supersedes the 1-month sprint plan from 2026-04-29*
