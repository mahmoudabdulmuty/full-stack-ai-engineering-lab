# ============================================================
# M3L4 — Extracting restaurant information from journal entries
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m3l4-extract-info.py
#
# NEW THIS LESSON: Extract structured data from text + write files
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ======================================
#  SET UP: We have 7 data files in practice/data/
#  Food-relevant: cape-town, tokyo, rio-de-janeiro, istanbul,
#                 new-york, paris, sydney
#  NOT food-relevant: madrid
# ======================================


# ---- CHALLENGE 1: Extract info from ONE file (HTML highlight) ----
# Read rio-de-janeiro.txt. Build a prompt:
#   "Given the following journal entry for a food critic, identify
#    restaurants and best dishes, highlight and bold each restaurant
#    and best dish within the original text. Entry: {content}"
# Call get_llm_response(prompt), store in a variable, then print it.
# PREDICT: will the LLM response contain restaurant names?
# -------------------------------------
# YOUR CODE STARTS HERE
f = open("practice/data/rio-de-janeiro.txt")
content = f.read()
f.close()
prompt = f"""Given the following journal entry for a food critic, identify
   restaurants and best dishes, highlight and bold each restaurant
   and best dish within the original text. Entry: {content}"""
response = get_llm_response(prompt)
# yes, names will appear as it's fake helper method only having LLM and then the prompt, not because it extracted or highlighted them only because the stub echoes the prompt
print(response)

# -------------------------------------
# END CHALLENGE 1


# ---- CHALLENGE 2: Extract into CSV format ----
# Read tokyo.txt. Build a prompt:
#   "Please extract a comprehensive list of restaurants and their
#    respective dishes mentioned in the following journal entry.
#    Ensure that each restaurant name is accurately identified and
#    listed. Provide your answer in CSV format, ready to save.
#    Entry: {content}"
# Call get_llm_response(prompt), print: filename -> response
# PREDICT: how many restaurants will appear in the CSV?
# -------------------------------------
# YOUR CODE STARTS HERE
fileName = "practice/data/tokyo.txt"
f = open(fileName)
content = f.read()
f.close()
prompt = f"""
Please extract a comprehensive list of restaurants and their
    respective dishes mentioned in the following journal entry.
    Ensure that each restaurant name is accurately identified and
    listed. Provide your answer in CSV format, ready to save.
    Entry: {content} """
response = get_llm_response(prompt)
# 5 restaurants it has tokyo
print(f"{fileName} -> {response}")

# -------------------------------------
# END CHALLENGE 2


# ---- CHALLENGE 3: Loop over ALL files, extract CSV from each ----
# Use the full list of 7 files (paths starting with "practice/data/").
# For each: open, read, close, build the same CSV prompt as C2,
# get the LLM response, print: filename -> response
# PREDICT: which file will produce the longest CSV output?
# -------------------------------------
# YOUR CODE STARTS HERE
files_list = [
    "practice/data/cape-town.txt",
    "practice/data/istanbul.txt",
    "practice/data/new-york.txt",
    "practice/data/paris.txt",
    "practice/data/rio-de-janeiro.txt",
    "practice/data/sydney.txt",
    "practice/data/tokyo.txt",
]
for file in files_list:
    f = open(file, "r")
    file_content = f.read()
    f.close()
    prompt = f"""
    Please extract a comprehensive list of restaurants and their
    respective dishes mentioned in the following journal entry.
    Ensure that each restaurant name is accurately identified and
    listed. Provide your answer in CSV format, ready to save.
    Entry: {file_content} """
    response = get_llm_response(prompt)
    # sydney and tokyo having 5 restaurants they will have the longest CSV OUTPUT
    print(f"{file} -> {response}")

# -------------------------------------
# END CHALLENGE 3


# ---- CHALLENGE 4: Write results to a file ----
# After the loop in C3, collect ALL the LLM responses into one string.
# Each line should be: "filename: response"
# Then write that string to "practice/data/extracted-restaurants.txt"
# using: open("practice/data/extracted-restaurants.txt", "w")
#        f.write(your_string)
#        f.close()
# After writing, read the file back and print its content.
# PREDICT: what will the file contain?
# -------------------------------------
# YOUR CODE STARTS HERE
acc = ""
for file in files_list:
    f = open(file, "r")
    file_content = f.read()
    f.close()
    prompt = f"""
    Please extract a comprehensive list of restaurants and their
    respective dishes mentioned in the following journal entry.
    Ensure that each restaurant name is accurately identified and
    listed. Provide your answer in CSV format, ready to save.
    Entry: {file_content} """
    response = get_llm_response(prompt)
    acc += f"{file}: {response} \n"
# WRITE MODE
extracted_file = open("practice/data/extracted-restaurants.txt", "w")
extracted_file.write(acc)
extracted_file.close()

# READ MODE
extracted_file = open("practice/data/extracted-restaurants.txt", "r")
file_content = extracted_file.read()
extracted_file.close()
# CONTAINING all the LLM responses each in a line
print(file_content)

# -------------------------------------
# END CHALLENGE 4
