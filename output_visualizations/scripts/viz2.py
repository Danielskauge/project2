import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from the JSON file
with open("result.json", "r") as file:
    data = json.load(file)

# Create a DataFrame for easy table display and manipulation
rows = []
for warehouse, results in data.items():
    for result in results:
        algo_name = result['algorithm'].split("_")[0]  # Get the algorithm name (e.g., "astar" from "astar_graph_search")
        rows.append({
            'Warehouse': warehouse,
            'Algorithm': algo_name.capitalize(),
            'Steps': result['steps'],
            'Method': result['method']
        })
df = pd.DataFrame(rows)

# Display the table
print(df)

# Visualization: Plotting the steps taken by each algorithm for each warehouse
plt.figure(figsize=(10, 6))

# Define a width for the bars and an offset to separate bars for different warehouses
bar_width = 0.2

# Create a list of algorithms (ensuring unique and sorted)
algorithms = df['Algorithm'].unique()
algorithms.sort()

# Position the bars based on the number of warehouses
positions = range(len(algorithms))

for index, (warehouse, group) in enumerate(df.groupby('Warehouse')):
    # Adjust position for each warehouse to avoid overlap
    adjusted_positions = [p + index * bar_width for p in positions]
    plt.bar(adjusted_positions, group['Steps'], width=bar_width, label=warehouse, align='center')

# Adjust x-tick positions and labels to center them
centered_positions = [p + bar_width * (len(df['Warehouse'].unique()) - 1) / 2 for p in positions]
plt.xticks(centered_positions, algorithms)

plt.title('Steps Taken by Algorithms')
plt.xlabel('Algorithm')
plt.ylabel('Steps')
plt.legend(title='Warehouse')
plt.tight_layout()

max_steps = df['Steps'].max() if df['Steps'].dtype != object else 0  # Ensure that Steps are numeric
yticks_interval = max(1, max_steps // 10)  # For example, divide the maximum steps by 10
plt.yticks(np.arange(0, max_steps + yticks_interval, yticks_interval))

# Define the directory to save the output
output_directory = 'output_visualizations'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Determine the unique filename for the new output
existing_files = [f for f in os.listdir(output_directory) if f.endswith('.png')]
new_file_number = len(existing_files) + 1
filename = os.path.join(output_directory, f'output_{new_file_number}.png')

# Save the figure to the file
plt.savefig(filename)

plt.show()
