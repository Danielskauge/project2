import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import pandas as pd

def get_latest_dataframe(directory="results"):
    """
    Retrieve the latest CSV file from the directory and convert it to a DataFrame.
    """
    # List existing CSV files in the directory
    existing_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # If no CSV files found, return None
    if not existing_files:
        print("No CSV files found in the directory.")
        return None
    
    # Extract the file numbers from the filenames
    file_numbers = [int(f.split('_')[-1].replace('.csv', '')) for f in existing_files]
    
    # Determine the filename of the latest CSV
    max_file_number = max(file_numbers)
    latest_filepath = os.path.join(directory, f"result_{max_file_number}.csv")
    
    # Convert the CSV to a DataFrame and return
    df = pd.read_csv(latest_filepath)
    return df

# Example usage:
# df_latest = get_latest_dataframe()
# print(df_latest)

def plot_results_old(df):

    # Algorithms and Warehouses
    algorithms = sorted(df['Algorithm'].unique())
    warehouses = sorted(df['Warehouse'].unique())

    # Assigning unique colors to each warehouse
    warehouse_colors = plt.cm.jet(np.linspace(0, 1, len(warehouses)))

    bar_width = 0.35

    fig, axs = plt.subplots(len(algorithms), 1, figsize=(16, len(algorithms) * 6), sharey=True)

    for algo_index, algorithm in enumerate(algorithms):
        ax = axs[algo_index]
        current_positions = np.arange(len(warehouses))
        heights = []
        labels = []
        colors = []
        
        for wh_index, warehouse in enumerate(warehouses):
            warehouse_data = df[(df['Algorithm'] == algorithm) & (df['Warehouse'] == warehouse)]
            
            if not warehouse_data.empty:
                steps = warehouse_data['Steps'].values[0]
                
                # Skip plotting failed warehouses
                if steps == -1:
                    heights.append(0)
                else:
                    heights.append(steps)
                labels.append(warehouse)
                colors.append(warehouse_colors[wh_index])
                
        ax.bar(current_positions, heights, width=bar_width, color=colors, align='center')
        ax.set_title(algorithm)
        ax.set_xticks(current_positions)
        ax.set_xticklabels(labels, rotation=90)
        
    # Common Title, Legend and Adjustments
    fig.suptitle('Steps Taken by Algorithms per Warehouse', y=1.02)
    fig.tight_layout()
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=warehouse, 
                                markersize=10, markerfacecolor=warehouse_colors[idx]) 
                    for idx, warehouse in enumerate(warehouses)]
    fig.legend(handles=legend_handles, title='Warehouse', loc="upper left", bbox_to_anchor=(1, 0.5))
        
    # Saving the plot
    output_directory = 'output_visualizations'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    existing_files = [f for f in os.listdir(output_directory) if f.endswith('.png')]
    new_file_number = len(existing_files) + 1
    filename = os.path.join(output_directory, f'output_{new_file_number}.png')
    plt.savefig(filename, bbox_inches='tight')

    plt.show()


def plot_results_old2(df):

    # Algorithms and Warehouses
    algorithms = sorted(df['Algorithm'].unique())
    warehouses = sorted(df['Warehouse'].unique())

    # Assign colors for a clear distinction
    warehouse_colors = plt.cm.tab20(np.linspace(0, 1, min(len(warehouses), 20)))

    bar_width = 0.35

    fig, axs = plt.subplots(len(algorithms), 1, figsize=(16, len(algorithms) * 4), sharey=True)

    for algo_index, algorithm in enumerate(algorithms):
        ax = axs[algo_index]
        current_positions = np.arange(len(warehouses))
        heights = []
        labels = []
        colors = []
        
        for wh_index, warehouse in enumerate(warehouses):
            warehouse_data = df[(df['Algorithm'] == algorithm) & (df['Warehouse'] == warehouse)]
            
            if not warehouse_data.empty:
                steps = warehouse_data['Steps'].values[0]
                
                # Skip plotting failed warehouses
                if steps == -1:
                    heights.append(0)
                else:
                    heights.append(steps)
                labels.append(warehouse)
                # colors.append(warehouse_colors[wh_index])
                colors.append(warehouse_colors[wh_index % len(warehouse_colors)])

                
        # Set the bar width to 1 to remove any spacing between the bars
        ax.bar(current_positions, heights, width=1, color=colors, align='center')
        ax.set_title(algorithm)

    # Common Title, Legend and Adjustments
    fig.suptitle('Steps Taken by Algorithms per Warehouse', y=1.02)
    fig.tight_layout(pad=2)
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=warehouse, 
                                markersize=10, markerfacecolor=warehouse_colors[idx % 20]) 
                    for idx, warehouse in enumerate(warehouses)]
    fig.legend(handles=legend_handles, title='Warehouse', loc="upper left", bbox_to_anchor=(1, 0.5))

    # Saving the plot
    output_directory = 'output_visualizations'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    existing_files = [f for f in os.listdir(output_directory) if f.endswith('.png')]
    new_file_number = len(existing_files) + 1
    filename = os.path.join(output_directory, f'output_{new_file_number}.png')
    plt.savefig(filename, bbox_inches='tight')

    plt.show()

def plot_results(df):
    algorithms = sorted(df['Algorithm'].unique())
    warehouses = sorted(df['Warehouse'].unique())
    
    # Use as many colors as there are warehouses
    warehouse_colors = plt.cm.jet(np.linspace(0, 1, len(warehouses)))

    fig, axs = plt.subplots(len(algorithms), 1, figsize=(16, 2 * len(algorithms)), sharey=True)  # Adjust height here

    for algo_index, algorithm in enumerate(algorithms):
        ax = axs[algo_index]
        current_positions = np.arange(len(warehouses))
        heights = []
        labels = []
        colors = []
        
        for wh_index, warehouse in enumerate(warehouses):
            warehouse_data = df[(df['Algorithm'] == algorithm) & (df['Warehouse'] == warehouse)]
            
            if not warehouse_data.empty:
                steps = warehouse_data['Steps'].values[0]
                
                # Skip plotting failed warehouses
                if steps == -1:
                    heights.append(0)
                else:
                    heights.append(steps)
                labels.append(warehouse)
                colors.append(warehouse_colors[wh_index % len(warehouse_colors)])  # Cycling through colors
                
        ax.bar(current_positions, heights, width=1, color=colors, align='center')  # Set width to 1
        ax.set_title(algorithm)
        ax.set_xticks([])  # Remove x-axis ticks
        ax.set_ylim(0, max(heights) + 50)  # Adjust y-axis limits based on the highest bar value

    # Common Title, Legend, and Adjustments
    fig.suptitle('Steps Taken by Algorithms per Warehouse', y=1.02)
    fig.tight_layout()
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=warehouse, 
                                markersize=10, markerfacecolor=warehouse_colors[idx]) 
                    for idx, warehouse in enumerate(warehouses)]
    fig.legend(handles=legend_handles, title='Warehouse', loc="upper left", bbox_to_anchor=(1, 0.5))
        
    # Saving the plot
    output_directory = 'output_visualizations'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    existing_files = [f for f in os.listdir(output_directory) if f.endswith('.png')]
    new_file_number = len(existing_files) + 1
    filename = os.path.join(output_directory, f'output_{new_file_number}.png')
    plt.savefig(filename, bbox_inches='tight')

    plt.show()



if __name__ == '__main__':
    df = get_latest_dataframe()
    plot_results(df)
    # print(df)

