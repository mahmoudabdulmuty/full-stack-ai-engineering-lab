# ============================================================
# MODULE 4 - LESSON 1: Using functions from a local file
#
# Run from the repository root with:
#   python practice/m4l1_local_imports.py
#
# Target capability: import local functions explicitly and explain
# which names Python binds in the current namespace.
# ============================================================


# CHALLENGE 1
# Import the whole m4l1_local_helpers module.
# Then add a prediction comment and print the result of calling
# format_ticket("T-301", "Billing") through the module namespace.

# YOUR CHALLENGE 1 CODE STARTS HERE
import m4l1_local_helpers

# this will return the value of the function => T-301 -> Billing
print(m4l1_local_helpers.format_ticket("T-301", "Billing"))

# YOUR CHALLENGE 1 CODE ENDS HERE


# CHALLENGE 2
# Import only unresolved_count directly from m4l1_local_helpers.
# Then add a prediction comment and print unresolved_count(12, 7)
# without writing the module name before the function.

# YOUR CHALLENGE 2 CODE STARTS HERE
from m4l1_local_helpers import unresolved_count

# this will print the value of the function 12-7 is 5
print(unresolved_count(12, 7))

# YOUR CHALLENGE 2 CODE ENDS HERE


# EXPLANATION — answer in comments after both challenges run:
# 1. Which name did Challenge 1 bind in this file?
# 2. Which name did Challenge 2 bind in this file?
# 3. Why would bare format_ticket(...) fail with the Challenge 1 import style?

# YOUR EXPLANATION STARTS HERE
# 1. it bound the module only m4l1_local_helpers so we have to write it before every function needed to import through dot notation
# 2. only unresolved_count
# 3. because we didn't explicitly import it as in C1, we import the module so we have to write it this way namespaced
# YOUR EXPLANATION ENDS HERE
