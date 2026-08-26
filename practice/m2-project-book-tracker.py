# ============================================================
# MODULE 2 CAPSTONE PROJECT — Book Tracker (local edition)
# The graded assignment rebuilt locally. All code YOURS.
# Run: python practice/m2-project-book-tracker.py
#
# Skills graded: functions (M1), lists (L1), for loops (L2),
# dictionaries (L3), f-string prompts (L4), comparisons (L5),
# if/else decisions (L6). PREDICT-BEFORE-RUN as always.
# ============================================================

# ---- Offline stand-ins for the course helper functions ----
def print_llm_response(prompt):
    print(f"[LLM] {prompt}")


def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- PROVIDED DATA (do not modify this block) ----
book_database = [
    {
        "title": "The Arrival",
        "author": "Shaun Tan",
        "genre": "graphic novel",
        "pages": 128,
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "self-help",
        "pages": 320,
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Hunt & Thomas",
        "genre": "tech",
        "pages": 352,
    },
    {
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "genre": "history",
        "pages": 498,
    },
    {"title": "Dune", "author": "Frank Herbert", "genre": "sci-fi", "pages": 658},
]


# ============================================================
# PART 1 — Add a book
# Write a function add_book(title, author, genre, pages) that:
#   - builds a dict with those four keys
#   - appends it to book_database
#   - RETURNS the new total number of books (len!)
# Then call it once with any book you like and print the result.
# PREDICT the printed number before running.
# ============================================================
# YOUR CODE STARTS HERE
def add_book(title, author, genre, pages):
    if title and author and genre and pages:
        new_book = {"title": title, "author": author, "genre": genre, "pages": pages}

        book_database.append(new_book)
        print("book added successfully to the data base")
        print(f"now the total number of books is {len(book_database)}")
        return len(book_database)
    else:
        print("book not added. maybe you haven't described on of book mandatory keys")


add_book(
    "Maus", "Art Spiegelman", "graphic novel", 296
)  # expects good add with number icreases with one as new book added
# add_book("Watchmen")  # expects not adding throwing an error
# another issue I see here not passing an object to define more what's inside it
# params here not going further than making it not descriptive, I have to remember each param to pass it

# update it still gives the same error TypeError: add_book() missing 3 required positional arguments: 'author', 'genre', and 'pages'

# ============================================================
# PART 2 — Display the shelf
# Loop over book_database and print each book as ONE line:
#   "Title by Author — N pages [genre]"
# Use an f-string with nested dict access. No raw dicts printed.
# ============================================================
# YOUR CODE STARTS HERE
for book in book_database:
    print(
        f"{book['title']} by {book['author']} — {book['pages']} pages [{book['genre']}]"
    )
# note with add_book function it gives the good case output but with this error
# when commenting the function, it's good without this error
# Traceback (most recent call last):
#   File "C:\Users\Mahmoud\Downloads\ai-python-tutor\practice\m2-project-book-tracker.py", line 86, in <module>
#     f"{book['title']} by {book['author']} — {book['pages']} pages [{book['genre']}]"
#        ~~~~^^^^^^^^^
# TypeError: 'set' object is not subscriptable


# ============================================================
# PART 3 — Search by genre
# Write a function find_books(genre) that:
#   - loops over book_database
#   - collects titles whose genre matches into a NEW list
#     (accumulator pattern — case-insensitive comparison!)
#   - RETURNS the list
# Call it twice: once for an existing genre, once for one that
# doesn't exist. Print both results. PREDICT each first.
# ============================================================
# YOUR CODE STARTS HERE


def find_books(genre):
    matching_genre_list = []
    for book in book_database:
        book_genre = book["genre"]
        if book_genre.lower() == genre.lower():
            matching_genre_list.append(book["title"])
            print(
                f"books found with new list containing titles {matching_genre_list}!!"
            )
    return matching_genre_list


find_books("tech")
find_books("horror")
# print("find-tech", find_books("tech"))
# print("find-horror", find_books("horror"))

# when making else instead of notes the second function got the prompt but when making return statement it doesn't print any ?!

# ============================================================
# PART 4 — The pre-bedtime pick (decisions + LLM)
# You have 20 minutes before bed. Loop over book_database:
#   - books with pages <= 200 -> ask the LLM (print_llm_response)
#     why this book is a good short read tonight
#   - longer books -> append their TITLES to weekend_books
# After the loop print len(weekend_books) AND the list.
# ============================================================
weekend_books = []
# YOUR CODE STARTS HERE
for book in book_database:
    if book["pages"] <= 200:
        print_llm_response("why this book is a good short read tonight")
        # return #`return` statement outside of a function/method ruff why?!
    else:
        weekend_books.append(book["title"])
print(len(weekend_books), f"list of weekend_books {weekend_books}")


# ============================================================
# PART 5 — AI recommendations (custom prompts — M2L4 style)
# Build a dict reader_profile with keys:
#   favorite_genre -> any genre string
#   max_pages      -> some int
# Then build ONE multi-line f-string prompt that interpolates
# BOTH profile values plus the full book_database, asking the
# LLM to recommend which book to read next and why.
# Store the response with get_llm_response and print it.
# REMEMBER the evaluation trap: interpolate AFTER the dict is final.
# ============================================================
# YOUR CODE STARTS HERE


def reader_profile_builder(favorite_genre, max_pages):
    return {"favorite_genre": favorite_genre, "max_pages": max_pages}


reader_profile = reader_profile_builder("history", 200)
prompt = f"""recommend for this reader which book to read next and why, it favorite genre is {reader_profile["favorite_genre"]} and his max pages is {reader_profile["max_pages"]} while this is the full book database
{book_database}"""
response = get_llm_response(prompt)
print(response)
