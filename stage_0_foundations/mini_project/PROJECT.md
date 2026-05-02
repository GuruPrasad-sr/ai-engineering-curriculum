# Mini-Project: LLM Behavior Analysis Report

> **Time:** 1.5-2 hours (Day 3, after exercises)
> **Purpose:** Synthesize everything from Stage 0 into one deliverable artifact.

---

## Overview

You will send the same prompt to an LLM 20 times at different parameter settings,
measure output variance, and write a structured analysis report. This is your first
real evaluation experiment — the same workflow you'll scale up throughout the curriculum.

---

## What You Will Produce

A single markdown file: `stage_0_foundations/mini_project/my_variance_report.md`
containing:

1. **Parameter Reference Card** — every LLM API parameter, what it does, your conductor's value, and why
2. **Variance Experiment Results** — raw data from 20 runs at temp=0 vs temp=1.0
3. **Statistical Analysis** — exact match rate, semantic similarity, variance quantification
4. **Conclusions** — what this means for testing AI systems

---

## Part 1: Parameter Reference Card (20 min)

Using what you learned in Chapters 1-2 and Exercise 1 (Decode Your Conductor's Config),
create a reference card for every LLM parameter used in your workspace.

### Template

```markdown
## My LLM Parameter Reference Card

| Parameter | What It Controls | Your Conductor's Value | Why This Value |
|-----------|-----------------|----------------------|----------------|
| temperature | Randomness of output | 0 | Deterministic tool selection |
| max_tokens | Maximum response length | ? | ? |
| model | Which LLM backbone | gpt_41_2025_04_14 | ? |
| top_p | Nucleus sampling threshold | ? | ? |
| response_format | Constrained output structure | json_schema | Structured tool outputs |
| ... | ... | ... | ... |
```

**Source files to reference:**
- `wos-ri-conductor/app/config.py` — main model configuration
- `agai-api/api/model_config.py` — model routing and parameters
- Any tool definition files with `response_format` settings

---

## Part 2: Variance Experiment (40 min)

### Setup

Write a Python script that:
1. Sends the SAME prompt to an LLM 20 times at `temperature=0`
2. Sends the SAME prompt 20 times at `temperature=1.0`
3. Logs every response to a JSON file

### Starter Code

```python
"""Stage 0 Mini-Project: LLM Variance Experiment."""

import json
import time
from openai import OpenAI  # or your Azure/local setup

client = OpenAI()  # adapt to your API

PROMPT = "List the top 3 benefits of automated testing for AI systems. Be concise."
MODEL = "gpt-4.1"  # or whatever model you have access to
RUNS = 20

def run_experiment(temperature: float) -> list[dict]:
    """Run the same prompt N times and collect results."""
    results = []
    for i in range(RUNS):
        start = time.time()
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": PROMPT}],
            temperature=temperature,
            max_tokens=300,
        )
        elapsed = time.time() - start
        results.append({
            "run": i + 1,
            "temperature": temperature,
            "response": response.choices[0].message.content,
            "tokens_used": response.usage.total_tokens,
            "latency_ms": round(elapsed * 1000),
            "finish_reason": response.choices[0].finish_reason,
        })
        print(f"  Run {i+1}/{RUNS} (temp={temperature}): {elapsed:.2f}s")
    return results

if __name__ == "__main__":
    print("=== Temperature 0 ===")
    temp0_results = run_experiment(0.0)

    print("\n=== Temperature 1.0 ===")
    temp1_results = run_experiment(1.0)

    all_results = {"temp_0": temp0_results, "temp_1": temp1_results}
    with open("variance_data.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\nDone. Results saved to variance_data.json")
```

### What to Measure

For each temperature setting, calculate:

| Metric | How to Calculate | What It Tells You |
|--------|-----------------|-------------------|
| **Exact match rate** | # of identical responses / 20 | How deterministic is this setting? |
| **Unique responses** | # of distinct responses / 20 | How much variety does this setting produce? |
| **Avg response length** | Mean character count | Does temperature affect verbosity? |
| **Length variance** | Std dev of character counts | How stable is output length? |
| **Token cost variance** | Std dev of token usage | How predictable are costs? |
| **Latency variance** | Std dev of response time | How predictable is performance? |

**Bonus (if you have access to an embedding model):**
- Compute pairwise cosine similarity between all 20 responses
- Report mean and min similarity — this measures **semantic** variance, not just textual

---

## Part 3: Analysis Report (30 min)

Write your findings in `my_variance_report.md` using this structure:

```markdown
# LLM Variance Analysis Report
> Stage 0 Mini-Project | [Your Name] | [Date]

## 1. Parameter Reference Card
[From Part 1]

## 2. Experiment Setup
- Model: ___
- Prompt: "___"
- Runs per setting: 20
- Settings tested: temperature=0, temperature=1.0

## 3. Results

### Temperature = 0
- Exact match rate: ___%
- Unique responses: ___/20
- Avg response length: ___ chars
- Length std dev: ___
- Avg tokens: ___
- Token std dev: ___

### Temperature = 1.0
- Exact match rate: ___%
- Unique responses: ___/20
- Avg response length: ___ chars
- Length std dev: ___
- Avg tokens: ___
- Token std dev: ___

## 4. Key Findings
1. [Finding about determinism at temp=0]
2. [Finding about variance at temp=1.0]
3. [Finding about cost/latency implications]

## 5. Implications for AI Testing
- Why fractional scoring makes more sense than pass/fail for AI systems
- Why your conductor uses temp=0 for tool selection
- What this means for test reliability and flakiness
- How many runs you'd need for statistically meaningful evaluation

## 6. Connections to My Workspace
- How this explains the non-determinism I see in conductor tests
- Why gold questions need to be run multiple times
- What this means for the evaluation framework I'll build in Stage 1
```

---

## Success Criteria

You're done when:

- [ ] Parameter reference card covers all LLM params in your workspace
- [ ] Variance experiment ran successfully (40 data points collected)
- [ ] At least 4 metrics calculated for each temperature setting
- [ ] Analysis connects findings to your daily work
- [ ] Report is clear enough that a colleague could read it and understand

---

## Why This Matters

This mini-project is the bridge between "I read about LLMs" and "I can reason about
LLM behavior empirically." Every evaluation framework you'll build in Stages 1-4
is a more sophisticated version of what you just did:

1. **Define what to measure** (you picked variance metrics)
2. **Run controlled experiments** (same prompt, different settings)
3. **Quantify results** (not "it seems random" but "exact match rate was 85%")
4. **Draw actionable conclusions** (temp=0 for reliability, temp>0 for creativity)

You just ran your first AI evaluation. The rest of the curriculum scales this up.
