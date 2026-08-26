# ============================================================
# M3L1 — Using files in Python
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m3l1-files.py
#
# NEW THIS LESSON: open() / .read() / .close()
# Data file: email.txt (in the workspace ROOT — note the path!)
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- REFERENCE (the pattern Andrew shows — do not retype here) ----
# f = open("email.txt", "r")   # open in READ mode -> file handle
# text = f.read()              # pour the whole file into one string
# f.close()                    # release it


# ---- CHALLENGE 1: Read the real file ----
# Open email.txt, read it into a variable `email`, close the file,
# then print the email. PREDICT: what does print(email) show that
# print("email") would not?
# -------------------------------------
# YOUR CODE STARTS HERE
f = open("email.txt", "r")
# why ruff has this warning in open => Use a context manager for opening filesRuffSIM115
email = f.read()
f.close()
print(email)
# print('email') it's the string now 'email' while print(email) display the actual file

# -------------------------------------
# END CHALLENGE 1


# ---- CHALLENGE 2: AI reads it for you ----
# Build an f-string prompt asking the LLM to extract bullet-point
# highlights from the email (include sender info), get the response
# with the RETURNING helper, store it, and print it.
# PREDICT: which helper do you need and why?
# -------------------------------------
# YOUR CODE STARTS HERE
prompt = f"""extract bullet-point highlights from the email
which is {email} (include sender info) """
response = get_llm_response(prompt)
print_llm_response(response)
# I think for the getting the prompt as we need it's value get_llm_response
# and for printing the result so print_llm_response that's it
# as you told before question → get answer → store answer, that's the whole idea
# prefer to remember that maybe in our files or visualize, you tell and find best approach
# -------------------------------------
# END CHALLENGE 2


# ---- CHALLENGE 3: The trap (predict BEFORE running) ----
# One line: open a file that does not exist.
# PREDICT in a comment: which error, exactly?
# Then uncomment and run. Was your prediction right?
# -------------------------------------
# YOUR CODE STARTS HERE
# f = open("404.text")
# the file isn't found so not syntax error as the syntax is clear
# so maybe the type error file
# oh I run it it's FileNotFoundError !! 😂

# -------------------------------------
# END CHALLENGE 3
