# M3L7 multi-city itinerary integration guided

On 2026-09-04, the learner completed M3L7, "Creating detailed itineraries for multiple cities," after the authenticated DeepLearning.AI transcript and notebook (`fvhf6`) were inspected.

Evidence in `practice/m3l7-multi-city-itineraries.py`:

- Independently wrote a reusable CSV loader using a context manager, `csv.DictReader`, a list accumulator, and `return`; corrected its return annotation after a focused question.
- Loaded a two-row itinerary and, for each stop, constructed the matching restaurant CSV path and loaded restaurant dictionaries.
- Built a prompt containing city, country, dates, restaurants, and specialties.
- Called the local helper once per city and stored each returned string under a dynamic city-name key.
- Final bundled-Python run exited successfully with ordered keys `Tokyo` and `Rio de Janeiro`; the Tokyo output matched the learner's detailed prediction.

Guided debugging was material. The learner initially included literal angle brackets in the filename, loaded restaurant rows without using them, called the helper twice, and stored every response under literal key `"City"`, overwriting the earlier response. Prediction evidence and the end-to-end data-flow explanation also needed stepwise prompts.

The learner-owned debrief correctly identified the functions-plus-loops integration. It omitted the dynamic-key accumulator and stub boundary. In a changed ticket-summary context, the learner correctly diagnosed literal-key overwrite and selected `ticket["id"]` as the dynamic key. The learner then explained that the local helper only echoes the prompt because no real LLM call is present.

**Implication:** the integrated capability is **Guided**, not Independent. A cold, non-travel implementation recheck belongs inside Quiz 3 / the Module 3 assessment. That upcoming assessment provides the necessary repetition, so a separate 30–60 minute practice session is not justified yet.
