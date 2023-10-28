from collections import defaultdict
from solveSokoban import solve_sokoban_elem, solve_sokoban_macro
from sokoban import Warehouse
import os


def evaluate_search_algorithms(search_algorithms, warehouse_limit):
    # Initialize a data structure for results
    results = defaultdict(list)

    # Get list of warehouse files
    warehouse_files = [f for f in os.listdir(
        'warehouses') if f.endswith('.txt')]

    # Sort them to maintain some order, if needed
    warehouse_files.sort()

    # Limit the number of warehouses to test
    warehouse_files = warehouse_files[:warehouse_limit]

    # Loop through warehouse files
    for warehouse_filename in warehouse_files:
        full_path = os.path.join('warehouses', warehouse_filename)

        # Initialize and load warehouse
        warehouse = Warehouse()
        warehouse.load_warehouse(full_path)

        # Loop through both macro and elem solvers
        for solver in [solve_sokoban_macro, solve_sokoban_elem]:
            solver_name = "macro" if solver == solve_sokoban_macro else "elem"

            # Loop through all search algorithms
            for search_algorithm in search_algorithms:
                search_algorithm_name = search_algorithm.__name__

                # Solve the problem
                result = solver(warehouse, search_algorithm)

                if result == 'Impossible':
                    steps = 'Impossible'
                    path = 'Impossible'
                else:
                    steps = len(result)
                    path = result

                # Log the result
                entry = {
                    'steps': steps,
                    'path': path,
                    'algorithm': search_algorithm_name,
                    'method': solver_name,
                }

                results[warehouse_filename].append(entry)

    return results
