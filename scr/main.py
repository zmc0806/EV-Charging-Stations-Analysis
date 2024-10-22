# src/main.py

from data_acquisition import fetch_ev_station_data
from data_processing import load_and_filter_data
from analysis import count_stations_in_service_area, analyze_stations_by_year
from visualization import (
    plot_stations_by_year,
    plot_station_locations,
    create_interactive_map
)

def main():
    # Configuration
    API_KEY = "3sAEbbB4m1usrLLgLuNsjLVcb4fLfKLnBB4QDuee"
    EV_FILE = 'data/raw/alt_fuel_stations.csv'
    SDGE_FILE = 'data/raw/SDGE-ELEC-2024-Q3.csv'
    
    # Fetch data
    print("Fetching data...")
    json_data, _ = fetch_ev_station_data(API_KEY)
    
    # Load and process data
    print("Loading and processing data...")
    ev_df, sdge_df, san_diego_df = load_and_filter_data(EV_FILE, SDGE_FILE, city='San Diego')
    
    # Analyze data
    print("Analyzing data...")
    station_count = count_stations_in_service_area(ev_df, sdge_df)
    stations_by_year = analyze_stations_by_year(ev_df)
    
    print(f"Number of EV chargers in SDGE service area: {station_count}")
    
    # Create visualizations
    print("Creating visualizations...")
    plot_stations_by_year(stations_by_year)
    plot_station_locations(ev_df)
    create_interactive_map(ev_df)
    
    print("Analysis complete! Check the outputs directory for results.")

if __name__ == "__main__":
    main()