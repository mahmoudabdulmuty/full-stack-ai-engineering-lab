# ============================================================
# MODULE 3 - Complete assessment (M3L1-M3L7)
#
# Work in this file instead of writing Python in chat.
# Run from the repository root with:
#   python practice/module-3-quiz-assessment.py
#
# Coverage map:
#   M3L1 - opening, reading, closing, and missing files        -> Q5, Q9
#   M3L2 - current working directory and relative paths       -> Q5
#   M3L3 - looping over files and classification flow         -> Q7, Q9
#   M3L4 - structured prompts and write/read lifecycle        -> Q3, Q6, Q9
#   M3L5 - csv.DictReader, row dictionaries, filtering        -> Q1, Q8, Q9
#   M3L6 - reusable functions, return, caller ownership       -> Q2, Q9
#   M3L7 - combined pipeline, one call, dynamic result keys   -> Q4, Q9, Q10
#
# Structure:
#   Q1-Q4  - completed Quiz 3 equivalent and targeted rechecks
#   Q5-Q8  - missing lesson-level knowledge/debugging checks
#   Q9     - cold all-lesson integration challenge
#   Q10    - stub-boundary explanation
#
# Rules:
#   1. Work on only the question marked CURRENT.
#   2. Predict output in a comment before running new code.
#   3. Keep your own earlier answers; do not erase the evidence.
#   4. The LLM helper below is an echo stub, not a real AI call.
# ============================================================

import csv


def get_llm_response(prompt: str) -> str:
    """Offline stand-in: returns the prompt without generating new content."""
    return f"[LLM reply] {prompt}"


# ------------------------------------------------------------
# QUESTION 1 - Safe dictionary access (COMPLETED)
# ------------------------------------------------------------
# Given a player with no "goals" key:
#   A. What happens with player["goals"]?
#   B. What value does "goals" in player produce?
#   C. What value does player.get("goals", 0) produce?

player = {"name": "Pedri", "assists": 8}

# Mahmoud's answers:
# A. player["goals"] raises KeyError.
# B. "goals" in player produces False.
# C. player.get("goals", 0) produces 0.

# Predictions:
# Q1 membership: False
# Q1 safe value: 0
print("Q1 membership:", "goals" in player)
print("Q1 safe value:", player.get("goals", 0))


# ------------------------------------------------------------
# QUESTION 2 - print versus return (COMPLETED)
# ------------------------------------------------------------
# The original function printed its result but did not return it:
#
# def total_cost(price, quantity):
#     result = price * quantity
#     print(result)
#
# invoice_total = total_cost(12, 3)
# print(invoice_total)
#
# Mahmoud's prediction for that version:
# 36
# None
#
# Mahmoud's explanation:
# Printing is a side effect. With no explicit return statement, the function
# call evaluates to None, so the caller's print displays None.


def total_cost(price, quantity):
    return price * quantity


invoice_total = total_cost(12, 3)
# Prediction: Q2 total: 36
print("Q2 total:", invoice_total)


# ------------------------------------------------------------
# QUESTION 3 - Precise f-string prompt (COMPLETED - GUIDED)
# ------------------------------------------------------------
# Customer reviews are stored in reviews_text.
# Assign an f-string to prompt that asks an LLM to:
#   - classify each review as positive, negative, or neutral;
#   - count each category;
#   - return exactly three labelled count lines;
#   - analyze the actual contents of reviews_text.
#
# Do not call get_llm_response yet.

reviews_text = """The setup was quick and everything works.
The application crashes when I upload a large file.
The dashboard uses a blue navigation bar."""

# Mahmoud's first draft is preserved below. It is commented out because
# Markdown backticks are not valid around a Python variable inside {...}:
# prompt = f"""classify each review in the {`reviews_text`} as `positive`,
# `negative`, or `neutral`, count each category, return exactly three labelled
# count lines and analyze the contents of {`reviews_text`}"""

# YOUR RETRY STARTS HERE
# Replace None with your corrected f-string.
prompt = f"""classify each review in the Reviews as `positive`,
`negative`, or `neutral`, count each category, return exactly three labelled
count lines and analyze the contents of Reviews.
Reviews: {reviews_text}"""
# YOUR RETRY ENDS HERE

# When prompt is complete, predict its important contents before running.
# one interpolation containing all three reviews;
# no classification or [LLM reply], because the helper is not called.
if prompt is not None:
    print("Q3 prompt:")
    print(prompt)


# ------------------------------------------------------------
# QUESTION 4 - Dynamic dictionary keys (COMPLETED)
# ------------------------------------------------------------
# Build a separate result dictionary from the tickets below.
# For every ticket:
#   - build a prompt containing its ID and message;
#   - call get_llm_response exactly once;
#   - store the response under the ticket's changing ID value.
# Then predict and print the result keys.
#
# A literal key such as "ticket_id" must not overwrite earlier results.

tickets = [
    {"ticket_id": "T-101", "message": "Password reset link expired."},
    {"ticket_id": "T-102", "message": "Invoice total is incorrect."},
]

# YOUR CODE STARTS HERE

result = {}
for ticket in tickets:
    ticket_id = ticket["ticket_id"]
    ticket_msg = ticket["message"]
    prompt = f"ticket id is {ticket_id}, its message {ticket_msg}"
    result[ticket_id] = get_llm_response(prompt)
# dict_keys(['T-101', 'T-102'])
print(result.keys())

# YOUR CODE ENDS HERE


# ------------------------------------------------------------
# QUESTION 5 - Files and the current working directory (COMPLETED - GUIDED)
# ------------------------------------------------------------
# The assessment file contains this path:
#
#     open("practice/data/tokyo.txt", "r")
#
# Answer all three parts as comments. Do not execute anything yet.
#
#   A. If the terminal's current working directory is the repository root and
#      you run `python practice/module-3-quiz-assessment.py`, does that path
#      succeed or raise an exception? Name the exception if one occurs.
#
#   B. If you first `cd practice` and then run
#      `python module-3-quiz-assessment.py`, what happens to the same path?
#      Explain the exact path Python attempts to resolve.
#
#   C. From the `practice` working directory, what relative path would reach
#      the same Tokyo file?
#
#   D. From the repository root, would `os.listdir()` with no argument show
#      `practice`, `tokyo.txt`, or both? Explain whether it searches inside
#      child directories automatically.
#
# YOUR ANSWER STARTS HERE

# a. it'll see the path as we're in the working directory
# b. error file is not found, tries to resolve practice/practice/data/tokyo.txt and we're inside it for the file path
# c. data/tokyo.txt
# d. it's like dir command in terminal showing the current directory we're in so it'll show practice

# YOUR ANSWER ENDS HERE


# ------------------------------------------------------------
# QUESTION 6 - File modes and handle state (COMPLETED - GUIDED)
# ------------------------------------------------------------
# Assume report.txt initially contains OLD. Predict and explain each case:
#
#   A. Python executes `open("report.txt", "w")`, then crashes before any
#      `.write(...)` call. What remains in the file, and when did it change?
#
#   B. While a file is open in "w" mode, code calls `.read()`. What kind of
#      failure occurs, and why?
#
#   C. A `with open(..., "r") as file:` block has ended. Code then calls
#      `file.read()`. What kind of failure occurs, and why is it different
#      from case B?
#
# YOUR ANSWER WILL GO HERE.
# a. the file is empty
# b. handle open, operation unsupported by mode
# c. mode correct, but handle already closed

# TUTOR REVIEW: "w" truncates immediately at open. Case B raises
# io.UnsupportedOperation because the open handle is not readable. Case C
# raises ValueError because the readable handle has already been closed.

# ------------------------------------------------------------
# QUESTION 7 - Multi-file loop and echo-stub trap (COMPLETED)
# ------------------------------------------------------------
# Read the code. Before uncommenting the call, predict the exact filenames
# printed and explain your result from the helper's actual implementation.


def run_relevance_check():
    documents = {
        "stadium.txt": "The match finished 2-1 after extra time.",
        "support.txt": "The customer cannot reset their password.",
        "invoice.txt": "The invoice total does not match the order.",
    }

    for filename, document_text in documents.items():
        relevance_prompt = f"""Is this document relevant to customer support?
Answer only relevant or not relevant.
Document: {document_text}"""
        response = get_llm_response(relevance_prompt)
        if "relevant" in response:
            print(filename)


# PREDICTION WILL GO HERE.
# it will print the 3 files as they're in the loop from the first one as the word "relevant" itself in the prompt --- this is not real LLM it a fake method
# in real call for LLM it will print the last two filenames
# run_relevance_check()

# TUTOR VERIFIED OUTPUT: stadium.txt, support.txt, invoice.txt, in that order.
# The learner predicted and reported these exact lines in chat. A real model
# could change which filenames pass, but its classification is not guaranteed.


# ------------------------------------------------------------
# QUESTION 8 - csv.DictReader boundary and lifetime (COMPLETED - GUIDED)
# ------------------------------------------------------------
# The function below is intentionally wrong. When this question becomes
# CURRENT, make the smallest repair; do not rewrite the whole function.
# Then explain:
#   1. Why csv.DictReader needs the live file handle rather than file.read().
#   2. Why the returned list remains usable after the `with` block closes.
#   3. Why continuing to consume the reader itself after closing would fail.
# Finally, call the repaired function with
# `practice/data/m3-assessment-tickets.csv`. Before printing, predict the row
# count and the type of the first row. Print both values for verification.


def load_ticket_rows_broken(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    return rows


# MINIMAL REPAIR, CALLER, PREDICTION, AND EXPLANATION WILL GO HERE.
# 1. we don't need the context of the file (file.read())
# 2. because handle closes the original file, we've made other changes with a new variable called rows which is living right now
# 3. because using with block already closes the file and it throws error as the file is closed and can't read anything from it
# it will be a list of dicts containing in each dict
# {
# "TicketID" : "T-201", "Team": "Accounts", "Priority": "high", "DetailFile":"T-201.txt", ...
# }
# and so on with the rest of dicts which is 3
returned_rows = load_ticket_rows_broken("practice/data/m3-assessment-tickets.csv")
# <class 'dict'>
print(type(returned_rows[0]))
# 3
print(len(returned_rows))


# TUTOR-VERIFIED ORAL CHECK:
# - file.read() returns one string; direct iteration yields characters.
# - the live file handle yields CSV lines to DictReader.
# - list(reader) consumes the rows while the file is open and materializes
#   independent dictionaries, so the returned list survives file closure.
# - returning the reader object itself succeeds, but next(reader) later raises
#   ValueError because its source file was closed by the context manager.
# ------------------------------------------------------------
# QUESTION 9 - Module 3 integration challenge (COMPLETED - GUIDED)
# ------------------------------------------------------------
# Build one support-ticket reporting pipeline from a blank section below.
# Do not reuse or copy the M3L7 implementation.
# We will work one stage at a time; do not implement later stages early.
#
# Input fixtures:
#   practice/data/m3-assessment-tickets.csv
#   practice/data/m3-assessment-ticket-details/<DetailFile>
#
# Requirements:
#   1. Create a reusable text-reading function that accepts a path, uses a
#      context manager, and RETURNS the complete string without printing.
#   2. Create a reusable CSV-reading function that accepts a path, passes the
#      live file handle to csv.DictReader, and returns a list of row dicts.
#   3. Load all ticket rows and deterministically select only priority "high".
#   4. Create a separate empty result dictionary before processing them.
#   5. For each selected row, derive its detail-file path from DetailFile,
#      read the detail, and build a structured prompt containing TicketID,
#      Team, and the detail text. Request exactly two labelled output lines:
#      category and summary.
#   6. Call get_llm_response exactly once per selected ticket. Store each
#      response under the ticket's changing TicketID value.
#   7. Build one output string containing every selected ID and response.
#      Write it to `practice/data/m3-assessment-output.txt` using "w" mode.
#      Reopen that file in "r" mode and store its verified content.
#   8. Before output-producing lines run, predict the exact result-key order
#      and whether the verified file contains real classifications or echoed
#      prompts. Print the keys and the verified file content.
#
# The tutor will review requirements and run the finished program. A clean
# run alone is not sufficient; data flow and the stub boundary must be clear.
#
# STAGE A - COMPLETED
# Implement requirement 1 only: the reusable text-reading function.
# Do not call or print from it yet.
#
# YOUR STAGE A CODE STARTS HERE
def text_reader(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
        return content


# YOUR STAGE A CODE ENDS HERE


# STAGE B - COMPLETED
# Implement requirement 2 only: a reusable CSV-reading function.
# Choose its name and parameter. Use a context manager, pass the live file
# handle to csv.DictReader, materialize its rows, and return the list.
# Do not call or print from it yet.
#
# YOUR STAGE B CODE STARTS HERE
def csv_reader(file_path: str) -> list:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


# YOUR STAGE B CODE ENDS HERE


# STAGE C - COMPLETED
# Use csv_reader to load `practice/data/m3-assessment-tickets.csv`.
# Then use ordinary Python, not the LLM helper, to collect only rows whose
# Priority is exactly "high" into a separate list. Do not print yet.
#
# YOUR STAGE C CODE STARTS HERE
tickets_rows = csv_reader("practice/data/m3-assessment-tickets.csv")

priority_list = []
for ticket_row in tickets_rows:
    if ticket_row["Priority"] == "high":
        priority_list.append(ticket_row)
# YOUR STAGE C CODE ENDS HERE


# STAGE D - COMPLETED
# Create the empty final result dictionary before a loop over priority_list.
# Inside the loop, derive the current detail path from the row's DetailFile:
#   practice/data/m3-assessment-ticket-details/<DetailFile>
# Read that file with text_reader and store its returned string in a variable.
# Do not build the prompt, call the helper, store a response, or print yet.
#
# YOUR STAGE D CODE STARTS HERE
result = {}
for priority_item in priority_list:
    ticket_id = priority_item["TicketID"]
    team = priority_item["Team"]
    priority = priority_item["Priority"]
    detail_file = priority_item["DetailFile"]

    detail_file_path = f"practice/data/m3-assessment-ticket-details/{detail_file}"
    detail_file_read = text_reader(detail_file_path)

    prompt = f"""this is the current TicketID: {ticket_id} for Team: {team} and its detail text {detail_file_read},
    please create exactly two labelled lines category and summary """
    result[ticket_id] = get_llm_response(prompt)

    # STAGE E - COMPLETED (implemented above)
    # Still inside this same loop, build a structured prompt containing the
    # current TicketID, Team, and detail text. Request exactly two labelled
    # output lines: category and summary. Call get_llm_response once, then
    # store that response in result under the current TicketID value.
    # Do not print yet.
# YOUR STAGES D-E CODE ENDS HERE


# STAGE F - COMPLETED
# After the ticket-processing loop, build one string containing every entry
# currently stored in result. Include each ticket ID and its response exactly
# once, and separate entries with newlines. Do not write or print it yet.
#
# YOUR STAGE F CODE STARTS HERE
result_string = ""
for ticket_id, response in result.items():
    result_string += f"{ticket_id}:\n{response}\n"
# YOUR STAGE F CODE ENDS HERE


# STAGE G - COMPLETED
# Store the output path `practice/data/m3-assessment-output.txt` in a variable.
# Open it in "w" mode with a context manager and write result_string once.
# After that context manager closes, call text_reader with the same path and
# store the returned verification string. Do not print yet.
#
# YOUR STAGE G CODE STARTS HERE
output_path = "practice/data/m3-assessment-output.txt"
with open(output_path, "w") as file:
    file.write(result_string)
returned_verification_string = text_reader(output_path)
# YOUR STAGE G CODE ENDS HERE


# STAGE H - COMPLETED
# Before running, add prediction comments that state:
#   - the exact result keys in their expected order;
#   - whether returned_verification_string contains real AI classifications
#     or echoed prompts, and why.
# Then print result.keys() and returned_verification_string. Do not run yet.
#
# YOUR STAGE H CODE STARTS HERE
# - "T-201" then "T-203"
# - no it doesn't contain real ai classifications, it's echoed prompts because get_llm_response is fake function not real LLM function
print(result.keys())
print(returned_verification_string)
# YOUR STAGE H CODE ENDS HERE

# TUTOR-VERIFIED Q9 RESULT (2026-09-05):
# - The complete program exited successfully from the repository root.
# - The result keys were exactly T-201 followed by T-203.
# - The written/read-back output contained both selected tickets and echoed
#   prompts, not real classifications.
# - The final code, prediction, and stub explanation were correct.
# - Overall evidence is Guided because the pipeline was built in tutor-led
#   stages and the output accumulator needed focused repair assistance.


# ------------------------------------------------------------
# QUESTION 10 - Stub boundary and final explanation (COMPLETED - GUIDED)
# ------------------------------------------------------------
# We will answer this in three small parts. Work only on the part marked
# CURRENT; do not answer later parts early.
#
# PART 1 - COMPLETED (GUIDED)
# In your own words, what facts did the Python program prove before and at the
# get_llm_response(...) call? Focus on what the program itself can verify.
#
# YOUR PART 1 ANSWER STARTS HERE
# in my own words, it's just a function call echoed prompt not real LLM call
# YOUR PART 1 ANSWER ENDS HERE
#
# TUTOR FEEDBACK: The statement above is correct, but it answers Part 2.
# Retry Part 1 below. Trace the pipeline only up to the helper call and begin:
# "Before the helper call, Python proved that ..."
#
# YOUR PART 1 RETRY STARTS HERE
# Before the helper call, python proved that it can handles csv files read it deal with it, convert this data into known DS that any programming languag    e can handle, write useful output in another file
# YOUR PART 1 RETRY ENDS HERE
#
# TUTOR FEEDBACK 2: CSV reading and conversion to ordinary Python data are
# correct. Writing the output file happens after the helper call.
# One focused question: for T-201, what three current values had Python already
# inserted into prompt immediately before get_llm_response(prompt) ran?
#
# YOUR PART 1 RETRY 2 STARTS HERE
# ticket_id, team, detail_file_read can be inject inside prompts as variables
# YOUR PART 1 RETRY 2 ENDS HERE
#
# TUTOR-VERIFIED PART 1: ticket_id, team, and detail_file_read are the three
# source variables inserted into each current prompt. The earlier answer also
# correctly identified CSV reading and conversion to ordinary Python data.
#
# PART 2 - COMPLETED
# You already identified that this helper only echoes. State one thing that
# this successful run therefore cannot prove about a real LLM's output.
# it didn't create exactly two labelled lines category and summary
# YOUR PART 2 ANSWER STARTS HERE

# YOUR PART 2 ANSWER ENDS HERE
#
# TUTOR-VERIFIED PART 2: The stub did not create the requested category and
# summary lines, so this run cannot prove real-LLM instruction following.
#
# PART 3 - COMPLETED
# Choose one operation from Q9 that should remain ordinary deterministic Python
# instead of being delegated to an LLM. Explain why in one sentence.
#
# YOUR PART 3 ANSWER STARTS HERE
# all works with files read and write, this is what python can handle
# YOUR PART 3 ANSWER ENDS HERE
#
# TUTOR FEEDBACK: File handling is an appropriate choice, but "Python can
# handle it" does not yet explain why it should stay deterministic.
# Focus on reading one unchanged detail file: what should happen every time,
# and does that operation require interpretation?
#
# YOUR PART 3 RETRY STARTS HERE
# TUTOR-RECORDED VERBATIM CHAT ANSWER:
# it should return the same exact output not being uncertain about the file reading output, it doesn't require interpretation
# YOUR PART 3 RETRY ENDS HERE
#
# TUTOR-VERIFIED PART 3: Correct. Reading an unchanged file should return the
# same exact text each time and requires no interpretation, so it belongs in
# deterministic Python code rather than an LLM call.
#
# TUTOR-VERIFIED Q10 RESULT (2026-09-05):
# - Part 1 identified the data already verified and inserted into the prompt,
#   after two focused retries.
# - Part 2 correctly identified that the echo stub cannot prove real-LLM
#   instruction following.
# - Part 3 correctly explained why exact file reading stays deterministic,
#   after one focused retry.
# - Overall explanation evidence is Guided.
