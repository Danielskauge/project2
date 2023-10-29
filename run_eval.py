from search import astar_graph_search, breadth_first_graph_search, depth_first_graph_search
from evaluation import evaluate_search_algorithms, evaluate_warehouse
import json

if __name__ == '__main__':
    search_algos = [astar_graph_search,
                    breadth_first_graph_search, depth_first_graph_search]
    results = evaluate_search_algorithms([astar_graph_search], 10, 'macro',20)
    #results_single = evaluate_warehouse(
     #   'warehouses/warehouse_07.txt', 'elem', astar_graph_search,)

    with open("result.json", "w") as file:
        json.dump(results_single, file, indent=3)
