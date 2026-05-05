---
tags: [timetable, schedule, daily, routine]
created: 2026-05-05
status: active
---

# Daily Timetable — Optimised for AI Engineering Study

> **Design principles:**
> 1. Every session produces a concrete output — not "I studied for 2 hours" but "I built X"
> 2. Spaced repetition is built in — each day reviews yesterday before going forward
> 3. Python is a separate track — never sacrificed for course content
> 4. Friday is always integration + review — no new content
> 5. Sunday is always project work — no new content
> 6. Flexibility rules: life happens. The catch-up protocol is at the bottom.

---

## Weekday Block — 2 Hours

```
┌─────────────────────────────────────────────────────────┐
│  TIME     │  ACTIVITY                       │  OUTPUT   │
├─────────────────────────────────────────────────────────┤
│  0:00–0:05│  Yesterday review               │  1 recall │
│           │  Open Obsidian daily note        │           │
│           │  Read what you wrote yesterday   │           │
│           │  Try to recall it without looking│           │
├─────────────────────────────────────────────────────────┤
│  0:05–0:35│  Course content (30 min)        │  Notes    │
│           │  1–2 lectures at correct speed   │           │
│           │  Pause every 10 min, write notes │           │
│           │  No passive watching             │           │
├─────────────────────────────────────────────────────────┤
│  0:35–1:15│  Hands-on practice (40 min)     │  Code file│
│           │  Close the laptop screen         │           │
│           │  Retype the code from memory     │           │
│           │  Fail → peek briefly → try again │           │
│           │  Succeed → modify one thing      │           │
├─────────────────────────────────────────────────────────┤
│  1:15–1:45│  Python accelerator (30 min)    │  Exercise │
│           │  That week's Python exercise     │           │
│           │  No AI writing the code          │           │
│           │  Write, break, fix               │           │
├─────────────────────────────────────────────────────────┤
│  1:45–1:55│  Obsidian daily note (10 min)   │  Note     │
│           │  1 concept in your own words     │           │
│           │  1 WOSRI connection (file ref)   │           │
│           │  1 thing still unclear           │           │
├─────────────────────────────────────────────────────────┤
│  1:55–2:00│  Preview (5 min)                │  Question │
│           │  Read tomorrow's lecture title   │           │
│           │  Write 1 question you expect it  │           │
│           │  to answer                       │           │
└─────────────────────────────────────────────────────────┘
```

**Non-negotiable output per weekday session:**
- 1 Obsidian daily note entry
- 1 code file (even 10 lines)
- 1 Python exercise (partial counts — write as far as you can)

---

## Friday Block — 2 Hours (Review Only — No New Content)

```
┌─────────────────────────────────────────────────────────┐
│  TIME     │  ACTIVITY                       │  OUTPUT   │
├─────────────────────────────────────────────────────────┤
│  0:00–0:30│  Week review                    │  Notes    │
│           │  Read all 4 daily notes          │           │
│           │  What did you study Mon–Thu?     │           │
│           │  What can you recall now?        │           │
├─────────────────────────────────────────────────────────┤
│  0:30–1:00│  WOSRI integration task         │  Task done│
│           │  Apply week's concept to WOSRI   │           │
│           │  See WORK_INTEGRATION.md: Week X │           │
│           │  Friday column                   │           │
├─────────────────────────────────────────────────────────┤
│  1:00–1:30│  Confidence checklist review    │  Checked  │
│           │  Go through that week's          │           │
│           │  confidence checklist            │           │
│           │  Be honest — don't tick if       │           │
│           │  you're not sure                 │           │
├─────────────────────────────────────────────────────────┤
│  1:30–2:00│  Weekly Obsidian note           │  Entry    │
│           │  5 things I understand now       │           │
│           │  that I didn't on Monday         │           │
│           │  1 thing I'm going to revisit    │           │
│           │  next week                       │           │
└─────────────────────────────────────────────────────────┘
```

---

## Saturday Block — 3–4 Hours (Deep Work)

```
┌─────────────────────────────────────────────────────────┐
│  TIME     │  ACTIVITY                       │  OUTPUT   │
├─────────────────────────────────────────────────────────┤
│  0:00–0:10│  Weekly goal check              │  Focus    │
│           │  Read MASTER_CURRICULUM.md       │           │
│           │  What is this week's milestone?  │           │
│           │  Are you on track?               │           │
├─────────────────────────────────────────────────────────┤
│  0:10–1:10│  Deep dive (60 min)             │  Notes    │
│           │  Rewatch 1 key section at 1x     │           │
│           │  The section most relevant to    │           │
│           │  your WOSRI work this week       │           │
│           │  Write comprehensive notes       │           │
├─────────────────────────────────────────────────────────┤
│  1:10–2:40│  Build something (90 min)       │  Project  │
│           │  Apply the week's concept        │           │
│           │  See WORK_INTEGRATION.md         │           │
│           │  Saturday column for guidance    │           │
│           │  Must produce a working output   │           │
├─────────────────────────────────────────────────────────┤
│  2:40–3:10│  Scenario question practice     │  Answers  │
│           │  Pick 3 questions from           │           │
│           │  SCENARIO_QUESTION_BANK.md       │           │
│           │  Write answers — not mentally    │           │
│           │  rehearse, actually write        │           │
├─────────────────────────────────────────────────────────┤
│  3:10–3:40│  Python accelerator (30 min)    │  Exercise │
│           │  Continue that week's exercise   │           │
│           │  Aim for completion today        │           │
├─────────────────────────────────────────────────────────┤
│  3:40–4:00│  Weekly plan for next week      │  Plan     │
│           │  Open MASTER_CURRICULUM.md       │           │
│           │  Read next week's schedule       │           │
│           │  Set up Obsidian note template   │           │
└─────────────────────────────────────────────────────────┘
```

---

## Sunday Block — 3–4 Hours (Project + Application)

```
┌─────────────────────────────────────────────────────────┐
│  TIME     │  ACTIVITY                       │  OUTPUT   │
├─────────────────────────────────────────────────────────┤
│  0:00–0:10│  Sunday intent                  │  Clarity  │
│           │  What are you building today?    │           │
│           │  Write: "Today I will ship X"    │           │
│           │  Not "I will try to do X"        │           │
├─────────────────────────────────────────────────────────┤
│  0:10–2:10│  Project work (2 hours)         │  Code     │
│           │  See WORK_INTEGRATION.md         │           │
│           │  Sunday column for that week     │           │
│           │  This is the project milestone   │           │
│           │  for the week                    │           │
├─────────────────────────────────────────────────────────┤
│  2:10–2:40│  Work application (30 min)      │  Tests    │
│           │  Write or improve 2 WOSRI test   │           │
│           │  cases using week's concept      │           │
│           │  Commit them to the test repo    │           │
├─────────────────────────────────────────────────────────┤
│  2:40–3:10│  Retrospective (30 min)         │  Entry    │
│           │  Obsidian weekly retrospective:  │           │
│           │  What was hard? What was easy?   │           │
│           │  What would I do differently?    │           │
│           │  What did I ship this week?      │           │
├─────────────────────────────────────────────────────────┤
│  3:10–3:30│  Push everything to GitHub      │  Commits  │
│           │  Code, notes, curriculum updates │           │
│           │  git add, commit, push           │           │
└─────────────────────────────────────────────────────────┘
```

---

## Weekly Hours Summary

| Day | Duration | Type |
|-----|----------|------|
| Monday | 2 hrs | New content + practice |
| Tuesday | 2 hrs | New content + practice |
| Wednesday | 2 hrs | New content + Python |
| Thursday | 2 hrs | New content + practice |
| Friday | 2 hrs | Review + WOSRI integration |
| Saturday | 3–4 hrs | Deep dive + project build |
| Sunday | 3–4 hrs | Project + application + retro |
| **Total** | **16–18 hrs** | |

This is above the average self-study commitment and below the point of burnout.
It is sustainable only if weekday sessions are protected. 2 hours is not negotiable downward.
If a weekday session is missed, see catch-up protocol below.

---

## Rules for Maximum Efficiency

**Rule 1: Start with output, not input.**
Before opening Udemy, write what you expect to get out of today's session.
One sentence. This primes your brain to filter for relevant information.

**Rule 2: Close the video before you code.**
Do not watch and code simultaneously. Watch. Then close. Then try.
Simultaneous watching produces the illusion of understanding.

**Rule 3: Never skip the Obsidian entry.**
The Obsidian entry is not documentation. It is the actual learning moment.
Writing forces you to construct understanding, not just receive it.
If you skip it, you did not learn today — you consumed content today.

**Rule 4: Python is non-negotiable.**
The Python track is 25–30 min, not 2 hours. There is no valid excuse to skip it.
If you skip Python for 3 days, you will not reach 3.5/5 in 12 weeks.

**Rule 5: Friday has no new content.**
Friday is only for review and integration. Never watch new lectures on Friday.
The brain needs processing time. Friday gives it.

**Rule 6: Sunday ships something.**
Every Sunday, something gets committed to GitHub.
Not "I made progress." A file, a script, a test case, a note with file references.
Something that exists and can be pointed to.

---

## Catch-Up Protocol

**Missed 1 weekday session:**
- Add 30 min to Saturday or Sunday
- Do not try to cover two days in one — pick the more important lecture

**Missed 2 weekday sessions:**
- Saturday covers the missed practice
- Drop the Saturday deep dive for that week
- Sunday covers the missed Python exercise

**Missed a full week:**
- Do not try to catch up on content — you will create a backlog spiral
- Instead: do one Saturday session covering the week's most important concept only
- Skip the Python exercise for that week
- Resume the normal schedule the following Monday
- Mark the missed week as "partial" in PROGRESS.md

**Rule: never skip the Obsidian entry, even if you only studied for 20 minutes.**
Even a partial session with a note beats a full session with no output.

---

## Session Tracker (weekly)

```
Week ___

Monday:    [ ] Complete  [ ] Partial  [ ] Missed   Note: ________________
Tuesday:   [ ] Complete  [ ] Partial  [ ] Missed   Note: ________________
Wednesday: [ ] Complete  [ ] Partial  [ ] Missed   Note: ________________
Thursday:  [ ] Complete  [ ] Partial  [ ] Missed   Note: ________________
Friday:    [ ] Complete  [ ] Partial  [ ] Missed   Note: ________________
Saturday:  [ ] Complete  [ ] Partial  [ ] Missed   Note: ________________
Sunday:    [ ] Complete  [ ] Partial  [ ] Missed   Note: ________________

Sessions completed: ___/7
Something shipped this week: [ ] Yes — what: ________________
Python exercise completed: [ ] Yes  [ ] Partial
WOSRI connection made: [ ] Yes  [ ] No
```

Copy this block into your Obsidian weekly note.

---

*3-month target: Python 3.5/5 | AI domain vocabulary: proficient | Projects shipped: 4*
*Review against: curriculum/my_knowledge_map/honest_assessment.md every 4 weeks*
