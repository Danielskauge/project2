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
        algo_name = result['algorithm'].split("_")[0]  # Get the algorithm name
        rows.append({
            'Warehouse': warehouse,
            'Algorithm': algo_name.capitalize(),
            'Steps': result['steps'],
            'Method': result['method']
        })
df = pd.DataFrame(rows)
# df = df[df['Steps'].apply(lambda x: str(x).isdigit())]
df['Steps'] = pd.to_numeric(df['Steps'], errors='coerce').fillna(-1).astype(int)

# Display the table
print(df)

# Visualization
plt.figure(figsize=(12, 8))

bar_width = 0.2

warehouses = df['Warehouse'].unique()
warehouses.sort()

num_warehouses = len(warehouses)

positions = np.arange(num_warehouses)

failure_color = 'red'  # Color to represent failed warehouses
default_color = 'blue'  # Default color for regular data

for index, (algo, group) in enumerate(df.groupby('Algorithm')):
    for warehouse_index, warehouse in enumerate(df['Warehouse'].unique()):
        warehouse_data = group[group['Warehouse'] == warehouse]
        if not warehouse_data.empty:
            color = failure_color if warehouse_data['Steps'].values[0] == -1 else default_color
            plt.bar(positions[index] + warehouse_index * 3 * bar_width, 
                    warehouse_data['Steps'].values[0], 
                    width=bar_width, 
                    color=color,
                    label=warehouse if index == 0 else "",  # Label only once
                    align='center')


plt.xticks(positions + bar_width * (len(df['Algorithm'].unique()) - 1) / 2, warehouses)

plt.title('Steps Taken by Algorithms')
plt.xlabel('Warehouse')
plt.ylabel('Steps')
plt.legend(title='Algorithm', loc="upper left", bbox_to_anchor=(1,1))
plt.tight_layout()

max_steps = df['Steps'].max() if df['Steps'].dtype != object else 0
yticks_interval = max(1, max_steps // 10)
plt.yticks(np.arange(0, max_steps + yticks_interval, yticks_interval))
plt.ylim(0, max_steps + yticks_interval)
plt.annotate('Failed warehouses', xy=(0, 0), xycoords='axes fraction', 
             xytext=(5, 5), textcoords='offset points',
             color=failure_color)

output_directory = 'output_visualizations'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

existing_files = [f for f in os.listdir(output_directory) if f.endswith('.png')]
new_file_number = len(existing_files) + 1
filename = os.path.join(output_directory, f'output_{new_file_number}.png')

plt.savefig(filename)

plt.show()
