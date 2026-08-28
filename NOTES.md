# NOTES.md

Working notes for tutoring sessions.

## Learner profile
- Frontend developer, 4 years: Vue 3 + Quasar + Pinia, LIGHT TypeScript (types only, not full TS). Strong on programming concepts, JS/TS analogies are the fastest route to understanding. NOT a Next.js/React dev (profile corrected at M2 close).
- Football loyalty: FC Barcelona (cúlé) + Al-Ahly Egypt (Ahlawy). Use THEIR players in analogies: Yamal, Pedri, De Jong, Cubarsí, Lewandowski; El Shenawy, Aboutrika, Emam Ashour. NEVER Real Madrid players — rival club (corrected at M2 close; apologies for the Vinicius era, files since swapped).
- Python beginner. Module 1 of the course complete (see learning-records).

## Teaching preferences (from user prompt)
- Socratic method: guide with questions, don't hand over answers.
- No spoilers on errors: explain what the error means, give a subtle hint. Only give corrected code after being explicitly asked twice.
- QUIZ INTEGRITY (learner request, M2 close): RANDOMIZE correct-answer positions in all MCQs — learner spotted the correct answer sat in slot 1 too often and gamed it deliberately. Vary position every question; keep options equal length where possible. Applies to lesson HTML + module reviews.
- TYPED-ANSWER UX (learner request, M2 close): coding inside HTML textareas is heavy for them (indentation pain). Keep `.typed` cards in reviews SHORT (1–3 lines max); real code practice always goes to practice files instead.
- Analogies: football/soccer preferred. NO cooking examples, ever.
- Mini challenges after each module — slightly tricky, not basic recall.
- Knowledge checks: don't let incomplete answers slide; don't over-push tangents outside current lesson scope.
- Keep pace reasonable.
- Honest and direct — no sugarcoating, action-oriented feedback.
- LESSON OPENING UX (learner feedback, M3L4, 2026-08-28): begin with a compact "match briefing" — connection to the previous lesson, why the new concept matters, one concrete before/after, then a small reasoning check before code. Keep the session interactive in short rounds; define unfamiliar terms (for example, "stub") using Vue/frontend analogies before testing them.
- **NEXT-CHAT OPENER (updated 2026-08-28):** use the compact prompt stored in `START_HERE.md`. New chats read `START_HERE.md` + the current temp handoff + current practice file; deeper governance documents load only on their listed trigger. Do not repeat the old full Operating System read-list at every startup.

## Working method (set at M2L2, updated M2L5)
- Code is ALWAYS written by the learner into per-lesson practice files under `practice\` — never in chat. Chat is for non-code answers only (predictions, explanations, scope questions).
- PREDICT-BEFORE-RUN (standard since M2L5): every print/challenge line gets an inline comment with the predicted output BEFORE running — predict first, run second, compare. Applies to ALL future challenges.
- AUTO-OPEN ARTIFACTS (standard since M2 close): whenever a session finishes building lesson/assessment HTML artifacts, open them immediately in the learner's default browser via `Start-Process <path>` — the learner should never have to hunt for files. Applies at end of every lesson and module session.
- Each lesson gets its own practice file (e.g. `practice\m2l2-for-loops.py`) with the course LLM helpers stubbed out (`print_llm_response` prints `[LLM] ...`, `get_llm_response` returns `[LLM reply] ...`) so scripts run locally with no API key. Run with: `python practice\<file>.py`.
- As new challenges start, previous challenge code gets commented out (`#`) and the new one is written fresh below its markers.
- Reference/comparison code snippets in chat are fine (answers to the learner's questions); challenge code is always theirs to write.

## Codex model + reasoning policy (reviewed 2026-08-28)
- **Preferred model:** `gpt-5.6-sol` — use the flagship model for this tutor because sessions combine source verification, learner-code grading, multi-file state, pedagogy, and long-horizon planning.
- **Default effort:** `high` for full lesson sessions, transcript synthesis, debugging/grading learner work, session close, module assessments, and roadmap reviews. Accuracy and continuity matter more here than minimum latency.
- **Fast path:** `medium` is acceptable for short definition questions, simple recall drills, and low-risk follow-ups when faster replies are preferred.
- Do not default to `xhigh` or `max`; reserve them for unusually difficult architecture, migration, or high-stakes review work only after a representative task shows a real quality gain.
- If usage/cost becomes the priority, use `gpt-5.6-terra` at `medium` as the balanced fallback. Do not use a smaller/faster model as the default tutor merely to save latency.
- Re-check current official OpenAI model guidance periodically because model names and recommended settings can change: https://developers.openai.com/api/docs/guides/latest-model

## Session workflow (user-defined)
1. Start of each lesson: fetch DeepLearning.AI / GitHub content, compare with learner's known material, flag gaps BEFORE teaching.
2. After last lesson of a module: knowledge check first, then deep dive + challenge.
3. End of each module: interview-style hard test — no hints, trick questions, follow-up pressure, combined concepts.
4. End of entire course: interview-style hard test per module.

## Progress
- Module 1: COMPLETE (incl. gap-fill on len(), round(), get_llm_response vs print_llm_response).
- Module 2: Lesson 1 "Completing a task list with AI" — Lists: COMPLETE. Covered creation, indexing, IndexError, append/remove, mutators-return-None, compaction, multi-line/heterogeneous lists, task list + LLM prompt wrapper. Learning record 0002 written. Repetition trap set for loops.
- Module 2: Lesson 2 "Repeating tasks with for loops" — COMPLETE. Covered for-loop syntax, loop-variable semantics + persistence (no block scope), indentation-as-membership trap, common errors (missing colon/indent), multi-line body, accumulator pattern (empty list + append), prompt-vs-response flow. Practice file `practice\m2l2-for-loops.py`. Learning record 0003 written. Dictionaries hook set for next lesson.
- Module 2: Lesson 3 "Prioritizing tasks with dictionaries and AI" — COMPLETE. Covered dict creation (curly braces, key: value), access by key (square brackets), KeyError on missing keys, safe access with .get() and in, add/update with same syntax, values of any type (incl. lists), priority dict-of-lists + for loop combo. Practice file `practice\m2l3-dictionaries.py`. Learning record 0004 written.
- Module 2: Lesson 4 "Customizing recipes with lists, dictionaries and AI" — COMPLETE. Covered extracting dict keys/lists into multi-line f-string prompts, chained lookups in f-strings, immutable evaluation timing of f-strings upon assignment. Practice file `practice\m2l4-custom-prompts.py`. Learning record 0005 written.
- Module 2: Lessons 5–6 "Comparing data" + "Helping AI make decisions" — COMPLETE as one COMPRESSED session (learner approved pacing change). Covered bools/comparisons (storable results, == vs = incl. keyword-arg TypeError), no-coercion equality, case-sensitive strings, and/or/not, if/else syntax + nesting, capstone pipeline (list-of-dicts → loop → branch → accumulator → len). Practice file `practice\m2l5-m2l6-comparisons-decisions.py` (shared for both lessons). Learning record 0006 written.
- Module 2 CAPSTONE: Book Tracker (local rebuild of graded assignment — learner has no premium account) — PASSED after 3 iterations. Self-discovered/fixed: JS shorthand `{title, author}` doesn't exist (keys must be string literals), set-vs-dict literals, `.toLowerCase()`→`.lower()` leak, early-return-in-loop vs guard-clause placement, dead code after return. Practice file `practice\m2-project-book-tracker.py`. Learning record 0007 written. Platform Quiz 2 done by learner; certificate deferred (optional $1 trial — learner's call, no pressure).
- Module 2 INTERVIEW TEST — PASSED (7/7 concepts, 2 corrected under pressure: return-trapdoor-in-loop traced mechanically, coercion leak at `"5" + 5`). Guard-clause pattern validated + NameError edge taught (init before loop / early-return shape).
- Module 2: FULLY CLOSED. `assessments\module-2-review.html` built (12 cards, shuffled answers per quiz-integrity rule, auto-opened). All M2 cheat-sheets, lessons 0004–0007, records 0006–0007 in place.
- Module 3 (next session): "Working with Your Own Data and Documents in Python" — mission-critical (files/documents), teach deep, not compressed. M3 intro lesson id `cu8ww`.
- Module 3 Lesson 4 "Extracting restaurant information from journal entries" — COMPLETE 2026-08-28. Transcript `x5zu6` fetched from authenticated course URL. Learner completed C1–C4 in `practice/m3l4-extract-info.py`: structured HTML/CSV prompts, seven-file loop, string accumulator, `"w"` + `.write()`, close/reopen `"r"`, read-back. Final script clean; output file has seven sections. Debug evidence: stale C2 variables in C3; writer/closed-handle read errors in C4; all repaired with guided tracing. Learner correctly explained stub vs real LLM and overwrite semantics. Next: M3L5 `jz515`.

## Practice-first output policy (updated 2026-08-28)
- Default lesson output: learner-written practice, inspected execution, explanation, evidence/review updates, and a concise handoff.
- Mahmoud owns `LEARNER_NOTES.md`. Every lesson ends with a mandatory lesson debrief: Mahmoud writes five short bullets from memory; the tutor discusses one strong point and one omission/fragile point without rewriting the note; then asks exactly one changed-context question. First miss → one focused hint and retry. Second miss → direct explanation, weak-point record, and later cold recheck.
- Extend or create a cheatsheet only for recurring syntax or patterns that deserve later lookup; consolidate by module or concept family.
- Build a visualizer only when state, lifecycle, scope, or data flow is materially clearer through interaction, or when a concept remains fragile after explanation. Existing visualizers remain useful concept labs; no automatic one-per-concept rule.
- Per-lesson HTML is not a default artifact. The seven redundant M1–M2 lesson pages were removed after this review; create future HTML only for a requested review need or a module assessment.
- End each module with a knowledge check, cold project, and `assessments\module-N-review.html` when the interactive format adds value.
- Target learning-time balance: roughly 70% code/debugging, 20% explanation/retrieval, 10% support artifacts.
- Update records only when their evidence threshold is met, refresh the handoff at session close, and auto-open only artifacts actually created or materially changed.

## Workspace facts
- Workspace root: `C:\Users\Mahmoud\Downloads\ai-python-tutor\`
- Mission = "all of it": own AI tools, extend dev stack, understand LLM calls. Certificate DROPPED (M2 close, learner confirmed) — maybe later via subscription. Deeper driver: escape prompt-jockey mode, rebuild hands-on engineering muscle. Career target: remote Full-Stack AI Engineer roles (US/EU/Gulf) — full plan in `ROADMAP.md` (agreed M2 close; tutor tracks solo-project progression against it).
- Folder map: `practice/` learner code, `LEARNER_NOTES.md` learner-owned retrieval notes, `reference/` consolidated cheatsheets and audits, `visualizers/` conditional concept labs, `assessments/` module reviews, `learning-records/`, `assets/`, `ROADMAP.md`, and `books/` (Chip Huyen's *AI Engineering* PDF — selective conceptual spine).
- Build pattern for later assessments: reuse `../assets/styles.css` + `../assets/quiz.js`; quiz cards need `.mcq`/`.typed` classes and the `#scorebar` block.
