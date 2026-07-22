import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌤")

st.title("🌤 Weather App")
st.write("Get the current weather of any city.")

city = st.text_input("Enter a city")

if st.button("Get Weather"):

    if city == "":
        st.warning("Please enter a city.")
    else:
        # Geocoding API
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {
            "name": city,
            "count": 1
        }

        geo_response = requests.get(geo_url, params=geo_params)
        geo_data = geo_response.json()

        if geo_data.get("results"):

            location = geo_data["results"][0]
            latitude = location["latitude"]
            longitude = location["longitude"]
            country = location["country"]

            # Weather API
            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,wind_speed_10m"
            }

            weather_response = requests.get(weather_url, params=weather_params)
            weather_data = weather_response.json()

            current = weather_data["current"]

            temperature = current["temperature_2m"]
            wind_speed = current["wind_speed_10m"]
            time = current["time"]

            st.success(f"Weather for {location['name']}")

            st.write(f"**Country:** {country}")
            st.write(f"**Temperature:** {temperature} °C")
            st.write(f"**Wind Speed:** {wind_speed} km/h")
            st.write(f"**Time:** {time}")

        else:
            st.error("City not found.")