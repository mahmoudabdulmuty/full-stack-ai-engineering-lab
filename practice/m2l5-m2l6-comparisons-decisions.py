# ============================================================
# M2L5 + M2L6 (compressed) — Comparing data & helping AI decide
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m2l5-m2l6-comparisons-decisions.py
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- CHALLENGE 1: Booleans & comparisons ----
# Squad ages:
vini_age = 26
modric_age = 40
bellingham_age = 22
# Print each expression's result:
#   1. vini_age < modric_age
#   2. bellingham_age >= vini_age
#   3. Store "is_modric_the_oldest" = (modric_age > vini_age) in a
#      variable and print it AND its type().
# -------------------------------------
# YOUR CODE STARTS HERE

print(vini_age < modric_age)  # this will give True as predictions
print(bellingham_age >= vini_age)  # this will give False as Predictions
is_modric_the_oldest = modric_age > vini_age
print(
    is_modric_the_oldest, type(is_modric_the_oldest)
)  # this will give True & type will be <class 'bool'>

# -------------------------------------
# END CHALLENGE 1


# ---- CHALLENGE 2: Equality (= vs ==) ----
# Two lines below — PREDICT in chat before running:
#   line A: print(vini_age == 26)
#   line B: print(vini_age = 26)
# Write BOTH, run, observe. Then add:
#   print("starter" == "Starter")
# -------------------------------------
# YOUR CODE STARTS HERE
print(vini_age == 26)  # prediction gives True
# print(vini_age=26)  # this is like reassign value again and then print it, I think None
print("starter" == "Starter")  # This will give False? as like elements has it's place in the chart in unicode maybe ?! so 's' has different unicode than 'S'

# -------------------------------------
# END CHALLENGE 2


# ---- CHALLENGE 3: and / or / not ----
# Given: fitness_rating = 8, is_injured = False
# Print the results of:
#   1. (fitness_rating >= 8) and (not is_injured)
#   2. (fitness_rating < 5) or is_injured
#   3. not (fitness_rating == 8)
# Say each answer OUT LOUD in chat before you run it.
# -------------------------------------
# YOUR CODE STARTS HERE
# fitness_rating = 8, is_injured = False # why this line gives error Invalid assignment targetRuff(invalid-syntax)
fitness_rating = 8
is_injured = False
print(fitness_rating >= 8)  # True as predictions before run
print(fitness_rating < 5)  # False as predictions before run
print(fitness_rating != 8)
# vscode extension recommend Use `fitness_rating != 8` instead of `not fitness_rating == 8`help: Replace with `!=` operator
# any way it gives not True so it's False
# -------------------------------------
# END CHALLENGE 3


# ---- CHALLENGE 4: Decisions — the pre-lunch filter (capstone) ----
# Data (list of dicts — M2L3 + M2L4 combined):
tasks = [
    {"description": "Compose a brief email", "minutes": 3},
    {"description": "Create presentation outline", "minutes": 60},
    {"description": "Write a movie review", "minutes": 30},
    {"description": "Create a shopping list", "minutes": 5},
]
# Loop over tasks:
#   - if the task takes <= 5 minutes -> print_llm_response asking AI
#     to complete it RIGHT NOW
#   - else -> append its description to a NEW list called later_tasks
# After the loop: print len(later_tasks) and the list itself.
# -------------------------------------
later_tasks = []
# YOUR CODE STARTS HERE
for task in tasks:
    if task["minutes"] <= 5:
        print_llm_response(f"complete this task: ({task['description']}) right now")
    else:
        later_tasks.append(task["description"])
print(len(later_tasks), later_tasks)


# -------------------------------------
# END CHALLENGE 4
