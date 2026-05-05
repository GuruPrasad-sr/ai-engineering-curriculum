---
tags: [python, accelerator, checklist, track]
created: 2026-05-05
status: active
---

# Python Accelerator Track

> **Target:** From 1.5/5 (reads with AI help) → 3.5/5 (writes scripts independently)
> **Timeline:** 12 weeks, ~25–30 min/day, parallel to course content
> **Philosophy:** Do not learn Python in the abstract. Learn the specific Python patterns
> that appear in AI engineering code. 90% of AI framework code uses the same 20 patterns.
> Master those 20 patterns first.

---

## Why This Track Exists Separately

Your current Python level: you read it, you review AI-generated code, you don't author it alone.
The 3 Udemy courses assume you can write Python. They will show code and move on.
If you cannot type out what you see and modify it, the courses become documentation you watch.
This track runs in parallel so that by Week 4, you can keep up. By Week 8, you can build.
By Week 12, you can write Project 1 (Ticket-to-Test Pipeline) without AI writing the code for you.

---

## Phase 1 — Survival Python (Weeks 1–2)

**Goal:** Read any Python script and explain what every line does. Modify small things confidently.

### Week 1 Checklist — The Absolute Basics

**Variables and Types**
- [ ] Know the 4 built-in types you'll use 90% of the time: `str`, `int`, `float`, `bool`
- [ ] Know that `dict` and `list` are the two data structures that appear everywhere
- [ ] Understand that Python uses indentation instead of braces — and why this matters
- [ ] Can declare a variable and print its type using `type()`

**Functions**
- [ ] Can write a function with parameters and a return value
- [ ] Understand `def`, `return`, and why functions exist (reuse, naming)
- [ ] Know what happens if you forget `return` (returns `None`)
- [ ] Can call a function with positional and keyword arguments

**Conditionals and Loops**
- [ ] Write `if / elif / else` without looking it up
- [ ] Write a `for` loop over a list
- [ ] Write a `while` loop with a break condition
- [ ] Understand list comprehension: `[x for x in items if condition]`

**Strings**
- [ ] Use f-strings: `f"Hello {name}, you scored {score}"`
- [ ] Know `.split()`, `.strip()`, `.lower()`, `.upper()`, `.replace()`
- [ ] Know how to check if a string contains a substring: `"word" in text`

**Week 1 Exercise:**
```python
# Write this from scratch — no AI, no looking up:
# A function that takes a paragraph of text and returns:
# - word count
# - sentence count (sentences end with . or ? or !)
# - average word length (characters)
# - the 3 most common words

def analyze_text(text: str) -> dict:
    pass  # you write the body
```
You will need this pattern constantly in AI engineering (parsing LLM responses).

---

### Week 2 Checklist — Data Structures and Files

**Dictionaries (the most important Python structure)**
- [ ] Create, read, update, delete keys in a dict
- [ ] Use `.get(key, default)` — never use `dict[key]` without a fallback in production code
- [ ] Iterate: `for key, value in my_dict.items()`
- [ ] Nested dicts: `config["agents"]["impact"]["temperature"]`
- [ ] Can explain why dict lookup is O(1) and list search is O(n)

**Lists and operations**
- [ ] `.append()`, `.extend()`, `.pop()`, `.sort()`, `.index()`
- [ ] Slicing: `my_list[1:4]`, `my_list[-1]`, `my_list[::2]`
- [ ] `zip()`, `enumerate()`, `sorted()`

**File I/O**
- [ ] Open and read a text file: `with open("file.txt", "r") as f:`
- [ ] Write to a file: `with open("output.txt", "w") as f:`
- [ ] Understand why `with` exists (context manager, auto-closes file)
- [ ] Read a JSON file: `json.load(f)`
- [ ] Write a JSON file: `json.dump(data, f, indent=2)`

**Week 2 Exercise:**
```python
# Write a script that:
# 1. Opens a JSON file containing a list of test results
# 2. Calculates: pass rate, fail rate, most common failure reason
# 3. Writes a summary dict back to a new JSON file

# Sample input format (create this file yourself):
# [{"test_name": "impact_agent_basic", "status": "pass", "reason": null},
#  {"test_name": "impact_agent_long_query", "status": "fail", "reason": "timeout"}]
```
You will write code exactly like this when extending the DDA framework.

---

## Phase 2 — AI Engineering Python (Weeks 3–6)

**Goal:** Call any LLM API, process the response, save results. Write a class. Handle errors.

### Week 3 Checklist — HTTP and APIs

**The requests library**
- [ ] `pip install requests` and import it
- [ ] Make a GET request: `response = requests.get(url, headers=headers)`
- [ ] Make a POST request with JSON body: `requests.post(url, json=payload, headers=headers)`
- [ ] Read the response: `.json()`, `.text`, `.status_code`
- [ ] Check for errors: `response.raise_for_status()`
- [ ] Understand what headers are and why `Authorization: Bearer <token>` is the pattern

**Environment variables (never hardcode credentials)**
- [ ] `pip install python-dotenv`
- [ ] Create a `.env` file: `API_KEY=your_key_here`
- [ ] Load it: `from dotenv import load_dotenv; load_dotenv()`
- [ ] Read it: `import os; key = os.getenv("API_KEY")`

**Virtual environments**
- [ ] `python -m venv venv`
- [ ] Activate: `venv\Scripts\activate` (Windows)
- [ ] `pip install package` and `pip freeze > requirements.txt`
- [ ] Understand why venvs exist (dependency isolation)

**Week 3 Exercise:**
```python
# Call any free LLM API (OpenAI, Anthropic, or use agai-api if you have access)
# Send a test prompt, get a response, print:
# - The response text
# - The token count (if returned)
# - How long the call took (use time.time())
# Save the result to a JSON file with timestamp in the filename
```

---

### Week 4 Checklist — Prompt Templates and JSON Handling

**String templates for prompts**
- [ ] Understand why you never concatenate prompts with `+` (fragile and unreadable)
- [ ] Use f-strings for simple templates
- [ ] Use `string.Template` or Jinja2 for complex prompt templates
- [ ] Build a function that takes variables and returns a formatted system prompt

**JSON handling (the language of AI)**
- [ ] `json.loads(string)` — string to dict
- [ ] `json.dumps(dict)` — dict to string
- [ ] Handle missing keys safely: `.get("key", "default")`
- [ ] Parse nested JSON: agent responses often have 3-4 levels of nesting
- [ ] Handle malformed JSON: `try / except json.JSONDecodeError`

**Week 4 Exercise:**
```python
# Build a prompt template system:
# A class PromptTemplate that takes a template string with {placeholders}
# Has a .render(**kwargs) method that fills in the placeholders
# Has a .validate(**kwargs) method that checks all required fields are provided
# Write 3 templates: system_prompt, user_query, few_shot_example
# Test it with different inputs including missing fields
```

---

### Week 5 Checklist — Classes and Data Models

**Classes — why they matter for AI engineering**
- [ ] Write a class with `__init__`, instance variables, and methods
- [ ] Understand `self` — it is just the instance reference, not magic
- [ ] Use `@dataclass` from dataclasses — cleaner than manual `__init__` for data containers
- [ ] Understand `@property` — computed attributes that look like variables
- [ ] Write a class that represents a test case: scenario, steps, expected, actual, status

**Type hints**
- [ ] Add type hints to all function signatures: `def fn(name: str, score: int) -> dict:`
- [ ] Use `Optional[str]` for nullable fields: `from typing import Optional`
- [ ] Use `List[str]`, `Dict[str, Any]` for container types
- [ ] Understand that hints are documentation — Python does not enforce them at runtime

**Week 5 Exercise:**
```python
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

class TestStatus(Enum):
    PASS = "pass"
    FAIL = "fail"
    SKIP = "skip"

@dataclass
class AgentTestCase:
    # You define the fields
    # Must include: name, agent, query, expected_contains, actual, status, failure_reason
    pass

@dataclass
class TestSuiteResult:
    # A collection of AgentTestCase objects + summary stats
    # Must have methods: pass_rate(), failures(), to_json()
    pass
```

---

### Week 6 Checklist — Error Handling and Logging

**Error handling (critical for AI code — APIs fail constantly)**
- [ ] `try / except ExceptionType as e:` — catch specific exceptions, not bare `except:`
- [ ] Know the exceptions you'll hit: `requests.exceptions.Timeout`, `json.JSONDecodeError`, `KeyError`, `ValueError`
- [ ] Implement retry logic: try 3 times with 2-second wait between attempts
- [ ] Use `finally` for cleanup (closing files, logging completion)

**Logging (use logging, not print)**
- [ ] `import logging; logging.basicConfig(level=logging.INFO)`
- [ ] `logging.info()`, `logging.warning()`, `logging.error()`
- [ ] Understand why print() is not for production code (no timestamps, no levels, no file output)
- [ ] Add logging to your Week 3 API caller

**Week 6 Exercise:**
```python
# Upgrade your Week 3 API caller to be production-grade:
# - Retry 3 times on failure with exponential backoff (1s, 2s, 4s)
# - Log every attempt with timestamp and attempt number
# - Catch specific exceptions (timeout, rate limit, malformed response)
# - On permanent failure, write a failure record to a JSON file
# - On success, log the token count and response time
```

---

## Phase 3 — Independent Authorship (Weeks 7–12)

**Goal:** Write a complete working tool from requirements to shipped script.

### Week 7 Checklist — async/await

- [ ] Understand why async exists: non-blocking I/O for concurrent API calls
- [ ] Write an async function: `async def fetch_response(prompt: str) -> str:`
- [ ] Use `await` correctly: only inside `async def` functions
- [ ] Run multiple API calls concurrently: `asyncio.gather(call1(), call2(), call3())`
- [ ] Understand: async does not mean "faster per call" — it means "not waiting between calls"

**Week 7 Exercise:**
```python
# Call the LLM API 5 times concurrently with the same prompt
# Measure: total time for 5 concurrent calls vs 5 sequential calls
# This demonstrates non-determinism — 5 identical prompts, 5 different responses
# Save all 5 responses and calculate a basic similarity score
```
This exercise directly teaches you why your WOSRI DDA tests vary.

---

### Week 8 Checklist — pytest

- [ ] Write a test file: `test_my_module.py`
- [ ] Write a test function: `def test_something():`
- [ ] Use `assert` statements: `assert result == expected`
- [ ] Use `pytest.raises()` to test that errors are raised correctly
- [ ] Use `@pytest.mark.parametrize` to run one test with 10 different inputs
- [ ] Run tests: `pytest tests/ -v`
- [ ] Understand fixtures: shared setup across tests via `@pytest.fixture`

**Week 8 Exercise:**
```python
# Write pytest tests for the PromptTemplate class from Week 4:
# - Test that all placeholders are filled correctly
# - Test that missing required fields raise an error
# - Test with 5 different template inputs using parametrize
# - Test that the validator catches bad inputs
# Run: pytest -v and all tests should pass
```

---

### Week 9 Checklist — Pydantic (the language of AI frameworks)

- [ ] Understand why Pydantic exists: runtime validation of data shape
- [ ] Write a Pydantic model: `class AgentResponse(BaseModel):`
- [ ] Add field types and defaults: `field: Optional[str] = None`
- [ ] Parse a dict into a model: `AgentResponse(**response_dict)`
- [ ] Use validators: `@field_validator` for custom validation logic
- [ ] Use `.model_dump()` to convert back to dict
- [ ] Understand: LangChain, FastAPI, and most AI frameworks use Pydantic internally

**Week 9 Exercise:**
```python
# Rewrite your AgentTestCase from Week 5 using Pydantic instead of dataclass
# Add field validators:
# - status must be "pass", "fail", or "skip"
# - query cannot be empty
# - failure_reason is required when status is "fail"
# Try creating invalid instances and confirm the validation errors are helpful
```

---

### Week 10 Checklist — CLI Tools

- [ ] Use `argparse` to add command-line arguments to a script
- [ ] Add: `--input`, `--output`, `--agent`, `--verbose` flags
- [ ] Understand `nargs`, `choices`, `required`, `default`
- [ ] Print usage help: `python tool.py --help`
- [ ] Alternative: learn `click` (cleaner API, used more in modern tools)

**Week 10 Exercise:**
```python
# Turn your Week 3 API caller into a CLI tool:
# Usage: python agent_tester.py --agent impact --query "who is the top author in machine learning?" --output results.json --verbose
# The tool calls the LLM, validates the response shape, and saves the output
# --verbose flag enables detailed logging
```

---

### Weeks 11–12 — Project 1: Ticket-to-Test Pipeline

Integrate everything into a real tool. See `curriculum/projects/project_1_ticket_to_test_pipeline.md`.

The tool:
- Input: a Jira ticket description (pasted text or --ticket argument)
- Processing: structured prompt → LLM call → parse response → validate output
- Output: a `.feature` file + step definition stubs, ready to commit

**This is your Python target.** If you can build this tool independently, you are at 3.5/5.

---

## What to Learn Next (After This Track)

Once you complete the 12 weeks, these are the natural next steps in priority order:

| Next Skill | Why | How Long |
|-----------|-----|----------|
| **FastAPI** | Build APIs for your tools (connects to Production Track) | 1–2 weeks |
| **Pydantic advanced** (validators, settings) | Used in every modern Python AI service | 3–4 days |
| **LangChain / LangGraph basics** | Understand the abstractions your test targets use | 2–3 weeks |
| **pytest-asyncio** | Testing async AI code | 3–4 days |
| **httpx** | Better async HTTP client than requests | 2 days |
| **Typer** | Better CLI tool than argparse | 2 days |
| **pandas basics** | Data analysis for evaluation results | 1 week |

**Do not start these until you've completed Weeks 1–12.** Breadth before depth is why most
self-taught developers can't build anything independently.

---

## Resources (Free — No New Courses Needed)

| Resource | Use |
|----------|-----|
| [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial) | Dry but authoritative — use when something is unclear |
| [automatetheboringstuff.com](https://automatetheboringstuff.com) | Free book — practical, not theoretical |
| [realpython.com](https://realpython.com) | Best quality free tutorials for specific patterns |
| [pydantic-docs.helpmanual.io](https://docs.pydantic.dev) | When you reach Week 9 |
| OpenAI Python SDK examples on GitHub | Real-world AI engineering Python patterns |

---

## The One Rule

**Write the code. Do not have AI write it for you during practice.**

You use AI to write production code at work. During this track, write it yourself.
The goal is not to produce code. The goal is to build the mental model of how it works.
If AI writes it, you do not build the model. You stay at 1.5/5.
After you've written it yourself and it works, then you can ask AI to improve it.
That order matters.

---

*Python current level: 1.5/5 | Target: 3.5/5 | Timeline: 12 weeks*
*Honest Assessment ref: curriculum/my_knowledge_map/honest_assessment.md*
