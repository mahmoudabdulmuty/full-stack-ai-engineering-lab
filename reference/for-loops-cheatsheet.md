# For loops — reference (Module 2, Lesson 2)

Source: DeepLearning.AI "Repeating tasks with for loops" (Andrew Ng).

## What a for loop is
A **statement** that repeats a block of code once for each item in a list — Python's answer to JS `for...of` / `.forEach()`. No callback, no braces, no method chain.

## Syntax
```python
for task in tasks:
    print_llm_response(f"Please complete this task: {task}")
```
- `for` — the keyword that starts the statement
- `task` — the loop variable, **your chosen name**; takes each item's value in turn
- `in` — the keyword before the list
- `tasks` — the list to walk
- `:` — ends the header line (forget it → `SyntaxError: expected ':'`)
- **4-space indent** — marks the body; **only indented lines repeat** (uneven indent → `IndentationError`)

Reads like English: *"for each task in tasks, print the LLM response for that task."*

## Loop variable mental model
- The variable holds the **VALUE**, not the index. No C-style `for (let i = 0; ...)` — `range()`/`enumerate()` come much later.
- First pass: `task == tasks[0]`. Last pass: the final element. 100 items → 100 passes.
- **No block scope.** The variable is ordinary; after the loop it still exists, holding the last value. (JS `const` in `for...of` is scoped to the braces and gone — Python is different.)

## Indentation is membership
```python
for flavor in ice_cream_flavors:
    prompt = f"Write a captivating description for {flavor}"
    print_llm_response(prompt)
```
Both lines run on every pass, each with a fresh `flavor`. Un-indent the last line and it runs **once, after the loop**, holding the **last** prompt — no error, silently wrong.

## Accumulator pattern (build a list with a loop)
```python
promotional_descriptions = []            # start empty
for flavor in ice_cream_flavors:
    prompt = f"Write a captivating description for {flavor}"   # the question
    response = get_llm_response(prompt)  # the ANSWER
    promotional_descriptions.append(response)                  # store the answer
```
- prompt = what you ask; response = what comes back; the list holds **answers**, not questions.
- `len(list)` after the loop == `len(source list)`. Measure, don't guess.

## Scope
- Python has module scope (≈ global) and function scope. **No block scope** — `for`/`if`/`while` never create one.
- A variable assigned inside a loop is visible after it. (`global`/`nonlocal` are edge cases; not in this lesson.)

## JS → Python
| JS | Python |
|----|--------|
| `arr.forEach(x => ...)` | `for x in arr:` |
| `for (const x of arr) { }` | `for x in arr:` |
| `const out = []; out.push(x)` | `out = []; out.append(x)` |
| C-style `for (let i = 0; ...)` | doesn't exist directly (later: `range()`) |

## Common errors
- Missing `:` → `SyntaxError: expected ':'`
- Missing / uneven indent → `IndentationError: expected an indented block`
- Storing the prompt instead of the response → runs clean, silently wrong

## Course helper recap (used with loops)
```python
print_llm_response(f"Please complete this task: {task}")   # prints, returns None
response = get_llm_response(prompt)                        # returns the string — store it
```