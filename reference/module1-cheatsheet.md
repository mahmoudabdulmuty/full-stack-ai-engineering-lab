# Module 1 — Basics of AI Python Coding (reference)

Source: DeepLearning.AI "AI Python for Beginners" (Andrew Ng), Module 1.

## Program & execution
- A program is instructions executed **top to bottom**.
- In Jupyter: the **last line of a cell auto-displays** without `print()`. In a `.py` script: you MUST `print()` explicitly.

## Data types
| Type | Example | JS parallel |
|------|---------|-------------|
| str | `"hello"`, `'hello'`, `"""multi-line"""` | string |
| int | `42` | number (integer) |
| float | `3.14` | number (float) |
| bool | `True` / `False` (capital letters!) | `true` / `false` |

- `"""triple quotes"""` and `'''single triple'''` are identical.
- **No silent coercion**: `"1" + 1` raises `TypeError` (JS would say `"11"`). Python fails loud.

## Variables
- `snake_case` convention: `player_name`, `book_copies`.
- Dynamically typed — type comes from the current value, like JS `let`. No `let`/`const`/`var` keywords.

## Operators
`+  -  *  /  **` (power). No `++` / `--` in Python — use `x = x + 1` or `x += 1`.

## Strings & f-strings
- `print(a, b)` → separates with a space. `print(a + b)` → concatenates.
- f-string: `f"text {variable}"` — the `f` prefix is mandatory; without it, `{variable}` prints literally.
- Formatting: `{value:.2f}` → 2 decimal places (e.g. `f"{42.66666:.2f}"` → `'42.67'`).

## Built-in functions
- `type(value)` → the class of a value (`<class 'str'>`, `<class 'float'>`, ...).
- `len(value)` → count of items in a **container**: characters in a string, elements in a list.
- `round(value)` → rounds to int. `round(value, 2)` → rounds to 2 decimals.

## Functions
```python
def function_name(param1, param2):
    return param1 + param2     # indented body, colon at end, no {}
```
- `def name(params):` — colon ends the line, body indented **4 spaces** (no braces).
- `return` sends a value back **silently**.
- No `return` → returns `None` (not JS `undefined`).
- `print()` inside a function = **side effect only**, still returns `None`.
- `return a, b` → returns a **tuple** `(a, b)`, not an array.

## Imports
- `import module` → use `module.func()` (keeps namespace, avoids clashes).
- `from module import func` → use `func()` directly. No `{}` needed (unlike JS destructuring).
- **No `export` keyword** — all functions importable by default.
- `_prefix` = private **by convention only**, not enforced.

## LLM helpers (course utilities)
| Helper | Does | Returns |
|--------|------|---------|
| `print_llm_prompt(prompt)` | shows the prompt like `console.log` | `None` — NO LLM call |
| `print_llm_response(prompt)` | sends to LLM, prints answer | `None` |
| `get_llm_response(prompt)` | sends to LLM | **the string** — store & reuse |

Rule: need the value → `get_llm_response`. Just showing → `print_llm_response`.

## The None habit
Anything that does a side effect in Python returns `None`: `print`, `print_llm_response`, and (Module 2) list mutators like `append`/`remove`. Never assign from them expecting a value back.

## JS → Python quick translation
| JS | Python |
|----|--------|
| `let x = 5` | `x = 5` |
| `"text " + x` | `f"text {x}"` |
| `arr.push(x)` | `list.append(x)` |
| `arr.splice(i, 1)` | `list.remove(value)` |
| `x++` | `x += 1` |
| `null` / `undefined` | `None` |
| `{ a, b }` destructure import | `from m import a, b` |
| `export function f()` | `def f():` (importable anyway) |
| `forEach` / `for` | for loop (Module 2) |