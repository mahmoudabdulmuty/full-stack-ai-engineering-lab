# ============================================================
# MODULE 4 - LESSON 2: Built-in packages / standard-library modules
#
# Run from the repository root with:
#   python practice/m4l2_built_in_modules.py
#
# You write all imports and challenge code.
# ============================================================


# CHALLENGE 1 — deterministic standard-library functions
# Import floor from math and mean from statistics.
#
# Use the values below to:
#   1. print floor(9.8);
#   2. print the mean response time.
# Add an exact prediction comment immediately before each print.

response_times = [4, 8, 6, 10]

# YOUR CHALLENGE 1 CODE STARTS HERE
from math import floor
from statistics import mean

# 9
print(floor(9.8))
# (4 + 8 + 6 + 10) / 4 = 7
print(mean(response_times))
# YOUR CHALLENGE 1 CODE ENDS HERE


# CHALLENGE 2 — deliberate randomness (wait until instructed)
# Import sample from random.
# Select two unique reviewers from reviewers and print the returned list.
# Before printing, predict only the guarantees that remain stable:
# returned type, length, allowed members, and whether one input position can
# be selected twice. Do not predict the exact names or order.

reviewers = ["Mona", "Youssef", "Salma", "Omar"]

# YOUR CHALLENGE 2 CODE STARTS HERE
from random import sample

# should I know a function what's returning, it's the first time I see it
# what are we making here? what should we learn? I think buit in functions in python should be mastered across using it
# not by asking about inputs?! discuss with me what are we doing here

# returns a list
# length 2 as we specified this
# must come from the population
# no can't be selected twice as it selects without replacement
# when I run it gives me ['Mona', 'Youssef'] randomize every time but nothing got duplicated
print(sample(reviewers, 2))

# YOUR CHALLENGE 2 CODE ENDS HERE
