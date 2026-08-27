# PROGRESS.md

Evidence-based progress tracking. Updated every session close. Source hierarchy: this file > NOTES.md history sections.

Last updated: 2026-08-27 · Current module: **Module 3 — Working with Your Own Data and Documents** (in progress)

## Capability ledger

Statuses: `Introduced` → `Practicing` → `Demonstrated` (observable evidence only) → periodic re-check via REVIEW_QUEUE.

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

## Weak spots (watchlist)

1. **CWD-relative path reasoning** — patched once (2026-08-27); expect it to surface again when scripts run from different folders. Probe during M3L3 C2/C4.
2. **JS→Python leak class under pressure** — `.toLowerCase()`→`.lower()`, `{a,b}` shorthand/set-literal, early-return-in-loop (0007). Re-probe at module review with changed inputs.
3. **Predict-before-run discipline** — standard since M2L5; keep enforcing inline prediction comments.
4. **Case-choice before `in`-checks on strings** — D5: predicted "2 matches" for `"a" in item.lower()` because "GAMMA" has no lowercase `a`; forgot the check runs on the **lowered copy**. Expect the same slip when the classification filter lands in M3L3 C4. Probe: flip the drill input and re-predict.

## Session log (most recent last)

- **2026-08-27 (early)**: Handoff resumed. Graded M3L2 retroactively (C1–C4 pass after comment fix); CWD confusion resolved. M3L3 transcript fetched, 3 data files + practice file created. Governance layer adopted (this file set). Wrote M2 weak-spot mini-drill (D1–D5) incl. accumulator recall.
- **2026-08-27 (later)**: M3L3 session 2. Ran + graded mini-drill: D1–D4 predictions correct, D5 WRONG (predicted 2, actual 3 — case-lowering before `in`; "GAMMA"→"gamma" matches). Accumulator init-before-loop confirmed via D1. Ledger: added #12 (`in` on strings, Introduced), weak-spot #4. Scaffolded **Drill 6** (file accumulator, "the" across the 3 data files) in mini-drill file. **Taught M3L3 C1–C4 guidance** — learner's code pending next session.
- **2026-08-27 (close)**: M3L3 closed. Drill 6: code right, predicted all-3 (additive mistake — counted occurrences, not files) — partial credit; corrected. C1 ✅. C2 ⚠️ (`print(file)` vs `print(req_file)` — fixed in chat). C3 ✅ code; **prediction miss**: madrid file actually contains "tapas"/"dinner" so "odd-one" label was wrong; lesson: ground predictions in the text the LLM will see, not in file labels. C4 ✅ code; **prediction miss**: predicted 2 files, got 3 — but learner **explained the cause correctly** post-run (stub includes the word "relevant" in its own instructions → always-true filter). CWD lesson moved Demonstrated (self-recovered when `cd`-ing into `practice\data` and re-anchoring the rule). Ledger updated: #10, #11, #12 all Demonstrated. Files cheatsheet + visualizer built. Next: M3L4 (transcript x5zu6 retry).

## M3 lesson tracker

- M3L1 Using files in Python — COMPLETE (Demonstrated)
- M3L2 Loading and using your own data — COMPLETE, graded ✅✅✅⚠️→fixed
- M3L3 Reading journals from food critics — ✅ CLOSED 2026-08-27 (C1 ✅, C2 ⚠️→fixed, C3 ✅ code / ⚠️ prediction-grounding, C4 ✅ code / ❌ prediction / ✅ explanation; capability Demonstrated, predict-grounding lesson captured)
- M3L4–L7, Quiz 3, module 3 artifact/assessment — not started (transcripts x5zu6/jz515/vvkwa/fvhf6 fetch pending)
