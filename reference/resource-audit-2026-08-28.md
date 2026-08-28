# Resource audit — AI Python Tutor

Date: 2026-08-28

## Decision

The workspace already has enough material to reach the stated goal: become a pragmatic full-stack AI product engineer who can independently build, explain, test, and deploy Python + LLM features. The limiting factor is no longer access to content; it is converting concepts into cold, learner-written, deployed evidence.

Use a deliberately small stack:

1. one active beginner curriculum;
2. official Python documentation for language truth;
3. one conceptual AI-engineering book, read selectively;
4. official FastAPI documentation for the backend phase;
5. current model-provider documentation for implementation details;
6. learner-written projects, tests, and deployments as the real assessment.

Do not add another general Python course, another broad AI-engineering track, or another LLM book now.

## What is already strongest in this workspace

| Workspace resource | Role | Verdict |
|---|---|---|
| `practice/` | Learner-written code and observable debugging evidence | Highest value; this is where ability is built. |
| `PROGRESS.md` + `REVIEW_QUEUE.md` | Evidence ledger and cold-recall scheduling | Keep authoritative; prevents guided completion from being mistaken for independent mastery. |
| `learning-records/` | Compact demonstrations and weak-point history | Keep; useful for targeted retrieval, not automatic startup reading. |
| `START_HERE.md` + `QUALITY_CHECKLIST.md` | Tutor behavior and close criteria | Keep; the lean bootstrap avoids context inflation. |
| `reference/` + `visualizers/` | On-demand reinforcement | Keep selective. Build only when a concept is genuinely hard or repeatedly fragile. |
| `assessments/` | Module-level review and pressure checks | Keep when the interactive format adds value; secondary to blank-file projects and real execution. |
| Per-lesson HTML | Duplicate explanation artifact | Removed from the default workflow; recreate only for a specific review need. |
| `books/` | One conceptual reference book | Keep the single title; do not expand the shelf yet. |

## Local-book classification

The local inventory contains exactly one book.

### Core local books

None for the current Python-fundamentals phase. The active curriculum plus learner-written practice is a better spine than reading a book linearly.

### Selective/reference

**Chip Huyen, _AI Engineering: Building Applications with Foundation Models_** — keep.

- O'Reilly lists it as an intermediate-to-advanced, 534-page title published in December 2024. Its scope includes AI-application planning, evaluation, prompt engineering, RAG, agents, dataset engineering, latency/cost, architecture, monitoring, and feedback. That aligns well with the later product-engineering phases, but not with Mahmoud's immediate need to finish Python fundamentals and make a first real API call. [Official O'Reilly book page](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)
- Use it alongside projects, not cover to cover. Good routing is: product planning before the first serious feature; evaluation chapters after a working feature exists; RAG/agents only when a product requirement justifies them; architecture and feedback before production hardening.
- Treat its durable concepts as valuable. Verify all model names, SDK examples, provider behavior, cost figures, and framework syntax against current official documentation before teaching or implementing them.
- The author's companion repository is the appropriate source for book resources and updates. [Official companion repository](https://github.com/chiphuyen/aie-book)

### Outdated/low priority

No local book should be discarded as a whole. The outdated/low-priority category applies only to time-sensitive implementation details inside the 2024 book, not to its systems and product-design concepts.

No additional local book is currently necessary. In particular, adding another broad LLM book would overlap with the existing conceptual spine while delaying project work.

## Minimal resource stack for the agent tutor

### 1. Finish the current Python spine

**DeepLearning.AI — AI Python for Beginners** remains the active Phase 1 curriculum. Its official outline covers Python fundamentals, files and structured data, packages, web APIs, and interaction with AI models. [Official course page](https://www.deeplearning.ai/courses/ai-python-for-beginners)

Tutor rule: authenticated lesson transcript first; compare it with demonstrated capability; teach only the missing step; require learner-written practice and changed-context rechecks.

### 2. Use Python's documentation as the language authority

The official Python tutorial explicitly targets programmers who are new to Python rather than people new to programming, which fits an experienced Vue/frontend developer well. Use it on demand for language semantics, modules, exceptions, files, classes, virtual environments, and standard-library behavior—not as a second linear course. [The Python Tutorial](https://docs.python.org/3/tutorial/)

### 3. Make the first real LLM feature with current provider docs

After the course's API module, replace the local echo stub in one small project with a real, budget-capped API call. The current implementation authority should be:

- [OpenAI developer quickstart](https://developers.openai.com/api/docs/quickstart)
- [Responses API migration guide](https://developers.openai.com/api/docs/guides/migrate-to-responses) — OpenAI recommends Responses for new projects.
- [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) — use schemas for reliable application data instead of trusting free-form CSV or JSON text.
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling) — add only when the product actually needs tools.
- [Current model guidance](https://developers.openai.com/api/docs/guides/latest-model) — re-check at implementation time rather than freezing a model name in the curriculum.
- [Production best practices](https://developers.openai.com/api/docs/guides/production-best-practices) — secrets, environments, limits, reliability, and go-live concerns.

The [OpenAI Cookbook](https://github.com/openai/openai-cookbook) is a conditional recipe source after the core docs, not a course to complete.

### 4. Learn backend engineering through one real API

Use the [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/) as the sole primary backend curriculum. FastAPI describes it as a step-by-step tutorial whose examples are tested and whose main guide is sufficient to build a complete application. Build the first public API while learning routes, request/response models, validation, errors, dependency injection, async boundaries, and tests.

Use [Pydantic's current validation documentation](https://pydantic.dev/docs/validation/latest/get-started/) when data contracts become real. Pydantic's type-hint-based validation and JSON Schema support connect familiar frontend typing ideas to API boundaries and structured LLM outputs.

### 5. Add production infrastructure only when the project reaches it

- [Docker Get Started](https://docs.docker.com/get-started/) when packaging the first backend for deployment.
- [PostgreSQL official tutorial](https://www.postgresql.org/docs/current/tutorial.html) when persistent relational data becomes a requirement.
- A deployment provider's own current documentation when the artifact is ready to deploy; do not choose a platform months in advance.
- [OpenAI evaluation datasets guide](https://developers.openai.com/api/docs/guides/evaluation-getting-started) after a real feature has representative inputs and known failure modes.

## Recommended teaching route

| Milestone | Primary material | Required evidence before advancing |
|---|---|---|
| Finish Python fundamentals | DeepLearning.AI transcript + Python docs | Cold blank-file module project, clean run, learner explanation |
| First real AI automation | OpenAI quickstart + Responses + Structured Outputs | Real API response validated, saved, errors handled, cost bounded |
| First backend | FastAPI tutorial + Pydantic docs | Tested API consumed by Mahmoud's existing Vue/Quasar frontend |
| First deployed product | Docker + selected provider docs | Public URL, README, demo, logs, failure handling |
| Retrieval/tools only if justified | Provider docs + selected _AI Engineering_ chapters | A product requirement and an eval showing the added complexity improves results |
| Portfolio readiness | Existing roadmap + project retrospectives | Two deep deployed projects with trade-offs, limitations, tests, and evidence of independent debugging |

## Deprioritize deliberately

- More overlapping beginner courses or certificate chasing.
- Framework-first LangChain/LangGraph study before the underlying retrieval, tool, state, and evaluation patterns are understood.
- Pinecone or any vector database before ordinary storage/search fails a measured requirement.
- RAG, agents, voice, fine-tuning, and multi-provider abstraction before one simple model-backed product is reliable.
- React/Next.js as a prerequisite. Use Mahmoud's Vue/Quasar strength for the first end-to-end product; add React/Next later only for a clear market or project reason.
- Reading the local book cover to cover before building.

## Final recommendation

Keep the workspace lean and project-led. The best immediate sequence is:

**finish M3 and M4 → cold Module 3 project → real API automation → FastAPI + Pydantic backend → connect Vue/Quasar → test and deploy → introduce evaluation → add RAG/tools only when measured need appears.**

This route directly serves the mission: independent hands-on engineering, not content completion.
