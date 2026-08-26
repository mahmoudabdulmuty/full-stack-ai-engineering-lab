# ============================================================
# M2L3 — Prioritizing tasks with dictionaries and AI
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m2l3-dictionaries.py
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
# The course notebook provides these from a helper module (needs an API key).
# These stubs let you run the exact same code locally, with no key.
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- RECAP from M2L2 (commented out) ----
# You found promotional_descriptions[1] == chocolate only because you
# remembered seat 1. With dozens of flavors that breaks. Find by NAME.
# ice_cream_flavors = ["vanilla", "chocolate", "strawberry", "mint chocolate chip"]
# promotional_descriptions = []
# for flavor in ice_cream_flavors:
#     prompt = f"write a captivating description for {flavor}"
#     response = get_llm_response(prompt)
#     promotional_descriptions.append(response)
# print(len(promotional_descriptions))
# print(promotional_descriptions[1])


# ---- CHALLENGE 1 ----
# Build a dictionary `ice_cream_flavors` mapping THREE flavor names to
# their descriptions:
#   "mint chocolate chip" -> "Mint ice cream loaded with chocolate chunks"
#   "cookie dough"        -> "Vanilla ice cream loaded with cookie dough chunks"
#   "salted caramel"      -> "Caramel ice cream with a salted caramel ribbon"
# Remember: curly braces, key colon value, pairs separated by commas.
# -------------------------------------
# YOUR CODE STARTS HERE
ice_cream_flavors = {
    "mint chocolate chip": "Mint ice cream loaded with chocolate chunks",
    "cookie dough": "Vanilla ice cream loaded with cookie dough chunks",
    "salted caramel": "Caramel ice cream with a salted caramel ribbon",
}

# print(type(ice_cream_flavors))

# -------------------------------------
# END CHALLENGE 1


# ---- CHALLENGE 2 ----
# Pull out the description for "cookie dough" into a variable and print it.
# Square brackets with the KEY, like JS obj["key"] — no dot notation.
# -------------------------------------
# YOUR CODE STARTS HERE
# cookie_dough_desc = ice_cream_flavors["cookie dough"]
# print(cookie_dough_desc)

# temp tests
# print(ice_cream_flavors[0])        # what happen`s?
# print(ice_cream_flavors["mango"])  # what happens?

# -------------------------------------
# END CHALLENGE 2


# ---- CHALLENGE 3 ----
# Add "rocky road" with description "Chocolate ice cream mixed with nuts
# and marshmallows". Then print the dictionary to check.
# BONUS: your chocolate description has a typo — "mixed with nuts and
# marshmallows" should be "mixed with marshmallows and nuts". Fix it
# with the SAME pattern you used to add it.
# -------------------------------------
# YOUR CODE STARTS HERE
# ice_cream_flavors["rocky road"] = "Chocolate ice cream mixed with nuts and marshmallows"
# print(ice_cream_flavors)
# ice_cream_flavors["rocky road"] = "Chocolate ice cream mixed with marshmallows and nuts"
# print(ice_cream_flavors)

# -------------------------------------
# END CHALLENGE 3


# ---- CHALLENGE 4 ----
# Build a dictionary `isabel_facts` about Isabel:
#   age -> 28
#   favorite_color -> "red"
# Then add a key "cat_names" whose VALUE is a LIST of Isabel's three cats:
#   ["Charlie", "Smokey", "Tabitha"]
# Print the whole dictionary.
# -------------------------------------
# YOUR CODE STARTS HERE
# isabel_facts = {"age": 28, "favorite_color": "red"}
# isabel_facts["cat_names"] = ["Charlie", "Smokey", "Tabitha"]
# print(isabel_facts)
# -------------------------------------
# END CHALLENGE 4


# ---- CHALLENGE 5 ----
# Three priority lists are given. Bundle them into one dictionary
# `prioritized_tasks` whose keys are the priority levels and whose values
# are the lists. Then loop over the HIGH priority tasks with
# print_llm_response, same shape as M2L2.
# -------------------------------------
high_priority_tasks = ["Compose a brief email", "Create an outline for a presentation"]
medium_priority_tasks = ["Schedule a meeting", "Draft a project update"]
low_priority_tasks = ["Clean up the desktop"]

# YOUR CODE STARTS HERE
prioritized_tasks = {
    "high_priority": high_priority_tasks,
    "medium_priority": medium_priority_tasks,
    "low_priority": low_priority_tasks,
}

for task in prioritized_tasks["high_priority"]:
    print_llm_response(task)
# -------------------------------------
# END CHALLENGE 5
