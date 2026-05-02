# Stage 3: Curated Resources (2024-2025)

Resources organized by chapter. Start with [PARETO-20] items — they cover the critical 20%.

---

## Chapter 1: MLOps for LLM Systems

### Books

| Resource | Why Read It | Priority |
|----------|------------|----------|
| **"Designing Machine Learning Systems"** by Chip Huyen (O'Reilly, 2022) | Chapters 9-11 cover deployment, monitoring, and infrastructure. The mental models apply directly to LLMOps. | [PARETO-20] |
| **"AI Engineering"** by Chip Huyen (O'Reilly, 2025) | Dedicated to LLM systems in production. Covers evaluation, RAG, agents, and LLMOps. Most relevant single book for Stage 3. | [PARETO-20] |

### Online Resources

| Resource | URL | Why |
|----------|-----|-----|
| MLOps Community | https://mlops.community/ | Active community, practical talks, real-world case studies |
| MLflow Documentation | https://mlflow.org/docs/latest/llms/index.html | Free experiment tracking, specifically their LLM tracking features |
| LangSmith Documentation | https://docs.smith.langchain.com/ | Best-in-class LLM tracing and evaluation platform |
| Weights & Biases Prompts | https://docs.wandb.ai/guides/prompts | Prompt experiment tracking with free tier |

### Articles

| Article | Why |
|---------|-----|
| "LLMOps: Everything You Need to Know" — Chip Huyen's blog | Concise overview of how LLMOps differs from MLOps |
| "A Survey on LLMOps" (2024) | Academic survey of the LLMOps landscape |

---

## Chapter 2: Deployment Patterns

### Documentation

| Resource | URL | Why |
|----------|-----|-----|
| **Ray Documentation** | https://docs.ray.io/en/latest/ | Your workspace uses Ray. Start with "Ray Core" and "Ray Serve" sections. | 
| **Ray Serve for LLMs** | https://docs.ray.io/en/latest/serve/index.html | Specifically relevant: serving LLM applications with Ray |
| FastAPI Deployment | https://fastapi.tiangolo.com/deployment/ | Your services use FastAPI. Review async best practices. |
| AWS ECS Best Practices | https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/ | Your deployment target |

### Articles

| Article | Why |
|---------|-----|
| "Scaling LLM Applications" — a]16z blog | Practical patterns for scaling LLM-powered applications |
| "GPTCache: An Open-Source Semantic Cache for LLM Applications" | The academic paper behind semantic caching |

---

## Chapter 3: Fine-Tuning

### Guides

| Resource | URL | Why |
|----------|-----|-----|
| **OpenAI Fine-Tuning Guide** | https://platform.openai.com/docs/guides/fine-tuning | Practical guide for the models you use. Start here. | [PARETO-20] |
| Hugging Face PEFT (LoRA) | https://huggingface.co/docs/peft | If you ever need to fine-tune open-source models |
| "A Beginner's Guide to LLM Fine-Tuning" — Sebastian Raschka | Clear explanation of LoRA, QLoRA, and when to use them |

### Papers (conceptual understanding, not implementation)

| Paper | Why |
|-------|-----|
| "LoRA: Low-Rank Adaptation of Large Language Models" (2021) | The foundational paper. Read the introduction and method sections. |
| "Direct Preference Optimization" (2023) | Understand DPO as the simpler alternative to RLHF |
| "Training Language Models to Follow Instructions with Human Feedback" (2022) | The InstructGPT paper — how RLHF works in practice |

---

## Chapter 4: AI Safety and Alignment [PARETO-20]

### Frameworks and Standards

| Resource | URL | Why |
|----------|-----|-----|
| **NIST AI Risk Management Framework** | https://www.nist.gov/itl/ai-risk-management-framework | US standard for AI risk management. Read the "Playbook" for practical guidance. | [PARETO-20] |
| **EU AI Act Summary** | https://artificialintelligenceact.eu/ | Comprehensive summary of the regulation. Focus on risk classifications and requirements. | [PARETO-20] |
| OWASP Top 10 for LLM Applications | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | Security-focused. Essential for prompt injection defense. | [PARETO-20] |

### Tools

| Tool | URL | Why |
|------|-----|-----|
| **Guardrails AI** | https://www.guardrailsai.com/docs | Python framework for LLM output validation. Practical and well-documented. |
| **NeMo Guardrails** | https://github.com/NVIDIA/NeMo-Guardrails | NVIDIA's toolkit for adding safety rails to conversational AI |
| LlamaGuard | https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/ | Meta's safety classifier for input/output screening |

### Articles

| Article | Why |
|---------|-----|
| "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" (2023) | The definitive paper on indirect prompt injection. Eye-opening. |
| "Prompt Injection: A Critical Vulnerability in LLM Applications" — Simon Willison's blog | Accessible explanation with real examples |
| "Red Teaming Language Models" (Anthropic, 2022) | How to systematically test AI safety |

---

## Chapter 5: Observability and Monitoring

### Tools and Documentation

| Resource | URL | Why |
|----------|-----|-----|
| **Datadog LLM Observability** | https://docs.datadoghq.com/llm_observability/ | Your workspace uses Datadog. Their LLM-specific features are directly applicable. | [PARETO-20] |
| OpenTelemetry for Python | https://opentelemetry.io/docs/languages/python/ | Industry standard for distributed tracing |
| Langfuse | https://langfuse.com/docs | Open-source LLM observability. Good alternative/complement to Datadog |

### Articles

| Article | Why |
|---------|-----|
| "Monitoring LLMs in Production" — Arize AI blog | Practical guide to LLM monitoring metrics |
| "Building Observable LLM Applications" | How to add observability to existing LLM applications |

---

## General Resources

### Must-Read Newsletters (stay current)

| Newsletter | Why |
|------------|-----|
| **The Batch** (Andrew Ng) | Weekly AI news, practical and accessible |
| **Latent Space** | Podcast and newsletter focused on AI engineering |
| **Last Week in AI** | Comprehensive weekly roundup |

### Communities

| Community | Why |
|-----------|-----|
| MLOps Community Slack | Active practitioners sharing real-world patterns |
| r/LocalLLaMA | Open-source model community, useful for fine-tuning discussions |
| AI Engineer Discord | AI engineering-focused community |

---

## Recommended Reading Order (if time is limited)

If you only have 4-5 hours for reading:

1. **Chip Huyen's "AI Engineering"** — Chapters on evaluation, deployment, and monitoring (~2 hours)
2. **OWASP Top 10 for LLMs** — Full document (~30 minutes)
3. **Datadog LLM Observability docs** — Getting started guide (~30 minutes)
4. **OpenAI Fine-Tuning Guide** — When/how to fine-tune (~30 minutes)
5. **NIST AI RMF Playbook** — Skim the "Measure" and "Manage" sections (~30 minutes)
