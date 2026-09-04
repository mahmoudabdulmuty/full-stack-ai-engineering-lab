# REVIEW_QUEUE.md

Spaced retrieval schedule. Interval ladder per item: 1st review ~3 days → 2nd ~7 days → 3rd ~21–30 days → then fold into project work. Each review must use a genuinely new context/task, not renamed variables.

Rule: each session opens with 0–1 due item as a 5–10 min warm-up BEFORE new material. Learner answers cold; tutor grades honestly; item only leaves the queue after passing on schedule.

Rechecks should progressively increase transfer distance: unfamiliar domain or dataset → incomplete existing program → interacting concepts → deliberately inserted bug/edge case → ambiguous requirement where the learner chooses the relevant concepts. Do not reveal the bug category or failing line once debugging independence is being tested. Record meaningful hints/repair assistance so Guided is never mistaken for Independent.

Keep retrieval lean: schedule meaningful or fragile capabilities, not every syntax detail. Require explicit prediction mainly when the mental model, state transition, failure, or integration is under test. Fluency observations (start independence, hint count, trial-and-error, explanation clarity, retrieval effort) are qualitative and separate from correctness.

## Due now (seeded 2026-08-27 — past natural interval)

Do ONE per session until cleared. New-context tasks below are first-pass drafts — vary further at delivery.

| Item | Origin | Status | Warm-up task (new context) | Last result | Next due |
|---|---|---|---|---|---|
| Accumulator pattern | 0003/0007 | ✅ PASSED CHECK (2026-08-27) — D1 ran clean, predicted 2, got 2; init-before-loop confirmed. Residual: case-lowering before `in` (weak-spot #4, re-rolled below) | Given 3 filenames, count how many contain the word "the" using a loop + accumulator; store result in variable named so it survives loop exit. No hints. → now **Drill 6** in mini-drill, learner code pending | — | re-roll into capstone practice ~21–30d |
| Dict safe access (KeyError vs `.get()` vs `in`) | 0004 + M3L5 | ✅ FIRST COLD RECHECK PASSED 2026-09-04 | Changed context: search a player-stat dictionary, then guard a missing key before an f-string using `.get()` or `in`. No list indexing in the setup. | Correctly predicted `KeyError`; after self-correcting an initially mistyped key, stated `"goals" in player` is `False` and `player.get("goals", 0)` returns `0` | next spaced recheck ~7d |
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
| File mode + handle lifecycle (Demonstrated practical flow 2026-08-28; ✅ truncation-on-open cold recheck 2026-08-28) | At M3L5 open, correctly predicted that `open(..., "w")` immediately empties an existing file, so a crash before `.write()` leaves it empty. | Later mixed-state recheck: distinguish wrong-mode errors from closed-handle errors without a scaffold. |
| Stale variables across consecutive loops (M3L4 C3) | targeted re-probe | Give two loops over different datasets where the second loop accidentally interpolates the first loop's variables; learner traces output and repairs without naming the stale variables. |
| `csv.DictReader` input + context-manager lifetime (M3L5) | first cold recheck after guided repair | New `players.csv`: predict the malformed result when passed `f.read()` vs row dictionaries when passed the handle; then explain which collected values survive after `with` exits. No vacation data. |
| Parameterized reusable function + `return`/caller boundary (M3L6 Guided 2026-09-04) | first changed-context implementation recheck | In M3L7 or Quiz 3, give repeated processing in a non-journal domain without a function scaffold. Learner chooses the parameter and return value, keeps presentation in the caller, predicts output, and explains the boundary. |
| Input list vs result accumulator + dynamic dictionary keys (M3L7 Guided 2026-09-04) | immediate ticket transfer passed; cold implementation recheck needed | Fold into Quiz 3/module assessment: provide a non-travel input collection and require a separate result dictionary keyed by a changing field. Include a literal-key overwrite bug or let the learner design the key without naming the category. |

## Completed reviews

| Date | Item | Result |
|---|---|---|
| 2026-08-27 | Accumulator pattern (review queue seeded item) | Cold, no hints. D1 ran clean; output `2` matched prediction on first try. Confirmed init-before-loop; list accumulator survives loop exit. Single residual: Drill D5 predicted "2" but actual `"a" in item.lower()` matched 3 — learner forgot the check runs on the lowered copy. Moved to weak-spot #4 + scheduled review row; Drill 6 (the "the"-files task) left as next warm-up. |
| 2026-08-27 | CWD-relative paths (re-probe during M3L3 C1) | Self-recovered: ran from `practice\data` with `open("cape-town.txt", ...)`; reflected, switched paths, articulated the rule (terminal CWD = where Python looks; open() path is relative to terminal, not script). Moved to Demonstrated. |
| 2026-08-27 | `in`-on-strings case choice (M3L3 C4) | Code correct: `if "relevant" in response:`. Predicted 2 files; actual 3 (stub echoes prompt). Learner explained cause after run (stub includes the word in its own instructions). Capability Demonstrated, predict-grounding lesson captured. |
| 2026-08-28 | File truncation timing (M3L5 cold opener) | Correctly predicted that opening an existing file with `"w"` empties it immediately, so a crash before `.write()` leaves an empty file. Passed cold without hints. |
| 2026-09-04 | Basic `return` versus `print` transfer check (M3L6 debrief) | Given a changed player-report function that printed a slice but had no `return`, correctly predicted the caller variable contains `None` and explained why. This checks basic return semantics only; the broader mutator-return-`None` item remains queued. |
| 2026-09-04 | Literal versus dynamic dictionary key, immediate transfer (M3L7 debrief) | In a ticket-summary loop, correctly predicted that literal key `"id"` retains only the last response and proposed `ticket["id"]` so both IDs become keys. Same-session guided transfer, not cold evidence. |
| 2026-09-04 | Missing dictionary key vs safe access | Cold player-stat context after the M3L5 miss: correctly predicted `player["goals"]` raises `KeyError`, self-corrected the membership key to `"goals" in player` → `False`, and supplied `player.get("goals", 0)`. First spaced check passed; recheck later for retention. |
