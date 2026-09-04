# ROADMAP — Full-Stack AI Product Engineer Transition

Target: remote roles (US / Europe / Gulf-UAE-KSA), visa relocation later.
Positioning: **experienced Vue/frontend engineer expanding into end-to-end AI product ownership**—not an ML researcher and not a zero-experience career switcher.

North-star progression:

**Frontend Software Engineer → broader Software Engineer → Python/Backend Engineer → Full-Stack AI Product Engineer**

The outcome is the ability to independently clarify, build, debug, test, explain, deploy, operate, and improve useful AI-powered products. Completion dates and certificates are inputs; evidence is the gate.

## Standing rules

1. **Training Mode protects skill acquisition.** Mahmoud writes core challenge code; the tutor uses Socratic questions, one hint at a time, and honest grading.
2. **Production / AI-Assisted Mode follows evidence.** Once a capability is Independent and Retained, AI may help with boilerplate, unfamiliar APIs, review, refactoring ideas, documentation, test ideas, and debugging hypotheses. Mahmoud remains responsible for understanding, diffs, tests, architecture, security, and acceptance.
3. **Every major phase produces a credible artifact.** Deployed, tested, explained work beats playlist completion.
4. **Patterns over frameworks.** Structured outputs, tool calling, retrieval, routing, validation, retries, evaluation, observability, latency, cost, reliability, and security outlast framework churn.
5. **Start with the product problem.** RAG, agents, MCP, vector databases, LangChain/LangGraph, and multi-provider abstractions enter only when a requirement and evidence justify them.
6. **Use existing frontend leverage.** Vue 3 / Quasar / Pinia ships the first serious product faster; Python/backend/AI capability is never assumed without evidence.
7. **Two deep, deployed, README-documented, demo-able projects beat three shallow ones.** English-first communication supports the target hiring markets.

## Capability cycle and scaffolding fade

Across each major phase, the system should eventually cover:

**Learn → Practice → Consolidate → Build → Explain → Ship**

Not every daily lesson needs all six stages. The tutor’s role and task specification fade with demonstrated competence:

| Mode | Tutor supplies | Mahmoud increasingly owns |
|---|---|---|
| Early learning | goal, constraints, smaller steps, reasoning prompts, focused hints | implementation and explanations |
| Developing independence | problem, expected behavior, important constraints | names, data structures, control flow, boundaries, error handling |
| Backend/project stage | requirements, acceptance criteria, constraints | design, implementation, tests, debugging, documentation |
| Advanced product stage | product problem, constraints, review feedback | clarification, architecture, delivery, operation, decisions |
| Solo capstone | review, interview pressure, debugging coaching only when blocked | end-to-end ownership |

At checkpoints ask: **Am I giving Mahmoud structure he still needs, or structure he should now be generating himself?** Difficulty should grow through independence, ambiguity, integration, unfamiliarity, judgment, and ownership—not meaningless repetition.

## Phase 1 — Python core and local automation (NOW)

- Complete DeepLearning.AI M1–M4 in the existing sequence; Module 3 remains current.
- Compress concepts already understood from JavaScript/TypeScript: diagnose the transferable concept, teach Python-specific semantics, use one small transfer task, and move on when demonstrated.
- Keep prediction discipline strong during fundamentals. Later target predictions at non-obvious state, files, mutability, failures, and integrations rather than every trivial print.
- Use unfamiliar code progressively: trace behavior, explain data flow, locate bugs, preserve behavior while changing a feature, and review another implementation.
- Add type hints and async/await basics when Module 4/project needs them—not earlier for completeness.
- **Exit evidence:** retained Python foundations, cold Module 3 project, personal automation using a real budget-capped LLM call, validated output, failure handling, saved result, and an explanation of the complete flow.

## Phase 2 — Production backend

Project-driven coverage for the first serious backend:

- HTTP fundamentals; FastAPI; Pydantic contracts; PostgreSQL; practical SQL fundamentals.
- ORM use without becoming ORM-dependent or losing the ability to reason about SQL.
- pytest and test design; configuration; environment variables; secrets handling.
- structured errors; useful logging; Docker; basic CI/CD; deployment; basic cloud/runtime literacy; practical API security.
- authentication and authorization only when the product’s users/data justify them.
- SSE/streaming and async boundaries when the feature requires them.

Do not add Kubernetes, microservices, Kafka, Redis, Celery, complex cloud certifications, or infrastructure without a real requirement.

**Exit evidence:** a publicly deployed LLM-backed API with tests, validated contracts, useful logs, visible failure handling, documented setup/limitations, and a Vue/Quasar consumer.

## Phase 3 — AI application patterns

- Start with one current foundation-model API and direct SDK usage.
- Add structured outputs, validation, streaming, retries, cost/latency controls, and evaluation before abstraction.
- Separate deterministic unit tests, integration tests, schema/contract checks, evaluation datasets, and probabilistic quality evaluation.
- Add tool use, retrieval, embeddings, vector storage, routing, agents, or MCP only when the product problem and evaluation support the extra complexity.
- Require explicit answers to: What is deterministic? What genuinely needs an LLM? What should deliberately not be built?

**Exit evidence:** Enterprise Document Copilot v1 with evaluated AI behavior, controlled failure modes, and defensible architecture. Retrieval enters only if its measured use case needs it.

## Phase 4 — Product frontend layer

- Connect the backend through Mahmoud’s Vue 3 / Quasar / Pinia strength so the first full-stack artifact ships quickly.
- Cover streaming UX, loading/error states, contract changes, observability surfaces, and end-to-end debugging.
- After the first serious Vue + FastAPI AI product is deployed, run a React/Next.js market checkpoint. Add a focused transition sprint only if repeated target-role evidence shows a meaningful access gap; teach it as a second ecosystem to an experienced frontend engineer.

**Exit evidence:** a polished, deployed, streaming full-stack product with a coherent demo and architecture walkthrough.

## Phase 5 — Reliability and differentiators

- Evaluation datasets and automated graders, tracing/observability, guardrails, practical AI security, cost/latency analysis, and feedback loops.
- Before serious deployment, create a lightweight threat model: assets, trust boundaries, abuse cases, controls, and remaining risks.
- Exercise prompt injection, secret exposure, unauthorized access, cross-user leakage, unsafe file handling, excessive tool/model permissions, and untrusted model output in product-relevant contexts.
- Optional specialization only when useful: realtime voice via supported APIs; do not hand-build unnecessary cascaded infrastructure.

**Exit evidence:** production-like reliability demonstrated through evals, incident exercises, security controls, and explained trade-offs.

## Engineering practice progression

### Documentation literacy

Progress from tutor-provided facts to independently locating official documentation, reading parameters and return types, distinguishing examples from guarantees, noticing version differences, and verifying uncertain behavior with a small experiment. Official current documentation wins over model memory.

### Debugging independence

Progressively require Mahmoud to: reproduce → state expected/actual behavior → gather evidence → reduce the problem → form/test hypotheses → locate root cause → make the smallest correct fix → add regression protection when appropriate. Later broken programs should expose symptoms without naming the bug category or failing line.

### Testing and refactoring

Testing starts from guarantees and risks, not pytest syntax: happy path, failures, boundaries, regressions, and what should or should not be mocked. Sometimes define test cases before implementation. Use **make it work → understand it → test it → improve it**; require a reason for refactors involving duplication, naming, function size, assumptions, complexity, boundaries, or testability.

### Product ownership

Introduce incomplete requirements gradually. Require clarification of user, problem, success, available data, failure cases, deterministic vs LLM work, simplest viable architecture, latency/cost/reliability constraints, and deliberate non-goals. Do not turn current Python fundamentals into system-design interviews.

### Professional repository workflow

When projects are substantial enough, simulate: requirement → inspect existing code → plan → implement → test → inspect diff → commit → PR description → code review → revision. Practise meaningful commits, safe changes, concise PRs, and professional responses to review feedback. Do not interrupt fundamentals with Git ceremony.

## Assessment modes introduced only when earned

### INTERVIEW MODE

Clearly announce `INTERVIEW MODE`. The tutor does not teach or give normal hints, challenges vague claims, asks realistic follow-ups, and may change a requirement. “I don’t know” plus first-principles reasoning is allowed. If Mahmoud explicitly abandons the problem, exit the mode before hints resume.

Debrief separately: technical correctness, reasoning, depth, communication, English, interview behavior, knowledge gaps, evidence gaps, and next reinforcement. Grow from short module interviews to realistic 30–60 minute interviews near application readiness.

### PROJECT DEFENSE

After a serious project is feature-complete, the tutor acts as a demanding senior reviewer. Require evidence for architecture, database/LLM choices, deterministic alternatives, failure handling, tests, scaling constraints, expensive operations, observed evaluation failures, risks, and removable complexity. Reject buzzword-only answers.

The defense output records strengths, shallow areas, technical/architecture/reliability gaps, interview stories, README improvements, portfolio/CV evidence, and required fixes.

### Production incident mode

Only after deployment, provide symptoms such as 500s, dependency latency, database failure, bad release, cost spike, or unexpected AI behavior. Require: observe → logs/metrics → hypotheses → reproduce → mitigate → root cause → fix → regression protection → short postmortem.

## Lightweight architecture decisions

Record only consequential project decisions, near the project that uses them:

**Decision · Context · Alternatives · Chosen approach · Why · Trade-off accepted · Would reconsider if**

Examples include persistence choice, sync vs async, RAG vs no RAG, streaming, frontend ecosystem, or direct SDK vs framework. Do not log trivial implementation choices. These records become project-defense and interview evidence.

## Market calibration and focused CS floor

At major phase boundaries or roughly every 4–6 weeks when useful, inspect reliable current hiring evidence across repeated target roles. For any roadmap change state: what changed, supporting evidence, signal repetition, relevance to target roles, what changes, and what deliberately does not.

Do not react to one post, recruiter, influencer, listing, or framework release. Before serious applications, add only the CS/interview floor repeatedly required by target roles—lists/arrays, hash maps, sets, stacks/queues, search/sort intuition, basic complexity, recursion basics, and practical problem solving. Avoid arbitrary months of LeetCode unless the market actually demands it.

## Application-readiness gates

- **Stage A — Learning:** foundations developing; insufficient target-role evidence.
- **Stage B — Early Portfolio:** independent features/projects exist; major backend/AI gaps remain.
- **Stage C — Credible Adjacent Applications:** evidence supports roles leveraging existing frontend strength plus growing backend/AI capability.
- **Stage D — Competitive Full-Stack AI Applications:** serious deployed work demonstrates target capabilities.
- **Stage E — Strong Target Positioning:** strong end-to-end ownership, debugging, architecture judgment, communication, and interview readiness.

Advance through evidence, never elapsed time or course completion. No stage implies a job guarantee. At major milestones audit Knowledge, Independent Implementation, Retention, Integration, Debugging, Testing, Engineering Judgment, Product Judgment, Communication, and Hiring Evidence. Record the result in `CAREER_EVIDENCE.md`.

## Portfolio build order

1. **Enterprise Document Copilot** — Vue/Quasar + FastAPI + Pydantic validation + streaming first; add PostgreSQL/retrieval only when its evaluated use case needs them. Flagship.
2. **Text-to-SQL Analytics Dashboard** — natural language → validated SQL → PostgreSQL → dynamic charts.
3. _(Optional)_ Voice support agent — realtime-API-based, scope cut ruthlessly.

## Timeline and sources

A planning estimate is 6–9 months of consistent part-time work after Python fundamentals to become meaningfully competitive, but evidence gates—not the calendar—control readiness.

Sources: `MISSION.md`; `PROGRESS.md`; `REVIEW_QUEUE.md`; `CAREER_EVIDENCE.md`; learning records; the verified hierarchy in `RESOURCES.md`; selected durable concepts from Chip Huyen’s *AI Engineering*; and current official documentation for Python, providers, frameworks, databases, testing, security, and deployment.
