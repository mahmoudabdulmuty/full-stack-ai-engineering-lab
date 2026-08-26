# Customizing Prompts with Data — reference (Module 2, Lesson 4)

Source: DeepLearning.AI "Customizing recipes with lists, dictionaries and AI" (Andrew Ng).

## Core Concept
Instead of hardcoding prompt strings, store structured data (profiles, configurations, user inputs) in dictionaries and lists, and interpolate them into f-string prompt templates.

## Pattern: Dict → f-string Template
```python
player_profile = {
    "name": "Vinicius Jr",
    "position": "Winger",
    "preferred_drills": ["1v1 finishing", "pace dribbling"],
    "fitness_rating": 8,
}

# Interpolating dict lookups and list indexes directly
prompt = f"""Generate a training plan for {player_profile['name']}:
- Position: {player_profile['position']}
- Primary Drill: {player_profile['preferred_drills'][0]}
- Intensity Level: {player_profile['fitness_rating']}/10"""

response = get_llm_response(prompt)
```

## Quotes Inside f-strings
- Outer double quotes `f"..."` -> use single quotes for keys `f"{d['key']}"`.
- Multi-line strings `f"""..."""` make prompt formatting clean and readable without `\n`.

## Evaluation Timing (Crucial Trap)
- **f-strings evaluate at definition time**, not when printed or passed to a function.
- If you mutate a list (`.remove()`, `.append()`) or update a dict key (`d["rating"] = 9`), you **must reconstruct the f-string prompt** for the changes to appear.

```python
d = {"rating": 8}
prompt = f"Rating is {d['rating']}"  # prompt is now "Rating is 8"
d["rating"] = 9                     # dict updated, but 'prompt' is unchanged!

prompt = f"Rating is {d['rating']}"  # Re-evaluate to get "Rating is 9"
```

## Preview: Booleans for Decision Making (M2L5)
```python
player_profile["is_starter"] = True  # bool flag for if/else comparisons
```
