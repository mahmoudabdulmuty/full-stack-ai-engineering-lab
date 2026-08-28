# ============================================================
# M3L5 — Vacation planning using CSV files
# Practice file for Mahmoud — write challenge code here, then run:
#   python practice/m3l5-csv-itinerary.py
#
# NEW THIS LESSON: csv.DictReader + structured-data filtering
# ============================================================

import csv


# Offline stand-in: verifies the Python prompt pipeline, not real AI quality.
def get_llm_response(prompt):
    return f"[LLM reply] {prompt}"


# ---- ROUND 1: Load CSV rows as dictionaries ----
# 1. Open "practice/data/itinerary.csv" in read mode.
# 2. Pass the file handle to csv.DictReader(...).
# 3. Start with an empty list named itinerary.
# 4. Loop over the reader and append every row to itinerary.
# 5. Close the file.
# 6. Immediately before printing, add a prediction comment that says:
#    - how many items itinerary contains
#    - what type itinerary[0] is
# 7. Print itinerary.
#
# Do not filter the data yet. First prove that loading works.
# -----------------------------------------------------------
# YOUR CODE STARTS HERE
with open("practice/data/itinerary.csv", "r") as file:
    # file = f.read()
    # f.close()
    reader = csv.DictReader(file)

    itinerary = []
    for row in reader:
        itinerary.append(row)

# it will print the file csv like dict
# {"City": "Cairo", "Country": "Egypt", "Arrival": "2026-09-01", "Departure": "2026-09-04"}
# and so on for others like this
# itinerary will contains 6 dicts,
# itinerary[0] will have the first object that is above
# print(itinerary)


# -----------------------------------------------------------
# YOUR CODE ENDS HERE


# ---- ROUND 2: Filter structured rows without an LLM ----
# Use the existing itinerary list from Round 1.
# 1. Create an empty list named egypt_stops.
# 2. Loop over itinerary.
# 3. Append only rows whose "Country" value is "Egypt".
# 4. Immediately before printing, add a prediction comment that says:
#    - how many dictionaries egypt_stops contains
#    - which cities they represent
# 5. Print egypt_stops.
# -----------------------------------------------------------
# YOUR CODE STARTS HERE

egypt_stops = []
for item in itinerary:
    requested_country = "Egypt"
    if item["Country"] == requested_country:
        egypt_stops.append(item)
        # 2 dicts egypt stops contains
        # Cairo and Alexandria
# print(egypt_stops)
# -----------------------------------------------------------
# YOUR CODE ENDS HERE


# ---- ROUND 3: Feed one selected row into an LLM prompt ----
# Use egypt_stops from Round 2.
# 1. Select Alexandria by its list index and store it in selected_stop.
# 2. Read its "City", "Country", "Arrival", and "Departure" values
#    into four variables.
# 3. Build this prompt with an f-string:
#    "I will visit {city}, {country}, from {arrival} to {departure}.
#     Please create a detailed daily itinerary."
# 4. Pass the prompt to get_llm_response(...) and store the response.
# 5. Immediately before printing, predict:
#    - which city and dates will appear
#    - whether the stub genuinely invents any activities, and why
# 6. Print the response.
# -----------------------------------------------------------
# YOUR CODE STARTS HERE
selected_stop = {}
for egypt_stop in egypt_stops:
    selected_city = "Alexandria"
    if egypt_stop["City"] == selected_city:
        selected_stop = egypt_stop

prompt = f"""I will visit {selected_stop["City"]}, {selected_stop["Country"]}, from {selected_stop["Arrival"]} to {selected_stop["Departure"]}.
    Please create a detailed daily itinerary."""
response = get_llm_response(prompt)
# Alexandria of course with it's data in the file
# the stub don't make it as not real LLM, with a real model call it'll do eventually
print(response)
# -----------------------------------------------------------
# YOUR CODE ENDS HERE
