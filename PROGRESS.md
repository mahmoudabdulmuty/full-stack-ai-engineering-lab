# PROGRESS.md

Evidence-based progress tracking. Updated every session close. Source hierarchy: this file > NOTES.md history sections.

Last updated: 2026-09-03 · Current module: **Module 3 — Working with Your Own Data and Documents** (in progress)

Current lesson: **M3L6 — Turning code blocks into reusable functions**. Official transcript `vvkwa` fetched; `print` vs `return` warm-up passed. Current practice file: `practice/m3l6-reusable-functions.py`. Immediate next action: learner implements Round 1 `read_journal(file_path)` and runs the two-call prediction check.

## Capability ledger

For new or next-reviewed meaningful capabilities, use:

1. **Introduced** — taught, not yet demonstrated.
2. **Guided** — completed with meaningful hints or repair assistance.
3. **Independent** — solved in a changed context without implementation help.
4. **Retained** — reproduced cold after spacing.
5. **Integrated** — combined correctly with other capabilities.
6. **Production Evidence** — demonstrated in credible tested/deployed engineering work.

Rows created before 2026-09-03 keep their historical `Practicing` / `Demonstrated` labels so the existing state is not rewritten without evidence. `Demonstrated` means observable evidence under the listed conditions; it does **not** automatically mean Independent, Retained, Integrated, or Production Evidence. Migrate a row only when a later task supplies the required evidence. A guided repair never silently becomes independent mastery.

| # | Capability | Status | Evidence | Conditions met | Next review |
|---|---|---|---|---|---|
| 1 | Variables, f-strings, print vs stored responses, len/round | Demonstrated | Module 1 complete (`learning-records/0001`), interview test | cold recall, pressure | via queue |
| 2 | Lists: create/index/slice, append/remove, mutators-return-None, IndexError | Demonstrated | `0002`, `assessments/module-2-review.html` | task-list build, no hints | via queue |
| 3 | For loops: syntax, loop-var persistence, no-block-scope traps | Demonstrated | `0003` | repeat-trap, explain-the-bug | via queue |
| 4 | Accumulator pattern (init + collect-then-use) | Demonstrated | `0003`, `0007` capstone part 4 | new filtering task solo | via queue |
| 5 | Dicts: key access, KeyError, `.get()`, `in` safe access, add/update, any-type values | Demonstrated | `0004` | priority-dict build | via queue |
| 6 | Multi-source f-string prompts (lists + dicts interpolated) | Demonstrated | `0005` | recipe customizer | via queue |
| 7 | Bools, comparisons (`==` vs `=`), case-sensitive strings, and/or/not, if/else nesting | Demonstrated | `0006` | compressed-session assessment | via queue |
| 8 | Capstone-level integration: list-of-dicts → loop → branch → accumulator → len | Demonstrated | `0007` Book Tracker, self-debugged 5 bugs | blank-file build, 3 iterations | via queue |
| 9 | Files: open/read/close, print content | Demonstrated | M3L1 (`practice/m3l1-*` per handoff) | single file, known path | via queue |
| 10 | CWD-relative paths: why identical code succeeds/fails by run location | **Demonstrated** | M3L2 C4 + M3L3 C1 self-recovery (learner `cd`-ed into `practice\data` and re-anchored the rule from a single experiment, 2026-08-27) | self-recovered without hint | re-probe at M3L4+ |
| 11 | Loop over MANY files + LLM classification pipeline | **Demonstrated** | M3L3 C1–C4 (`practice/m3l3-food-critics.py`, all four pass code-wise) | new pipeline solo | re-probe in M3L4/M3L5 |
| 12 | `in` operator on strings (substring, case choice, `.lower()`) | **Demonstrated** | M3L3 C4 filter `if "relevant" in response:`; Drill-5 lesson learned & corrected | file+LLM context | re-probe in C4 re-roll (case-choice row) |
| 13 | Structured extraction prompts + stub-vs-real-LLM boundary | **Demonstrated** | M3L4 C1–C3 (`practice/m3l4-extract-info.py`); learner explained that the stub echoes the prompt rather than performing extraction | HTML/CSV prompt contracts, seven-file loop | re-probe in M3L5 |
| 14 | Write/read file lifecycle: `"w"`, `.write()`, close, reopen `"r"`, read back | **Demonstrated** | M3L4 C4 final clean run; M3L5 cold opener correctly predicted that `open(..., "w")` truncates immediately, so a crash before `.write()` leaves the file empty. | string accumulator → disk → verified read-back + cold truncation timing | later mixed-mode/closed-handle recheck |
| 15 | CSV structured-data pipeline: `csv.DictReader` → list of dicts → deterministic filter → selected-row prompt | **Demonstrated, fragile retrieval** | M3L5 R1–R3 (`practice/m3l5-csv-itinerary.py`), final run clean; six rows loaded, two Egypt rows filtered, Alexandria row selected by city and passed into stub prompt. Post-close learner reported the combined file/handle/reader lifecycle still felt confusing. | repaired string-vs-file-handle bug, adopted `with`, predicted outputs, explained deterministic-vs-LLM boundary | consolidated notes + visualizer added; cold recheck reader lifetime/input in M3L6+ |

## Fluency signals (separate from correctness)

For recurring foundational skills, record only useful qualitative signals: ability to start independently, hint count, unnecessary trial-and-error, explanation clarity, and retrieval effort. Correct but hesitant work can need retrieval practice without being marked incorrect. Do not use speed tests. Current fragile-retrieval labels and weak spots remain unchanged until new evidence appears.

## Weak spots (watchlist)

1. **CWD-relative path reasoning** — patched once (2026-08-27); expect it to surface again when scripts run from different folders. Probe during M3L3 C2/C4.
2. **JS→Python leak class under pressure** — `.toLowerCase()`→`.lower()`, `{a,b}` shorthand/set-literal, early-return-in-loop (0007). Re-probe at module review with changed inputs.
3. **Predict-before-run discipline** — standard since M2L5; keep enforcing inline prediction comments.
4. **Case-choice before `in`-checks on strings** — D5: predicted "2 matches" for `"a" in item.lower()` because "GAMMA" has no lowercase `a`; forgot the check runs on the **lowered copy**. Expect the same slip when the classification filter lands in M3L3 C4. Probe: flip the drill input and re-predict.
5. **Stale variables across successive loops** — M3L4 C3 initially used C2's `content` and `fileName`, causing every prompt/label to appear as Tokyo. Learner repaired prompt content first, then the label after output-based tracing. Re-probe with a changed two-loop task.
6. **File-handle mode/lifecycle and truncation timing** — M3L4 C4 first read from a `"w"` handle (`UnsupportedOperation`), then read after closing it (`ValueError`). Final version correctly closes the writer and reopens in `"r"`. In the later note debrief, learner twice predicted `OLD` survives when a crash occurs after `open(..., "w")` but before `.write()`; direct explanation established that opening in `"w"` truncates immediately. Re-probe cold.
7. **Missing dict key vs missing list index** — M3L5 R3 robustness discussion: learner correctly saw a failed search leaves `{}`, but predicted `selected_stop["City"]` raises `IndexError`. Direct explanation: missing dict key → `KeyError`; missing list position → `IndexError`. Scheduled without list context.

## Session log (most recent last)

- **2026-08-27 (early)**: Handoff resumed. Graded M3L2 retroactively (C1–C4 pass after comment fix); CWD confusion resolved. M3L3 transcript fetched, 3 data files + practice file created. Governance layer adopted (this file set). Wrote M2 weak-spot mini-drill (D1–D5) incl. accumulator recall.
- **2026-08-27 (later)**: M3L3 session 2. Ran + graded mini-drill: D1–D4 predictions correct, D5 WRONG (predicted 2, actual 3 — case-lowering before `in`; "GAMMA"→"gamma" matches). Accumulator init-before-loop confirmed via D1. Ledger: added #12 (`in` on strings, Introduced), weak-spot #4. Scaffolded **Drill 6** (file accumulator, "the" across the 3 data files) in mini-drill file. **Taught M3L3 C1–C4 guidance** — learner's code pending next session.
- **2026-08-27 (close)**: M3L3 closed. Drill 6: code right, predicted all-3 (additive mistake — counted occurrences, not files) — partial credit; corrected. C1 ✅. C2 ⚠️ (`print(file)` vs `print(req_file)` — fixed in chat). C3 ✅ code; **prediction miss**: madrid file actually contains "tapas"/"dinner" so "odd-one" label was wrong; lesson: ground predictions in the text the LLM will see, not in file labels. C4 ✅ code; **prediction miss**: predicted 2 files, got 3 — but learner **explained the cause correctly** post-run (stub includes the word "relevant" in its own instructions → always-true filter). CWD lesson moved Demonstrated (self-recovered when `cd`-ing into `practice\data` and re-anchoring the rule). Ledger updated: #10, #11, #12 all Demonstrated. Files cheatsheet + visualizer built. Next: M3L4 (transcript x5zu6 retry).
- **2026-08-28 (close)**: M3L4 transcript fetched from the authenticated DeepLearning.AI lesson (`x5zu6`) and taught source-first. C1 ✅ extraction-prompt pipeline + stub boundary explained. C2 ✅ Tokyo CSV contract, grounded prediction of 5 restaurants. C3 ✅ after guided repair of stale C2 variables and removal of Madrid: seven filenames match seven journal contents. C4 ✅ after two file-handle debugging rounds: string accumulator, newline-separated entries, write with `"w"`, close, reopen `"r"`, read back, final run exit 0; generated file has 7 sections. Knowledge check: correctly predicted `OLD` is discarded and only `NEW` remains after `"w"`. Next: M3L5 transcript `jz515`.
- **2026-08-28 (M3L4 note debrief)**: Learner's note accurately recalled the multi-file pipeline, stale-variable repair, writer/read-handle separation, and stub boundary. Changed-context question exposed a narrower gap: twice predicted `OLD` remains if execution crashes after `open(..., "w")` but before `.write()`. Direct explanation given: truncation happens during open. Scheduled a cold M3L5+ recheck.
- **2026-08-28 (M3L5 close)**: Authenticated transcript `jz515` fetched and compared with prior capability. Cold opener passed: `"w"` truncates at open. R1 initially passed `f.read()` string into `csv.DictReader`, producing character-level rows; learner repaired it by passing the open file handle and adopted a `with` context manager. R2 filtered six structured rows to Cairo/Alexandria without an LLM. R3 selected Alexandria by semantic city search (accepted real-world alternative to fixed index), built the dated prompt, and correctly explained the local stub boundary. Final run exited 0. Debrief completed after one hint on reader/file lifetime. Missing dict key was confused with `IndexError`; direct `KeyError` explanation given and cold recheck scheduled.
- **2026-08-28 (M3 file-flow consolidation)**: After close, learner explicitly reported confusion across the combined `open`/mode/handle/`read`/`write`/`with`/`DictReader` lifecycle and requested interview-ready notes plus a visualizer. Expanded the single files cheatsheet into a complete decision/error/interview guide and extended `visualizers/files.html` with a four-object map, lazy CSV-reader stepper, `f.read()` failure state, and error clinic. JavaScript, DOM references, interactions, and 360px responsive layout verified. This support does not replace the scheduled cold recheck.
- **2026-08-28 (parallel professional-English track)**: Learner requested English-only tutor replies even when he writes in Arabic, while keeping Arabic available for expressing difficult ideas. Added `ENGLISH_INTERVIEW_TRACK.md`: technical explanations, prediction/debug narration, one focused correction at a time, recovery phrases, a short mock interview at each module checkpoint, and realistic engineering-meeting/client communication practice.
- **2026-09-03 (learning-system/roadmap upgrade)**: Audited the active governance, roadmap, evidence, review, English, resource, learning-record, and practice workflow. Added the six-level evidence ladder, phase-aware scaffolding/prediction/retrieval, long-term engineering modes and readiness gates, and `CAREER_EVIDENCE.md` without changing learner code or weak-point state. Reconstructed the missing handoff. M3L6 remains active: transcript fetched, `print`/`return` warm-up passed, Round 1 implementation pending.

## M3 lesson tracker

- M3L1 Using files in Python — COMPLETE (Demonstrated)
- M3L2 Loading and using your own data — COMPLETE, graded ✅✅✅⚠️→fixed
- M3L3 Reading journals from food critics — ✅ CLOSED 2026-08-27 (C1 ✅, C2 ⚠️→fixed, C3 ✅ code / ⚠️ prediction-grounding, C4 ✅ code / ❌ prediction / ✅ explanation; capability Demonstrated, predict-grounding lesson captured)
- M3L4 Extracting restaurant information from journal entries — ✅ CLOSED 2026-08-28 (C1–C4 final code clean; stub boundary + overwrite behavior explained; file-handle lifecycle scheduled for cold review)
- M3L5 Vacation planning using CSV files — ✅ CLOSED 2026-08-28 (R1–R3 clean final run; `DictReader`, context manager, deterministic filter, row-to-prompt pipeline demonstrated; reader lifetime scheduled for cold recheck)
- M3L6 Turning code blocks into reusable functions — 🔄 IN PROGRESS (transcript `vvkwa` fetched; warm-up passed; `practice/m3l6-reusable-functions.py` Round 1 awaiting learner implementation)
- M3L7, Quiz 3, module 3 artifact/assessment — not started (transcript `fvhf6` pending)
