---
tags: [assessment, skills, work-history, honest-review]
generated: 2026-05-02
revised: 2026-05-06
source: workspace-artifacts + impact-reports + self-correction
---

# Honest Skills & Work History Assessment (Corrected v2)

> **Revision note (v1 → v2):** The first correction fixed overclaiming on WOSRI team-built artifacts.
> This second revision adds 3 years of WOS work history (2023–2025) that was entirely absent from v1.
> As a result, TypeScript/Playwright, BDD/Cucumber, CI/CD, and accessibility were all significantly
> understated. Python remains the genuine gap. This version reflects the complete picture.
>
> **Guiding principle:** It is better to have an accurate baseline than a flattering one.
> You cannot close gaps you don't know you have.

---

## 1. Background: WOS (Jan 2023 – ~Aug 2025)

Before joining the WOSRI/RI Assistant team, you spent approximately 2.5 years on the
Web of Science product across three repos: `wos-e2e-smoketests`, `wos-nx-ui`,
`wos-restapi-automation`.

**What you built and shipped independently:**

- E2E test suites for **6 collections from zero** — Grants, WOS Cancelled Customer,
  Research Assistant, Policy Citation Index, Research Commons, WOS Publisher Portal
- **80+ PRs merged** across 3 repos over 3 years
- **9 WCAG accessibility fixes** shipped directly to production in `wos-nx-ui`
  (Angular/CSS code, real production commits with WOSAR numbers)
- Accessibility Nightly Build established — designed and configured the Jenkins pipeline
- **Playwright Agents POC** — 3-agent system (Planner → Generator → Healer) designed
  by you, built with AI assistance; reusable architecture for the whole team
- **GitHub Copilot Healer Mode** (`copilot-healer.ts`) — standalone utility designed
  and directed by you
- **Snowplow DUID validation** — parallel analytics validation pipeline with CI integration
- 30+ locator and stability fixes across all page objects
- REST API automation for ListBLC from scratch
- Jenkins pipeline fixes (hanging indefinitely, silent failures, email routing)

This is not background context. This is 3 years of production engineering output.
It establishes your real TypeScript, Playwright, BDD, accessibility, and CI/CD baseline —
none of which was visible in the v1 assessment because v1 only looked at WOSRI.

---

## 2. What You Actually Did (last ~4 months at Clarivate, WOSRI)

### Primary role: Functional QA on 4 AI agents

Your core job for the past 4 months has been moving tickets from **Ready to Test** to **Done**
for the RI Assistant product — manually and semi-automatically testing the four agents:

- Impact Evaluation agent
- Collaboration Analysis agent
- Funding Discovery agent
- Emerging Topics agent

This is exploratory testing and regression validation of an AI-powered product. You
identify whether each agent behaves correctly after development changes, raise defects,
and sign off on completions. That is meaningful QA work on a live production AI system.
Most QA engineers at this stage do not work on AI products at all.

---

### UI automation: AI-assisted test case generation

Your specific workflow for UI automation:

1. Take a Jira ticket (feature description, acceptance criteria)
2. Paste it into GitHub Copilot agent mode with enough context
3. AI generates the Playwright + Cucumber test cases
4. You review, adjust, and commit them

**What this means:** You are not writing Playwright code from scratch. You are using
AI as a code generator, providing requirements and context, and validating the output.
This is a valid and increasingly common workflow, but the skill being exercised is
**requirements communication and output validation**, not Playwright proficiency.

---

### The DDA (Daily Data Analytics) Testing Framework

This is the one thing you built — and the correction is important: you built it
**with AI**, not alone, and not without contribution. Here is what actually happened:

**What you did:**
- Wrote `DDA prompt.txt` — a 222-line structured system prompt defining the
  architecture, requirements, quality standards, and output expectations for the
  entire framework
- Directed GitHub Copilot Agent Mode through a 4,014-line conversation to generate
  the framework code, iterating until it met your requirements
- The resulting `dda_framework/` is a real, layered Python framework with 9 modules:
  clients, comparison, execution, models, parsers, reporting, validators, CLI
- You ran it, got reports (`dda_validation_20260428_050745.html`), and used the
  results to produce real analysis (LLM non-determinism vs. true bugs, 7 root cause findings)

**What the AI did:**
- Wrote all the Python code
- Explored the codebase to understand context
- Produced the layered architecture

**The honest framing:** You were the **architect and product manager**. The AI was
the **developer**. You defined what good looked like, held the AI to that standard,
and verified the output worked. This is a real skill — it is just not "I wrote Python."

The `DDA prompt.txt` specifically is worth keeping. It shows you can structure a
complex engineering problem clearly enough for AI to implement it. That document
has: role definition, business context, 9 ordered tasks, explicit quality bar, output
format requirements, and domain-specific constraints. That is not basic prompting.

---

## 3. Technical Skills (Honest — Full Picture)

> **Scale:** 5 = Builds independently | 4 = Proficient with reference | 3 = Working
> knowledge | 2 = Familiar / AI-assisted | 1 = Exposure only

---

### Core Testing Skills

| Skill | Rating | Honest Assessment |
|-------|--------|------------------|
| **E2E test automation (Playwright + Cucumber)** | 4/5 | 3 years authoring Playwright feature files independently across `wos-e2e-smoketests`. Built 6 full E2E suites from zero. Refactored page objects and locators across the entire suite. This is genuine independent authorship, not AI-generated output reviewed. |
| **BDD / Gherkin / Cucumber** | 4/5 | Hundreds of feature files authored from scratch over 3 years — scenario outlines, backgrounds, step definitions, tag strategies. Reviewed and extended AI-generated feature files on WOSRI. Can author and review with equal confidence. |
| **Accessibility testing (WCAG)** | 4/5 | Deep practical skill built across 2024–2025. Identified and fixed 9 WCAG violations in production Angular code. Established and configured the Accessibility Nightly Build. Built the WPP accessibility suite from scratch. Knows WCAG criteria by number (2.4.4, 4.1.2, 1.3.1, etc.). |
| **Manual AI agent testing** | 4/5 | 4 months on WOSRI, 4 agents, real production system. Knows how the agents behave, what breaks them, and when a failure is LLM variance vs. a real bug. Most QA engineers do not work on AI products at all. |
| **Functional QA / ticket execution** | 4.5/5 | 3 years + 4 months of consistent ticket-to-done workflow across two very different products (traditional web app and AI agent system). |
| **LLM non-determinism (understanding)** | 4/5 | DDA analysis findings 1 and 5 show correct distinction between reproducible bugs and LLM variance. Rare practical knowledge. |
| **Exploratory testing of AI systems** | 3.5/5 | Knows where agents fail — off-topic refusals, entity normalisation edge cases, multi-turn context loss. Hard-won from 4 months on WOSRI. |
| **Page Object Model** | 4/5 | 3 years refactoring and maintaining page objects across `wos-e2e-smoketests`. Standardised locator naming conventions across the entire suite. This is the user's own work, not a team artifact. |
| **REST API testing** | 2.5/5 | Built ListBLC API automation from scratch. Fixed API automation bugs. Has not written complex API test suites independently — this is the ceiling. |

---

### AI & Tooling Skills

| Skill | Rating | Honest Assessment |
|-------|--------|------------------|
| **AI-assisted system design** | 4/5 | Designed the Playwright Agents POC (Planner → Generator → Healer architecture), the DDA framework requirements (222-line prompt), and the Copilot Healer strategy. AI wrote the code; you designed what to build and held it to quality. This is a real and distinct skill. |
| **Structured system prompt design** | 3.5/5 | `DDA prompt.txt` (222 lines) — role, context, ordered tasks, quality bar, constraints, output format. A senior engineer would recognise this as intentional architecture. |
| **Context provision for AI** | 3.5/5 | `RI_ASSISTANT_WORKSPACE_MAP.md`, skill files, prompt libraries. You understand that AI tools produce better output with better context, and you act on this understanding consistently. |
| **Conversational AI usage** | 3/5 | Clear goals, adequate context, identifies and corrects AI errors. Does not apply formal prompt structure to everyday requests — informal but effective. |
| **Recognising AI output errors** | 3.5/5 | Caught overclaims in the v1 assessment, identified incorrect test generations on WOSRI, corrected DDA outputs. Critical evaluation applied consistently. |

---

### Programming Languages

| Skill | Rating | Honest Assessment |
|-------|--------|------------------|
| **TypeScript / Playwright** | 3.5/5 | 3 years of independent authorship in `wos-e2e-smoketests`. Can write Playwright selectors, step definitions, page objects, and scenario outlines without AI help. Can read and modify Angular/CSS code (9 production fixes in `wos-nx-ui`). The AI-generated workflow on WOSRI was a deliberate efficiency choice, not a capability ceiling. |
| **Python** | 1.5/5 | **The real gap.** You read Python and understand what it does. You use AI to write it. You have not authored production Python independently. The DDA framework code was entirely AI-generated. No WOS work was Python. This needs to be fixed — that is what the Python track is for. |
| **YAML** | 3/5 | Authored test files extensively in WOS context. Worked with existing WOSRI YAML DSL. Did not design the WOSRI DSL but is proficient in using and extending YAML structures. |
| **Java / REST-Assured** | 1/5 | Exposure only. |

---

### Software Engineering

| Skill | Rating | Honest Assessment |
|-------|--------|---------------------|
| **CI/CD (configuration and maintenance)** | 3.5/5 | Set up the Accessibility Nightly Build from scratch. Fixed Jenkins hanging indefinitely. Added error handling to pipeline build stages. Configured email routing by squad. This is pipeline authorship, not just triggering runs. |
| **Git** | 3.5/5 | 80+ PRs merged across 3 repos over 3 years. Consistent commit discipline, merge conflict resolution, branch management. Evidence is the git log itself. |
| **Systems understanding (WOSRI)** | 3.5/5 | Understands the 5-service architecture — conductor, normalizer, BFF, UI, agai-api. Knows what each service does and how they connect. Built from 4 months of testing it. |
| **Documentation** | 3.5/5 | Clear Jira tickets, DDA prompt, workspace map, impact reports, architecture comparison docs. Consistent quality across different output types. |

---

## 4. Prompting Skills Assessment — From Our Sessions

> This section looks specifically at how you interact with AI tools, using our
> conversation history as the primary evidence.

### What our conversation reveals

**1. Goal clarity:** When you asked for the curriculum, you gave a clear goal, career
direction, time constraints, and audience (yourself). You did not over-specify and
trusted the AI to make reasonable decisions. That is effective.

**2. Context calibration:** You knew to mention your specific workspace, your current
role, and what you already know. You didn't ask for a generic "learn AI" curriculum —
you asked for one grounded in your 16 repos. That shows you understand that context
is what makes AI output useful vs. generic.

**3. Error identification:** You caught and corrected a significant error in the first
assessment without being aggressive or vague. "I haven't built anything — all these
frameworks were built by somebody else" is a precise, actionable correction. That is
a skill many AI users don't have.

**4. Delegation with boundaries:** "Continue if you have next steps, or stop and ask
for clarification if you are unsure how to proceed" is a well-formed delegation
instruction. It gives autonomy within a safety net. That is above-average AI usage.

**5. What is missing:** In casual interactions you use natural language without
structure. The `DDA prompt.txt` shows you can write highly structured prompts when
you invest the effort. The gap is that you don't apply that structure to smaller,
everyday requests — which sometimes leads to AI responses that are close but not
quite right, requiring correction.

### Prompting Skill Level: Intermediate (3/5)

**Your current level:** You can formulate clear goals, provide relevant context, and
identify errors in AI output. In high-stakes situations (like the DDA prompt) you
apply structured technique effectively. In day-to-day use, you rely on natural
language and correct errors after the fact.

**What intermediate means practically:**
- You get useful output from AI most of the time
- You spend some time correcting and re-prompting
- You know domain context matters but don't always front-load it
- You can write a structured system prompt but don't do it by default

**What advancing to 4/5 looks like:**
- Applying role/context/task/constraints/format structure to everyday requests, not just big designs
- Fewer correction cycles because the first prompt is more complete
- Knowing when to use chain-of-thought, few-shot examples, and explicit output formats

---

## 5. Where You Actually Stand

**Honest one-paragraph summary:**

You are a QA Engineer with 3 years of production TypeScript/Playwright automation and
deep accessibility engineering, who spent the last 4 months testing a production
multi-agent AI system. You can write Playwright tests independently. You cannot write
Python independently — that is the actual gap and it is a specific one, not a general
coding gap. You designed two AI-assisted engineering systems (DDA framework and
Playwright Agents POC) with sufficient sophistication that a senior engineer would
recognise both as real system designs. Your understanding of how AI agents fail —
LLM variance, non-determinism, entity normalisation edge cases — is hard-won
practical knowledge most QA engineers don't have. What you are not, yet, is an
AI Validation Engineer in the formal sense (you lack framework vocabulary, statistical
methods, and red teaming depth) and you are not a Python developer. The curriculum
closes those specific gaps, not programming from scratch.

---

## 6. What the Curriculum Changes

Given this accurate baseline, here is what the 30 days actually do for you:

| Stage | What it adds |
|-------|-------------|
| **Stage 0** | Formal vocabulary for things you already see (tokens, temperature, context window) but don't have names for |
| **Stage 1** | Transforms "I know how to test AI agents" into "I can design and run a formal evaluation programme" — adds DeepEval/RAGAS vocabulary, statistical methods, red teaming |
| **Stage 2** | Teaches you to build what you currently only test — RAG, agents, orchestration — so you can discuss architecture credibly |
| **Stage 3** | Production engineering concerns (cost, safety, monitoring) that broaden you beyond testing |
| **Stage 4** | Pulls it into a portfolio artifact you can show |

The most important stage for you is **Stage 1**, because it takes your practical
agent-testing experience and gives it formal structure. You are not learning from zero
there — you are getting the academic vocabulary for things you already do.

---

## 7. What to Say in Interviews (With Integrity)

**Instead of:** "I built an LLM evaluation framework"
**Say:** "I designed the requirements and architecture for a DDA testing framework and
directed GitHub Copilot Agent Mode to build it. I validated the output and used it to
produce root cause analysis on a v0/v1 data environment migration."

**Instead of:** "I have advanced Playwright skills"
**Say:** "I have 3 years of Playwright automation across Web of Science — built E2E suites
for 6 collections from scratch, 80+ PRs merged. On my current AI product team I use
an AI-assisted workflow for test generation because it's faster, but I can author
Playwright independently."

**Instead of:** "I test AI agents"
**Say:** "I've spent 4 months doing functional QA on a production multi-agent AI system —
4 agents, daily ticket flow, and one data environment validation framework I designed
and built with AI tooling. I understand how LLM non-determinism affects test reliability
in a way most QA engineers don't."

**For WOS work:**
**Say:** "I spent 3 years building E2E and accessibility test automation for Web of Science.
I shipped 9 WCAG fixes directly to production in Angular/CSS, established a nightly
accessibility pipeline, and built a 3-agent AI system for autonomous test generation
and locator healing. My output is in the git log — 80+ PRs across 3 repos."

The last framing is completely honest and significantly stronger than generic claims.

---

*Corrected v2: 2026-05-06 | Added WOS background (2023–2025), corrected TypeScript/Playwright from 1.5/5 to 3.5/5,
added accessibility as 4/5, upgraded BDD/Cucumber to 4/5, upgraded CI/CD to 3.5/5, upgraded Git to 3.5/5.
Python remains 1.5/5 — the real and specific gap.*

*Corrected v1: 2026-05-02 | Based on: DA_ChatHistory.md (4,014 lines),
DDA prompt.txt (222 lines), dda_framework/ (66 files), conversation evidence,
direct self-correction from subject*
