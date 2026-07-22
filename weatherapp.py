import requests

city = input("Enter city: ").strip()

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {
    "name": city,
    "count": 1
}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

if not geo_data.get("results"):
    print("City not found!")
    raise SystemExit

location = geo_data["results"][0]
latitude = location["latitude"]
longitude = location["longitude"]
print(f"City: {location['name']}")

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

temperature = data["current"]["temperature_2m"]
wind_speed = data["current"]["wind_speed_10m"]
time = data["current"]["time"]

print(f"Time: {time}")
print(f"Temperature: {temperature}°C")
print(f"Wind Speed: {wind_speed} km/h")