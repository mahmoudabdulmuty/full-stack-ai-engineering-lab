# ============================================================
# M2L4 — Customizing Prompts with Lists, Dictionaries and AI
# Practice file for Mahmoud — write challenges here, then run:
#   python practice/m2l4-custom-prompts.py
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] Generated output based on: {prompt[:40]}..."


# ---- CHALLENGE 1: Structured Profile ----
# Build a dictionary `player_profile` containing:
#   "name": "Vinicius Jr"
#   "position": "Winger"
#   "preferred_drills": ["1v1 finishing", "pace dribbling", "cutbacks"]
#   "fitness_rating": 8
#
# Print the dictionary to verify.
# -------------------------------------
# YOUR CODE STARTS HERE
player_profile = {
    "name": "Vinicius Jr",
    "position": "Winger",
    "preferred_drills": ["1v1 finishing", "pace dribbling", "cutbacks"],
    "fitness_rating": 8,
}
# print(player_profile)

# -------------------------------------
# END CHALLENGE 1


# ---- CHALLENGE 2: Prompt Interpolation from Dict ----
# Build a multi-line f-string `training_prompt` requesting an AI training plan.
# Inside the f-string, interpolate values directly from `player_profile`:
#   - Target drill focus: {player_profile["preferred_drills"]}
#   - Position: {player_profile["position"]}
#   - Intensity (out of 10): {player_profile["fitness_rating"]}
#
# Pass `training_prompt` to `print_llm_response(training_prompt)`.
# -------------------------------------
# YOUR CODE STARTS HERE
training_prompt = f""" I want a traing session
 to this player {player_profile["name"]} drill focus {player_profile["preferred_drills"][0]}
 Position is {player_profile["position"]} and Intensity is {player_profile["fitness_rating"]}
 """
# (print_llm_response(training_prompt))
# -------------------------------------
# END CHALLENGE 2


# ---- CHALLENGE 3: Combining with Standalone Lists & Updating ----
# 1. Define a standalone list `available_equipment` = ["cones", "resistance bands", "mini goals"]
# 2. Add an instruction in the prompt using `{available_equipment}`.
# 3. Simulate equipment change: remove "resistance bands" from `available_equipment`.
# 4. Update player's "fitness_rating" to 9 in the dictionary.
# 5. Re-run and print the updated LLM response.
# -------------------------------------
# YOUR CODE STARTS HERE
player_profile["available_equipment"] = ["cones", "resistance bands", "mini goals"]
player_profile["fitness_rating"] = 9

training_prompt = f""" I want a traing session
 to this player {player_profile["name"]} drill focus {player_profile["preferred_drills"][0]}
 Position is {player_profile["position"]} and Intensity is {player_profile["fitness_rating"]}
 and his available equipment is {player_profile["available_equipment"][0]} and {player_profile["available_equipment"][1]}
  """
player_profile["available_equipment"].remove("resistance bands")
print_llm_response(training_prompt)

# -------------------------------------
# END CHALLENGE 3
