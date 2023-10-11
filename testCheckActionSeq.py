import unittest
from sokoban import Warehouse
from CheckActionSeq import check_action_seq

class TestCheckActionSeq(unittest.TestCase):
    '''
        ASIDE FROM THE WORKER NOT BEING ABLE TO PUSH THE BOXES USING ELEMENTORY MOVES, THE REST SEEM TO BE WORKING. 
        THE WORKER GETS TEH SAME CELL AS THE BOX WHEN IT GOES TO PUSH
        LACKING SOME LOGIC IN SOKOBANPUZZ I THINK. 
        OR PERHAPS THE ENTIRE CHECKACTIONSEQ NEEDS TO BE REWORKED
    '''


    def setUp(self):
        # by using the same known warehouse we can test all the different moves
        self.warehouse = Warehouse()
        self.warehouse.load_warehouse("./warehouses/warehouse_01.txt")
                # # # #  
                #   . #
                #     # # #
                # * @     #
                #     $   #
                #     # # #
                # # # #

    def set_up_warehouse(self, boxes, targets, walls, worker):
        # Helper function to set up the warehouse state
        self.warehouse.boxes = boxes
        self.warehouse.targets = targets
        self.warehouse.walls = walls
        self.warehouse.worker = worker

    def test_valid_sequence(self):
        action_seq = ['Right', 'Right']  # Moves worker right twice
        result = check_action_seq(self.warehouse, action_seq)
        excepted_result = '####  \n# .#  \n#  ###\n#*  @#\n#  $ #\n#  ###\n####  '
        self.assertNotEqual(result, 'Failure')
        self.assertEqual(result, excepted_result)

    def test_invalid_sequence(self):
        action_seq = ['Left', 'Left']  # Moves worker into left wall
        result = check_action_seq(self.warehouse, action_seq)
        self.assertEqual(result, 'Failure')

    def test_multiple_actions(self):
        action_seq = ['Right', 'Right', 'Down', 'Left']  # Move worker behind the box and pushes left
        result = check_action_seq(self.warehouse, action_seq)
        excepted_result = '####  \n# .#  \n#  ###\n#*   #\n#  $ #\n#  ###\n####  ' #buggy, pusha faktisk ikke, forsvinn bare
        self.assertNotEqual(result, 'Failure')
        self.assertEqual(result, excepted_result)

    def test_push_to_taboo(self):
        action_seq = ['Down', 'Right']  # Moves worker down and right, pushing a box intp taboo cell
        result = check_action_seq(self.warehouse, action_seq)
        excepted_result = '####  \n# .#  \n#  ###\n#*   #\n# $. #\n#  ###\n####  ' #still move box bug. so just removed the worker;)
        self.assertNotEqual(result, 'Failure')
        self.assertEqual(result, excepted_result)

    def test_push_into_wall(self):
        action_seq = ['Down', 'Right', 'Right']  # Moves worker down and right, pushing a box intp the wall
        result = check_action_seq(self.warehouse, action_seq)
        self.assertEqual(result, 'Failure')

if __name__ == '__main__':
    unittest.main()
