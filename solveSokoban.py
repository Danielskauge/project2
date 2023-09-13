from SokobanPuzzle import SokobanPuzzle
from search import breadth_first_graph_search, depth_first_graph_search, uniform_cost_search, astar_graph_search

def solve_sokoban_macro(warehouse, search_algorithm=breadth_first_graph_search, f_func=None, g_func=None):
    '''
    @param warehouse: a valid Warehouse object
    @param search_algorithm: a search function to use (e.g., breadth_first_graph_search, astar_search, etc.)
    @param f_func: heuristic function for f (only used for greedy and informed searches)
    @param g_func: cost function for g (only used for informed searches like A*)

    @return
        If puzzle cannot be solved return the string 'Impossible'
        Otherwise return M a sequence of macro actions that solves the puzzle.
        If the puzzle is already in a goal state, simply return []
    '''
    problem = SokobanPuzzle(warehouse, 
                            allow_taboo_push=False, 
                            macro=True)

    if problem.goal_test(problem.initial): 
        return []

    # Depending on the search algorithm, provide appropriate arguments
    solution_actions_sequence = search_algorithm(problem)

    if solution_actions_sequence:
        return solution_actions_sequence.solution()
    
    return 'Impossible'


def solve_sokoban_elem(warehouse):
    #
    '''    
    This function should solve using elementary actions 
    the puzzle defined in a file.
    
    @param warehouse: a valid Warehouse object

    @return
        If puzzle cannot be solved return the string 'Impossible'
        If a solution was found, return a list of elementary actions that solves
            the given puzzle coded with 'Left', 'Right', 'Up', 'Down'
            For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
            If the puzzle is already in a goal state, simply return []
    '''

    problem = SokobanPuzzle(warehouse,
                            allow_taboo_push=False,
                            macro=False)

    if problem.goal_test(problem.initial):
        return []

    solution_actions_sequence = breadth_first_graph_search(problem)

    if solution_actions_sequence is not None:
        return solution_actions_sequence

    return 'Impossible'
