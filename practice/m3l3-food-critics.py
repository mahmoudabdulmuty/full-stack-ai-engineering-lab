# ============================================================
# M3L3 — Reading journals from food critics
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m3l3-food-critics.py
#
# NEW THIS LESSON: For-loop over files + text classification
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ======================================
#  SET UP: sample data files (already created in practice/data/)
#  madrid.txt  |  tokyo.txt  |  cape-town.txt
#  madrid = NOT food-relevant (city/tourism article)
#  tokyo = food-relevant (restaurant list)
#  cape-town = food-relevant (restaurant reviews)
# ======================================


# ---- CHALLENGE 1: Read one file ----
# Open, read, and close cape-town.txt (use "practice/data/cape-town.txt").
# Print the content.
# -------------------------------------
# YOUR CODE STARTS HERE
f = open("practice/data/cape-town.txt", "r")
cape_town_file = f.read()
f.close()
# print(cape_town_file)
# -------------------------------------
# END CHALLENGE 1


# ---- CHALLENGE 2: The for-loop over files ----
# Create a LIST of the three filenames (just the .txt parts):
#   ["practice/data/madrid.txt", "practice/data/tokyo.txt", "practice/data/cape-town.txt"]
# Then use a for loop to open, read, close, and print each file.
# PREDICT: what will print first — madrid or cape-town?
# -------------------------------------
# YOUR CODE STARTS HERE
files_list = [
    "practice/data/madrid.txt",
    "practice/data/tokyo.txt",
    "practice/data/cape-town.txt",
]

for file in files_list:
    f = open(file, "r")
    req_file = f.read()
    f.close()
    # print(req_file)
# madrid will print first as it the first one in the list
# -------------------------------------
# END CHALLENGE 2


# ---- CHALLENGE 3: Build a relevance classifier ----
# For each file in the list, open/read/close it, then build a prompt:
#   "Is this journal entry about restaurants or food? Answer only relevant or not relevant."
# Pass the content into the prompt via f-string.
# Use get_llm_response() to classify, then print:  filename -> classification
# PREDICT: which files will the LLM say are "relevant"?
# -------------------------------------
# YOUR CODE STARTS HERE
for file in files_list:
    f = open(file, "r")
    req_file = f.read()
    f.close()
    prompt = f"Is this journal entry about restaurants or food? Answer only relevant or not relevant. Entry: {req_file}"
    response = get_llm_response(prompt)
    # print(file, "->", response)
# -------------------------------------
# END CHALLENGE 3


# ---- CHALLENGE 4: Only show relevant files ----
# Same loop, but now only print the filename when the classification
# contains "relevant" (hint: use the `in` operator on the response string).
# PREDICT: how many files will print?
# -------------------------------------
# YOUR CODE STARTS HERE
for file in files_list:
    f = open(file, "r")
    req_file = f.read()
    f.close()
    prompt = f"Is this journal entry about restaurants or food? Answer only relevant or not relevant. Entry: {req_file}"
    response = get_llm_response(prompt)
    if "relevant" in response:
        print(file, "->", response)
# will print 2 files only not madrid
# -------------------------------------
# END CHALLENGE 4
