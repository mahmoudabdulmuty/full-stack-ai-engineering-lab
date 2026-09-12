# M4L5 web API guided

Closed on 2026-09-12 after reviewing the authenticated DeepLearning.AI transcript and notebook for [APIs to get data from the web](https://learn.deeplearning.ai/courses/ai-python-for-beginners-c4/lesson/gsjzp/apis-to-get-data-from-the-web) in the Codex in-app browser.

## Source and practice scope

The course demonstrates a keyed OpenWeather request, JSON parsing, nested weather extraction, reporting, an outfit prompt, and API-key handling. Local practice used the [documented Open-Meteo endpoint](https://open-meteo.com/en/docs) without a key. It prepared and printed an outfit prompt; it did not execute the course's LLM call. Credential loading and real-model execution are not established by this lesson's local evidence.

## Observed learner work

- Installed `requests` into the same project `.venv` used to run the script; import/version verification succeeded (2.34.2).
- Wrote `practice/m4l5_web_api.py`: GET request, `.json()`, status/type/membership checks, nested `current` extraction, a Cairo temperature/wind report, and an f-string outfit prompt incorporating that report.
- Final verification: `.\.venv\Scripts\python.exe -X utf8 .\practice\m4l5_web_api.py` exited 0 on 2026-09-12. Outputs included `200`, `Response`, `dict`, `True`, `<class 'dict'>`, `True`, and `Cairo weather: 27.5°C, wind 7.3 km/h`. The printed prompt contained the same report. Numbers are observations from that request, not future guarantees.
- Learner correctly explained the need for internet access to the remote weather server and the possibility of unauthorized API-key use. Tutor clarified `.gitignore` spelling and its limits; no secret file or keyed request was created.

## Assistance, predictions, and limits

Task steps and the endpoint were supplied. Guidance resolved Python entered into PowerShell, Response versus decoded Python data, JSON root shape, and `type(value)` versus `type(value).__name__`. The JSON/type distinctions needed direct teaching after repeated misses.

Most structural predictions matched. The nested-type prediction was corrected to `<class 'dict'>`, and report units to `km/h`. The earlier comment `types is Response dict` remains ambiguous; that print produces only `Response`. Prompt prediction wording needed qualification: values may change on a later request, while the stored string does not update automatically. These residual wording issues remain learner-owned and were not silently corrected. Suggested English: "Please suggest an appropriate outdoor outfit."

The happy-path run does not establish timeout/error handling, secure credential implementation, deployment, or LLM quality. Initial verification socket failures were sandbox restrictions; network-authorized reruns succeeded. The local echo helper was not used for this practice and remains distinct from a real model.

## Debrief and transfer

The learner answered five tutor-supplied recall questions in `LEARNER_NOTES.md`. Strong: requests contact a server and the prompt uses weather. Fragile: Response versus parsed data and exact nested-key access. Feedback also clarified printing versus a model call and `.gitignore` versus protection of already committed secrets. Original notes remain unchanged.

Exactly one changed-context question used parcel JSON `[{"parcel":{"status":"delivered"}}]`. The learner correctly predicted `delivered` from `print(data[0]["parcel"]["status"])` and explained that `[0]` selects the first list item. First attempt; no hint on this question. This is immediate transfer after feedback, not cold retention.

**Result: Guided.** Recheck JSON/type/nested-data reasoning around 2026-09-15 or later under the normal review cap. Next action: inspect authenticated M4L6 (`kkwv2`, "APIs to use AI models") before its briefing. No immediate duplicate M4L5 or Module 3 practice.
