from search import astar_graph_search, breadth_first_graph_search, depth_first_graph_search
from evaluation import evaluate_search_algorithms
import json

search_algos = [astar_graph_search, breadth_first_graph_search, depth_first_graph_search]
results = evaluate_search_algorithms(search_algos, 2)

with open("result.json", "w") as file:
    json.dump(results, file, indent=3)