import matplotlib.pyplot as plt

def analyze_and_visualize(temperatures):
    # Calculate mean
    mean_temp = sum(temperatures) / len(temperatures)
    
    # Calculate standard deviation
    squared_diffs = [(x - mean_temp) ** 2 for x in temperatures]
    std_dev = (sum(squared_diffs) / len(temperatures)) ** 0.5
    
    # Line plot of daily temperatures
    plt.figure(figsize=(10, 4))
    plt.plot(range(1, len(temperatures)+1), temperatures, marker='o')
    plt.title("Daily Temperatures")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°F)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Histogram of temperature distribution
    plt.figure(figsize=(8, 4))
    plt.hist(temperatures, bins=5, edgecolor='black')
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature (°F)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
    
    mean_result = mean_temp
    std_result = std_dev
    print(f"Mean temperature: {mean_result:.2f}")
    print(f"Standard deviation: {std_result:.2f}")

temps = [68, 70, 72, 71, 69, 73, 75, 74, 72, 70]
analyze_and_visualize(temps)
