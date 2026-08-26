# ============================================================
# M2L2 — Repeating tasks with for loops
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m2l2-for-loops.py
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
# The course notebook provides these from a helper module (needs an API key).
# These stubs let you run the exact same code locally, with no key.
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- RECAP from M2L1 (commented out) ----
# The 3-line pain that for loops exist to kill.
tasks = [
    "Email my boss",
    "Write a poem for Otto",
    "Review the budget",
]

# print_llm_response(f"Please complete this task: {tasks[0]}")
# print_llm_response(f"Please complete this task: {tasks[1]}")
# print_llm_response(f"Please complete this task: {tasks[2]}")


# ---- CHALLENGE 1 ----
# Replace the 3 commented lines above with ONE for loop.
# Same output: an "[LLM]" line for each task in order.
# Write your loop below the marker. Don't touch the recap above.
# -------------------------------------
# YOUR CODE STARTS HERE
# for task in tasks:
#     print_llm_response(f"Please complete this task: {task}")

# -------------------------------------
# END CHALLENGE 1


# ice_cream_flavors = ["vanilla", "chocolate", "strawberry", "mint chocolate chip"]
# promotional_descriptions = []

# for flavor in ice_cream_flavors:
#     prompt = f"write a captivating description for {flavor}"
#     response = get_llm_response(prompt)
#     promotional_descriptions.append(response)

# print(len(promotional_descriptions))
# print(promotional_descriptions[1])
