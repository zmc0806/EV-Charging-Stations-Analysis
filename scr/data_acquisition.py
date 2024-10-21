import requests
import json

# Constants
API_KEY = "your_api_key_here"
BASE_URL = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"

def fetch_data(api_key, base_url, params):
    """Fetch data from API and save as JSON."""
    response = requests.get(f"{base_url}?api_key={api_key}&{params}")
    if response.status_code == 200:
        data = response.json()
        with open('data/alt_fuel_stations.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data downloaded and saved.")
    else:
        print(f"Request failed: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_data(API_KEY, BASE_URL, "fuel_type=ELEC&state=CA")
