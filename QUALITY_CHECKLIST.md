# QUALITY_CHECKLIST.md

Run before closing ANY lesson, module, or artifact. Compact, non-negotiable.

## Teaching integrity
- [ ] Code written BY LEARNER in practice file; chat used for reasoning/questions only
- [ ] Predict-before-run comments present for every challenge line that produces output
- [ ] Socratic flow maintained; one hint at a time; full corrections only after agreed threshold
- [ ] MCQ answer positions randomized; options equal-length (learner has caught slot bias before)
- [ ] Honest grading — nothing passes on vibes; empty/failure cases verified where relevant

## Practice files
- [ ] Runs clean with `python practice/<file>.py` (stubbed helpers, no API key needed)
- [ ] Previous challenge code commented out, new challenges below their markers
- [ ] Output checked against predictions; discrepancies explained by learner

## Workspace sync (end of lesson/session)
- [ ] PROGRESS.md — capability table, weak spots, session log updated with EVIDENCE
- [ ] REVIEW_QUEUE.md — new demonstrable concept scheduled; overdue items worked
- [ ] Learning records written ONLY on demonstrated understanding
- [ ] GLOSSARY.md terms added only post-demonstration
- [ ] Learner prompted once to add a short `LEARNER_NOTES.md` entry from memory; tutor did not write it

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

## Safety & change control
- [ ] No secrets/personal data in repo-bound artifacts; paid APIs/subscriptions only with explicit approval
- [ ] Workspace restructuring explained + approved beforehand
- [ ] Learner-written code preserved; cleanup only with approval

## Module close (additional)
- [ ] Requirements re-read; learner's code actually run against every requirement
- [ ] Remaining issues explicitly recorded — no blanket "all parts pass"
- [ ] Retrospective questions answered (what's independent now? still fragile? resource redundancy? next-module change? highest-value gap?)
- [ ] Temp handoff doc refreshed; concise handover given (done / demonstrated / weak point / next action)
