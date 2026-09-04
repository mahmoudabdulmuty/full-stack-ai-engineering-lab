# M3L6 reusable file function guided

On 2026-09-04, the learner completed M3L6, "Turning code blocks into reusable functions," from the authenticated DeepLearning.AI transcript (`vvkwa`).

Evidence in `practice/m3l6-reusable-functions.py`:

- Defined `read_journal(file_path)` with a context manager, read the selected file, and returned its text rather than printing inside the function.
- Reused the function with Sydney and Paris paths and stored both returned strings in clearly named caller variables.
- Printed the first 80 characters of each string and added separate predictions identifying the city and sliced result type.
- The bundled workspace Python runtime exited successfully and produced the expected Sydney and Paris previews.
- Explained that the parameter allows the same behavior to accept different arguments and that a partial string slice does not mutate the original string.

One hint was required for slicing syntax: the tutor provided an unrelated `message[:3]` example, and the learner transferred it to both journal strings. The learner-owned lesson note accurately recalled DRY and the frontend reusable-component analogy but omitted `return` versus `print`. In the changed-context debrief, the learner correctly predicted that a function which only prints and has no `return` assigns `None` to its caller variable.

**Implication:** the lesson is closed, but the capability is **Guided**, not Independent. Recheck in a different domain without a function scaffold: the learner should choose the function boundary, parameter, and return value while keeping presentation in the caller. No separate 30–60 minute repetition session is warranted from this evidence.
