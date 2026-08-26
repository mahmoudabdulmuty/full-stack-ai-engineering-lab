# Dictionaries — reference (Module 2, Lesson 3)

Source: DeepLearning.AI "Prioritizing tasks with dictionaries and AI" (Andrew Ng).

## What a dictionary is
A single variable holding **key–value pairs**. The Python equivalent of a JS object — find by **name**, not by position.

## Creating
```python
ice_cream_flavors = {
    "mint chocolate chip": "Mint ice cream loaded with chocolate chunks",
    "cookie dough":        "Vanilla ice cream loaded with cookie dough chunks",
    "salted caramel":      "Caramel ice cream with a salted caramel ribbon",
}
```
- Curly braces `{}` open/close the dict (not square brackets).
- Each line: `"key": value` — key and value separated by a **colon**.
- Pairs separated by **commas**.
- Keys are usually strings. Values can be ANY type.

## Reading
```python
type(ice_cream_flavors)              # -> <class 'dict'>
ice_cream_flavors["cookie dough"]    # -> "Vanilla ice cream loaded with cookie dough chunks"
ice_cream_flavors["mango"]           # KeyError: 'mango'  (no silent undefined!)
ice_cream_flavors.get("mango")       # -> None           (safe)
ice_cream_flavors.get("mango", "?")  # -> "?"            (custom default)
"mango" in ice_cream_flavors         # -> False          (membership test)
```

## Modifying
```python
# Add a new key–value
ice_cream_flavors["rocky road"] = "Chocolate ice cream mixed with marshmallows and nuts"

# Update an existing key — SAME SYNTAX
ice_cream_flavors["rocky road"] = "Chocolate ice cream mixed with marshmallows and nuts (fixed)"

# Delete
del ice_cream_flavors["rocky road"]
```

## Inspection
```python
ice_cream_flavors.keys()   # view of keys
ice_cream_flavors.values() # view of values
# list(ice_cream_flavors.keys()) -> ['mint chocolate chip', 'cookie dough', ...]
```

## Values can be ANY type (including lists)
```python
isabel_facts = {
    "age": 28,
    "favorite_color": "red",
}
isabel_facts["cat_names"] = ["Charlie", "Smokey", "Tabitha"]  # value is a LIST
```

## Priority example — dict of lists + for loop
```python
high_priority_tasks = ["Compose a brief email", "Create an outline for a presentation"]
medium_priority_tasks = ["Schedule a meeting", "Draft a project update"]
low_priority_tasks = ["Clean up the desktop"]

prioritized_tasks = {
    "high priority":   high_priority_tasks,
    "medium priority": medium_priority_tasks,
    "low priority":    low_priority_tasks,
}

for task in prioritized_tasks["high priority"]:
    print_llm_response(f"Please complete this task: {task}")
```

## JS → Python
| JS | Python |
|----|--------|
| `{ key: "value" }` | `{ "key": "value" }` (quotes on keys required) |
| `obj.key` / `obj["key"]` | `dict["key"]` only — **no dot access** |
| `obj.key = val` | `dict["key"] = val` |
| missing key → `undefined` | missing key → **KeyError** (use `.get()` or `in`) |
| `Object.keys(obj)` | `dict.keys()` |
| `Object.values(obj)` | `dict.values()` |
| `for (const k in obj)` | `for k in dict:` (iterates keys) |

## Common errors
- `dict[0]` → KeyError — no index positions, only keys
- Missing key → KeyError — not `undefined`, use `.get()` or `in`
- Forgetting quotes on string keys → NameError (looks for variable)

## Course helper recap (used with dicts)
```python
# Loop over a dict VALUE that is a list
for task in prioritized_tasks["high priority"]:
    print_llm_response(f"Please complete this task: {task}")
```