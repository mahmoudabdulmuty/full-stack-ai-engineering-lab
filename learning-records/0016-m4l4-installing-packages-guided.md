# M4L4 installing packages guided

On 2026-09-10, the learner closed Module 4 Lesson 4, "Installing packages," after the authenticated DeepLearning.AI transcript and notebook (`lufq3`) had been inspected in the Codex in-app browser.

Installation evidence:

- Created a project-local `.venv`, which is excluded by `.gitignore`.
- Ran the venv Python before installation and observed `ModuleNotFoundError: No module named 'bs4'`.
- Installed the `beautifulsoup4` distribution into that same venv with its Python-targeted pip.
- Verified that `import bs4` succeeded and reported version 4.15.0.
- Distinguished the installation/distribution name `beautifulsoup4`, import namespace `bs4`, and imported class `BeautifulSoup` after feedback.

Evidence in `practice/m4l4_installing_packages.py`:

- Imported `BeautifulSoup` from `bs4`.
- Parsed provided local HTML with `html.parser` without making a web request.
- Selected the first `h1` and all `p` elements.
- Added exact predictions and produced `Barcelona Match Report` followed by `2` in a clean `.venv` run.

The learner-owned debrief correctly described HTML parsing and element lookup, but initially described `.venv` as a module installation and reversed the relationship between `beautifulsoup4` and `bs4`.

In the changed-context environment check, the learner selected `.venv\Scripts\python.exe` correctly but explicitly reported that the reason was still unclear. Two visual explanations and direct teaching established the model: the package lives under the environment's `site-packages`; the explicit Python executable running the script determines which environment/package store is searched; the project location of `app.py` does not make a different Python search the project's venv. The learner then explained this accurately in Arabic using the project Python versus system Python distinction.

**Implication:** package installation and environment targeting are **Guided**, not Independent. Schedule a cold changed-context executable/package-store recheck around 2026-09-13 or later. Do not add immediate duplicate installation practice.
