import unittest
from sokoban import Warehouse  # Replace 'your_module' with the actual module name
from solveSokoban import solve_sokoban_elem

class TestSolveSokobanElem(unittest.TestCase):

    def setUp(self):
        self.warehouse = Warehouse()

    def set_warehouse(self, boxes, targets, walls, worker):
        self.warehouse.boxes = boxes
        self.warehouse.targets = targets
        self.warehouse.walls = walls
        self.warehouse.worker = worker

    def test_already_solved(self):
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

        print('Test already solved \n', self.warehouse)
        result = solve_sokoban_elem(self.warehouse)
        self.assertEqual(result, [])

    def test_solvable(self):
        self.warehouse.load_warehouse('warehouses/warehouse_07.txt')
        print('Test solveable \n', self.warehouse)
        result = solve_sokoban_elem(self.warehouse)
        self.assertNotEqual(result,[])
        self.assertNotEqual(result,'Impossible')

    def test_impossible(self):
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
        print('Test Impossible \n', self.warehouse)
        result = solve_sokoban_elem(self.warehouse)
        self.assertEqual(result, 'Impossible')

if __name__ == '__main__':
    unittest.main()
