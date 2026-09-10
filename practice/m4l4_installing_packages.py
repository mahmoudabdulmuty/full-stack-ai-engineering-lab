# ============================================================
# MODULE 4 - LESSON 4: Installing packages
#
# Run from the repository root with the project environment:
#   & ".\.venv\Scripts\python.exe" "practice\m4l4_installing_packages.py"
#
# You write all imports and challenge code.
# ============================================================


html = """
<article>
    <h1>Barcelona Match Report</h1>
    <p>Barcelona won 3-1.</p>
    <p>Pedri completed 92 passes.</p>
</article>
"""


# CHALLENGE 1 — prove the installed package works
#
# 1. Import `BeautifulSoup` from `bs4`.
# 2. Parse `html` using `BeautifulSoup(html, "html.parser")`.
# 3. Find the first `h1` element with `.find("h1")`.
# 4. Find all `p` elements with `.find_all("p")`.
# 5. Add an exact prediction comment, then print the h1 text using `.get_text()`.
# 6. Add an exact prediction comment, then print the number of paragraph elements.
#
# Do not use a web request or manually copy the expected text into print().

# YOUR CHALLENGE 1 CODE STARTS HERE
from bs4 import BeautifulSoup

parsed_html = BeautifulSoup(html, "html.parser")
h1 = parsed_html.find("h1")
p = parsed_html.find_all("p")

# Barcelona Match Report
print(h1.get_text())
# 2
print(len(p))

# YOUR CHALLENGE 1 CODE ENDS HERE
