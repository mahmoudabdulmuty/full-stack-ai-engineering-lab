# ============================================================
# MINI-DRILL — M2 weak spots (post-review repair)
# Targets: JS method leaks · quote discipline · return placement ·
#          dict-key comparisons · indentation membership
# Rules: PREDICT-BEFORE-RUN comments beside every print.
#        Run often: python practice/mini-drill-m2-weakspots.py
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- DRILL 1 — Script-block accumulator (NO function, NO return) ----
# Given:
titles = ["py for js devs", "Clean Code", "why python", "The Pragmatic Programmer"]
# Collect every title containing "py" (case-insensitive!) into `matches`,
# then print the count. This is a script block: collect -> print. Nothing else.
# PREDICT in comments: which titles match? what number prints?
# -------------------------------------
# YOUR CODE STARTS HERE
matches = []
for title in titles:
    if "py" in title.lower():
        matches.append(title)
print(len(matches))  # predicts it has 2 as matches = ["py for js devs", "why python"]
# -------------------------------------
# END DRILL 1


# ---- DRILL 2 — Quote discipline ----
# Given:
reader = {"genre": "history", "max_pages": 350}
# Build ONE f-string `prompt` interpolating BOTH values.
# HARD RULE: outer quote style and key quote style must DIFFER.
# Print the prompt. PREDICT the exact output line first.
# -------------------------------------
# YOUR CODE STARTS HERE
prompt = f"reader has his genre {reader['genre']} and has this max pages {reader['max_pages']}"
print(prompt)
# this prints reader has his genre history and has this max pages 350
# -------------------------------------
# END DRILL 2


# ---- DRILL 3 — Fix the trapdoor (surgical edits only) ----
# This function has the else-return bug. FIX it minimally:
#   - return the player on match
#   - return None ONLY after the loop finishes
# Do NOT rewrite from scratch — edit what's broken.
squad = [
    {"name": "Cubarsí", "goals": 5},
    {"name": "Yamal", "goals": 8},
    {"name": "Pedri", "goals": 2},
]


def find_player(squad, name):
    matches = []
    for player in squad:
        if player["name"] == name:
            matches.append(player)
            return player
    return None


# edited it return now is indentation as in for-loop

# After fixing, UNCOMMENT and PREDICT each line's output:
print(find_player(squad, "Yamal"))
# loop goes first for vini not going in the if as not matches so back to loop
# the loop continues goes for billi, matches so goes to return player and return inside the if so we're jumping outside the if statement and back to loop and it continues with last one modric not matches so not entering the if and goes back, the loop ends the function return None as value for it
print(find_player(squad, "Mbappe"))
# the loop continues with nothing matches in all 3 cases so it ends with None Value for function also
# Why does the second one prove your fix works?
# -------------------------------------
# YOUR CODE STARTS HERE


# -------------------------------------
# END DRILL 3


# ---- DRILL 4 — Dict-key comparison + else-body indentation ----
tasks = [
    {"description": "Email boss", "minutes": 3},
    {"description": "Outline presentation", "minutes": 60},
    {"description": "Shopping list", "minutes": 20},
]
# Loop over tasks: minutes <= 20 -> print_llm_response with the
# description interpolated in an f-string; else -> append the
# description to later_tasks. Print len AND the list after the loop.
# PREDICT: which descriptions print [LLM]? what len? which list?
# -------------------------------------
later_tasks = []
# YOUR CODE STARTS HERE
for task in tasks:
    if task["minutes"] <= 20:
        prompt = f"the description of task is {task['description']}"
        print_llm_response(prompt)
    else:
        later_tasks.append(task["description"])
print(len(later_tasks), later_tasks)
# Email boss and Shopping list goes to [LLM]
# len in 1 and it's with the description of Outline presentation

# -------------------------------------
# END DRILL 4


# ---- DRILL 5 — Spot the JS leaks (surgical fixes) ----
# EXACTLY FOUR JavaScript-isms are planted below. Find them all,
# fix them, and add a comment beside each:  # was .push  etc.
# Do NOT rewrite the block — surgical fixes only.
# PREDICT the final list and count (after fixing) before running.
result = []
items = ["alpha", "Beta", "GAMMA"]
# for item in items:
#     if item.toLowerCase().contains("a"):
#         result.push(item)
# console.log(result)
# print(len(result))
# -------------------------------------
# YOUR CODE STARTS HERE

for item in items:
    if "a" in item.lower():
        result.append(item)
print(len(result))
# print with 2 as only 'alpha' and 'Beta' has 'a' small in it
# final list will result will contain only 'alpha' and 'Beta'
# -------------------------------------
# END DRILL 5
