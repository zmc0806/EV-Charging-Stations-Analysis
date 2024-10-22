# src/analysis.py

import pandas as pd
from datetime import datetime

def count_stations_in_service_area(ev_df, sdge_df):
    """
    Count EV stations in SDGE service area
    
    Args:
        ev_df (DataFrame): EV stations DataFrame
        sdge_df (DataFrame): SDGE service area DataFrame
    
    Returns:
        int: Number of stations in service area
    """
    sdge_zip_codes = sdge_df['ZipCode'].unique()
    ev_in_sdge = ev_df[ev_df['ZIP'].isin(sdge_zip_codes)]
    return ev_in_sdge.shape[0]

def analyze_stations_by_year(ev_df):
    """
    Analyze number of stations opened per year
    
    Args:
        ev_df (DataFrame): EV stations DataFrame
    
    Returns:
        DataFrame: Stations opened per year
    """
    ev_df = ev_df.copy()
    ev_df['Open Date'] = pd.to_datetime(ev_df['Open Date'], errors='coerce')
    ev_df['Open Year'] = ev_df['Open Date'].dt.year
    
    stations_per_year = ev_df.groupby('Open Year').size().reset_index(name='Number of Stations Opened')
    return stations_per_year

if __name__ == "__main__":
    # Test analysis functions
    from data_processing import load_and_filter_data
    
    ev_df, sdge_df, _ = load_and_filter_data(
        'data/raw/alt_fuel_stations.csv',
        'data/raw/SDGE-ELEC-2024-Q3.csv'
    )
    
    station_count = count_stations_in_service_area(ev_df, sdge_df)
    stations_by_year = analyze_stations_by_year(ev_df)
    print(f"Stations in service area: {station_count}")
    print("\nStations by year:")
    print(stations_by_year)