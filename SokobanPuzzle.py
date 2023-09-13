
import search
import sokoban
import tabooCells
from canGoThereSearch import can_go_there, CanGoThereSearch
from tabooCells import get_taboo_cells_positions
from collections import namedtuple

class SokobanPuzzle(search.Problem):
    '''
    An instance of the class 'SokobanPuzzle' represents a Sokoban puzzle.
    An instance contains information about the walls, the targets, the boxes
    and the worker.

    Your implementation should be fully compatible with the search functions of 
    the provided module 'search.py'. 
    
    Each instance should have at least the following attributes
    - self.allow_taboo_push
    - self.macro
    
    When self.allow_taboo_push is set to True, the 'actions' function should 
    return all possible legal moves including those that move a box on a taboo 
    cell. If self.allow_taboo_push is set to False, those moves should not be
    included in the returned list of actions.
    
    If self.macro is set True, the 'actions' function should return 
    macro actions. If self.macro is set False, the 'actions' function should 
    return elementary actions.
    
    
    '''
    def __init__(self, warehouse,allow_taboo_push=True,macro=True):
        State = namedtuple('State', ['walls', 'boxes', 'targets','worker'])
        self.state = State(
            walls=tuple(warehouse.walls),
            boxes=tuple(warehouse.boxes),
            targets=tuple(warehouse.targets),
            worker=tuple(warehouse.worker)
        )

        super().__init__(initial=self.state, goal=tuple(warehouse.targets))
        self.allow_taboo_push = allow_taboo_push
        self.taboo_cells = get_taboo_cells_positions(warehouse)
        self.macro = macro
        self.warehouse = warehouse

    def goal_test(self, state):
        return set(state.boxes) == set(self.goal)


    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state.
        
        As specified in the header comment of this class, the attributes
        'self.allow_taboo_push' and 'self.macro' should be tested to determine
        what type of list of actions is to be returned.

        if elem
            check if the positions at each direction from the worker is wall or box 
            if box check if the cell one step beyond that box in the same dir is taboo, wall or other box, and determine if possible on that
            
        elif macro
            for each box, which direction can it move in based on next by taboo cells, wall or other box
                for each viable direction, can the worker reach the cell it needs to be in to move the box without moving other boxes on the way
                    add each viable direction to the action set
        """
        if self.macro:
            return self.macro_actions(state)
        else:
            return self.elementary_actions(state)
        
    def macro_actions(self, state):
        actions = []
        directions = ['left', 'up', 'right', 'down']
        for box in state.boxes:
            for dir in directions:
                if self.is_valid_macro_action(box, dir, state):
                    actions.append((box, dir))
        return actions

    def is_valid_macro_action(self, box, dir, state):
        candidate_cell = self.get_neighbor_cell_in_direction(box, dir)
        if not self.warehouse.is_in_warehouse(candidate_cell):
            return False
        if candidate_cell in state.walls or candidate_cell in state.boxes:
            return False
        if candidate_cell in self.taboo_cells and not self.allow_taboo_push:
            return False
        worker_push_position = self.get_worker_push_position(box, dir)
        return can_go_there(self.warehouse, worker_push_position)

    def elementary_actions(self, state):
        actions = []
        directions = ['left', 'up', 'right', 'down']
        for dir in directions:
            if self.is_valid_elementary_action(state.worker, dir, state):
                actions.append(dir)
        return actions

    def is_valid_elementary_action(self, worker, dir, state):
        candidate_cell = self.get_neighbor_cell_in_direction(worker, dir)
        if not self.warehouse.is_in_warehouse(candidate_cell):
            return False
        if candidate_cell in state.walls:
            return False
        if candidate_cell in state.boxes:
            beyond_box_pos = self.get_neighbor_cell_in_direction(candidate_cell, dir)
            return self.is_push_possible(beyond_box_pos, state)
        return True

    def is_push_possible(self, beyond_box_pos, state):
        return not (beyond_box_pos in state.boxes or beyond_box_pos in state.walls or
                    (beyond_box_pos in self.taboo_cells and not self.allow_taboo_push))
    
    def get_neighbor_cell_in_direction(self,cell,dir):
        return {
                'left': (cell[0]-1,cell[1]),
                'right': (cell[0]+1,cell[1]),
                'up': (cell[0],cell[1]-1),
                'down': (cell[0],cell[1]+1)
            }.get(dir)
    
    def get_worker_push_position(self, box,dir):
        return {
            'left': (box[0]+1,box[1]),
            'right': (box[0]-1,box[1]),
            'up': (box[0],box[1]+1),
            'down': (box[0],box[1]-1)
        }.get(dir)
    
    def result(self, state, action):
        return self.macro_result(state, action) if self.macro else self.elem_result(state, action)

    def macro_result(self, state, action):
        box_to_move_coords, direction = action
        new_boxes_coords = self.update_boxes_coords(state, box_to_move_coords, direction)
        new_worker_coords = box_to_move_coords
        return state._replace(boxes=new_boxes_coords, worker=new_worker_coords)

    def elem_result(self, state, action):
        direction = action
        new_worker_coords = self.update_worker_coords(state, direction)

        if new_worker_coords in state.boxes:
            new_boxes_coords = self.update_boxes_coords(state, new_worker_coords, direction)
        else:
            new_boxes_coords = state.boxes

        return state._replace(boxes=new_boxes_coords, worker=new_worker_coords)

    def update_boxes_coords(self, state, old_box_coords, direction):
        new_box_coords = self.get_neighbor_cell_in_direction(old_box_coords, direction)
        box_index = state.boxes.index(old_box_coords)
        return tuple(new_box_coords if i == box_index else box for i, box in enumerate(state.boxes))

    def update_worker_coords(self, state, direction):
        return self.get_neighbor_cell_in_direction(state.worker, direction)
    
    #def heurustic(self, state, goal):