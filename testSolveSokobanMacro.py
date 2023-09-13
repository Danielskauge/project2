import unittest
from sokoban import Warehouse  # Replace 'your_module' with the actual module name
from solveSokoban import solve_sokoban_macro  # Assuming the function is in this module
import search

class TestSolveSokobanMacro(unittest.TestCase):

    def setUp(self):
        self.warehouse = Warehouse()

    def set_warehouse(self, boxes, targets, walls, worker):
        self.warehouse.boxes = boxes
        self.warehouse.targets = targets
        self.warehouse.walls = walls
        self.warehouse.worker = worker

    def test_already_solved_BFS(self):
        self.set_warehouse(
            boxes=((1, 3),),
            targets=((1, 3),),
            walls=(    (1,0),
                    (0,1), (2,1),
                    (0,2), (2,2),
                    (0,3), (2,3),
                        (1,4)),
            worker=(1, 1)
        )
        result = solve_sokoban_macro(self.warehouse)
        self.assertEqual(result, [])

    def test_solvable_BFS(self):
        self.warehouse.load_warehouse('warehouses/warehouse_01.txt')
        result = solve_sokoban_macro(self.warehouse)
        self.assertNotEqual(result, [])
        self.assertNotEqual(result, 'Impossible')

    def test_impossible_BFS(self):
        self.set_warehouse(
            boxes=((1, 3),),
            targets=((1, 4),),
            walls=(       (1,0),
                    (0,1),      (2,1),
                    (0,2),(1,2),(2,2),
                    (0,3),      (2,3),
                    (0,4),      (2,4),
                          (1,5)),
            worker=(1, 1)
        )
        result = solve_sokoban_macro(self.warehouse)
        self.assertEqual(result, 'Impossible')
    '''
    def test_uniform_cost_search(self):
        self.warehouse.load_warehouse('warehouses/warehouse_01.txt')
        result = solve_sokoban_macro(self.warehouse, search.uniform_cost_search)
        print(result)
        self.assertNotEqual(result, [])
        self.assertNotEqual(result, 'Impossible')
    '''

    def test_astar(self):
        self.warehouse.load_warehouse('warehouses/warehouse_01.txt')
        result = solve_sokoban_macro(self.warehouse, search.astar_graph_search)
        self.assertNotEqual(result, [])
        self.assertNotEqual(result, 'Impossible')

if __name__ == '__main__':
    unittest.main()
