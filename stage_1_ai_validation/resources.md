# Resources — Curated for AI Validation Engineering (2024-2025)

> Every resource here is selected for relevance to your work. Prioritized by impact.

---

## Essential Papers

### [PARETO-20] Must-Read Papers (Read These First)

1. **"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"**
   - Authors: Zheng et al. (2023)
   - Link: https://arxiv.org/abs/2306.05685
   - Why: THE foundational paper for LLM-as-a-Judge. Proves GPT-4 judges agree with
     humans ~80% of the time. Covers position bias, verbosity bias, and mitigation
     strategies.
   - Read sections: 1 (intro), 3 (MT-Bench design), 4 (agreement analysis), 6 (limitations)
   - Time: 2 hours

2. **"RAGAS: Automated Evaluation of Retrieval Augmented Generation"**
   - Authors: Es et al. (2023)
   - Link: https://arxiv.org/abs/2309.15217
   - Why: Defines the 4 standard metrics for RAG evaluation (faithfulness, answer
     relevancy, context precision, context recall). Directly applicable to your
     normalizer.
   - Read sections: 1-3 (metrics definitions), 4 (experiments)
   - Time: 1.5 hours

3. **"A Survey on Evaluation of Large Language Models"**
   - Authors: Chang et al. (2024)
   - Link: https://arxiv.org/abs/2307.03109
   - Why: Comprehensive survey of ALL evaluation approaches. Use as a reference —
     when you encounter a new evaluation concept, look it up here.
   - Read sections: 1 (taxonomy overview), 3 (automated evaluation), 5 (human evaluation)
   - Time: 3 hours (skim), 8 hours (thorough)

### Additional Important Papers

4. **"G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment"**
   - Authors: Liu et al. (2023)
   - Link: https://arxiv.org/abs/2303.16634
   - Why: The paper behind DeepEval's GEval metric. Shows how chain-of-thought
     improves LLM-as-judge accuracy.

5. **"Challenges and Applications of Large Language Models"**
   - Authors: Kaddour et al. (2023)
   - Link: https://arxiv.org/abs/2307.10169
   - Why: Comprehensive overview of LLM failure modes and challenges.

6. **"Practices for Governing Agentic AI Systems"**
   - Authors: OpenAI (2024)
   - Link: https://openai.com/research/practices-for-governing-agentic-ai-systems
   - Why: OpenAI's framework for evaluating and governing agent systems. Relevant to
     your multi-agent testing approach.

7. **"Red Teaming Language Models to Reduce Harms"**
   - Authors: Ganguli et al. (2022)
   - Link: https://arxiv.org/abs/2209.07858
   - Why: Anthropic's approach to red teaming. Practical methodology you can adapt.

---

## Tools

### [PARETO-20] Primary Tools (Install and Learn These)

| Tool | Purpose | Install | Priority |
|------|---------|---------|----------|
| **DeepEval** | LLM evaluation framework | `pip install deepeval` | #1 |
| **RAGAS** | RAG evaluation metrics | `pip install ragas` | #2 |
| **Promptfoo** | Prompt testing & comparison | `npm install -g promptfoo` | #3 |

### Secondary Tools (Learn About, Install If Needed)

| Tool | Purpose | Install | When to Use |
|------|---------|---------|------------|
| **Garak** | LLM vulnerability scanning | `pip install garak` | Red teaming |
| **PyRIT** | Microsoft's red team toolkit | `pip install pyrit` | Advanced red teaming |
| **LangFuse** | Open-source LLM observability | Docker / cloud | Production tracing |
| **LangSmith** | LangChain's observability | Cloud service | If using LangChain |
| **OpenAI Evals** | OpenAI's eval framework | `pip install evals` | OpenAI-specific evals |
| **Weights & Biases** | ML experiment tracking | `pip install wandb` | Experiment tracking |
| **Arize Phoenix** | LLM observability & eval | `pip install arize-phoenix` | Alternative to LangFuse |

### Tool Comparison Matrix

| Feature | DeepEval | RAGAS | Promptfoo | OpenAI Evals |
|---------|----------|-------|-----------|-------------|
| Language | Python | Python | Node.js | Python |
| LLM-as-Judge | Yes (GEval) | Yes | Yes (llm-rubric) | Yes |
| RAG metrics | Yes | Yes (best) | Partial | Partial |
| Hallucination detect | Yes | Yes | Via rubric | Via rubric |
| Side-by-side comparison | No | No | Yes (best) | No |
| Red teaming | No | No | Yes | No |
| CI/CD integration | pytest | Python | CLI | CLI |
| Free | Yes | Yes | Yes | Yes |
| Dashboard | Yes (cloud) | No | Yes (local) | No |

---

## Courses and Tutorials

### [PARETO-20] Start Here

1. **"Evaluating and Debugging Generative AI" — DeepLearning.AI**
   - Link: https://www.deeplearning.ai/short-courses/evaluating-debugging-generative-ai/
   - Why: Short course by Andrew Ng's team. Covers evaluation fundamentals with
     hands-on code.
   - Time: 1.5 hours
   - Free: Yes

2. **"Building and Evaluating Advanced RAG" — DeepLearning.AI**
   - Link: https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/
   - Why: Covers RAG evaluation with RAGAS metrics. Directly applicable to your
     normalizer.
   - Time: 1.5 hours
   - Free: Yes

3. **Hamel Husain's LLM Evaluation Blog Series**
   - Link: https://hamel.dev/blog/posts/evals/
   - Why: Practical, practitioner-focused guide to LLM evaluation from a senior ML
     engineer. No fluff, all substance.
   - Time: 2-3 hours for the full series
   - Free: Yes

### Additional Courses

4. **"Quality and Safety for LLM Applications" — DeepLearning.AI**
   - Link: https://www.deeplearning.ai/short-courses/quality-safety-llm-applications/
   - Why: Covers safety evaluation, guardrails, content moderation
   - Time: 1.5 hours

5. **"Automated Testing for LLMOps" — DeepLearning.AI**
   - Link: https://www.deeplearning.ai/short-courses/automated-testing-llmops/
   - Why: CI/CD for LLM evaluation pipelines
   - Time: 1.5 hours

6. **"Red Teaming LLM Applications" — DeepLearning.AI**
   - Link: https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/
   - Why: Hands-on red teaming with Garak
   - Time: 1.5 hours

---

## Books

1. **"Building LLM Apps: A Clear Step-by-Step Guide" — Chip Huyen (2025)**
   - Why: Most current book on building and evaluating LLM applications.
     Chapter on evaluation is excellent.
   - Status: Published 2025

2. **"AI Engineering" — Chip Huyen (2024)**
   - Why: Broader view of AI engineering, including evaluation, monitoring, and
     deployment. Written by a Stanford instructor and industry practitioner.

3. **"Designing Machine Learning Systems" — Chip Huyen (2022)**
   - Why: While focused on ML broadly, the chapters on testing, monitoring, and
     data quality are directly applicable to LLM systems.

4. **"Prompt Engineering for Generative AI" — James Phoenix & Mike Taylor (2024)**
   - Why: Covers prompt design and testing methodology. Good companion to Chapter 5.

---

## Blogs and Articles

### Must-Read Blog Posts

- **"Your AI Product Needs Evals"** — Hamel Husain
  https://hamel.dev/blog/posts/evals/
  Practical guide to building eval suites. Best single article on the topic.

- **"LLM Evaluation Doesn't Need to Be Complicated"** — Eugene Yan
  https://eugeneyan.com/writing/llm-evaluations/
  Simple, actionable framework for starting with evals.

- **"How to Evaluate LLM Applications"** — Shreya Shankar
  https://www.shreya-shankar.com/
  Academic rigor meets practical advice.

- **"Testing in Production for AI"** — Lina Weichbrodt
  Covers online evaluation and production monitoring strategies.

### Company Engineering Blogs (Evaluation-Focused)

- **Anthropic's research blog** — https://www.anthropic.com/research
  Covers evaluation methodology, red teaming, safety testing.

- **OpenAI's blog** — https://openai.com/blog
  Model evaluation results, safety benchmarks.

- **Weights & Biases blog** — https://wandb.ai/site/articles
  Practical ML evaluation tutorials.

---

## Communities

### Where AI Evaluation Engineers Hang Out

1. **r/LocalLLaMA** (Reddit)
   - Why: Active discussions on model evaluation, benchmarking, and testing
   - Look for: Evaluation threads, benchmark discussions
   - Link: https://reddit.com/r/LocalLLaMA

2. **Eleuther AI Evaluation Harness** (GitHub)
   - Why: Open-source evaluation framework used for model benchmarking
   - Link: https://github.com/EleutherAI/lm-evaluation-harness
   - Useful for understanding evaluation benchmark design

3. **MLOps Community** (Slack)
   - Why: Practitioners discussing ML testing, evaluation, and deployment
   - Link: https://mlops.community

4. **AI Quality Engineering** (LinkedIn groups)
   - Why: Specific to QA/testing for AI systems
   - Search: "AI Quality Engineering" on LinkedIn Groups

5. **DeepEval Community** (Discord)
   - Why: Direct access to the DeepEval team and other users
   - Link: Available via DeepEval's GitHub page

---

## Job Boards and Role Research

### Where to Find AI Validation Roles

1. **LinkedIn** — Search: "AI Quality Engineer," "ML Test Engineer," "LLM Evaluation
   Engineer," "AI Validation Engineer"

2. **Greenhouse/Lever** — Many AI startups post here. Search for evaluation roles.

3. **Y Combinator Work at a Startup** — https://www.ycombinator.com/jobs
   Search: "evaluation," "quality," "testing" in AI companies

### Key Skills Companies Ask For (Study These Job Postings)

Based on current (2024-2025) job postings for AI evaluation roles:

| Skill | Frequency | You Have It? |
|-------|-----------|-------------|
| LLM evaluation frameworks | Very Common | After this stage: Yes |
| Python (pytest, data analysis) | Very Common | Yes |
| Prompt engineering & testing | Very Common | Yes |
| RAG evaluation | Common | After this stage: Yes |
| Red teaming / safety testing | Common | After this stage: Yes |
| CI/CD for AI pipelines | Common | Yes |
| Statistical analysis | Common | Learning in Stage 2 |
| Human evaluation management | Less Common | Partial |
| MLOps tools (W&B, MLflow) | Less Common | Learning |

### Example Job Descriptions to Study

Search LinkedIn for these exact titles and read the requirements:
- "AI Evaluation Engineer" at Anthropic
- "LLM Quality Engineer" at Scale AI
- "ML Test Engineer" at Google DeepMind
- "AI Safety Researcher" at OpenAI
- "Quality Engineer, AI Products" at Microsoft

Compare their requirements to your skills after completing this stage.

---

## Tool Documentation Quick Links

| Tool | Docs | Getting Started |
|------|------|----------------|
| DeepEval | https://docs.confident-ai.com | https://docs.confident-ai.com/docs/getting-started |
| RAGAS | https://docs.ragas.io | https://docs.ragas.io/en/latest/getstarted/ |
| Promptfoo | https://www.promptfoo.dev/docs/intro | https://www.promptfoo.dev/docs/getting-started |
| Garak | https://docs.garak.ai | https://docs.garak.ai/garak |
| LangFuse | https://langfuse.com/docs | https://langfuse.com/docs/get-started |
| LangSmith | https://docs.smith.langchain.com | https://docs.smith.langchain.com/tutorials |

---

## Recommended Learning Sequence

**Week 1 (Days 4-7):**
1. Read Chapters 1-2 of concepts.md
2. Watch "Evaluating and Debugging Generative AI" course
3. Read Hamel Husain's eval blog post
4. Do Exercises 1-3

**Week 2 (Days 8-11):**
1. Read Chapters 3-4 of concepts.md
2. Watch "Building and Evaluating Advanced RAG" course
3. Skim the Zheng et al. paper (focus on sections 1, 3, 4)
4. Do Exercises 4-7

**Week 3 (Days 12-14):**
1. Read Chapters 5-6 of concepts.md
2. Watch "Red Teaming LLM Applications" course
3. Do Exercises 8-10
4. Start the mini-project
