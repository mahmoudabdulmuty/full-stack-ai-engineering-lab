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

### Module 3 file and CSV pipelines — 2026-08-28

- **Evidence:** `practice/m3l4-extract-info.py`; `practice/m3l5-csv-itinerary.py`; `learning-records/0008-m3l4-extraction-writing-files-demonstrated.md`; `learning-records/0009-m3l5-csv-structured-data-demonstrated.md`.
- **Built:** multi-file prompt pipeline with saved output; CSV-to-row-dictionaries pipeline with deterministic filtering and selected-row prompt construction.
- **Debugged:** used observed output to repair stale variables, wrong handle mode/lifecycle, and `DictReader` string-vs-stream input.
- **Independence level:** **Guided** for the fragile file/reader and stale-variable repairs; cold rechecks remain scheduled. Do not claim Independent or Retained yet.
- **AI boundary:** local helper only echoes prompts; it does not prove model quality, semantic extraction, or real API integration.
- **Testing/deployment:** scripts ran clean and output was inspected; no automated tests, real provider, deployment, or production reliability evidence.
- **Interview story:** explaining why a live file handle is a stream for `DictReader`, while `f.read()` returns a string with different iteration behavior.
- **Career value:** useful integrated learning evidence; **not yet hiring evidence**.

## Current readiness audit

| Dimension | Current evidence | Important gap |
|---|---|---|
| Knowledge | M1–M2 closed; M3 files/data in progress | finish M3–M4 and verify Python-specific semantics |
| Independent implementation | learner-written practice and Module 2 capstone | more changed-context work with reduced scaffolding |
| Retention | several cold checks passed | CSV/file lifecycle and dict-key error remain scheduled |
| Integration | Module 2 capstone; M3 local pipelines | real API and cross-system integration |
| Debugging | meaningful output-led repairs | independently run the full diagnosis loop and add regression protection |
| Testing | manual execution checks | test-design reasoning and automated tests not started |
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
