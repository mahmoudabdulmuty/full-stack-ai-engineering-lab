# M3L5 CSV structured-data pipeline demonstrated

On 2026-08-28, the learner completed M3L5, "Vacation planning using CSV files," from the authenticated DeepLearning.AI transcript (`jz515`).

Evidence in `practice/m3l5-csv-itinerary.py`:

- R1: opened `practice/data/itinerary.csv`, passed the live file handle to `csv.DictReader`, collected six row dictionaries, and used a `with` context manager. The first attempt passed the string returned by `f.read()`, which made `DictReader` iterate character by character; the learner repaired the data flow after inspecting actual output.
- R2: used ordinary Python conditions to filter the six structured rows into two Egypt stops—Cairo and Alexandria—and explained why exact table filtering does not require an LLM.
- R3: searched the filtered list for Alexandria by its `"City"` value, built a dated activity prompt from the selected row, passed it to the local helper, and predicted the final output. The learner justified semantic search as more robust than a fixed list index when CSV order is unknown.
- Final verification: the bundled workspace Python executable ran the practice file with exit code 0 and printed the Alexandria/Egypt prompt for `2026-09-20` through `2026-09-22`.
- Lesson debrief: the learner wrote the required five-note entry. On the changed-context retry, they correctly explained that a collected list remains usable after the `with` block while `DictReader` cannot continue reading its closed file stream.

The learner also passed the delayed file-truncation recheck cold: `open(..., "w")` empties an existing file immediately, even if execution crashes before `.write()`.

**Implication:** CSV-to-list-of-dictionaries loading, deterministic row filtering, context-managed file reading, and selected-row-to-prompt data flow are demonstrated. Because the initial `f.read()`/handle distinction required guidance, it is scheduled for a changed-context cold recheck. A separate missing-key discussion exposed `KeyError` vs `IndexError` confusion, which is also scheduled.

Post-close, the learner reported that the full file/handle/context-manager/CSV relationship still felt difficult to explain and requested consolidation for interview recall. `reference/files-documents-cheatsheet.md` and `visualizers/files.html` were expanded in response. The demonstrated status remains evidence-based, but retrieval is marked fragile until the scheduled changed-context recheck passes.
