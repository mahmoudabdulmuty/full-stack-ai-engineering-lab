# Files & Documents — M3 cheatsheet

Files / text documents live on disk. You get them into Python with `open(..., "r")`,
pour the whole contents into one string with `.read()`, and release the handle with
`.close()`. Run scripts from the workspace root (`C:\Users\Mahmoud\Downloads\ai-python-tutor`) —
the working directory decides which relative paths resolve.

## The file pattern (used throughout Module 3)

```python
f = open("email.txt", "r")    # "r" = read mode → file handle
text = f.read()                # whole file → ONE string
f.close()                      # release the handle
```

## The `with` form (modern Python, runs M3L1)

```python
with open("email.txt", "r") as f:
    text = f.read()            # file auto-closes at the end of the block
```

## Loop over many files

```python
files = ["practice/data/a.txt", "practice/data/b.txt", ...]
for fname in files:
    f = open(fname, "r")
    content = f.read()
    f.close()
    print(fname)
```

## Write, close, then reopen to verify (M3L4)

```python
out = open("report.txt", "w")  # creates or OVERWRITES
out.write(result)               # write mode cannot read
out.close()

saved = open("report.txt", "r")
checked = saved.read()
saved.close()
```

- `"w"` discards old contents before writing; it does not append.
- A handle opened with `"w"` is not readable.
- A closed handle cannot be reused. Reopen the path in `"r"` for verification.
- Add `"\n"` between accumulated entries when each result needs its own line.

## Structured extraction + the local stub

- Classification returns a label such as `relevant`.
- Extraction returns useful fields such as restaurant and dish names.
- CSV is plain-text table data: one row per line, columns separated by commas.
- The local `get_llm_response` **stub echoes the prompt**. It proves the Python pipeline is wired correctly, but not that real extraction or CSV formatting works.

## `in` on strings — substring test (M3L3 tool)

```python
if "the" in content.lower():   # content lowered FIRST, then checked
    print("contains 'the'")
```

- `"the" in content` is **case-sensitive**: `"THE"` will not match.
- Lowercase the content first: `"the" in content.lower()` so THE / The / the all count.
- `.lower()` returns a **new lowered string**; the original is unchanged.

## Relative paths & CWD

- Relative paths resolve from the working directory (`os.listdir()` shows it).
- Run from the workspace root: `python practice/m3l3-food-critics.py` → open "practice/data/...".
- Run from inside `practice\`: "practice/data/..." breaks — those files live one level up.

## The LLM helpers (stubbed, no API key)

```python
print_llm_response(prompt)   # prints  [LLM] {prompt}
get_llm_response(prompt)     # returns "[LLM reply] {prompt}" — STORE it
```

## Compare this to M2

- Files are just strings stored on disk → open → `.read()` → work with the text like any string.
- A file's text is an ordinary Python string: `len(...)`, `in`, `.lower()`, f-strings all work on it.
