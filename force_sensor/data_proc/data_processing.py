import csv
import numpy as np
import matplotlib.pyplot as plt

# Constants
num_sensors = 9
num_values_to_average = 10

# Variables for storing data
time_data = []
sensor_data = [[] for _ in range(num_sensors)]

# Read CSV data
with open('sensor_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header
    for row in reader:
        time_data.append(int(row[0]))
        for i in range(num_sensors):
            sensor_data[i].append(int(row[i + 1]))

# Calculate aggregated statistics
all_sensor_values = np.array(sensor_data)
average_values = np.mean(all_sensor_values, axis=1)
mean_values = np.mean(all_sensor_values, axis=1)
p1_values = np.percentile(all_sensor_values, 1, axis=1)
p10_values = np.percentile(all_sensor_values, 10, axis=1)
p50_values = np.percentile(all_sensor_values, 50, axis=1)
p90_values = np.percentile(all_sensor_values, 90, axis=1)
p99_values = np.percentile(all_sensor_values, 99, axis=1)

# Create a spatial force map using Matplotlib
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting individual sensors
for i in range(num_sensors):
    x = i % 3
    y = i // 3
    z = average_values[i]

    ax.bar3d(x, y, 0, 1, 1, z, shade=True, color='skyblue', alpha=0.7)

ax.set_xlabel('Lateral-Medial Direction')
ax.set_ylabel('Superior-Inferior Direction')
ax.set_zlabel('Force Magnitude')

plt.title('Spatial Force Map for Individual Sensors')
plt.show()

# Calculate aggregated statistics across all sensors
agg_average = np.mean(all_sensor_values)
agg_mean = np.mean(all_sensor_values)
agg_p1 = np.percentile(all_sensor_values, 1)
agg_p10 = np.percentile(all_sensor_values, 10)
agg_p50 = np.percentile(all_sensor_values, 50)
agg_p90 = np.percentile(all_sensor_values, 90)
agg_p99 = np.percentile(all_sensor_values, 99)

# Display aggregated statistics
print(f"Aggregated Average: {agg_average}")
print(f"Aggregated Mean: {agg_mean}")
print(f"Aggregated P1: {agg_p1}")
print(f"Aggregated P10: {agg_p10}")
print(f"Aggregated P50: {agg_p50}")
print(f"Aggregated P90: {agg_p90}")
print(f"Aggregated P99: {agg_p99}")
