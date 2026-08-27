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
- **NEXT-CHAT OPENER (learner request, M3L3 close, 2026-08-27):** at the end of every lesson / session close, the tutor provides a short copy-pasteable block the learner can paste into the next chat to start it. Format: (1) greeting + workspace path, (2) Operating System protocol read-list, (3) the one specific thing to do next. Plain language, no jargon. Persistent across all future agents.

## Working method (set at M2L2, updated M2L5)
- Code is ALWAYS written by the learner into per-lesson practice files under `practice\` — never in chat. Chat is for non-code answers only (predictions, explanations, scope questions).
- PREDICT-BEFORE-RUN (standard since M2L5): every print/challenge line gets an inline comment with the predicted output BEFORE running — predict first, run second, compare. Applies to ALL future challenges.
- AUTO-OPEN ARTIFACTS (standard since M2 close): whenever a session finishes building lesson/assessment HTML artifacts, open them immediately in the learner's default browser via `Start-Process <path>` — the learner should never have to hunt for files. Applies at end of every lesson and module session.
- Each lesson gets its own practice file (e.g. `practice\m2l2-for-loops.py`) with the course LLM helpers stubbed out (`print_llm_response` prints `[LLM] ...`, `get_llm_response` returns `[LLM reply] ...`) so scripts run locally with no API key. Run with: `python practice\<file>.py`.
- As new challenges start, previous challenge code gets commented out (`#`) and the new one is written fresh below its markers.
- Reference/comparison code snippets in chat are fine (answers to the learner's questions); challenge code is always theirs to write.

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

## Build rule — apply to every lesson as we grow (learner request)
For every lesson completed, keep the workspace in sync:
- `reference\<topic>-cheatsheet.md` — reference cheat-sheet.
- `lessons\NNNN-<slug>.html` — self-contained HTML lesson (reuse assets/styles.css + assets/quiz.js; .mcq/.typed cards, #scorebar, links to references + primary source + ask-tutor reminder). Every lesson ends with navigation links: Back to the previous lesson AND "Next: see Lesson NNNN — Title (Module X Lesson Y)" — when lesson N+1 is built, add its Next link to lesson N.
- `visualizers\` (learner request, M2 close): an INTERACTIVE VISUALIZER for every core concept, built the session we learn it; hub page `visualizers\index.html` tracks ready/coming. Ready: loop-and-return, list-seats, accumulator, fstring-freeze, dict-drawers. Coming: functions/None + variables/types (M1 revisits), comparisons/bool-logic (M2L5 revisit), files/documents (with M3).
- End of each module: `assessments\module-N-review.html` — interactive test mirroring locked Quiz N + graded assignment.
- Update NOTES.md progress, GLOSSARY.md (terms only after demonstrated understanding), learning-records/ (only on demonstrated understanding).
- Refresh the handoff doc in temp at end of each session.

## Workspace facts
- Workspace root: `C:\Users\Mahmoud\Downloads\ai-python-tutor\`
- Mission = "all of it": own AI tools, extend dev stack, understand LLM calls. Certificate DROPPED (M2 close, learner confirmed) — maybe later via subscription. Deeper driver: escape prompt-jockey mode, rebuild hands-on engineering muscle. Career target: remote Full-Stack AI Engineer roles (US/EU/Gulf) — full plan in `ROADMAP.md` (agreed M2 close; tutor tracks solo-project progression against it).
- Folder map: `reference/` cheat-sheets (module1, lists, for-loops, dictionaries, custom-prompts, comparisons-conditionals), `lessons/` HTML lessons (0001–0007), `visualizers/` interactive concept visualizers (hub: index.html — standing artifact per concept), `assessments/` (module-1-review, module-2-review), `learning-records/`, `assets/`, `practice/` (learner scripts, helpers stubbed), `ROADMAP.md`, `books/` (Chip Huyen "AI Engineering" PDF — spine book, teach around chapters), `courses/` (Datacamp Associate AI Engineer track: OpenAI API, Embeddings, Vector DBs/Pinecone, LangChain, LLMOps Concepts, Hugging Face — has .vtt scripts + exercise .md files; mine as teaching material for Phases 3–5).
- Build pattern for later: new lesson/assessment HTML reuses `../assets/styles.css` + `../assets/quiz.js`; quiz cards need `.mcq`/`.typed` classes and the `#scorebar` block.