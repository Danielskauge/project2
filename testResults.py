import unittest
from sokoban import Warehouse  # Make sure to import your classes appropriately
from SokobanPuzzle import SokobanPuzzle

class TestSokobanResultFunction(unittest.TestCase):

    def setUp(self):
        self.warehouse1 = Warehouse()
        self.warehouse2 = Warehouse()

        self.warehouse1.load_warehouse('warehouses/warehouse_01.txt')
        self.warehouse2.load_warehouse('warehouses/warehouse_03.txt')
    
        self.sokoban1 = SokobanPuzzle(self.warehouse1)
        self.sokoban2 = SokobanPuzzle(self.warehouse2)

        print(self.warehouse1)
        print(self.warehouse2)
        
    def test_macro_result_1(self):
        self.sokoban1.macro = True
        initial_state = self.sokoban1.state
        action = ((3, 4), 'right')
        
        new_state = self.sokoban1.result(initial_state,action)
        
        self.assertNotEqual(initial_state, new_state)
        self.assertNotIn((3, 4), new_state.boxes)
        self.assertIn((4, 4), new_state.boxes)
        self.assertEqual((3,4),new_state.worker)

    def test_macro_result_2(self):
        self.sokoban2.macro = True

        initial_state = self.sokoban2.state
        action = ((6, 2), 'left')
        
        new_state = self.sokoban2.result(initial_state,action)
        
        self.assertNotEqual(initial_state, new_state)
        self.assertNotIn((6, 2), new_state.boxes)
        self.assertIn((5, 2), new_state.boxes)
        self.assertEqual((6,2),new_state.worker)


    def test_elem_result_worker_moved_1(self):
        self.sokoban1.macro = False
        initial_state = self.sokoban1.state
        action = 'right'
        
        expected_new_worker_position = self.sokoban1.get_neighbor_cell_in_direction(initial_state.worker, action)
        
        new_state = self.sokoban1.result(initial_state,action)
        
        self.assertEqual(expected_new_worker_position, new_state.worker)  # Assert exact expected value

    def test_elem_result_worker_moved_2(self):
        self.sokoban2.macro = False
        initial_state = self.sokoban2.state
        action = 'right'
        
        expected_new_worker_position = self.sokoban2.get_neighbor_cell_in_direction(initial_state.worker, action)
        
        new_state = self.sokoban2.result(initial_state,action)
        
        self.assertEqual(expected_new_worker_position, new_state.worker)  # Assert exact expected value

        
    def test_elem_result_box_moved_1(self):
        self.sokoban1.macro = False
        self.sokoban1.state = self.sokoban1.state._replace(worker=(4, 4))  # Assume this position is valid and beside the box
        initial_state = self.sokoban1.state
        action = 'left'
        
        new_state = self.sokoban1.result(initial_state,action)
        
        self.assertNotEqual(initial_state, new_state)
        self.assertNotIn((4, 4), new_state.boxes)
        self.assertIn((2, 4), new_state.boxes)

    def test_elem_result_box_moved_2(self):
        self.sokoban2.macro = False
        self.sokoban2.state = self.sokoban2.state._replace(worker=(8, 2))  # Assume this position is valid and beside the box
        initial_state = self.sokoban2.state
        action = 'left'
        
        new_state = self.sokoban2.result(initial_state, action)
        
        self.assertNotEqual(initial_state, new_state)
        self.assertNotIn((7, 2), new_state.boxes)
        self.assertIn((6, 2), new_state.boxes)

if __name__ == "__main__":
    unittest.main()
