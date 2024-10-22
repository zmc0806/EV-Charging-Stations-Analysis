# src/data_processing.py

import pandas as pd

def load_and_filter_data(ev_file_path, sdge_file_path, city=None):
    """
    Load EV and SDGE data files and filter by city if specified
    
    Args:
        ev_file_path (str): Path to EV stations CSV file
        sdge_file_path (str): Path to SDGE data CSV file
        city (str, optional): City name to filter by
    
    Returns:
        tuple: (ev_df, sdge_df, filtered_df)
    """
    ev_df = pd.read_csv(ev_file_path, low_memory=False)
    sdge_df = pd.read_csv(sdge_file_path)
    
    if city:
        filtered_df = ev_df[ev_df['City'] == city]
        return ev_df, sdge_df, filtered_df
    return ev_df, sdge_df, None

def clean_coordinates(df):
    """
    Clean latitude and longitude data
    
    Args:
        df (DataFrame): Input DataFrame
        
    Returns:
        DataFrame: Cleaned DataFrame
    """
    df_clean = df.dropna(subset=['Latitude', 'Longitude']).copy()
    df_clean.loc[:, 'Latitude'] = pd.to_numeric(df_clean['Latitude'], errors='coerce')
    df_clean.loc[:, 'Longitude'] = pd.to_numeric(df_clean['Longitude'], errors='coerce')
    return df_clean

if __name__ == "__main__":
    # Test data processing functions
    ev_df, sdge_df, san_diego_df = load_and_filter_data(
        'data/raw/alt_fuel_stations.csv',
        'data/raw/SDGE-ELEC-2024-Q3.csv',
        'San Diego'
    )