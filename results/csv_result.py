import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import json

def create_dateframe():
    # Load data from the JSON file
    with open("result_all_e.json", "r") as file:
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

    # Convert non-numeric 'Steps' to -1
    df['Steps'] = pd.to_numeric(df['Steps'], errors='coerce').fillna(-1).astype(int)

    return df

def save_dataframe_to_csv(df, directory="results"):
    """
    Save a DataFrame to a CSV file. If files with the same name already exist, 
    iterate on the filename to avoid overwriting.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # List existing files in the directory
    existing_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # Determine the filename
    base_name = "result"
    file_number = 1
    while f"{base_name}_{file_number}.csv" in existing_files:
        file_number += 1

    # Save the DataFrame to CSV
    filepath = os.path.join(directory, f"{base_name}_{file_number}.csv")
    df.to_csv(filepath, index=False)
    print(f"DataFrame saved to: {filepath}")

# Example usage:
# Assuming 'df' is your DataFrame
# save_dataframe_to_csv(df)

if __name__ == '__main__':
    df = create_dateframe()
    save_dataframe_to_csv(df)
    print(df)