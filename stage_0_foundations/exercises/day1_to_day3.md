# Stage 0: Exercises — Days 1 to 3

> **Approach:** Read the concept first, then do the exercise. The exercises are designed to move knowledge from "I read about it" to "I can explain it and use it."

---

## Day 1: How LLMs Work (Chapters 1.1–1.8)

### Exercise 1: Decode Your Conductor's Config

**Time:** 30 minutes

**Goal:** Read your conductor's `config.py` and identify every LLM-related parameter.

**Steps:**
1. Open `wos-ri-conductor/app/config.py`
2. Find every parameter related to LLM configuration
3. For each parameter, fill in this table:

| Parameter | Value | What it controls | Why this value was chosen |
|---|---|---|---|
| `temperature` | ? | Randomness of output | ? |
| `max_tokens` | ? | Maximum response length | ? |
| `model` | ? | Which LLM to use | ? |
| ... | ... | ... | ... |

**Success criteria:** You can explain every LLM parameter in the config to a colleague without looking anything up.

**Hint:** If you find a parameter you don't recognize, check the OpenAI API reference or the concepts chapter.

---

### Exercise 2: Temperature Experiment

**Time:** 30 minutes

**Goal:** See non-determinism in action by varying temperature.

**Steps:**
1. Write a simple Python script that calls an LLM API (OpenAI, Azure OpenAI, or whatever your workspace uses)
2. Send the SAME prompt 5 times with `temperature=0`. Record all 5 outputs.
3. Send the SAME prompt 5 times with `temperature=1.0`. Record all 5 outputs.
4. Compare.

```python
# Starter code — adapt to your API setup
import openai

client = openai.OpenAI()  # or your Azure/local setup

prompt = "List 3 benefits of automated testing."

print("=== Temperature 0 ===")
for i in range(5):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or your model
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200
    )
    print(f"Run {i+1}: {response.choices[0].message.content[:100]}...")

print("\n=== Temperature 1.0 ===")
for i in range(5):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
        max_tokens=200
    )
    print(f"Run {i+1}: {response.choices[0].message.content[:100]}...")
```

**What to observe:**
- temp=0: All 5 outputs should be identical (or nearly identical)
- temp=1.0: All 5 outputs should be noticeably different
- Both sets should be *correct* — temperature affects variety, not accuracy (usually)

**Success criteria:** You can explain to someone why temp=0 gives the same output every time and temp=1 doesn't.

---

### Exercise 3: Token Counting

**Time:** 30 minutes

**Goal:** Build intuition for token counts and costs.

**Steps:**
1. Install tiktoken: `pip install tiktoken`
2. Pick 3 different prompts from your conductor (a short one, a medium one, and a long system prompt)
3. Count their tokens and estimate costs

```python
import tiktoken

# Use the encoding for your model
enc = tiktoken.encoding_for_model("gpt-4o")

# Example prompts — replace with REAL prompts from your conductor
prompts = {
    "short": "What is the status of order 12345?",
    "medium": """You are a helpful assistant that selects the correct 
    application tool based on the user's query. Consider the intent, 
    keywords, and context.""",
    "long": "PASTE YOUR FULL SYSTEM PROMPT HERE"
}

for name, text in prompts.items():
    tokens = enc.encode(text)
    token_count = len(tokens)
    
    # Cost estimate (GPT-4o input pricing ~$2.50 per 1M tokens)
    cost_per_call = token_count * 2.50 / 1_000_000
    cost_per_1000_calls = cost_per_call * 1000
    
    print(f"\n{name}:")
    print(f"  Characters: {len(text)}")
    print(f"  Tokens: {token_count}")
    print(f"  Ratio: {len(text)/token_count:.1f} chars per token")
    print(f"  Cost per call: ${cost_per_call:.6f}")
    print(f"  Cost per 1,000 calls: ${cost_per_1000_calls:.4f}")
    
    # Show the first 20 tokens to see how text is split
    print(f"  First 20 tokens: {[enc.decode([t]) for t in tokens[:20]]}")
```

**What to observe:**
- How does the character-to-token ratio vary? (Typical: 3-4 characters per token for English)
- Look at how tokens split words — notice that common words are 1 token, rare words get split
- Calculate: if your test suite makes 500 LLM calls per run, what does it cost?

**Success criteria:** You can estimate the token count and cost of any prompt within 20% accuracy without running a tokenizer.

---

## Day 2: LLM APIs + AI System Differences (Chapters 2 & 3)

### Exercise 4: Anatomy of a Tool Prompt

**Time:** 45 minutes

**Goal:** Read one complete tool prompt in the conductor and identify every component.

**Steps:**
1. Pick one tool from the conductor (e.g., AppSelectorTool or any tool you work with frequently)
2. Find and read its complete configuration
3. Fill in this anatomy sheet:

```
TOOL ANATOMY SHEET
==================
Tool name: _______________

SYSTEM PROMPT
-------------
Full text (or location): _______________
Purpose: _______________
Key instructions: _______________
Output format instructions: _______________

USER PROMPT TEMPLATE
--------------------
Template text: _______________
Variables that get filled in: _______________
Example of a filled-in prompt: _______________

OUTPUT SCHEMA
-------------
Expected JSON structure: _______________
Required fields: _______________
Optional fields: _______________
Enum values (if any): _______________

LLM PARAMETERS
--------------
Model: _______________
Temperature: _______________
Max tokens: _______________
Other parameters: _______________

TESTING SURFACE
---------------
What could go wrong with tool selection? _______________
What could go wrong with arguments? _______________
What could go wrong with the response? _______________
How would you test each failure mode? _______________
```

**Success criteria:** You can draw the complete flow: user query → prompt assembly → LLM call → response parsing → downstream action.

---

### Exercise 5: Data Flow Diagram

**Time:** 45 minutes

**Goal:** Draw the complete data flow from user question to final response, labeling every AI concept.

**Steps:**
1. Start with a user typing a question in the UI
2. Trace the path through every layer
3. At each step, label the AI concept at play

**Template to fill in:**

```
USER types: "What's the status of order 12345?"
     │
     ▼
[UI] ──── (what happens here?)
     │
     ▼
[BFF] ──── (what happens here?)
     │
     ▼
[CONDUCTOR] 
     │
     ├─── Step 1: _____________ (what AI concept?)
     │         └── LLM call with: model=___, temp=___, tools=[___]
     │
     ├─── Step 2: LLM returns: _____________ (what is this called?)
     │
     ├─── Step 3: _____________ (what happens with the tool call?)
     │
     ├─── Step 4: Tool result → _____________ (what happens next?)
     │
     └─── Step 5: Final response → _____________ (how does it get back?)
     │
     ▼
[BFF] ──── (streaming? how?)
     │
     ▼
[UI] ──── User sees: _____________
```

**Label these concepts on your diagram:**
- [ ] Tokens (where are they counted?)
- [ ] Context window (where is it managed?)
- [ ] Temperature (where is it set?)
- [ ] System prompt (where does it live?)
- [ ] Structured output (where is the schema enforced?)
- [ ] Function/tool calling (where does the LLM decide, and where does your code execute?)
- [ ] Streaming/SSE (where does streaming happen?)
- [ ] Embeddings (are they used? where?)

**Success criteria:** Someone unfamiliar with your system could follow your diagram and understand the complete flow, including which parts are deterministic and which aren't.

---

## Day 3: Putting It All Together (Chapter 4 + Synthesis)

### Exercise 6: Failure Mode Scavenger Hunt

**Time:** 30 minutes

**Goal:** For each AI failure mode, find (or imagine) a real example in your system.

**Fill in the table:**

| Failure mode | Could this happen in your system? | Specific scenario | How would you detect it? | How would you test for it? |
|---|---|---|---|---|
| **Hallucination** | Yes/No | e.g., LLM invents an order status | | |
| **Refusal** | Yes/No | e.g., LLM refuses to process a valid query | | |
| **Format violation** | Yes/No | e.g., LLM returns text instead of JSON | | |
| **Reasoning error** | Yes/No | e.g., LLM selects wrong tool | | |
| **Instruction drift** | Yes/No | e.g., After 10 turns, stops following format | | |

**Success criteria:** You've identified at least 3 realistic failure scenarios specific to YOUR system and proposed a test for each.

---

### Exercise 7: Your AI Testing Map

**Time:** 30 minutes

**Goal:** Map your current work to the 5 types of AI testing and identify gaps.

**Steps:**
1. List all the tests/test types you currently run or maintain
2. Classify each into the 5 AI testing types
3. Identify what's missing

```
MY AI TESTING MAP
=================

UNIT TESTS (component-level)
  Currently: _______________
  Gap: _______________

INTEGRATION TESTS (API-level)  
  Currently: _______________
  Gap: _______________

BEHAVIORAL TESTS (prompt/scenario-level)
  Currently: _______________
  Gap: _______________

EVALUATION TESTS (quality measurement)
  Currently: _______________
  Gap: _______________

SAFETY TESTS (adversarial/guardrail)
  Currently: _______________
  Gap: _______________
```

**Success criteria:** You have a clear picture of what you're already doing and what you need to learn next.

---

### Exercise 8: Explain It to a Friend (The Ultimate Test)

**Time:** 30 minutes

**Goal:** Write a 1-page explanation (or voice-memo yourself) covering:

1. What is an LLM and how does it work? (3 sentences max)
2. What makes testing AI different from testing regular software? (3 key differences)
3. What do you currently do in your job that counts as AI testing? (concrete examples)
4. What's the most important thing you learned in this stage?

**The rule:** No jargon. If your non-technical friend wouldn't understand a sentence, rewrite it.

**Success criteria:** You could send this to a friend or family member and they'd understand it. If you can explain it simply, you truly understand it.

---

## Checklist: Stage 0 Complete

Before moving to Stage 1, verify:

- [ ] I can explain what tokens, context window, temperature, and embeddings are without notes
- [ ] I can read any LLM API call in my codebase and understand every parameter
- [ ] I can explain 3 ways AI testing differs from traditional testing
- [ ] I can name the 5 AI failure modes and give an example of each
- [ ] I can estimate token count and cost for a prompt
- [ ] I've drawn the complete data flow through my system
- [ ] I can explain my current work in terms of the AI testing pyramid

If all boxes are checked, you're ready for Stage 1.
