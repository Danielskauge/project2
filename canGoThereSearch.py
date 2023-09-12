import search
from collections import namedtuple

class CanGoThereSearch(search.Problem):  # Or SokobanPuzzle
    def __init__(self, warehouse, target_position):
        State = namedtuple('State', ['walls', 'boxes', 'worker'])
        self.state = State(
            walls=tuple(warehouse.walls),
            boxes=tuple(warehouse.boxes),
            worker=tuple(warehouse.worker),
        )
        self.target_position = target_position
        super().__init__(self.state,self.target_position)

    def goal_test(self, state):
        return state.worker == self.target_position

    def actions(self, state):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        worker_x, worker_y = state.worker
        possible_actions = []

        for dx, dy in directions:
            nx, ny = worker_x + dx, worker_y + dy

            if (nx, ny) in state.walls:
                continue
            if (nx, ny) in state.boxes:
                continue

            direction = (dx, dy)
            possible_actions.append(direction)

        return possible_actions

    def manhattan_distance_heuristic(self, node):
        x1, y1 = node.state.worker
        x2, y2 = self.target_position
        return abs(x1 - x2) + abs(y1 - y2)

    def result(self, state, action):
        # Apply the action to get the new state (ignoring box-moving for this part)
        worker_x, worker_y = state.worker
        dx, dy = action
        new_worker_position = (worker_x + dx, worker_y + dy)
        new_state = state._replace(worker=new_worker_position)
        return new_state
    


def can_go_there(warehouse, dst):
    '''
    Determine whether the worker can walk to the cell dst=(row,column) 
    without pushing any box.
    
    @param warehouse: a valid Warehouse object

    @return
      True if the worker can walk to cell dst=(row,column) without pushing any box
      False otherwise
    '''
    if not warehouse.is_in_warehouse(dst):
        return False
    sub_problem = CanGoThereSearch(warehouse, dst)
    goal_node = search.astar_graph_search(
        sub_problem, sub_problem.manhattan_distance_heuristic)
    return goal_node is not None  # If it's None, we couldn't reach the position
