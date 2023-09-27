import search
import sokoban
from sokoban import Warehouse
import tabooCells
from canGoThereSearch import can_go_there, CanGoThereSearch
from tabooCells import get_taboo_cells_positions
from collections import namedtuple
from SokobanPuzzle import SokobanPuzzle

def check_action_seq(warehouse, action_seq):

    '''
    
    Determine if the sequence of actions listed in 'action_seq' is legal or not.
    
    Important notes:
      - a legal sequence of actions does not necessarily solve the puzzle.
      - an action is legal even if it pushes a box onto a taboo cell.
        
    @param warehouse: a valid Warehouse object

    @param action_seq: a sequence of legal actions.
           For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
           
    @return
        The string 'Failure', if one of the action was not successul.
           For example, if the agent tries to push two boxes at the same time,
                        or push one box into a wall.
        Otherwise, if all actions were successful, return                 
               A string representing the state of the puzzle after applying
               the sequence of actions.  This must be the same string as the
               string returned by the method  Warehouse.__str__()
    '''
    
    ##         "INSERT YOUR CODE HERE"
    puzzel = SokobanPuzzle(warehouse, allow_taboo_push=True, macro=False)
    for action in action_seq:
        action = action.lower()
        if puzzel.is_valid_elementary_action(
            puzzel.state.worker,
            action,
            puzzel.state
        ):
          puzzel.state = puzzel.result(puzzel.state, action)
          warehouse = warehouse.copy(worker=puzzel.state.worker)
        else: 
           return 'Failure'
    
    
    return warehouse.__str__()
  
if __name__ == '__main__':
    wh = Warehouse()
    wh.load_warehouse("./warehouses/warehouse_01.txt")
    print(wh)
    action_seq = ['Right', 'Right', 'Down', 'Left']
    result = check_action_seq(wh, action_seq)
    print(result)

    ### ?? should valid move still affect the puzzle, or should only complete action sequences count??

    # ok faktisk usikker på om d e bedre å sjekk valid move for hver moe så update state, eller sjekk om move e i lista av legal moves, så sjekk for neste state

    # burde vi sjekk om move'et flytta en box?

    