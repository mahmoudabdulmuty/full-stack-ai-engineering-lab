# M4L6 — APIs to use AI models — Guided

Date: 2026-09-12

## Source and scope

- Inspected the authenticated DeepLearning.AI transcript and notebook for lesson `kkwv2`, "APIs to use AI models," in the Codex in-app browser.
- Covered the real OpenAI-client flow shown by the course: model selection, system and user messages, temperature, completion-object traversal, response-text extraction, and API-key loading with `.env`, `load_dotenv()`, and `os.getenv()`.
- Kept the course's real provider call distinct from the repository's offline echo helpers.

## Learner evidence

- Correctly identified the system message as HOW the model should respond and the user message as WHAT it should respond to.
- Correctly predicted that `completion.choices[0].message.content` is the final response string.
- In the authenticated course notebook, changed the system instruction to a one-sentence football-commentator style and ran a real model call. The result preserved the requested API-success fact and adopted the requested style.
- Correctly predicted that `temperature=1.0` would vary wording while preserving the requested meaning and behavioral constraints. Three real calls produced different commentator phrasing while retaining the success message.
- Safely checked `print(openai_api_key is None)` without exposing the key; the course environment printed `False`.
- Wrote and completed the five-item lesson debrief in `LEARNER_NOTES.md`.
- Passed the single changed-context check: when `.env` contained only `OPENAI_API_KEY` and code requested `GEMINI_API_KEY`, predicted `None` because environment lookup uses the exact requested name.

## Assistance and limits

- The first two custom-response predictions (`"Brilliant."` and `"A Goal."`) followed only part of the system style and omitted the user's requested API-success meaning. After one hint and a second miss, direct teaching showed that output must combine HOW and WHAT.
- Initially predicted that missing `os.getenv()` data would raise an error. After one focused analogy to `dict.get()`, recalled `None`.
- Correctly predicted `openai_api_key is None` would be `False`, but the explanation initially said the value was not initialized; feedback clarified that assignment occurs and receives either a string or `None`.
- The debrief named `load_env()` instead of `load_dotenv()`, described `os.getenv()` as reading the file directly, omitted missing-name behavior, and did not fully state what the real call versus echo stub proves. These were corrected in feedback.
- No local provider package, personal API key, paid account, or production error handling was implemented. Course-notebook execution is real-provider Guided evidence, not independent local integration or production evidence.

## Result

M4L6 is **Guided**. Schedule a cold changed-context review of system/user-message roles, temperature guarantees, exact environment-variable lookup, and real-provider versus echo-stub evidence around 2026-09-15 or later.

