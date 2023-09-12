import unittest
from sokoban import Warehouse  # Replace with the actual import
from SokobanPuzzle import SokobanPuzzle

class TestSokobanActions(unittest.TestCase):

    def setUp(self):
        self.warehouse1 = Warehouse()  # Initialize with some state
        self.warehouse1.load_warehouse('warehouses/warehouse_01.txt')
        self.warehouse2 = Warehouse()  # Initialize with some different state
        self.warehouse2.load_warehouse('warehouses/warehouse_03.txt')
        print(self.warehouse1)
        print('\n')
        print(self.warehouse2)
        
        self.puzzle1 = SokobanPuzzle(self.warehouse1)
        self.puzzle2 = SokobanPuzzle(self.warehouse2)

    def test_actions_elem_1(self):
        self.puzzle1.macro = False
        self.puzzle1.allow_taboo_push = True

        actions = self.puzzle1.actions(self.puzzle1.state)  # Replace 'initial' with whatever you use to get the initial state
        expected_actions = ['right','up','down']  # Fill this in with the expected actions
        self.assertEqual(set(actions), set(expected_actions))


    def test_actions_elem_2(self):
        self.puzzle2.macro = False
        self.puzzle1.allow_taboo_push = True
        actions = self.puzzle2.actions(self.puzzle2.state)  # Replace 'initial' with whatever you use to get the initial state
        expected_actions = ['right']  # Fill this in with the expected actions
        self.assertEqual(set(actions), set(expected_actions))

    def test_actions_macro_1(self):
        self.puzzle1.macro = True
        self.puzzle1.allow_taboo_push = True
        actions = self.puzzle1.actions(self.puzzle1.state)  # Replace 'initial' with whatever you use to get the initial state
        expected_actions = [((1,3),'down'), 
                            ((1,3),'up'), 
                            ((3,4),'right'), 
                            ((3,4),'left')]  # Fill this in with the expected actions
        self.assertEqual(set(actions), set(expected_actions))


    def test_actions_macro_2(self):
        self.puzzle2.macro = True
        self.puzzle1.allow_taboo_push = True
        actions = self.puzzle2.actions(self.puzzle2.state)  # Replace 'initial' with whatever you use to get the initial state
        expected_actions = [((6, 2), 'left')]  # Fill this in with the expected actions
        self.assertEqual(set(actions), set(expected_actions))

    def test_actions_elem_taboo_1(self):
        self.puzzle1.allow_taboo_push = False
        self.puzzle1.macro = False
        actions = self.puzzle1.actions(self.puzzle1.initial)  # Replace 'initial' with whatever you use to get the initial state
        expected_actions = ['up','right','down']  # Fill this in with theSD expected actions
        self.assertEqual(set(actions), set(expected_actions))

    def test_actions_macro_taboo_1(self):
        self.puzzle1.allow_taboo_push = False
        self.puzzle1.macro = True
        actions = self.puzzle1.actions(self.puzzle1.initial)  # Replace 'initial' with whatever you use to get the initial state
        expected_actions = [((1,3),'down'), 
                            ((1,3),'up'), 
                            ((3,4),'left')]  # Fill this in with theSD expected actions
        self.assertEqual(set(actions), set(expected_actions))
   
if __name__ == '__main__':
    unittest.main()
