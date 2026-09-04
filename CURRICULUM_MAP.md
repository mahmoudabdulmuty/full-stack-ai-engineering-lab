# CURRICULUM_MAP.md

Goal → source → capability → project-evidence map. Governed by the lean tutor bootstrap, evidence ladder, and `ROADMAP.md`. Revisit at module/phase retrospectives; run market calibration only when useful, roughly every 4–6 weeks or at a major boundary.

## North star

Full-Stack AI Product Engineer who can independently clarify, build, debug, test, explain, deploy, operate, and improve useful AI-powered products. Existing frontend engineering experience accelerates transfer; unproven Python/backend/AI capability is never assumed.

## Phase map (from ROADMAP.md + progression rules)

| Roadmap phase | Target capabilities | Primary source | Required evidence | Status |
|---|---|---|---|---|
| 1. Python core + local automation | Python semantics, debugging discipline, files/data, functions/modules, real budget-capped model call | DeepLearning.AI M1–M4; official Python/provider docs on demand | Cold retention + integrated personal automation with validation/failure handling | 🔄 IN PROGRESS (M3L6) |
| 2. Production backend | HTTP, FastAPI, Pydantic, SQL/PostgreSQL, practical ORM use, pytest, configuration/secrets, errors/logging, Docker, basic CI/CD/deployment/security | Current official documentation, taught through one project | Tested public API consumed by Vue/Quasar, with logs and visible failure handling | ⬜ |
| 3. AI application patterns | structured outputs, validation, streaming, retries, cost/latency, evaluation; retrieval/tools/agents only when justified | Current provider docs + selected durable *AI Engineering* concepts | Evaluated AI feature with controlled failures and defensible architecture | ⬜ |
| 4. Product frontend | full-stack contracts, streaming UX, end-to-end debugging, product-quality Vue interface | Existing Vue skill + current provider/browser docs | Deployed full-stack product, demo, README, architecture walkthrough | ⬜ |
| 5. Reliability + differentiators | observability, eval automation, incident response, practical AI security, threat model | Official docs + measured product needs | Production-like reliability/security evidence and project defense | ⬜ |

Portfolio quality and `CAREER_EVIDENCE.md` run across phases rather than forming a separately numbered phase.

## Evidence and independence rules

- Meaningful capabilities use: **Introduced → Guided → Independent → Retained → Integrated → Production Evidence**.
- A Guided result cannot be promoted by completion alone. Independent requires a changed-context solution without implementation help; Retained requires later cold retrieval; Integrated requires combination with other capabilities; Production Evidence requires credible tested/deployed work.
- Correctness and fluency are separate. Track ability to start, hint count, trial-and-error, explanation clarity, and retrieval effort qualitatively; never use stressful speed tests.
- Each major phase should eventually cover: **Learn → Practice → Consolidate → Build → Explain → Ship**. Daily lessons do not need all six stages.
- `PROGRESS.md` is the capability truth; `REVIEW_QUEUE.md` drives retrieval; learning records preserve evidence; `CAREER_EVIDENCE.md` records only meaningful employer-facing milestones.

## Major-checkpoint audit

At a module project, phase exit, serious deployment, or readiness decision, evaluate separately:

**Knowledge · Independent Implementation · Retention · Integration · Debugging · Testing · Engineering Judgment · Product Judgment · Communication · Hiring Evidence**

Use the gaps—not calendar time—to choose reinforcement and application-readiness stage.

## Source hierarchy (binding)

1. **Active curriculum spine:** DeepLearning.AI "AI Python for Beginners" — transcripts fetched and taught directly; platform videos skipped.
2. **Conceptual spine:** Chip Huyen's *AI Engineering* PDF — selected only when a project or phase needs the concept; never treated as current API documentation.
3. **Changing technical facts:** official docs (Python, FastAPI, Pydantic, providers, deployment) — always wins over memory/books when they conflict; flag outdated material explicitly when found.
4. **Project evidence:** a resource is useful only when it improves an independently built, tested, explainable artifact.
5. Copyright rule: summarize + cite, never copy long passages into generated material.

## Governance rules enforced here

- Do not add overlapping curricula or large resource libraries without a specific capability gap in the current phase.
- RAG/agents/frameworks only enter when a real product requirement demands them.
- Domain-specific builds with real users/success criteria preferred over generic chatbot demos.
- Certificate deferred/dropped per mission decision — no subscription spending without explicit approval.
- Preserve the current sequence: no FastAPI, React, RAG, agents, MCP, cloud, DevOps, or advanced architecture before prerequisites and the current Python work are demonstrated.
- Progressively include unfamiliar code reading, documentation lookup, debugging, testing, refactoring, requirement clarification, and professional Git/PR workflow only when the current phase can support them.
