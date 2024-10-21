import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def filter_data(df, column, values):
    """Filter data based on values in a specific column."""
    return df[df[column].isin(values)]

# Example usage within this script
if __name__ == "__main__":
    df = load_data('data/alt_fuel_stations.csv')
    filtered_df = filter_data(df, 'ZIP', ['90001', '90002'])  # Example ZIP codes
    filtered_df.to_csv('data/filtered_data.csv', index=False)
