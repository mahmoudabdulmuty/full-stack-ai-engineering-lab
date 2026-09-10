# M4L2 built-in packages guided

On 2026-09-10, the learner closed Module 4 Lesson 2, "Built-in packages," after the authenticated DeepLearning.AI transcript and notebook (`kvhik`) had been inspected.

Evidence in `practice/m4l2_built_in_modules.py`:

- Imported `floor` from `math`, predicted `floor(9.8)` as `9`, and verified it.
- Imported `mean` from `statistics`, calculated and predicted the mean of `[4, 8, 6, 10]` as `7`, and verified it.
- Imported `sample` from `random` and repaired the call to `sample(reviewers, 2)` after learning the `sample(population, k)` signature.
- Recorded the stable guarantees: a list of length two, members originating from the population, and no repeated selection of the same input position; exact values and order remain unpredictable.
- The final bundled-Python run exited successfully with `9`, `7`, and a valid two-reviewer sample.

The learner-owned five-bullet debrief captured the deterministic imports and most of the `sample` contract. Feedback clarified that `math`, `statistics`, and `random` are standard-library modules containing functions, rather than all of these being built-in functions.

In the changed-context check using `["Mona", "Mona", "Salma"]`, the learner initially said `sample(names, 2)` could not return `["Mona", "Mona"]`. After one focused hint that the equal values occupy different positions, the learner correctly explained that sampling without replacement prevents selecting one position twice but does not guarantee unique values when the population itself contains duplicates.

**Implication:** standard-library selection and deliberate-randomness reasoning are **Guided**, not Independent. Keep the cold `random.sample` contract recheck around 2026-09-12 or later. Do not add immediate duplicate practice.
