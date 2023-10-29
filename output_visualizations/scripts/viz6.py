import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def plot_algorithm_results(df):
    algorithms = sorted(df['Algorithm'].unique())
    warehouses = sorted(df['Warehouse'].unique())
    
    # Use as many colors as there are warehouses
    warehouse_colors = plt.cm.jet(np.linspace(0, 1, len(warehouses)))
    
    for algorithm in algorithms:
        plt.figure(figsize=(16, 4))  # Adjust figure size as needed
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
                
        plt.bar(current_positions, heights, width=1, color=colors, align='center')  # Set width to 1
        plt.title(f'Steps Taken by {algorithm} Algorithm per Warehouse')
        plt.xticks(current_positions, labels, rotation=45, ha='right')
        plt.xticks(current_positions, labels, rotation=45, ha='right')
        plt.tight_layout()
        
        # Legend
        legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=warehouse, 
                                    markersize=10, markerfacecolor=warehouse_colors[idx]) 
                        for idx, warehouse in enumerate(warehouses)]
        plt.legend(handles=legend_handles, title='Warehouse', loc="upper left", bbox_to_anchor=(1, 0.5))
        
        # Saving the plot
        output_directory = 'output_visualizations'
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        filename = os.path.join(output_directory, f'{algorithm}_output.png')
        plt.savefig(filename, bbox_inches='tight')

        plt.show()

# Run the function




if __name__ == '__main__':
    df = get_latest_dataframe()
    plot_algorithm_results(df)