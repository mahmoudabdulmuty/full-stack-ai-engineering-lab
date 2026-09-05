# CAREER_EVIDENCE — proof of engineering capability

Purpose: distinguish **“I studied this”** from **“I can credibly prove this.”**

Update this file only after a meaningful project, deployment, project defense, major phase exit, interview-ready debugging/ownership story, or readiness audit. Routine lessons belong in `PROGRESS.md`, `REVIEW_QUEUE.md`, and `learning-records/`.

## Evidence standard

For each milestone, record what can be verified:

- independently built and independently debugged;
- tested and integrated with another system;
- deployed and operated;
- architecture and trade-offs explained;
- failure handling and AI behavior evaluated;
- production-like reliability/security demonstrated;
- code, README, demo, logs, tests, or decision-record evidence;
- CV-ready claim and interview-ready story;
- remaining guidance and why it is not yet hiring evidence.

Use the capability ladder from `PROGRESS.md`: **Introduced → Guided → Independent → Retained → Integrated → Production Evidence**. Never upgrade a milestone because it was completed or because time passed.

## Current application-readiness stage

**Stage A — Learning**

Reason: Python foundations and local data/file pipelines are developing, with useful learner-written integration and debugging evidence. There is not yet a tested, real-API, deployed backend/AI product, so the workspace does not support Full-Stack AI hiring claims. Existing frontend professional experience remains a genuine strength outside this learning ledger.

## Milestone ledger

### Module 2 Book Tracker capstone — 2026-08-27

- **Evidence:** `practice/m2-project-book-tracker.py`; `learning-records/0007-book-tracker-capstone.md`.
- **Built:** learner-written local capstone combining functions, lists, dictionaries, loops, branches, accumulators, validation, and prompt construction.
- **Debugged:** repaired Python/JavaScript transfer mistakes, set-vs-dict confusion, method-name leakage, early return inside a loop, silent `None`, and dead code across three iterations.
- **Independence level:** strong learning evidence with self-discovered debugging; historical record predates the six-level ladder, so it is not retroactively promoted beyond its documented conditions.
- **Testing/deployment:** manually verified; no automated tests, README/demo, external integration, or deployment.
- **Interview story:** tracing an early return that stopped collection and correcting JavaScript-shaped assumptions in Python.
- **Career value:** credible foundational engineering evidence; **not yet CV-ready Full-Stack AI evidence**.

### Module 3 file and CSV pipelines — 2026-08-28 to 2026-09-05

- **Evidence:** `practice/m3l4-extract-info.py`; `practice/m3l5-csv-itinerary.py`; `practice/m3l6-reusable-functions.py`; `practice/m3l7-multi-city-itineraries.py`; `practice/module-3-quiz-assessment.py`; learning records `0008`–`0012`.
- **Built:** multi-file prompt and saved-output pipelines; CSV-to-row-dictionaries filtering; reusable parameterized readers; per-item prompt calls stored under dynamic keys; and a two-ticket report written and read back from disk.
- **Debugged:** used observed output to repair stale variables, wrong handle mode/lifecycle, `DictReader` string-vs-stream input, literal-key overwrite, and result-string overwrite across loop iterations.
- **Independence level:** **Guided overall**. The final assessment was completed, but Q5–Q6, Q8–Q9, and Q10 required material scaffolding or focused repair. Cold changed-context rechecks remain scheduled; do not claim Independent or Retained yet.
- **AI boundary:** correctly distinguished deterministic Python-owned inputs and file output from the echo helper's behavior. The helper does not prove model quality, semantic extraction, or real API integration.
- **Testing/deployment:** final scripts ran clean and outputs were inspected; no automated tests, real provider, deployment, or production reliability evidence.
- **Interview story:** explaining why a live file handle is a stream for `DictReader` while `f.read()` returns a string, and why an unchanged file read returns exact stored text rather than an interpretation.
- **Career value:** useful integrated learning evidence; **not yet hiring evidence**.

## Current readiness audit

| Dimension | Current evidence | Important gap |
|---|---|---|
| Knowledge | M1–M3 closed; Module 3 is Guided overall; M4 next | complete M4 and verify fragile Python-specific semantics on schedule |
| Independent implementation | learner-written practice, Module 2 capstone, and a guided Module 3 assessment | cold changed-context pipeline work with reduced scaffolding |
| Retention | several cold checks passed | file/CSV lifecycle, accumulators, and dynamic keys remain scheduled |
| Integration | Module 2 capstone and Module 3 local multi-file/CSV pipelines | real provider/API and cross-system integration |
| Debugging | meaningful output-led repairs | independently run the full diagnosis loop and add regression protection |
| Testing | manual execution and output checks | learner-owned regression tests begin in the first real AI automation |
| Engineering judgment | deterministic filtering vs LLM boundary explained | backend boundaries and alternatives not yet reached |
| Product judgment | roadmap constraints understood | requirements, users, success metrics, cost/reliability decisions not yet evidenced |
| Communication | English explanation track active | longer project demos, trade-offs, incidents, and architecture defense later |
| Hiring evidence | professional frontend experience plus foundation learning records | deployed, tested, documented Full-Stack AI product evidence |

## Future milestone template

### Milestone — date

- **Problem/user/success:**
- **Evidence links:**
- **Independently built:**
- **Independently debugged:**
- **Tests and failure handling:**
- **Systems integrated:**
- **Deployment/operation:**
- **AI evaluation/reliability/security:**
- **Architecture and trade-offs explained:**
- **Decision records:**
- **README/demo/CV-ready claim:**
- **Interview-ready story:**
- **Capability level and evidence:**
- **Still guided / remaining gap:**
- **Application-readiness impact:**

## Application-readiness stages

- **Stage A — Learning:** foundations developing; insufficient target-role evidence.
- **Stage B — Early Portfolio:** independent features/projects appearing; major backend/AI gaps remain.
- **Stage C — Credible Adjacent Applications:** evidence supports roles leveraging existing frontend experience plus growing backend/AI capability.
- **Stage D — Competitive Full-Stack AI Applications:** serious deployed work demonstrates required capabilities.
- **Stage E — Strong Target Positioning:** strong end-to-end ownership, project evidence, debugging, architecture reasoning, communication, and interview readiness.

Stages are evidence-based, non-binary, and never job guarantees.
