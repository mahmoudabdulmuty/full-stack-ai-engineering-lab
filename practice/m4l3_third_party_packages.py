# ============================================================
# MODULE 4 - LESSON 3: Using third-party packages
#
# Run from the repository root with:
#   python practice/m4l3_third_party_packages.py
#
# You write all imports and challenge code.
# ============================================================


# CHALLENGE 1 — load and filter structured data with pandas
#
# 1. Import pandas using its conventional `pd` alias.
# 2. Load `practice/data/m4l3_car_sales.csv` with `pd.read_csv`.
# 3. Create a filtered table containing cars whose Price is at least 10000.
# 4. Immediately before each print, add an exact prediction comment.
# 5. Print the total number of loaded rows.
# 6. Print the number of rows in the filtered table.
#
# Do not print the complete tables yet.

# YOUR CHALLENGE 1 CODE STARTS HERE
import pandas as pd

reader = pd.read_csv("practice/data/m4l3_car_sales.csv")

filtered_rows = reader[reader["Price"] >= 10000]

# 6
print(len(reader))
# 3
print(len(filtered_rows))


# YOUR CHALLENGE 1 CODE ENDS HERE


# CHALLENGE 2 — filter, select a column, and calculate a statistic
#
# Using the existing `reader` DataFrame:
#   1. Create a filtered DataFrame containing only cars from 2015.
#   2. Add an exact prediction comment, then print its row count.
#   3. Select the `Price` column from that filtered DataFrame.
#   4. Add an exact prediction comment, then print its median.
#
# Do not manually calculate or hard-code the median in the print statement.

# YOUR CHALLENGE 2 CODE STARTS HERE

filtered_cars_by_year = reader[reader["Year"] == 2015]

# 2
print(len(filtered_cars_by_year))
# 7250.0
print(filtered_cars_by_year["Price"].median())

# YOUR CHALLENGE 2 CODE ENDS HERE
