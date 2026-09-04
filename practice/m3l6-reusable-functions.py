# ============================================================
# M3L6 — Turning code blocks into reusable functions
# Practice file for Mahmoud — write challenge code here, then run:
#   python practice/m3l6-reusable-functions.py
#
# NEW THIS LESSON: package file-reading logic into one function
# ============================================================


# ---- ROUND 1: Define once, reuse twice ----
# 1. Define a function named read_journal with one parameter: file_path.
# 2. Inside the function, open file_path in read mode with a context manager.
# 3. Read the file into a string.
# 4. Return that string. Do not print inside the function.
# 5. Call the function for:
#       practice/data/sydney.txt
#       practice/data/paris.txt
#    Store the two returned strings in clearly named variables.
# 6. Print the first 80 characters of each returned string.
# 7. Immediately before EACH print, add a prediction comment stating:
#       - which city's journal should appear
#       - that slicing the returned string produces a string
#
# Frontend connection: this function is like a reusable helper that accepts
# an input and returns data, while the caller decides how to display it.
# -----------------------------------------------------------
# YOUR CODE STARTS HERE


def read_journal(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
        return content


sydney_journal = read_journal("practice/data/sydney.txt")
paris_journal = read_journal("practice/data/paris.txt")

# Sydney should appear with only first 80 chars, result is str
print(sydney_journal[:80])
# paris should appear with only first 80 chars, result is str
print(paris_journal[:80])

# YOUR CODE ENDS HERE
