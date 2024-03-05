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

# Create an Alert
def create_alert():
    url = "https://tomorrow-io1.p.rapidapi.com/v4/events"
    data = {
        "name": "My Weather Alert",
        "conditions": [
            {
                "type": "temperature",
                "threshold": 25,
                "operator": ">"
            }
        ],
        "locations": [
            {
                "latitude": 42.15,
                "longitude": 82.1
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Created Alert:")
    print(response.json())
    return response.json().get('id')

# Update an Alert
def update_alert(alert_id):
    url = f"{base_url}/v4/alerts/{alert_id}"
    data = {
        "name": "Updated Weather Alert",
        "conditions": [
            {
                "type": "temperature",
                "threshold": 30,
                "operator": ">"
            }
        ]
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    print("Updated Alert:")
    print(response.json())

# Delete an Alert
def delete_alert(alert_id):
    url = f"{base_url}/v4/alerts/{alert_id}"
    response = requests.delete(url, headers=headers)
    print("Deleted Alert:")
    print(response.status_code)

# Example usage
if __name__ == "__main__":
    fetch_weather_forecast()
    alert_id = create_alert()
    if alert_id:
        update_alert(alert_id)
        delete_alert(alert_id)
   
