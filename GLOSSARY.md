# AI Python Glossary

The canonical vocabulary for this teaching workspace. A term enters the glossary only once the learner has demonstrated they can use it correctly.

## Core data

**Variable**:
A name bound to a value. Reassignable like `let` in JS — there is no `const`; Python relies on convention and discipline instead.
_Avoid_: const, let

**String (str)**:
A sequence of characters, written with single, double, or triple quotes. Triple quotes span multiple lines.
_Avoid_: text (JS), char array

**Integer (int)**:
A whole number without a decimal point.

**Float (float)**:
A number with a fractional part. `{value:.2f}` in an f-string formats a float to two decimals.

**Boolean (bool)**:
`True` or `False` — note the capital letters, unlike JS `true`/`false`.

**F-string**:
`f"text {variable}"` — a template string that interpolates values at runtime. The `f` prefix is mandatory.
_Avoid_: template literal (that's JS), concat with `+`

**List**:
An ordered collection of values in square brackets `[...]`, comma-separated, zero-indexed. JS array's twin, but the methods differ: `append()` (no push), `remove()` by value (no splice). Mutators return `None`.
_Avoid_: array, push, splice

**For loop**:
`for item in collection:` — repeats an indented body once per item; the loop variable holds each element's **value** in turn, not its index. Only indented lines repeat. No block scope: the variable persists after the loop, holding the last value.
_Avoid_: forEach (a JS method — not on Python lists), C-style `for (let i...)`, braces

**Dictionary (dict)**:
An unordered collection of key–value pairs in curly braces `{ "key": value }`. The Python twin of a JS object — find by **name**, not position. Keys are unique; values can be any type. Access with `d["key"]` (square brackets, no dot notation). Missing key → `KeyError` (not `undefined`); use `d.get("key")` for safe `None` or `d.get("key", default)`.
_Avoid_: object (JS), map (different type), dot access `d.key`, index access `d[0]`

**Boolean (bool) — comparisons**:
Every comparison (`>`, `<`, `>=`, `<=`, `==`, `!=`) evaluates to `True`/`False` (capitalized) and can be stored in a variable. No coercion: `"5" == 5` → `False`. Strings compare case-sensitively, char-by-char.
_Avoid_: `===`, loose-equality thinking

**Logical operators**:
Words, not symbols: `and` (JS `&&`), `or` (JS `||`), `not` (JS `!`). Prefer `a != b` over `not a == b`.
_Avoid_: `&&`, `||`, `!`

**if / else (conditional)**:
`if condition:` runs an indented block only when the condition is True; `else:` aligned with its `if` runs otherwise. No parentheses around conditions, no braces — colon + indentation is membership. Assignment is a statement in Python and cannot appear inside expressions/calls (JS's silent `if (x = 5)` bug is impossible).
_Avoid_: ternary `? :` at this stage, parens around condition

## Code structure

**Function**:
Reusable named block of instructions, defined with `def name(params):` and an indented body. Returns a value with `return`.
_Avoid_: method (unless on an object), arrow function

**Return**:
Sends a value back to the caller silently. A function with no `return` returns `None`.
_Avoid_: console.logging as a return

**None**:
Python's null — returned implicitly by functions with no `return`. Not `undefined`.

**Tuple**:
An immutable ordered collection; `return a, b` packs two values into a tuple.
_Avoid_: array (JS), pair only

**Comment**:
Text after `#` that Python ignores. The equivalent of `//` in JS.

**Import**:
`import module` vs `from module import func` — pulls in code from other files/packages. No `{}` needed, no `export` keyword.
_Avoid_: destructuring (that's JS), require

**Dynamic typing**:
Variables hold any type and can change type on reassignment — like JS `let`, but with no coercion surprises: `"1" + 1` raises an error instead of guessing.

## LLM helpers (course-specific)

**The AI loop**:
question (prompt) → `get_llm_response` → STORE the response → use it. The atom of every AI application — it scales all the way up: function calling (model returns a tool call you store and execute), agents (loops of the atom), RAG (retrieved docs stored into the prompt).
_Avoid_: printing when you need to store; storing prompts instead of responses; passing a RESPONSE back into print_llm_response (real course: that's a SECOND LLM call, not a display)

**get_llm_response(prompt)**:
Sends the prompt to an LLM and RETURNS the response as a string — store it and reuse it.
_Avoid_: print_llm_response when you need the value later

**print_llm_response(prompt)**:
Sends the prompt to an LLM, prints the response to screen, returns `None`.
_Avoid_: using it when the response must be stored