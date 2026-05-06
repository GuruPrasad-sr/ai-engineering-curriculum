---
tags: [home, dashboard]
---

# AI Engineering Curriculum

> **3 months. QA Engineer → AI Validation Engineer → AI Engineer.**
> Start here every session. The active schedule is the 3-month master plan below.
> The 30-day stage files are your reference library.

---

## Active Plan — 3-Month Master Plan (Start Here)

| File | Purpose |
|------|---------|
| [[3_month_master_plan/README\|3-Month Master Plan — README]] | Day 1 action list and overview |
| [[3_month_master_plan/MASTER_CURRICULUM\|12-Week Schedule]] | Week-by-week plan with milestones, builds, and scenario questions |
| [[3_month_master_plan/COURSE_NAVIGATION\|Course Navigation]] | Watch order for 3 Udemy courses + Day 1 start instruction |
| [[3_month_master_plan/PYTHON_ACCELERATOR\|Python Accelerator]] | Parallel Python track — Week 1–12 exercises |
| [[3_month_master_plan/WORK_INTEGRATION\|Work Integration]] | Day-by-day learning ↔ WOSRI connection plan |
| [[3_month_master_plan/DAILY_TIMETABLE\|Daily Timetable]] | Session structure and time allocation |

**Course watch order:** Weeks 1–2 = Core Track (Fundamentals + Embeddings) → Weeks 3–6 = Agentic Track (all) → Weeks 7–9 = Core Track (RAG + Prompting) → Weeks 10–12 = Production Track

---

## Reference Library — 30-Day Stage Files

| Stage | Days | Hours | Files |
|-------|------|-------|-------|
| [[stage_0_foundations/README\|Stage 0: Foundations]] | 1–3 | ~7 hrs | [[stage_0_foundations/concepts\|Concepts]] · [[stage_0_foundations/live_examples\|Live Examples]] · [[stage_0_foundations/exercises/day1_to_day3\|Exercises]] · [[stage_0_foundations/mini_project/PROJECT\|Mini Project]] |
| [[stage_1_ai_validation/README\|Stage 1: AI Validation]] ⭐ | 4–14 | ~22 hrs | [[stage_1_ai_validation/concepts\|Concepts]] · [[stage_1_ai_validation/live_examples\|Live Examples]] · [[stage_1_ai_validation/exercises/week1_exercises\|Exercises]] · [[stage_1_ai_validation/mini_project/PROJECT\|Mini Project]] |
| [[stage_2_ai_systems/README\|Stage 2: AI Systems]] | 15–22 | ~16 hrs | [[stage_2_ai_systems/concepts\|Concepts]] · [[stage_2_ai_systems/live_examples\|Live Examples]] · [[stage_2_ai_systems/exercises/week3_exercises\|Exercises]] · [[stage_2_ai_systems/mini_project/PROJECT\|Mini Project]] |
| [[stage_3_ai_engineering/README\|Stage 3: AI Engineering]] | 23–28 | ~13 hrs | [[stage_3_ai_engineering/concepts\|Concepts]] · [[stage_3_ai_engineering/live_examples\|Live Examples]] · [[stage_3_ai_engineering/exercises/week4_exercises\|Exercises]] · [[stage_3_ai_engineering/mini_project/PROJECT\|Mini Project]] |
| [[stage_4_expert_capstone/README\|Stage 4: Capstone]] | 29–30 | ~5 hrs | [[stage_4_expert_capstone/concepts\|Concepts]] · [[stage_4_expert_capstone/exercises/capstone_planning\|Exercises]] · [[stage_4_expert_capstone/mini_project/CAPSTONE_SPEC\|EvalForge Spec]] |

**Reference:** [[ROADMAP\|Master Roadmap]] · [[gap_analysis/skill_gap_report\|Skill Gap Report]] · [[my_knowledge_map/informal_to_formal_mapping\|Skills Mapped]] · [[my_knowledge_map/honest_assessment\|Honest Assessment]]

---

## Stage Progress

- [ ] **Stage 0** complete (Days 1–3)
- [ ] **Stage 1** complete (Days 4–14)
- [ ] **Stage 2** complete (Days 15–22)
- [ ] **Stage 3** complete (Days 23–28)
- [ ] **Stage 4** complete (Days 29–30)

→ Detailed day-by-day tracking: [[PROGRESS]]

---

## Today's Session

> Edit this block at the start of each session, then create a daily note with `Ctrl+Shift+D`.

**Current day:** <!-- Day X of 30 -->
**Stage:** <!-- e.g. Stage 1 — AI Validation -->
**Today's chapter:** <!-- e.g. Chapter 2: LLM-as-a-Judge -->
**Time budgeted:** <!-- e.g. 1.5 hrs -->
**Goal:** <!-- One sentence: what will I be able to do after this session? -->

---

## Recent Sessions

> Sessions are auto-logged in [[daily_notes/]] — open the folder to browse.

```dataview
TABLE file.ctime AS "Date", stage AS "Stage", day_number AS "Day", time_spent AS "Time"
FROM "daily_notes"
SORT file.ctime DESC
LIMIT 7
```

*If Dataview isn't installed yet, just browse the `daily_notes/` folder directly.*

---

## Boilerplate Projects

| Project | Purpose | Location |
|---------|---------|----------|
| [[boilerplate_python_validation/README\|Python Validation Framework]] | Standalone eval harness (evaluators, runner, HTML reporter) | `boilerplate_python_validation/` |
| [[boilerplate_fullstack_ai_eval/README\|Full-Stack AI Eval Platform]] | FastAPI + Angular evaluation dashboard | `boilerplate_fullstack_ai_eval/` |

---

## Key Concepts Quick Reference

| Concept | Where it's covered |
|---------|-------------------|
| LLM internals (tokens, attention, temperature) | [[stage_0_foundations/concepts]] Ch 1–2 |
| Why AI testing ≠ traditional testing | [[stage_0_foundations/concepts]] Ch 3 |
| Evaluation taxonomy (faithfulness, relevance…) | [[stage_1_ai_validation/concepts]] Ch 1 |
| LLM-as-Judge (pointwise, pairwise, G-Eval) | [[stage_1_ai_validation/concepts]] Ch 2 |
| DeepEval, RAGAS, Promptfoo | [[stage_1_ai_validation/concepts]] Ch 3 |
| Red teaming & adversarial evaluation | [[stage_1_ai_validation/concepts]] Ch 5 |
| RAG pipeline design & evaluation | [[stage_2_ai_systems/concepts]] Ch 1 |
| Agent architecture & orchestration | [[stage_2_ai_systems/concepts]] Ch 2–3 |
| Model Context Protocol (MCP) | [[stage_2_ai_systems/concepts]] Ch 4 |
| MLOps / LLMOps | [[stage_3_ai_engineering/concepts]] Ch 1 |
| AI Safety & Guardrails | [[stage_3_ai_engineering/concepts]] Ch 4 |
| Observability & Monitoring | [[stage_3_ai_engineering/concepts]] Ch 5 |

---

*Vault synced via Git — push/pull with `Ctrl+P → Git: Commit all → Git: Push`*
*Or it auto-commits every 10 minutes if obsidian-git is installed and configured.*
