import matplotlib.pyplot as plt

def plot_data(x, y):
    """Generate a simple line plot."""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title('Number of Charging Stations Opened Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Stations Opened')
    plt.grid(True)
    plt.show()

# This would be called from an analysis script or notebook
