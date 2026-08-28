# REVIEW_QUEUE.md

Spaced retrieval schedule. Interval ladder per item: 1st review ~3 days → 2nd ~7 days → 3rd ~21–30 days → then fold into project work. Each review must use a GENUINELY NEW context/task, not renamed variables.

Rule: each session opens with 0–1 due item as a 5–10 min warm-up BEFORE new material. Learner answers cold; tutor grades honestly; item only leaves the queue after passing on schedule.

## Due now (seeded 2026-08-27 — past natural interval)

Do ONE per session until cleared. New-context tasks below are first-pass drafts — vary further at delivery.

| Item | Origin | Status | Warm-up task (new context) | Last result | Next due |
|---|---|---|---|---|---|
| Accumulator pattern | 0003/0007 | ✅ PASSED CHECK (2026-08-27) — D1 ran clean, predicted 2, got 2; init-before-loop confirmed. Residual: case-lowering before `in` (weak-spot #4, re-rolled below) | Given 3 filenames, count how many contain the word "the" using a loop + accumulator; store result in variable named so it survives loop exit. No hints. → now **Drill 6** in mini-drill, learner code pending | — | re-roll into capstone practice ~21–30d |
| Dict safe access (KeyError vs `.get()` vs `in`) | 0004 | Demonstrated | Temperature log dict with 7 keys; ask about 8th key two ways; predict which errors and why. Then guard an f-string lookup. | — | queued |
| f-string freeze timing | 0005 | Demonstrated | Assign f-string to var, change source vars, print var — predict before run; explain what was frozen at assignment. | — | queued |
| Return semantics + mutators-return-None | 0002/M1 | Demonstrated | One function where the bug is `list.append(...)` assigned to a var and returned; trace output aloud. | — | queued |
| Set-vs-dict literals + string keys | 0007 | Demonstrated | Predict TypeError type and message for `{name}` followed by `[0]`; contrast working dict literal. | — | queued |
| Guard clauses & early returns placement | 0007 | Demonstrated | Two near-identical loops differing only in check placement inside vs before loop; explain outputs. | — | queued |

## Scheduled (later ladder steps)

| Item | Current step | Scheduled context idea |
|---|---|---|
| Comparisons / if-else nesting / bool operators | awaiting first timed re-test | fold into M3L4 or Quiz-3 prep: relevance logic with `and` conditions on file content |
| JS→Python method translation | recurring watchlist | random spot-check: given JS snippet, produce Python equivalent cold (`.toLowerCase`, `.trim`, ternary, spread vs `*unpack`) |
| CWD-relative paths (Demonstrated 2026-08-27 — self-recovered in M3L3 C1) | first formal review | M3L4+: a script that reads data with a `try`/absolute-path backstop; learner predicts the failure mode then runs |
| `in`-on-strings case choice (weak-spot #4; still Demonstrated 2026-08-27 — M3L3 C4 filter used `"relevant" in response` correctly) | first formal review | after M3L4: stub-modified `get_llm_response` returning `RELEVANT` (uppercase) for one file — does the same filter pass or fail? predict then run |
| File mode + handle lifecycle (Demonstrated 2026-08-28) | first formal review | M3L5+: create a short report with `"w"`, close it, reopen with `"r"`, and predict both the second-run contents and the errors caused by reading the writer/closed handle. No scaffold. |
| Stale variables across consecutive loops (M3L4 C3) | targeted re-probe | Give two loops over different datasets where the second loop accidentally interpolates the first loop's variables; learner traces output and repairs without naming the stale variables. |

## Completed reviews

| Date | Item | Result |
|---|---|---|
| 2026-08-27 | Accumulator pattern (review queue seeded item) | Cold, no hints. D1 ran clean; output `2` matched prediction on first try. Confirmed init-before-loop; list accumulator survives loop exit. Single residual: Drill D5 predicted "2" but actual `"a" in item.lower()` matched 3 — learner forgot the check runs on the lowered copy. Moved to weak-spot #4 + scheduled review row; Drill 6 (the "the"-files task) left as next warm-up. |
| 2026-08-27 | CWD-relative paths (re-probe during M3L3 C1) | Self-recovered: ran from `practice\data` with `open("cape-town.txt", ...)`; reflected, switched paths, articulated the rule (terminal CWD = where Python looks; open() path is relative to terminal, not script). Moved to Demonstrated. |
| 2026-08-27 | `in`-on-strings case choice (M3L3 C4) | Code correct: `if "relevant" in response:`. Predicted 2 files; actual 3 (stub echoes prompt). Learner explained cause after run (stub includes the word in its own instructions). Capability Demonstrated, predict-grounding lesson captured. |
