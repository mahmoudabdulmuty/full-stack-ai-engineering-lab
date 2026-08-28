# RESOURCES — minimal stack for the AI Python Tutor

Plan of record: `ROADMAP.md`. Detailed verification: `reference/resource-audit-2026-08-28.md`.

## Resource policy

The workspace already has enough material. Progress is measured by learner-written, tested, explainable, deployed work—not by collecting or completing more content.

Use this hierarchy:

1. The active DeepLearning.AI curriculum supplies the current learning sequence.
2. Official documentation is the authority for Python behavior, SDKs, APIs, models, framework syntax, deployment, and other changing facts.
3. Chip Huyen's *AI Engineering* supplies durable product and systems concepts, selected when a project needs them.
4. `practice/`, cold rechecks, tests, and deployed projects supply evidence of ability.

Do not add another broad curriculum or general LLM book unless a specific capability gap cannot be filled by this stack.

## Now — Python and local automation

- [DeepLearning.AI — AI Python for Beginners](https://www.deeplearning.ai/courses/ai-python-for-beginners/)
  Active curriculum. Fetch the authenticated transcript first, compare it with demonstrated capability, teach only the missing step, and require learner-written practice. Current position: Module 3 in progress; Module 4 follows.
- [The Python Tutorial](https://docs.python.org/3/tutorial/)
  Language authority for a programmer who is new to Python. Use on demand for semantics, files, exceptions, modules, classes, virtual environments, and standard-library behavior; do not run it as a second linear curriculum.

## Next — first real AI automation

After Module 4, replace the local echo stub in one small project with a real, budget-capped API call.

- [OpenAI developer quickstart](https://developers.openai.com/api/docs/quickstart)
- [Responses API migration guide](https://developers.openai.com/api/docs/guides/migrate-to-responses)
- [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Current model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Production best practices](https://developers.openai.com/api/docs/guides/production-best-practices)

Use [function calling](https://developers.openai.com/api/docs/guides/function-calling) only when the product needs tools. Use the [OpenAI Cookbook](https://github.com/openai/openai-cookbook) as a conditional recipe source after the core documentation, never as another curriculum to complete.

Required evidence: a real response is validated, failures are handled, useful output is saved, secrets stay outside the repository, and cost is bounded.

## Then — production backend

- [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/)
  The primary backend path. Learn routes, request/response models, validation, errors, dependencies, async boundaries, and tests while building one real API.
- [Pydantic validation documentation](https://pydantic.dev/docs/validation/latest/get-started/)
  Use for API data contracts and structured LLM outputs; connect Python type hints to familiar frontend typing ideas.
- [pytest documentation](https://docs.pytest.org/en/stable/)
  Introduce when the first backend needs repeatable behavior and failure-case checks.

Use Mahmoud's existing Vue/Quasar strength for the first end-to-end interface. React/Next.js is optional market expansion later, not a prerequisite.

Required evidence: a tested FastAPI feature consumed by a Vue/Quasar frontend, then deployed with a public URL, README, logs, and visible failure handling.

## Local book — selective conceptual spine

- `books/AI Engineering Building Applications with Foundation Models (Chip Huyen).pdf`
- [Official O'Reilly page](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)
- [Author's companion repository](https://github.com/chiphuyen/aie-book)

The local PDF is the December 2024 first edition. Keep it: its durable treatment of product planning, evaluation, prompting, RAG, agents, latency/cost, architecture, monitoring, and feedback matches the long-term goal. It is not a Python tutorial or current SDK authority.

Route chapters by need:

- Before the first serious AI feature: selected Chapter 1 planning sections.
- After a working feature exists: Chapters 3–4 on evaluation and selected Chapter 5 prompt-engineering sections.
- Only when retrieval or tools solve a measured problem: selected Chapter 6 sections.
- Before production hardening: selected Chapters 9–10 on inference, architecture, monitoring, and feedback.
- Defer fine-tuning and dataset engineering until a real requirement makes them useful.

Verify every model name, API call, price, provider behavior, and framework example against current official documentation before teaching or implementing it. Summarize and cite; do not copy long passages.

## Add only when the project reaches the requirement

- [Docker Get Started](https://docs.docker.com/get-started/) when packaging the first backend.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) when persistent relational data is required.
- The chosen deployment provider's current documentation when an artifact is ready to deploy.
- [OpenAI evaluation datasets guide](https://developers.openai.com/api/docs/guides/evaluation-getting-started) after a real feature has representative inputs and known failure modes.
- Retrieval, vector storage, RAG, agents, observability frameworks, or multi-provider abstractions only after a product requirement and evaluation justify the added complexity.

## Tutor routing rules

- Finish M3–M4 before expanding the stack.
- Fetch only the source needed for the current capability or project decision.
- Teach a small concept, then require prediction, implementation, execution, explanation, and a changed-context recheck.
- Prefer blank-file projects and real integration failures over additional lesson artifacts.
- Never treat guided completion, a stub response, or content consumption as production evidence.
- Re-check time-sensitive facts at implementation time and record the source used.
- Ask for a new resource only when the current stack leaves a named capability gap.

## Recommended route

**Finish M3 and M4 → cold Module 3 project → real API automation → FastAPI + Pydantic backend → connect Vue/Quasar → test and deploy → add evaluation → introduce retrieval/tools only when measured need appears.**
