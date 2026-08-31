# Files, handles, context managers & CSV — interview notes

This is the consolidated map for M3L1–M3L5. The key is to stop treating “the file” as
one thing. There are four different objects/stages:

```text
PATH ON DISK ──open()──> FILE HANDLE ──read()──────> STRING IN MEMORY
                                └──────DictReader──> ROW DICTS ──collect──> LIST OF DICTS
```

**Memory anchor:**

- The disk file is not the file handle.
- The file handle is not the data already copied into memory.
- Closing the handle does not erase a collected string, dictionary, or list.

Run scripts from the workspace root (`C:\Users\Mahmoud\Downloads\ai-python-tutor`) —
the current working directory decides which relative paths resolve.

## The objects you must not mix up

| Name | What it is | Example | What survives after close? |
|---|---|---|---|
| Path | A string telling Python where the file lives | `"practice/data/itinerary.csv"` | Yes |
| File on disk | Persistent bytes/text stored by the OS | `itinerary.csv` | Yes |
| File handle | The live object returned by `open()`; has mode and cursor position | `file` | No usable I/O after close |
| String | Text already copied into memory by `.read()` | `content` | Yes |
| `DictReader` | A lazy CSV parser connected to an iterable of lines, usually an open handle | `reader` | Cannot continue if its handle closed |
| Row dictionary | One parsed CSV row; header names become keys | `{"City": "Cairo"}` | Yes once produced |
| List of row dictionaries | Rows you deliberately collected | `itinerary` | Yes |

## Choose the pipeline by the data shape

| Goal | Use | Result | LLM needed? |
|---|---|---|---|
| Read one small text document | `content = file.read()` | One `str` | No |
| Process text line by line | `for line in file:` | One `str` per iteration | No |
| Read table-shaped CSV | `csv.DictReader(file)` | One `dict` per row | No |
| Keep CSV rows after close | append rows or call `list(reader)` inside `with` | `list[dict]` | No |
| Filter exact values | `if row["Country"] == "Egypt"` | Matching rows | No |
| Generate suggestions from a selected row | build prompt → real LLM call | Generative text | Yes, when creativity is the requirement |
| Replace a text file | open in `"w"`, then `.write(...)` | Old contents discarded | No |
| Add to the end | open in `"a"`, then `.write(...)` | Old contents preserved | No |

## `open()` — acquire a handle

```python
file = open(path, mode, encoding="utf-8")
```

- `open()` returns a **file handle**, not the file contents.
- Omitting `mode` defaults to `"r"`.
- `encoding="utf-8"` is the normal explicit choice for text files.
- For CSV, use `newline=""` so the `csv` module controls newline handling.

### Modes you should recognize

| Mode | Meaning | Existing file | Missing file | Allowed core operation |
|---|---|---|---|---|
| `"r"` | Read text | Preserved | `FileNotFoundError` | `.read()` |
| `"w"` | Write/replace text | **Truncated immediately at `open()`** | Created | `.write()` |
| `"a"` | Append text | Preserved; writes go to end | Created | `.write()` |
| `"x"` | Create only | `FileExistsError` | Created | `.write()` |
| `"b"` suffix | Binary data, e.g. `"rb"` | Preserved | Depends on base mode | bytes, not strings |
| `"+"` suffix | Read and write, e.g. `"r+"` | Preserved initially | Depends on base mode | Both; cursor rules matter |

For current course work, master `"r"`, `"w"`, and `"a"`; recognize the others for interviews.

## File-handle methods and cases

### `.read()` — copy content into one value

```python
content = file.read()       # whole remaining file → one string
first_20 = file.read(20)    # at most 20 characters from current cursor
```

- `.read()` returns a `str` in text mode and advances the handle's cursor.
- Calling it again at end-of-file returns `""`, not the contents again.
- Use it for small/medium raw text when you want string operations or an LLM prompt.
- Do **not** pass `file.read()` to `DictReader` as a replacement for the handle: a string
  is iterable character by character.

### `.readline()` and direct iteration — one line at a time

```python
line = file.readline()

for line in file:
    print(line)
```

- `.readline()` returns one line, usually including `"\n"`.
- `for line in file` is the normal memory-efficient line-by-line pattern.
- These also advance the cursor.

### `.write(text)` — send a string to a writable handle

```python
characters_written = file.write("NEW\n")
```

- Requires a writable mode such as `"w"` or `"a"`.
- Takes a string in text mode and returns the number of characters written.
- `"w"` decides replacement at **open time**; `.write()` supplies the new text later.
- `.write()` does not add a newline automatically.

### `.close()` — end the handle lifecycle

```python
file.close()
```

- Releases the OS resource and flushes pending writes.
- The disk file remains.
- Strings/lists/dictionaries already copied into memory remain.
- Further handle operations raise `ValueError: I/O operation on closed file`.

### `with` — automatic close, including on exceptions

```python
with open("email.txt", "r", encoding="utf-8") as file:
    content = file.read()

# file is closed here; content is still usable
```

Think of `with` as a Vue component/resource lifecycle boundary: acquire at entry,
use only inside the block, guaranteed cleanup at exit. Do not add `file.close()` inside a
normal `with` block.

## CSV: structured text → row dictionaries

CSV is still text on disk, but its rows and columns carry predictable structure.

```text
City,Country,Arrival,Departure
Cairo,Egypt,2026-09-01,2026-09-04
```

```python
import csv

with open("itinerary.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    itinerary = []
    for row in reader:
        itinerary.append(row)
```

What happens:

1. `open()` returns a readable handle.
2. `DictReader(file)` creates a **lazy parser**, not a list.
3. The first CSV row supplies dictionary keys and is not returned as data.
4. Each iteration reads the next CSV record and yields a new `dict`.
5. `append()` stores that dictionary in `itinerary`.
6. Leaving `with` closes the handle. The collected list remains usable.

All ordinary CSV field values arrive as strings. Convert explicitly when needed:

```python
goals = int(row["Goals"])
```

### Same collection, shorter form

```python
with open("itinerary.csv", encoding="utf-8", newline="") as file:
    itinerary = list(csv.DictReader(file))
```

Ruff may suggest this as `PERF402`. The explicit loop is useful while learning or when
you need conditions/transformation; `list(reader)` is concise when copying every row.

### Deterministic filtering before any LLM

```python
egypt_stops = []
for row in itinerary:
    if row["Country"] == "Egypt":
        egypt_stops.append(row)
```

Use Python for exact known rules. Use an LLM only for tasks that need language
understanding or generation. “Find Country == Egypt” is programming; “invent a useful
three-day plan” is generative.

## Error map — say the type and the cause

| Situation | Result | Why |
|---|---|---|
| `open("missing.txt", "r")` | `FileNotFoundError` | Read mode requires an existing path |
| `.read()` on a `"w"` handle | `io.UnsupportedOperation` | Mode is not readable |
| `.write()` on an `"r"` handle | `io.UnsupportedOperation` | Mode is not writable |
| `.read()` after close | `ValueError` | Handle lifecycle ended |
| `row["Missing"]` | `KeyError` | Dictionary key does not exist |
| `rows[99]` | `IndexError` | List position does not exist |
| `csv.DictReader(file.read())` | Often malformed character-level rows, not necessarily an exception | String iteration yields characters, not file lines |
| Wrong relative path from current terminal folder | `FileNotFoundError` | Relative paths start at CWD, not automatically at the script |

## Safe selection when position is unknown

```python
selected_stop = None
for stop in itinerary:
    if stop["City"] == "Alexandria":
        selected_stop = stop
        break

if selected_stop is not None:
    print(selected_stop["City"])
```

- Use list indexing when position is part of the contract.
- Search by a key when CSV ordering is not trustworthy.
- Guard the not-found case before bracket access.

## Interview-ready explanations

### “Explain Python file handling.”

> `open()` returns a file handle whose mode controls allowed operations. I normally use
> a `with` context manager so the handle closes even if an exception occurs. For raw text
> I call `.read()` or iterate by line. Values already read into memory remain usable after
> the handle closes.

### “How do you read CSV as dictionaries?”

> I open the CSV with `newline=""`, pass the live handle to `csv.DictReader`, and consume
> it inside the `with` block. The header becomes dictionary keys and each later record is
> yielded as a dictionary. I collect rows into a list only when later code needs them after
> the file is closed.

### “Why not use an LLM to filter the CSV?”

> Exact structured conditions are deterministic, cheaper, and testable in normal Python.
> I select the correct rows first, then use an LLM only for language-heavy generation or
> interpretation.

### JS/Vue translation—useful, but not exact

- Python `list` ≈ JS array.
- Python `dict` ≈ plain JS object.
- `print()` ≈ `console.log()` for quick debugging.
- `with open(...)` has no direct spread-operator equivalent; it is a resource lifecycle.
- `DictReader` is a parser/iterator, not `[...]` spread and not a copied list.
- A missing Python dict key with brackets raises `KeyError`; JS property access often gives `undefined`.

## Quick recipes

## The file pattern (used throughout Module 3)

```python
f = open("email.txt", "r")    # "r" = read mode → file handle
text = f.read()                # whole file → ONE string
f.close()                      # release the handle
```

## The `with` form (modern Python, runs M3L1)

```python
with open("email.txt", "r", encoding="utf-8") as f:
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

## Official references

- [Python tutorial — reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python `csv` module — `DictReader` and CSV newline handling](https://docs.python.org/3/library/csv.html)
