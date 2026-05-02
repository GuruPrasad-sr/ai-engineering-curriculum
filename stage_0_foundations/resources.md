# Stage 0: Resources — Curated Learning Materials

> Only resources from 2023-2025 that are high-quality, beginner-friendly, and still accurate. Ordered by priority within each category.

---

## Tier 1: Start Here (Essential)

### Video: Andrej Karpathy — "Intro to Large Language Models"
- **URL:** https://www.youtube.com/watch?v=zjkBMFhNj_g (Nov 2023, ~1 hour)
- **Why:** The single best first-principles explanation of LLMs by the former head of AI at Tesla. Assumes no ML background. Covers what LLMs are, how they work, where they're going.
- **Maps to:** Chapter 1 (all sections)
- **Watch time:** 1 hour. Worth every minute.

### Video: Andrej Karpathy — "Let's build GPT: from scratch, in code, in a spell"
- **URL:** https://www.youtube.com/watch?v=kCc8FmEb1nY (~2 hours)
- **Why:** If you want to go one level deeper and see a transformer built in Python. Optional but transforms your understanding.
- **Maps to:** Chapter 1 (transformers, attention)
- **Watch if:** You learn best by seeing code.

### Guide: Anthropic — Prompt Engineering Guide
- **URL:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- **Why:** The gold standard for practical prompt engineering. Written clearly, with examples. Directly applicable to your conductor work.
- **Maps to:** Chapter 2 (system prompts, structured outputs)
- **Read time:** 1-2 hours for the core sections.

### Interactive: LLM Visualization by Brendan Bycroft
- **URL:** https://bbycroft.net/llm
- **Why:** An interactive 3D visualization of how transformers process tokens. Seeing attention weights and token flow makes the abstract concrete.
- **Maps to:** Chapter 1 (transformers, attention, tokens)
- **Time:** 20-30 minutes of exploration.

---

## Tier 2: Go Deeper (Recommended)

### Guide: OpenAI Cookbook
- **URL:** https://github.com/openai/openai-cookbook
- **Why:** Practical code examples for every API feature — structured outputs, function calling, embeddings, token counting, streaming. You can copy-paste and adapt.
- **Maps to:** Chapter 2 (all sections)
- **Use as:** Reference when building exercises or exploring API features.

### Guide: OpenAI API Reference
- **URL:** https://platform.openai.com/docs/api-reference
- **Why:** The authoritative reference for every parameter in the API. When you see a parameter in your conductor's config and want to know exactly what it does, look here.
- **Maps to:** Chapter 2 (all sections)
- **Use as:** Reference manual, not reading material.

### Article: Simon Willison's Blog
- **URL:** https://simonwillison.net/ (ongoing)
- **Why:** Simon covers practical LLM topics with clarity and skepticism. His posts on prompt injection, structured output, and LLM testing are directly relevant to your work.
- **Maps to:** Chapter 3 (failure modes, prompt sensitivity)
- **Best posts to start with:** Search for "prompt injection" and "structured output"

### Guide: Google — Evaluation of Generative AI
- **URL:** https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview
- **Why:** Google's practical guide to evaluating LLM outputs — covers metrics, rubrics, and LLM-as-judge patterns.
- **Maps to:** Chapter 3 (evaluation problem)

---

## Tier 3: Optional Deep Dives

### Paper: "Attention Is All You Need" (Vaswani et al., 2017)
- **URL:** https://arxiv.org/abs/1706.03762
- **Why:** The paper that started it all. Dense and academic, but if you've read Chapter 1 first, the key figures and concepts will make sense.
- **Maps to:** Chapter 1 (transformers, attention)
- **Read if:** You want to be able to reference the original source in conversations.

### Course: fast.ai — Practical Deep Learning
- **URL:** https://course.fast.ai/
- **Why:** The most practical ML course. Top-down approach (build things first, theory later). Good if you decide to go deeper into ML fundamentals.
- **Maps to:** Beyond Stage 0 — for when you want to understand training, fine-tuning, etc.

### Newsletter: The Batch (by deeplearning.ai)
- **URL:** https://www.deeplearning.ai/the-batch/
- **Why:** Andrew Ng's weekly newsletter on AI developments. Good for staying current without drowning in noise.
- **Use as:** Weekly reading to build industry awareness.

---

## Tier 4: Your Workspace as a Learning Resource

The best learning resource is code you already work with. Here are specific files to study:

| What to study | Where to look | What you'll learn |
|---|---|---|
| LLM configuration | `wos-ri-conductor/app/config.py` | How LLM parameters are set in production |
| Tool definitions | Tool registration files in conductor | How function calling is configured |
| System prompts | Individual tool prompt files | How system prompts are structured |
| Rate limiting | `rate_limiter.py` | How token budgets are managed |
| Embeddings | `SentenceTransformerEmbeddingModel` usage | How semantic similarity works in practice |
| Streaming | SSE implementation in conductor/BFF | How token streaming is implemented |
| History management | `HistoryProcessorTool` | How context windows are managed |
| Test patterns | `Ui_Test_Gen_Skill.md` | How non-deterministic outputs are tested |
| Gold questions | Your evaluation dataset | What behavioral test cases look like for AI |

**Study method:** For each file, ask three questions:
1. What AI concept does this implement?
2. Why was it built this way? (What would break if it was different?)
3. How would I test this?

---

## Tools to Install

| Tool | Install | Purpose |
|---|---|---|
| `tiktoken` | `pip install tiktoken` | Count tokens offline — essential for Exercise 3 |
| `openai` | `pip install openai` | Direct API calls for experiments |
| `httpx` | `pip install httpx` | Async HTTP client for streaming experiments |

---

## How to Use These Resources

**Day 1:** Watch Karpathy's "Intro to LLMs" + explore bbycroft.net visualization. Read concepts.md Chapter 1.

**Day 2:** Read Anthropic's prompt engineering guide. Skim OpenAI Cookbook sections on structured output and function calling. Read concepts.md Chapters 2 & 3.

**Day 3:** Study your workspace files (Tier 4 table). Do all exercises. Read concepts.md Chapter 4.

**Ongoing:** Subscribe to Simon Willison's blog and The Batch newsletter for staying current.
