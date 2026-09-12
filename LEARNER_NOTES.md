# Mahmoud's learner notes

This file is learner-owned. The tutor may read it when Mahmoud asks for review or a knowledge check, but must not write, rewrite, or polish the entries.

After each lesson, write from memory before opening a transcript, cheatsheet, or chat history. Keep the entry to five short bullets; this is retrieval practice, not documentation.

When the entry is finished, tell the tutor: `I finished my <lesson> note—review my understanding.` The lesson debrief is mandatory: discuss the note and answer one changed-context question before the lesson is fully closed.

## Copy this template for each lesson

### Module _ — Lesson _ — Title — Date

- I can now:
- The main rule in my own words:
- A mistake I made or nearly made:
- Connection to Vue/frontend work:
- Recheck later:

### Module 3 — Lesson 4 — Extracting information — 28-08-2026

I can now read several files, build one response per file, combine the
responses, and save them.

"w" creates or overwrites a file when it is opened. I cannot read from a write-only
handle. I close it and reopen with "r".

My mistake was reusing stale variables from the previous loop.

The local LLM helper proves the Python pipeline works, but it does
not prove that real extraction works.

### Module 3 — Lesson 5 — Vacation planning using CSV files — 2026-08-28

- I can now use DictReader for making iterable list from a csv file
- DictReader is a method when import CSV it allowed you to work with
  csv files as like dicts with key and values
- mistake I made I thought that it uses the content itself as the content
  is returning string, but I've to work with line by line to make it iterable object later one
  so, I missed this point
- recheck later: maybe there's a lot of methods now with write, read mode and how to use in each case has to make something to revise this accurately not to making any mistakes in future with this

- Connection to Vue/frontend work: working with CSV and passing the values we got from open the object file itself to DictReader method to make it iterable, just like the spread operator we made to copy from arrays in JS, we just want to have like a copy and not making any change to the file itself

### Module 3 — Lesson 6 — Turning code blocks into reusable functions — 2026-09-04

- I can now: turn a block of code into a reusable function.
- The main rule in my own words: how can we use a reusable function instead of repeating blocks of code (DRY)
- a mistake I made: not knowing how to slice first chars of a file context
- connection to frontend work: we make this often alot, using reusable components across our apps instead of redundant code
- Recheck later: maybe there's other methods with read and write mode and how to pass parameters to this method can change the output

### Module 3 — Lesson 7 — Creating detailed itineraries for multiple cities — 2026-09-04

- I can now write a mini script retrieving data from csv file and build around it
- the main rule is how we can use loops with functions to build a mini script
- a mistake I made, I didn't have the ability to understand the instructions at first maybe I should concentrate more
- connect to FE: we usually do this write loops inside function and functions with loops to generate UI
- recheck later: read and write methods, has to build on it more

### Module 4 — Lesson 1 — Using functions from a local file — 2026-09-06

- I can now import modules and functions from other files through modules with dot notation.
- the main rule how to use functions from local file.
- a mistake I made, I thought importing the module directly imported all its functions.
- connect to FE: the same happens with frameworks as components is built on top of this, importing and exporting components
  through SPA app.
- recheck later: hmm, let's see; practice more I think.

### Module 4 — Lesson 2 — Built-in packages — 2026-09-09

1. built in functions through modules inside python
2. from math import floor
3. from statistics import mean
4. the population is the target list, tuble or whatever and the number is the length for the list returning,
5. sample is a built-in function selects without replacement, guarantees the returning type is list, the length of the list is the number passed as count
   what remains unpredictable is the items it selects from the population

### Module 4 — Lesson 3 — Using third-party packages — 2026-09-10

1. standard is installed in python already, Third-party needs insatllation
2. module is not installed in the python environment
3. series 
4. as pd.read_csv() returns series, it can be chained through .median
5. the first one in x-axis and the other in y-axis

### Module 4 — Lesson 4 — Installing packages — 2026-09-10
1. a module installation to be imported in the python environment
2. to be able to use it, if installs in another environment will have moduleNotFoundERROR
3. install the third-party packages through this command
4. we're importing this bs4 from the module name beautifualsoup4
5. it parse html to be able to use it's content using some methods like find and find_all


### Module 4 — Lesson 5 — APIs to get data from the web — 2026-09-12

1. requests.get(url) will make return a response through the api from the server url I pass, it needs internet connection as it's a request to server
2. the data is the response dict transferred to json python disct to retreive it's data from
3. through ["temprature"]
4. outfit_prompt contain prompt to LLM asking for an appropriate outfit according to live weather
5. cause it's private data, .gitignore make sure that git not tracking this file 
