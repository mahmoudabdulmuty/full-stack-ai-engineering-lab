# M4L1 local imports guided

On 2026-09-09, the learner closed Module 4 Lesson 1, "Using functions from a local file," after the authenticated DeepLearning.AI transcript and notebook (`dmaz5`) had been inspected.

Evidence in `practice/m4l1_local_imports.py`:

- Imported `m4l1_local_helpers` as a whole module and correctly called `m4l1_local_helpers.format_ticket(...)`.
- Imported `unresolved_count` directly and correctly called it without the module prefix.
- Added correct predictions before both output-producing calls.
- The final bundled-Python run exited successfully with `T-301 -> Billing` followed by `5`.
- Explained that whole-module import binds the module name while direct import binds the selected function name.

The learner-owned debrief connected Python module imports and dot notation to frontend component/module imports. In the changed-context alias check, the learner correctly selected `nh.send_alert()` after `import notification_helpers as nh`, but two explanation attempts reversed whether Python bound `nh` or the original module name. A direct explanation was required: the module is imported under the alias, and only `nh` is bound by that statement.

**Implication:** local-import capability is **Guided**, not Independent. Schedule a cold alias-binding recheck in a different module context around 2026-09-12 or later. Do not add immediate duplicate practice.
