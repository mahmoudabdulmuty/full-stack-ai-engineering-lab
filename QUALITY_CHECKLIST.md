# QUALITY_CHECKLIST.md

Use the sections relevant to the work before closing a substantive lesson, module, milestone, or artifact. Core integrity is non-negotiable; irrelevant ceremony is not.

## Teaching integrity
- [ ] Code written BY LEARNER in practice file; chat used for reasoning/questions only
- [ ] Prediction discipline matches the phase: every challenge output during current Python fundamentals; later, targeted at non-obvious behavior, state changes, debugging, files/database/network, mutability, async/concurrency, and API/LLM assumptions
- [ ] Socratic flow maintained; one hint at a time; full corrections only after agreed threshold
- [ ] MCQ answer positions randomized; options equal-length (learner has caught slot bias before)
- [ ] Honest grading — nothing passes on vibes; empty/failure cases verified where relevant
- [ ] Capability level reflects evidence (`Introduced → Guided → Independent → Retained → Integrated → Production Evidence`); guided work was not silently promoted
- [ ] Scaffolding matches demonstrated competence; tutor asked whether Mahmoud should now generate some of the provided structure
- [ ] Familiar JS/TS concept compressed to Python-specific differences plus a transfer check; no beginner-level repetition after demonstration

## Practice files
- [ ] Runs clean with `python practice/<file>.py` (stubbed helpers, no API key needed)
- [ ] Previous challenge code commented out, new challenges below their markers
- [ ] Output checked against predictions; discrepancies explained by learner

## Workspace sync (end of lesson/session)
- [ ] PROGRESS.md — capability table, weak spots, session log updated with EVIDENCE
- [ ] REVIEW_QUEUE.md — new demonstrable concept scheduled; overdue items worked
- [ ] Learning records written ONLY on demonstrated understanding
- [ ] GLOSSARY.md terms added only post-demonstration
- [ ] CAREER_EVIDENCE.md updated only if this is a meaningful employer-facing milestone; routine lesson work did not create ledger bureaucracy

## Lesson debrief (substantive lesson or major concept)
- [ ] Learner added a short `LEARNER_NOTES.md` entry from memory; tutor did not write or rewrite it
- [ ] Tutor discussed one accurate point and one omission/fragile point from the note
- [ ] Tutor asked exactly one genuinely changed-context question, not a restatement of the completed exercise
- [ ] First miss received one focused hint and retry; second miss received a direct explanation
- [ ] Any unresolved or twice-missed point was recorded in `PROGRESS.md` / `REVIEW_QUEUE.md` for a later cold recheck
- [ ] Trivial continuation inside the same lesson did not trigger a duplicate debrief

## Independence and transfer

- [ ] Recheck changes more than names: new domain/data, incomplete code, interacting concepts, hidden bug, edge case, or ambiguity appropriate to the learner’s level
- [ ] Code-reading work appears progressively: trace data flow, locate a change, preserve behavior, identify assumptions, or review an implementation
- [ ] Debugging evidence follows the earned level: reproduce, expected vs actual, evidence, reduction, hypotheses, root cause, smallest fix, regression protection when appropriate
- [ ] Fluency observations remain separate from correctness and do not become stressful speed tests

## Artifacts (minimal-default policy)
- [ ] Practice file + focused explanation = sufficient for most lessons — prefer them over new documents
- [ ] Interactive visualizer created only when state/flow is materially easier to understand visually or a concept remains fragile
- [ ] Cheatsheet created or extended only for recurring syntax/patterns; consolidate by concept family or module
- [ ] Per-lesson HTML skipped by default; use HTML for module assessments or a specifically requested review artifact
- [ ] Artifact budget remains subordinate to practice: roughly 70% code/debugging, 20% explanation/retrieval, 10% support artifacts
- [ ] End-of-module: knowledge check → deep dive/challenge → assessment HTML mirroring locked quiz
- [ ] Auto-open an artifact only when one was created or materially updated

## Facts & quality
- [ ] Time-sensitive technical facts verified against official documentation
- [ ] Outdated material flagged explicitly, current approach taught, source linked
- [ ] Resource choice follows `RESOURCES.md`; new material added only for a named capability gap
- [ ] Modern-Python framing: dicts preserve insertion order (never "unordered")
- [ ] No long copied passages from books/course transcripts anywhere
- [ ] Learner increasingly locates and reads authoritative documentation; parameters/returns, guarantees/examples, and version assumptions were checked with a small experiment when useful

## Project engineering (when the phase supports it)

- [ ] Requirements and acceptance criteria were stated; ambiguity was left for Mahmoud to clarify at an appropriate level
- [ ] Tests begin from guarantees, happy paths, failures, boundaries, regressions, and sensible mock boundaries—not pytest syntax alone
- [ ] AI checks distinguish deterministic unit/integration/contract tests from probabilistic evaluation
- [ ] Correctness came before refactoring; any refactor has an explained benefit in duplication, naming, boundaries, assumptions, complexity, or testability
- [ ] Significant change followed inspect → plan → implement → test → diff review; Git/PR ceremony was not imposed on fundamentals
- [ ] Important architecture choice received a lightweight decision record; trivial choices did not
- [ ] Production/AI-Assisted Mode was used only for already-independent/retained capabilities, with learner review and acceptance

## Safety & change control
- [ ] No secrets/personal data in repo-bound artifacts; paid APIs/subscriptions only with explicit approval
- [ ] Workspace restructuring explained + approved beforehand
- [ ] Learner-written code preserved; cleanup only with approval

## Module close (additional)
- [ ] Requirements re-read; learner's code actually run against every requirement
- [ ] Remaining issues explicitly recorded — no blanket "all parts pass"
- [ ] Retrospective questions answered (what's independent now? still fragile? resource redundancy? next-module change? highest-value gap?)
- [ ] Temp handoff doc refreshed; concise handover given (done / demonstrated / weak point / next action)
- [ ] Major readiness audit considered knowledge, independent implementation, retention, integration, debugging, testing, judgment, communication, and hiring evidence without inflating the result
