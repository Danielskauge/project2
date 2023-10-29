import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from search import astar_graph_search, breadth_first_graph_search, depth_first_graph_search
from evaluation import evaluate_search_algorithms, evaluate_warehouse
import json
import os

if __name__ == '__main__':
    search_algos = [astar_graph_search,
                    breadth_first_graph_search, depth_first_graph_search]
    warehouse_files = [f for f in os.listdir('warehouses') if f.endswith('.txt')]
    warehouse_files.sort()
    warehouses = warehouse_files

    # First, try to load the existing data
    # if os.path.exists("result.json"):
    #     with open("result.json", "r") as file:
    #         data = json.load(file)
    # else:
    #     data = {}

    data = {}
    # Now, append to the existing data
    i = 0
    for warehouse in warehouses:
        try:  # Start of the try block
            warehouse_results = []
            for algo in search_algos:
                result = evaluate_warehouse(
                    filename='warehouses/'+warehouse, 
                    solver='elem', # macro v eval
                    search_algorithm=algo,
                    timeout=10)
                warehouse_results.append(result)
            data[warehouse] = warehouse_results
            print(f"warehouse nr {i}")
            i += 1
        except Exception as e:  # Handle the exception
            print(f"An error occurred while processing warehouse {warehouse}. Error: {e}")

    # Finally, write the updated data back to the file
    with open("result_all_e.json", "w") as file:
        json.dump(data, file, indent=3)
