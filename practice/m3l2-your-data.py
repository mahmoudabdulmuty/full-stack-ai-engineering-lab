# ============================================================
# M3L2 — Loading and using YOUR OWN data
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m3l2-your-data.py
#
# NEW THIS LESSON: the WORKING DIRECTORY + your own files
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- NEW TOOL: the local version of Andrew's files_in_directory() ----
# import os  ->  os.listdir()  (os = operating system module; imports are
# an M1 skill — `import os` then `os.something()`)
# -------------------------------------


# ---- CHALLENGE 1: See what Python sees ----
# Import os, then print(os.listdir()).
# PREDICT: which entries do you expect in the list? Will you see
# email.txt? practice? Will you see the INSIDE of practice?
# -------------------------------------
# YOUR CODE STARTS HERE
import os

entries = os.listdir()
print(entries)
# I think will print this directory not all the directory, if I open the termianl in this folder will print its dir that's what I think
# TUTOR NOTE: `dir` shadows Python's built-in dir() function. Use a different name like `entries` or `files` in future.
# -------------------------------------
# END CHALLENGE 1


# ---- CHALLENGE 2: Your own file ----
# Create a file my-note.txt in the WORKSPACE ROOT (next to email.txt —
# NOT inside practice\) with any text you like (nothing confidential).
# Then: open it, read it, close it, print it. All four lines, no help.
# -------------------------------------
# YOUR CODE STARTS HERE
f = open("my-note.txt", "r")
note = f.read()
f.close()
print(note)
# it gives me this error Traceback (most recent call last):
#   File "C:\Users\Mahmoud\Downloads\ai-python-tutor\practice\m3l2-your-data.py", line 45, in <module>
#     f = open("my-note.txt", "r")
# FileNotFoundError: [Errno 2] No such file or directory: 'my-note.txt'
# also I tried the one from the last exercise email.txt giving also file not found !!!
# -------------------------------------
# END CHALLENGE 2


# ---- CHALLENGE 3: Summarize YOUR data ----
# Prompt the LLM to summarize your note in two sentences.
# Store the response, then print it — with the CORRECT display
# pattern (the one that does NOT send it back to the LLM).
# -------------------------------------
# YOUR CODE STARTS HERE
prompt = f""" summarize this note in two sentences
Note: {note}
"""
response = get_llm_response(prompt)
print(response)
# -------------------------------------
# END CHALLENGE 3


# ---- CHALLENGE 4: THE PROOF (do this in your terminal, not here) ----
# 1. PREDICT in a comment: what happens if you cd into practice\
#    and run:  python m3l2-your-data.py
# 2. Actually do it:   cd practice   →   python m3l2-your-data.py
# 3. Then come back:   cd ..
# Write what you saw as a comment below. This is the working
# directory lesson burned in forever.
# -------------------------------------
# YOUR PREDICTION + WHAT HAPPENED:

# PREDICTED: will error because my-note.txt is in workspace root, not practice/
# WHAT HAPPENED: [TODO - run: cd practice && python m3l2-your-data.py, then fill in]
# CONFIRMED: FileNotFoundError — CWD is practice\, my-note.txt lives one level up.
# Running from workspace root works because CWD contains my-note.txt.
# -------------------------------------
# END CHALLENGE 4
