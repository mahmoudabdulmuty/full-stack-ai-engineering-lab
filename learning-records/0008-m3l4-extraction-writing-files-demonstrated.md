# M3L4 extraction and file writing demonstrated

On 2026-08-28, the learner completed M3L4, "Extracting restaurant information from journal entries," from the authenticated DeepLearning.AI transcript (`x5zu6`).

Evidence in `practice/m3l4-extract-info.py`:

- C1: read one journal, embedded its text in an HTML-oriented extraction prompt, stored the helper response, and explained why the local stub shows restaurant names without performing real extraction.
- C2: built a CSV-oriented extraction prompt for Tokyo and grounded the prediction in five restaurant mentions.
- C3: processed seven relevant journal files. Initial output exposed stale variables from C2 (`content` and `fileName`) plus an extra Madrid input; the learner repaired the prompt, label, and list through output tracing. Final filenames and contents match.
- C4: accumulated seven filename/response sections into one string, separated entries with newlines, wrote them to `practice/data/extracted-restaurants.txt`, closed the writer, reopened in read mode, and printed the saved content. Final run exited cleanly and the file contained seven sections.

The learner encountered and repaired two meaningful file-state errors: reading from a `"w"` handle (`io.UnsupportedOperation`) and reading from a closed handle (`ValueError`). They then correctly predicted that opening a file containing `OLD` with `"w"` and writing `NEW` leaves only `NEW`.

**Implication:** structured-prompt data flow, stub-vs-real-LLM boundaries, string accumulation, and the write/close/reopen/read lifecycle are demonstrated. Because stale-variable and handle-state repairs required guidance, both are scheduled for a cold re-probe in M3L5 or later.
