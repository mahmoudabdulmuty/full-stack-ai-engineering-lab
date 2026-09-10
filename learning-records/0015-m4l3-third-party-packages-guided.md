# M4L3 third-party packages guided

On 2026-09-10, the learner closed Module 4 Lesson 3, "Using third-party packages," after the authenticated DeepLearning.AI transcript and notebook (`rwrs1`) had been inspected in the Codex in-app browser.

Evidence in `practice/m4l3_third_party_packages.py`:

- Correctly explained that standard-library modules ship with Python while third-party packages must be installed in the active environment.
- Imported pandas as `pd` and loaded `practice/data/m4l3_car_sales.csv` with `pd.read_csv()`.
- Filtered six car rows to three rows with `Price >= 10000` and printed exact predicted counts.
- Filtered two rows from 2015, selected the `Price` Series, and computed its pandas median as `7250.0`.
- The final bundled-Python run exited successfully with exactly `6`, `3`, `2`, and `7250.0`.

The work required guidance. Converting the DataFrame with `list(...)` produced column-name strings rather than row dictionaries. Using the resulting Boolean Series in a scalar `if` raised the ambiguous-truth-value error; the learner then transferred a Boolean-mask example to direct DataFrame filtering. Full tables were repeatedly printed where exact counts were required, and the first median attempt used `statistics.median` rather than the pandas Series method.

The local environment provided a useful package-boundary observation: the bundled Python contained pandas 3.0.1 but raised `ModuleNotFoundError` for matplotlib. No installation was performed before the authenticated installation lesson.

The scatter-plot concept initially caused strong confusion. A visualization and CSS `translate(x, y)` analogy established that each row becomes one point, with kilometers on the horizontal x-axis and price on the vertical y-axis. The learner then produced a correct hand drawing showing separately positioned car points.

The five-bullet learner debrief correctly captured the installation boundary but initially reversed DataFrame and Series. In the changed-context player-rating check, the learner correctly identified `players` from `pd.read_csv(...)` as a DataFrame, `ratings = players["Rating"]` as a Series, and `ratings.median()` as the correct aggregation without a hint.

**Implication:** third-party-package and introductory pandas capability is **Guided**, not Independent. Schedule a cold changed-context table/column/filter/aggregation recheck around 2026-09-13 or later. When a new mental model is hard, use a small drawing or visualization before returning to syntax; do not create decorative visuals for easy concepts.
