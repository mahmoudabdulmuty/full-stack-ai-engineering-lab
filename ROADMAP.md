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

## Tutor, source, and reasoning policy

- Keep DeepLearning.AI as the curriculum spine, but do not require passive viewing of every video. Inspect the authenticated transcript/notebook first, teach the missing capability, and require Mahmoud to predict, write, run, debug, and explain. Use a course video selectively when a visual demonstration or second explanation would materially improve understanding.
- Use **GPT-5.6 Sol at Medium** for normal Socratic lessons and explanations. Use **Sol at High** for substantive implementation, test design, debugging, and assessments.
- Use **GPT-6 Astra at High** for phase audits, difficult architecture decisions, project defense, and final hiring-readiness review. Escalate to **Astra XHigh** only for an unusually difficult unresolved decision or adversarial final audit. Max/Ultra is not part of the routine plan.
- Higher reasoning effort must not replace learner reasoning. The tutor still withholds challenge implementation, fades scaffolding, and records material hints honestly. Re-check current model guidance at major phase boundaries because model availability and recommendations can change.

## Phase 1 — Python core and local automation (NOW)

- Complete DeepLearning.AI M1–M4 in the existing sequence; Module 3 course coverage is complete as Guided, and Module 4 is next. Keep Module 3's fragile skills in spaced cold review rather than blocking course progression or adding immediate parallel practice.
- Compress concepts already understood from JavaScript/TypeScript: diagnose the transferable concept, teach Python-specific semantics, use one small transfer task, and move on when demonstrated.
- Keep prediction discipline strong during fundamentals. Later target predictions at non-obvious state, files, mutability, failures, and integrations rather than every trivial print.
- Use unfamiliar code progressively: trace behavior, explain data flow, locate bugs, preserve behavior while changing a feature, and review another implementation.
- Add type hints and async/await basics when Module 4/project needs them—not earlier for completeness.
- **Exit evidence:** retained Python foundations; a cold Module 3 project; and a small personal automation using a real budget-capped LLM call. The automation must be reproducible from a clean environment, keep configuration/secrets outside the repository, use clear import/module boundaries and exception handling, complete an HTTP/JSON request-response path, save validated output, expose failures, and include a few learner-owned regression tests. Before release, check representative inputs against a simple baseline and explicit quality/failure criteria, separating structural validity from usefulness and recording latency/cost. Mahmoud must explain the complete flow and which guarantees are deterministic versus probabilistic.

## Phase 2 — Production backend

Project-driven coverage for the first serious backend:

- HTTP fundamentals; FastAPI; Pydantic contracts; PostgreSQL; practical SQL fundamentals.
- Before Text-to-SQL, demonstrate joins and aggregation, constraints, a transaction rollback, one migration, and one slow-query investigation with evidence.
- ORM use without becoming ORM-dependent or losing the ability to reason about SQL.
- Deepen pytest and test design beyond the small Phase 1 regression suite; configuration; environment variables; secrets handling.
- structured errors; useful logging; Docker; basic CI/CD; deployment; basic cloud/runtime literacy; practical API security.
- authentication and authorization only when the product’s users/data justify them.
- SSE/streaming and async boundaries when the feature requires them.
- Build a thin Vue/Quasar consumer as part of the first deployed backend slice; Phase 4 later deepens the product UX rather than introducing frontend integration for the first time.
- Before public deployment, create a lightweight threat model covering assets, trust boundaries, abuse cases, controls, and remaining risks. Put usage limits around paid public operations; when private or multi-user data appears, enforce ownership server-side and test cross-user isolation.

Do not add Kubernetes, microservices, Kafka, Redis, Celery, complex cloud certifications, or infrastructure without a real requirement.

**Exit evidence:** a publicly deployed LLM-backed API with tests, validated contracts, useful logs, visible failure handling, documented setup/limitations, and a Vue/Quasar consumer.

## Phase 3 — AI application patterns

- Start with one current foundation-model API and direct SDK usage.
- Add structured outputs, validation, streaming, retries, cost/latency controls, and evaluation before abstraction. Deepen the evaluation baseline started in Phase 1 with representative and held-out examples, a simple baseline, explicit pass/failure criteria, measured latency/cost, and separate judgments for schema validity and task usefulness.
- Separate deterministic unit tests, integration tests, schema/contract checks, evaluation datasets, and probabilistic quality evaluation.
- Add tool use, retrieval, embeddings, vector storage, routing, agents, or MCP only when the product problem and evaluation support the extra complexity.
- Require explicit answers to: What is deterministic? What genuinely needs an LLM? What should deliberately not be built?

**Exit evidence:** Enterprise Document Copilot v1 with evaluated AI behavior, controlled failure modes, and defensible architecture. Retrieval enters only if its measured use case needs it.

## Phase 4 — Product frontend layer

- Deepen the thin Vue/Quasar slice from Phase 2 through Mahmoud’s Vue 3 / Quasar / Pinia strength so the first serious full-stack artifact ships quickly.
- Cover streaming UX, loading/error states, contract changes, observability surfaces, and end-to-end debugging.
- After the first serious Vue + FastAPI AI product is deployed, run a React/Next.js market checkpoint. Add a focused transition sprint only if repeated target-role evidence shows a meaningful access gap; teach it as a second ecosystem to an experienced frontend engineer.

**Exit evidence:** a polished, deployed, streaming full-stack product with a coherent demo and architecture walkthrough.

## Phase 5 — Reliability and differentiators

- Evaluation datasets and automated graders, tracing/observability, guardrails, practical AI security, cost/latency analysis, and feedback loops.
- Revisit and deepen the baseline threat model created before the first public deployment: assets, trust boundaries, abuse cases, controls, and remaining risks.
- Exercise prompt injection, secret exposure, unauthorized access, cross-user leakage, unsafe file handling, excessive tool/model permissions, and untrusted model output in product-relevant contexts.
- Before claiming Production Evidence, run a real pilot or realistic operational trial, use observed feedback or a failure to drive at least one improvement, and demonstrate a recovery procedure such as rollback or restore where persistent state is involved.
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

1. **Enterprise Document Copilot** — choose one user, domain, and document task before retrieval. Build Vue/Quasar + FastAPI + Pydantic validation + streaming first; compare against a simple baseline and require supported answers, explicit abstention, and access boundaries. Add PostgreSQL/retrieval only when the evaluated use case needs them, then make at least one feedback-driven improvement. Flagship.
2. **Text-to-SQL Analytics Dashboard** — begin only after the Phase 2 database gate. Use restricted database privileges, an explicit allowed-query scope, execution limits, and semantic answer checks for joins, aggregations, and ambiguous questions before rendering dynamic charts.
3. _(Optional)_ Voice support agent — realtime-API-based, scope cut ruthlessly.

## Four-month execution and application target

**Window:** 2026-09-05 through approximately 2027-01-05. **Capacity assumption:** 15–20 focused hours per week, with additional hours optional. Evidence gates still control advancement; the calendar does not convert Guided work into Independent mastery.

| Period | Primary outcome | Exit evidence before moving on |
|---|---|---|
| Month 1 — Sep 5 to Oct 4 | Complete Module 4, run the cold Module 3 project, then build the first real-provider personal automation | Learner-owned flow; reproducible setup; validated output; visible failure handling; regression tests; baseline usefulness check; measured/bounded latency and cost |
| Month 2 — Oct 5 to Nov 4 | Learn HTTP, FastAPI, Pydantic, SQL/PostgreSQL fundamentals, and deploy the first backend slice with a thin Vue/Quasar consumer | Tested contracts and failure paths; database gate evidence; logs; documented setup; baseline threat model/security; public deployment |
| Month 3 — Nov 5 to Dec 4 | Build Enterprise Document Copilot v1 for one specific user, domain, and document task | Deployed end-to-end feature; representative and held-out evaluation; supported answers/abstention; access boundaries; streaming and visible failure UX |
| Month 4 — Dec 5 to Jan 5 | Pilot, harden, improve, document, and defend the flagship; prepare and begin targeted applications | Observed feedback/failure drives an improvement; recovery procedure; README/demo; architecture walkthrough; project defense; targeted CV/LinkedIn/application package |

This is a **January 2027 application-launch target**, not a promise that every advanced phase and both major projects will be production-deep by then. Begin Text-to-SQL in Month 4 only if the flagship has met its gates; otherwise continue it while applying. A strong flagship plus deployed automation/backend evidence is preferable to two rushed projects.

When more than 20 hours are available, spend them on the current milestone's implementation, debugging, tests, evaluation, explanation, or pilot feedback. Do not add parallel courses, projects, or filler practice merely to consume the extra time. If sustained capacity falls below roughly 15 hours, preserve the sequence and move the application target rather than weakening the evidence gates.

To protect current focus, do not begin a Growth Lab assessment stream during Module 4. After Module 4 and the DeepLearning.AI Python course are complete, the Growth Lab should begin with a text-first Engineering Discovery Interview that maps Mahmoud's real experience, demonstrated capabilities, self-reported claims, and still-Unknown areas across practical software engineering. Its existing async/concurrency and testing priorities remain provisional until discovery confirms or replaces them. Do not begin with voice pressure; introduce hard voice interviews later at meaningful project-defense or hiring-readiness milestones. Any 30–60 minute remediation must be justified by demonstrated weakness and replace—not add to—the week's planned hours. Use real work and project problems rather than a parallel curriculum or technology checklist.

## Career launch coordination

- **Now through October:** keep technical focus; preserve evidence in this workspace. Do not add Guided course exercises to the CV as if they were hiring evidence.
- **November:** reactivate LinkedIn, update the established frontend experience honestly, and begin role/company tracking. “Open to Work” may remain private or disabled until the application package is ready.
- **December:** add only verified deployed project evidence, GitHub/demo links, measurable outcomes, and defensible technical claims to a master CV and LinkedIn.
- **January 2027:** begin targeted applications while continuing the second project and interview practice. Use LinkedIn and direct company careers as the primary route, Wellfound for startup/remote roles, and GulfTalent/Bayt for Gulf opportunities.
- The Full-Stack AI Engineering Lab owns the technical projects and their evidence. The Senior Engineering Growth Lab owns broader LinkedIn/CV packaging, interview stories, application strategy, and general software-engineering readiness. Share evidence without duplicating either track.

## Timeline and sources

A broader planning estimate remains 6–9 months of consistent part-time work after Python fundamentals to complete the roadmap deeply and become more broadly competitive. The four-month window above is an earlier application-launch target that leverages Mahmoud's existing frontend experience; evidence gates—not the calendar—control readiness.

Sources: `MISSION.md`; `PROGRESS.md`; `REVIEW_QUEUE.md`; `CAREER_EVIDENCE.md`; learning records; the verified hierarchy in `RESOURCES.md`; selected durable concepts from Chip Huyen’s *AI Engineering*; and current official documentation for Python, providers, frameworks, databases, testing, security, and deployment.
