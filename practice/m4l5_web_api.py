import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=30.0444&longitude=31.2357&current=temperature_2m,wind_speed_10m"


response = requests.get(url)
data = response.json()

# 200 as it's a valid request
print(response.status_code)

# types is Response dict
print(type(response).__name__)

# type is python dict
print(type(data).__name__)

# True
print("current" in data)

current_weather = data["current"]

# <class 'dict'>
print(type(current_weather))

# True
print("temperature_2m" in current_weather)

# Number
print(current_weather["temperature_2m"])

live_report = f"Cairo weather: {current_weather['temperature_2m']}°C, wind {current_weather['wind_speed_10m']} km/h"

# Cairo weather: [Number]°C, wind [Number] km/h
print(live_report)

# this will have this prompt with data from live report and the data will change of course as it's live prediction
outfit_prompt = f"this is the live report of weather today: \n{live_report}.\nplease give me an appropriate outdoor outfit?"
print(outfit_prompt)
