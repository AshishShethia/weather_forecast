import requests
import json

# Replace 'YOUR_RAPIDAPI_KEY' with your actual RapidAPI key
RAPIDAPI_KEY = "ba637b8d13msh3adbf6a09bf4b1cp1220a0jsnf8875a5b8c3d"
# Base URL for the Tomorrow.io API
base_url = "https://tomorrow-io1.p.rapidapi.com/v4/weather/forecast"

# Headers for the API request
headers = {
    "X-RapidAPI-Key": "ba637b8d13msh3adbf6a09bf4b1cp1220a0jsnf8875a5b8c3d",
	  "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Fetch Weather Forecast
def fetch_weather_forecast():
    url = base_url
    querystring = {"location": "42.15, 82.1", "timesteps": "1h", "units": "metric"}
    response = requests.get(url, headers=headers, params=querystring)
    print("Weather Forecast:")
    print(response.json())


# Example usage
if __name__ == "__main__":
    fetch_weather_forecast()
   
