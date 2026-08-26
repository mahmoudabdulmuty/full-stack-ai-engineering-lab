# Lists — reference (Module 2, Lesson 1)

Source: DeepLearning.AI "Completing a task list with AI" (Andrew Ng).

## What a list is
A single variable holding **multiple values** in order. The Python equivalent of a JS array.

## Creating
```python
friends_list = ["Tommy", "Isabel", "Daniel"]
ages = [23, 28, 31]          # lists hold numbers too
tasks = [                    # can span multiple lines
    "Email my boss",
    "Write a poem for Otto",
]
```
- `[]` opens/closes the list. Elements separated by commas.

## Reading
```python
type(friends_list)          # -> <class 'list'>
len(friends_list)           # -> 3   (same len() as strings)
friends_list[0]             # -> 'Tommy'   (counting starts at 0)
friends_list[1]             # -> 'Isabel'
friends_list[2]             # -> 'Daniel'
friends_list[3]             # IndexError: list index out of range
```
- Indexing uses **square brackets** `[ ]`. Parentheses `( )` cause an error.
- Ask for a position that doesn't exist → `IndexError: list index out of range`.
- Error messages look cryptic — pasting them into a chatbot is a legit debugging move.

## Modifying
```python
friends_list.append("Otto")        # add to the END
friends_list.remove("Tommy")       # remove the FIRST match of this value
print(friends_list)                # -> ['Isabel', 'Daniel', 'Otto']
```

## Key mental model
- **Index = position, counting from zero.** Like stadium seat numbers: seat 0 is the first seat, seat 1 the next.
- A list is *one* object you can pass around — this replaces the Module 1 pattern of repeating code once per value.
- The manual "do task[0], then task[1], then task[2]" loop is repetitive — that repetition is exactly what the next lesson (for loops) exists to kill.

## Course helper recap (used with lists)
```python
print_llm_response(f"Write a poem for {friends_list[0]}")   # prints, returns None
```

## Gap-fill notes from Module 1 that apply here
- `len()` generalizes: worked on strings, now works on lists.
- `type()` works on everything, including lists.