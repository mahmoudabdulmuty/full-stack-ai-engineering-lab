# Booleans & Conditionals — reference (Module 2, Lessons 5–6)

Source: DeepLearning.AI "Comparing data in Python" + "Helping AI make decisions" (Andrew Ng).

## The bool type
- Only two values: `True` / `False` — **capitalized** (JS: lowercase).
- `type(True)` → `<class 'bool'>`.

## Comparison operators (each returns a bool)
```python
age > other_age     # strictly greater
age < other_age     # strictly less
age >= other_age    # greater or equal
age <= other_age    # less or equal
a == b              # EQUALITY — double equals (no === in Python!)
a != b              # not equal
```
- Comparisons are values: `is_oldest = modric_age > vini_age` stores the bool.
- Works on strings too: `"starter" == "Starter"` → `False` (case-sensitive, char-by-char).
- **No coercion**: `"5" == 5` → `False`. Python never guesses across types.

## Assignment vs equality (the big one)
- `=` assigns (statement only — can't live inside expressions).
- `==` compares.
- JS bug `if (x = 5)` is impossible in Python: inside a call/condition, `name=value` parses as a keyword argument or raises SyntaxError.

## Logical operators — words, not symbols
```python
a and b    # True only if BOTH true      (JS &&)
a or b     # True if AT LEAST ONE true   (JS ||)
not a      # flips                       (JS !)
```
- Style tip (VS Code/Ruff agree): prefer `a != b` over `not a == b`.
- Multi-variable one-liner: `a, b = 8, False` (tuple unpacking) — NOT `a = 8, b = False`.

## if / else — colon + indentation, no braces, no parens
```python
if task["minutes"] <= 5:
    print_llm_response(f"Do now: {task['description']}")
else:
    later_tasks.append(task["description"])
```
- Condition needs NO parentheses; the `:` starts the block; 4-space indent = membership.
- `else:` aligns with its `if`, own colon, own indented block.
- Unindented code after runs once, after the whole construct.

## The full decision pipeline (M2 capstone pattern)
```python
later_tasks = []
for task in tasks:                      # walk the list of dicts
    if task["minutes"] <= 5:            # decide per item
        print_llm_response(...)         # act NOW
    else:
        later_tasks.append(task["description"])   # save for later
print(len(later_tasks))                 # measure after the loop
```

## JS → Python quick translation
| JS | Python |
|----|--------|
| `===` / `!==` | `==` / `!=` |
| `&&` / `\|\|` / `!` | `and` / `or` / `not` |
| `true` / `false` | `True` / `False` |
| `if (cond) { }` | `if cond:` + indent |
| `cond ? a : b` | doesn't exist at this stage |
| `"5" == 5` → `true` | `"5" == 5` → `False` |

## Common errors / traps
- `=` where you meant `==` → TypeError/SyntaxError (Python protects you).
- Forgetting `:` after if/else → SyntaxError.
- `"5" == 5` silently `False` — check types when equality misbehaves.
