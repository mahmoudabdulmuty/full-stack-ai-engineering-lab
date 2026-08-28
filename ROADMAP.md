# ROADMAP — Full-Stack AI Engineer Transition

Target: remote roles (US / Europe / Gulf-UAE-KSA), visa relocation later.
Positioning: **pragmatic product engineer** — FastAPI + modern frontend + LLM orchestration/RAG. NOT an ML researcher. Skip ML-math-from-scratch content.

## Standing rules (non-negotiable)

1. **Solo builds.** Tutor reviews, never writes. (Anti prompt-jockey rule.)
2. **Every phase ends with a DEPLOYED artifact** — never a completed playlist.
3. **Patterns over frameworks.** LangChain/LangGraph churn; retrieval, tool-use, and routing patterns persist.
4. **Two deployed, README-documented, demo-able projects beat three shallow ones.**
5. English-first GitHub / README / LinkedIn — the US/EU/Gulf remote funnel runs on it.

## Phase 1 — Python Core (NOW — this workspace)

- Course curriculum M1–M4 (M2 done), drills, visualizers, interview tests.
- Solo mini-project per module (80% known skills + 20% new).
- Add when M4 arrives: type hints, async/await basics (needed for streaming + concurrent LLM calls).
- **Exit artifact:** per-module solo mini-projects + the personal automation capstone script.

## Phase 2 — Production Backend

- FastAPI, Pydantic (structured LLM outputs = data contracts), SSE streaming, PostgreSQL (+ SQLModel), **Docker** (moved here — mandatory, not Phase-5 garnish).
- **Exit artifact:** an LLM-backed API deployed publicly (Railway / Fly.io / Render).

## Phase 3 — AI application patterns (the differentiator)

- Start with one current foundation-model API. Add structured outputs, streaming, retries, cost/latency controls, and evaluation before adding abstraction. Introduce tool use, embeddings, retrieval, vector storage, hybrid search, agents, or MCP only when a product requirement and evaluation justify them.
- **Exit artifact:** Enterprise Document Copilot v1 (the flagship product; retrieval enters only if its evidence supports it).

## Phase 4 — Product frontend layer

- Connect the first backend through Mahmoud's existing Vue 3 / Quasar / Pinia strength so the initial full-stack artifact ships quickly.
- React/Next.js is optional market expansion after the first deployed product, not a prerequisite. Choose its current official stack only when that phase begins.
- **Exit artifact:** a polished, streaming Vue/Quasar interface on the Document Copilot; optional later React/Next.js port.

## Phase 5 — Differentiators

- Evaluation datasets and automated graders, tracing/observability, guardrails, and LLM security awareness. Choose current tools from official documentation when the product reaches this phase.
- Optional specialization (only if time/interest): voice agents via realtime APIs — do NOT hand-build cascaded WebRTC pipelines.
- **Exit artifact:** Text-to-SQL Analytics Dashboard + evals wired into the Copilot.

## Portfolio (build order)

1. **Enterprise Document Copilot** — Vue/Quasar + FastAPI + Pydantic validation + streaming first; add PostgreSQL/retrieval only when its evaluated use case needs them. Flagship.
2. **Text-to-SQL Analytics Dashboard** — NL → validated SQL → PostgreSQL → dynamic charts.
3. _(Optional)_ Voice support agent — realtime-API-based, cut scope ruthlessly.

## Honest timeline

6–9 months of consistent part-time work from Python-fundamentals-complete to genuinely competitive applications. Ignore "$150K in 6 months" hooks — they sell communities, not careers.

## Sources feeding this plan

- `MISSION.md` and the capability evidence in `PROGRESS.md` / `learning-records/`
- The verified minimal stack and source hierarchy in `RESOURCES.md`
- Chip Huyen's *AI Engineering* for durable system concepts, selected around project needs
- Current official Python, framework, provider, database, testing, and deployment documentation for implementation details
