# src/data_acquisition.py

import requests
import json
import pandas as pd

def fetch_ev_station_data(api_key, state='CA', fuel_type='ELEC'):
    """
    Fetch EV station data from NREL API in both JSON and CSV formats
    
    Args:
        api_key (str): NREL API key
        state (str): State abbreviation
        fuel_type (str): Type of fuel
    
    Returns:
        tuple: (json_data, DataFrame)
    """
    # JSON request
    json_url = f"https://developer.nrel.gov/api/alt-fuel-stations/v1.json?api_key={api_key}&fuel_type={fuel_type}&state={state}"
    response = requests.get(json_url)
    
    if response.status_code == 200:
        json_data = response.json()
        with open('data/raw/alt_fuel_stations.json', 'w') as f:
            json.dump(json_data, f, indent=4)
        print("Data successfully saved as alt_fuel_stations.json")
    else:
        print(f"Request failed: {response.status_code}, {response.text}")
        return None, None
    
    # CSV request
    csv_url = f"https://developer.nrel.gov/api/alt-fuel-stations/v1.csv?api_key={api_key}&fuel_type={fuel_type}&state={state}"
    df = pd.read_csv(csv_url)
    df.to_csv('data/raw/alt_fuel_stations.csv', index=False)
    print("Data successfully saved as alt_fuel_stations.csv")
    
    return json_data, df

if __name__ == "__main__":
    API_KEY = "3sAEbbB4m1usrLLgLuNsjLVcb4fLfKLnBB4QDuee"
    json_data, ev_df = fetch_ev_station_data(API_KEY)