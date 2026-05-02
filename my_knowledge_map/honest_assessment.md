---
tags: [assessment, skills, work-history, honest-review]
generated: 2026-05-02
revised: 2026-05-02
source: workspace-artifacts + self-correction
---

# Honest Skills & Work History Assessment (Corrected)

> **Revision note:** The first version of this assessment was wrong. It attributed
> ownership of code and frameworks found in the workspace to you without verifying
> who actually wrote them. You correctly identified the error.
>
> **This version is based on:** What you have described doing, cross-checked against
> workspace artifacts (DDA prompt, chat history, conversation patterns in our sessions).
>
> **Guiding principle:** It is better to have an accurate baseline than a flattering one.
> You cannot close gaps you don't know you have.

---

## 1. What You Actually Did (4 months at Clarivate, WOSRI)

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

## 2. Technical Skills (Honest)

> **Scale:** 5 = Builds independently | 4 = Proficient with reference | 3 = Working
> knowledge | 2 = Familiar / AI-assisted | 1 = Exposure only

---

### Core Testing Skills

| Skill | Rating | Honest Assessment |
|-------|--------|------------------|
| **Manual AI agent testing** | 4/5 | 4 months, 4 agents, real production system. You know how these agents behave, what breaks them, and what correct output looks like. This is genuine domain knowledge. |
| **Functional QA / ticket execution** | 4/5 | Your workflow from ticket to test to done is solid. You understand acceptance criteria, can identify edge cases, and know when something is a bug vs. LLM variance. |
| **LLM non-determinism (understanding)** | 4/5 | The DDA analysis (finding 1, finding 5) shows you correctly distinguished reproducible bugs from LLM variance. Most QA engineers don't know this distinction exists. |
| **Exploratory testing of AI systems** | 3.5/5 | You know where AI agents fail — off-topic refusals, entity normalisation edge cases, multi-turn context loss. This is hard to learn from a book. |
| **BDD / Cucumber / Gherkin (reading)** | 3/5 | You read and work with feature files daily. You review AI-generated Gherkin output. You don't write it from scratch independently. |
| **Playwright (usage)** | 2/5 | You use AI-generated Playwright tests. You can read them and spot obvious errors. You have not written Playwright selectors or step definitions from scratch. |
| **API testing** | 2/5 | You understand that the BFF API exists and has contracts. You have not written REST-Assured tests or API test scenarios from scratch yourself. |

---

### AI & Prompting Skills

| Skill | Rating | Honest Assessment |
|-------|--------|------------------|
| **Structured system prompt design** | 3.5/5 | The `DDA prompt.txt` (222 lines) demonstrates real skill: role, context, ordered tasks, quality bar, constraints, output format. This is noticeably above beginner. Within your domain it is genuinely good. |
| **Conversational AI usage** | 3/5 | In day-to-day AI interactions (including our sessions) you communicate clearly in natural language, give adequate context, and can identify and correct AI errors. You do not apply formal prompt structure in conversation. Both approaches have their place. |
| **Context provision for AI** | 3.5/5 | You understand that AI tools need context to be useful. You give workspace context, ticket details, and domain knowledge. The workspace map and skill files exist partly because you understood this need. |
| **AI as code generator** | 3/5 | Your Copilot agent mode workflow (ticket → context → test cases) is effective and reproducible. The skill is in knowing what to ask for and spotting when the output is wrong. |
| **Recognising AI output errors** | 3.5/5 | You correctly identified that this assessment's first version overclaimed your skills based on workspace artifacts. That is exactly the critical evaluation skill needed when using AI. |
| **Prompt for framework design** | 3.5/5 | The DDA prompt is structured enough that a senior engineer would recognise it as intentional architecture, not improvised instructions. |

---

### Programming Languages

| Skill | Rating | Honest Assessment |
|-------|--------|------------------|
| **Python** | 1.5/5 | You can read Python and understand what it does. You use AI to write it. You have not independently written production Python from scratch. The DDA framework code was generated by AI. |
| **TypeScript / Playwright** | 1.5/5 | Same pattern. You read it, review it, don't author it independently. |
| **YAML** | 2.5/5 | You have worked with the existing YAML test DSL files. You may have added test cases by following existing patterns. You did not design the DSL. |
| **Java / REST-Assured** | 1/5 | Exposure only — you know the tests exist and what they cover. |

---

### Software Engineering

| Skill | Rating | Exposure Assessment |
|-------|--------|---------------------|
| **Systems understanding** | 3.5/5 | You understand how the 5-service architecture connects. You know what the conductor does, what the normalizer does, how SSE streaming works. This comes from 4 months of testing it. |
| **CI/CD (using)** | 2/5 | You trigger GitHub Actions runs and read results. You have not authored CI pipelines. |
| **Git** | 2/5 | You use Git for daily work (clone, pull, commit, PR). Multi-repo orchestration was a script you may have used, not written. |
| **Documentation** | 3/5 | You write clear Jira tickets, test notes, and context files. The DDA prompt is strong evidence of this. |

---

## 3. Prompting Skills Assessment — From Our Sessions

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

## 4. Where You Actually Stand

**Honest one-paragraph summary:**

You are a QA Engineer who has spent 4 months testing a production AI product, which
gives you genuine domain knowledge most QA engineers don't have. You are comfortable
directing AI tools to generate test code on your behalf, which is a real and valuable
skill. You wrote one sophisticated system prompt (DDA) that produced a working framework.
Your understanding of how AI agents fail — LLM variance, non-determinism, entity
normalisation edge cases — is hard-won practical knowledge. What you are not, yet, is
a developer of any kind (Python, TypeScript, or otherwise), and you are not an AI
Validation Engineer in the formal sense (you lack framework vocabulary, statistical
methods, and red teaming depth). The curriculum is correctly aimed at closing those
specific gaps.

---

## 5. What the Curriculum Changes

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

## 6. What to Say in Interviews (With Integrity)

**Instead of:** "I built an LLM evaluation framework"
**Say:** "I designed the requirements and architecture for a DDA testing framework and
directed GitHub Copilot Agent Mode to build it. I validated the output and used it to
produce root cause analysis on a v0/v1 data environment migration."

**Instead of:** "I have advanced Playwright skills"
**Say:** "I use AI-assisted test generation for Playwright. I provide the feature context,
review the generated test cases, and validate they match acceptance criteria."

**Instead of:** "I test AI agents"
**Say:** "I've spent 4 months doing functional QA on a production multi-agent AI system —
4 agents, daily ticket flow, and one data environment validation framework I designed
and built with AI tooling. I understand how LLM non-determinism affects test reliability
in a way most QA engineers don't."

The last framing is completely honest and significantly stronger than the others.

---

*Corrected: 2026-05-02 | Based on: DA_ChatHistory.md (4,014 lines),
DDA prompt.txt (222 lines), dda_framework/ (66 files), conversation evidence,
direct self-correction from subject*
