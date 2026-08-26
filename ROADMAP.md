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

## Phase 3 — AI Orchestration & RAG (the differentiator)

- Foundation model APIs (OpenAI / Claude / DeepSeek / Groq), function calling & tool use, structured outputs, embeddings, vector store (pgvector or Chroma), document chunking pipelines, hybrid search (BM25 + dense + reranking), agents + LangGraph _patterns_, MCP awareness.
- **Exit artifact:** Enterprise Document Copilot v1 (the flagship RAG project).

## Phase 4 — Modern Frontend Layer (2–4 weeks, not a phase)

- React 19 / Next.js App Router + TypeScript + TanStack Query + Zustand + shadcn/ui + Vercel AI SDK (streaming chat UI). Fast pickup — 4 years of Vue/Quasar transfers directly.
- Slot: AFTER first deployed backend, BEFORE capstone polish.
- **Exit artifact:** Next.js UI on the Document Copilot.

## Phase 5 — Differentiators

- Evals (Ragas, LLM-as-a-judge), tracing/observability (LangSmith), guardrails + LLM security awareness.
- Optional specialization (only if time/interest): voice agents via realtime APIs — do NOT hand-build cascaded WebRTC pipelines.
- **Exit artifact:** Text-to-SQL Analytics Dashboard + evals wired into the Copilot.

## Portfolio (build order)

1. **Enterprise Document Copilot** — Next.js + FastAPI + pgvector + Hybrid RAG + Pydantic validation + streaming. Flagship.
2. **Text-to-SQL Analytics Dashboard** — NL → validated SQL → PostgreSQL → dynamic charts.
3. _(Optional)_ Voice support agent — realtime-API-based, cut scope ruthlessly.

## Honest timeline

6–9 months of consistent part-time work from Python-fundamentals-complete to genuinely competitive applications. Ignore "$150K in 6 months" hooks — they sell communities, not careers.

## Sources feeding this plan

- Learner's Gemini-synthesized 5-phase roadmap (agreed with tweaks above)
- Reddit consensus on DL.AI gaps (production skills, deployment, end-to-end projects)
- John Crickett principle: "10 years to become a great engineer, one day to learn the tools — don't skip the first part." This roadmap IS the first part, in application-layer form.
