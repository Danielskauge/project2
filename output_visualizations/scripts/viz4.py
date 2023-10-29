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

# Display the table
print(df)

import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assume you've loaded your data into the DataFrame 'df'
# ...

# Convert non-numeric 'Steps' to -1
df['Steps'] = pd.to_numeric(df['Steps'], errors='coerce').fillna(-1).astype(int)

plt.figure(figsize=(16, 8))  # Increase the width

# Algorithms and Warehouses
algorithms = sorted(df['Algorithm'].unique())
warehouses = sorted(df['Warehouse'].unique())

# Assigning unique colors to each warehouse
warehouse_colors = plt.cm.jet(np.linspace(0, 1, len(warehouses)))

bar_width = 0.15

# Placeholder for failed warehouses legend
plt.bar(0, 0, color='red', label='Failed Warehouses')

# Plotting
for algo_index, algorithm in enumerate(algorithms):
    current_position = algo_index
    for wh_index, warehouse in enumerate(warehouses):
        warehouse_data = df[(df['Algorithm'] == algorithm) & (df['Warehouse'] == warehouse)]
        
        if not warehouse_data.empty:
            steps = warehouse_data['Steps'].values[0]
            
            # Skip plotting failed warehouses
            if steps == -1:
                continue
            
            color = warehouse_colors[wh_index]
            label = warehouse if algo_index == 0 else None
            plt.bar(current_position, steps, width=bar_width, 
                    color=color, label=label, align='center')
            
            current_position += bar_width

# x-tick adjustments
tick_positions = np.arange(len(algorithms)) + (bar_width * len(warehouses)) / 2
plt.xticks(tick_positions, algorithms)

# Labels, Title, and Legend
plt.xlabel('Algorithm')
plt.ylabel('Steps')
plt.title('Steps Taken by Algorithms per Warehouse')
plt.legend(title='Warehouse', loc="upper left", bbox_to_anchor=(1,1))
plt.tight_layout()

# Y-axis adjustments
max_steps = df['Steps'].max()
yticks_interval = max(1, max_steps // 10)
plt.yticks(np.arange(0, max_steps + yticks_interval, yticks_interval))

# Saving the plot
output_directory = 'output_visualizations'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
existing_files = [f for f in os.listdir(output_directory) if f.endswith('.png')]
new_file_number = len(existing_files) + 1
filename = os.path.join(output_directory, f'output_{new_file_number}.png')
plt.savefig(filename)

plt.show()
