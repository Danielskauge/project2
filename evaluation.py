from collections import defaultdict
from solveSokoban import solve_sokoban_elem, solve_sokoban_macro
from sokoban import Warehouse
import os
from multiprocessing import Process, Queue



def worker_solve(warehouse, solver, search_algorithm, queue):
    # This function will run in a separate process
    result = solver(warehouse, search_algorithm)
    queue.put(result)


# Default timeout set to 60 seconds
def evaluate_warehouse(filename, solver, search_algorithm, timeout=10):
    # Load the warehouse
    warehouse = Warehouse()
    warehouse.load_warehouse(filename)

    # Map to convert solver choice to function
    solver_map = {
        "macro": solve_sokoban_macro,
        "elem": solve_sokoban_elem
    }
    chosen_solver = solver_map[solver]

    # Use a Queue to retrieve the result
    q = Queue()
    # Create a new process to run the solver
    p = Process(target=worker_solve, args=(
        warehouse, chosen_solver, search_algorithm, q))
    p.start()

    # Wait for the specified timeout
    p.join(timeout)

    # If process is still alive after the timeout, terminate it
    if p.is_alive():
        p.terminate()
        p.join()
        result = 'Impossible'
    else:
        result = q.get()

    if result == 'Impossible':
        steps = 'Impossible'
        path = 'Impossible'
    else:
        steps = len(result)
        path = result

    # Log the result
    entry = {
        'warehouse': filename,
        'steps': steps,
        'path': path,
        'algorithm': search_algorithm.__name__,
        'method': solver,
    }

    return entry

# This function evaluates multiple warehouses using different configurations of solvers and search algorithms
def evaluate_search_algorithms(search_algorithms, warehouse_count, solver_choice,timeout):
    results = defaultdict(list)

    # Get list of warehouse files
    warehouse_files = [f for f in os.listdir('warehouses') if f.endswith('.txt')]
    warehouse_files.sort()
    warehouse_files = warehouse_files[:warehouse_count]

    solvers = ["macro", "elem"] if solver_choice is None else [solver_choice]

    for warehouse_filename in warehouse_files:
        print('warehouse: ', warehouse_filename)
        for solver in solvers:
            print('solver: ', solver)
            for search_algorithm in search_algorithms:
                print('algo: ', search_algorithm)
                full_path = os.path.join('warehouses', warehouse_filename)
                entry = evaluate_warehouse(full_path, solver, search_algorithm,timeout)
                results[warehouse_filename].append(entry)

    return results
