# ============================================================
# M3L7 — Creating detailed itineraries for multiple cities
# Practice file for Mahmoud — write challenge code here, then run:
#   python practice/m3l7-multi-city-itineraries.py
#
# NEW THIS LESSON: integrate reusable functions + per-city files
# + a loop + a dictionary of LLM responses
# ============================================================

import csv


# Offline stand-in: verifies the Python prompt pipeline, not real AI quality.
def get_llm_response(prompt: str) -> str:
    return f"[LLM reply] {prompt}"


# ---- INTEGRATION CHALLENGE: One workflow, multiple cities ----
#
# Build a reusable CSV-loading function. You choose its name, parameter name,
# and local variable names. Its contract must be:
#   - accept one file path
#   - open it with a context manager
#   - pass the live file handle to csv.DictReader
#   - return a list of row dictionaries
#   - do not print inside the function
#
# Then:
#   1. Load practice/data/m3l7-itinerary.csv with your function.
#   2. Create one empty dictionary for all generated city plans.
#   3. Loop through every trip stop.
#   4. Read City, Country, Arrival, and Departure from the current row.
#   5. Build the restaurant path from the city name:
#        practice/data/m3l7-restaurants/<City>.csv
#   6. Load that city's restaurant rows with the same CSV function.
#   7. Build an f-string prompt containing the city, country, dates, and
#      restaurant rows. Ask for a detailed daily itinerary with meal times.
#   8. Call get_llm_response(prompt) once per city.
#   9. Store each response in the result dictionary under its city key.
#
# Required verification outputs:
#   - Immediately before printing the result keys, predict their exact order.
#   - Immediately before printing Tokyo's response, predict which city, dates,
#     and restaurants will appear, and whether the stub invents activities.
#   - Print the keys, then print the stored Tokyo response.
#
# Do not hard-code the two city keys while building the result dictionary.
# -----------------------------------------------------------
# YOUR CODE STARTS HERE
def csv_reader(file_path: str) -> list:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        itinerary = []
        for row in reader:
            itinerary.append(row)
        return itinerary


city_plans = csv_reader("practice/data/m3l7-itinerary.csv")
# this will print list of dicts each of them representing the plan for each trip
# print(city_plans)

generated_city_plans = {}
for stop in city_plans:
    restaurant_path = f"practice/data/m3l7-restaurants/{stop['City']}.csv"
    city_rows = csv_reader(restaurant_path)
    selected_city = stop["City"]
    prompt = f"""give us detailed daily itinerary with meal times for this
    city {selected_city} country {stop["Country"]} {stop["Arrival"]} {stop["Departure"]} and its restaurants
      {city_rows[0]["Restaurant"]} -> Specialty {city_rows[0]["Specialty"]}
      and {city_rows[1]["Restaurant"]} -> Specialty {city_rows[1]["Specialty"]}"""

    generated_city_plans[selected_city] = get_llm_response(prompt)

# dictionary keys Tokyo then Rio
print(generated_city_plans.keys())

# print only Tokyo response "[LLM reply] give us detailed daily itinerary with meal times for this
# city Tokyo country Japan 2026-10-03 2026-10-06 and its restaurants
#   Tsuta -> Specialty Shoyu soba with black truffle oil
#   and Afuri -> Specialty Yuzu shio ramen"
# it'll not invent activities, it takes it from the file itself
print(generated_city_plans["Tokyo"])
# YOUR CODE ENDS HERE
