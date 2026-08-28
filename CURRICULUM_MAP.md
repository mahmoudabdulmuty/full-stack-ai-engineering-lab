# CURRICULUM_MAP.md

Goal → source → capability → project-evidence map. Governed by the tutor Operating System (source hierarchy, learning progression). Revisit at module retrospectives; roadmap-vs-evidence check every 4–6 weeks.

## North star

Pragmatic Full-Stack AI Product Engineer. Ultimate test: can Mahmoud independently ship, debug, explain, and improve a useful AI-powered product feature?

## Phase map (from ROADMAP.md + progression rules)

| Phase | Target capabilities | Primary source | Project evidence (target) | Status |
|---|---|---|---|---|
| 1. Python fundamentals + debugging discipline | Ledger #1–8 | DeepLearning.AI AI Python for Beginners M1–M2 | Book Tracker capstone (`learning-records/0007`) | ✅ DONE |
| 2. Local automations: files/data → transform → LLM call → validate → save output | Ledger #9–11, + writing output files | DL.AI M3 (+M4), official Python docs for time-sensitive details (e.g. pathlib, encoding) | Personal automation script (mission: automate his own busywork) | 🔄 IN PROGRESS (M3) |
| 3. Backend foundations | HTTP, FastAPI, Pydantic, PostgreSQL, testing basics, Docker, deployment | Official FastAPI, Pydantic, PostgreSQL, pytest, and Docker documentation; taught through the current project | Small API serving an LLM feature | ⬜ |
| 4. AI application patterns | Structured outputs, tool use, streaming, embeddings + retrieval WHEN justified, retries/cost/latency, evals, observability | Chip Huyen *AI Engineering* (selected chapters, never cover-to-cover), official provider documentation, and maintained first-party examples | Feature with error handling + basic eval harness | ⬜ |
| 5. Frontend AI experiences | Vue/Quasar-first; React/Next optional market-expansion later | His own strength + provider docs | Connected full-stack feature | ⬜ |
| 6. Portfolio | Two deep, deployed, documented projects w/ README: problem, approach, trade-offs, limitations | — | `CAREER_EVIDENCE.md` entries | ⬜ |

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
