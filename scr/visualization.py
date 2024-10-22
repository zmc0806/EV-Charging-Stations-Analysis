# src/visualization.py

import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from data_processing import clean_coordinates

def plot_stations_by_year(stations_per_year):
    """
    Plot number of stations opened per year
    
    Args:
        stations_per_year (DataFrame): DataFrame with yearly station counts
    """
    plt.figure(figsize=(10, 6))
    plt.plot(stations_per_year['Open Year'], stations_per_year['Number of Stations Opened'], marker='o')
    plt.title('Number of Charging Stations Opened Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Stations Opened')
    plt.grid(True)
    plt.savefig('outputs/stations_by_year.png')
    plt.close()

def plot_station_locations(ev_df):
    """
    Create a scatter plot of station locations
    
    Args:
        ev_df (DataFrame): EV stations DataFrame
    """
    ev_df_clean = clean_coordinates(ev_df)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(ev_df_clean['Longitude'], ev_df_clean['Latitude'], c='blue', alpha=0.6, s=10)
    plt.title('Geospatial Distribution of Charging Stations')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.savefig('outputs/station_locations.png')
    plt.close()

def create_interactive_map(stations_df, center_lat=32.7157, center_lon=-117.1611, zoom=10):
    """
    Create an interactive Folium map of EV stations
    
    Args:
        stations_df (DataFrame): EV stations DataFrame
        center_lat (float): Center latitude for map
        center_lon (float): Center longitude for map
        zoom (int): Initial zoom level
    
    Returns:
        folium.Map: Interactive map object
    """
    stations_clean = clean_coordinates(stations_df)
    
    # Create GeoDataFrame
    stations_gdf = gpd.GeoDataFrame(
        stations_clean,
        geometry=gpd.points_from_xy(stations_clean.Longitude, stations_clean.Latitude),
        crs="EPSG:4326"
    )
    
    # Create map
    ev_map = folium.Map(location=[center_lat, center_lon], zoom_start=zoom)
    
    # Add markers
    for _, row in stations_gdf.iterrows():
        popup_text = f"""
        <b>Station Name:</b> {row['Station Name']}<br>
        <b>Street Address:</b> {row['Street Address']}<br>
        <b>City:</b> {row['City']}<br>
        <b>ZIP Code:</b> {row['ZIP']}<br>
        <b>Fuel Type:</b> {row['Fuel Type Code']}<br>
        <b>EV Network:</b> {row['EV Network']}<br>
        """
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(ev_map)
    
    ev_map.save('outputs/ev_stations_map.html')
    return ev_map

if __name__ == "__main__":
    # Test visualization functions
    from data_processing import load_and_filter_data
    from analysis import analyze_stations_by_year
    
    ev_df, sdge_df, _ = load_and_filter_data(
        'data/raw/alt_fuel_stations.csv',
        'data/raw/SDGE-ELEC-2024-Q3.csv'
    )
    
    stations_by_year = analyze_stations_by_year(ev_df)
    plot_stations_by_year(stations_by_year)
    plot_station_locations(ev_df)
    create_interactive_map(ev_df)