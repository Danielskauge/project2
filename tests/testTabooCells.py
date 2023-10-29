import unittest
from sokoban import Warehouse
from tabooCells import taboo_cells

class TestTabooCells(unittest.TestCase):

    def test_single_wall(self):
        warehouse = Warehouse()
        warehouse.walls = [(0, 0)]
        warehouse.targets = []
        result = taboo_cells(warehouse)
        self.assertEqual(result, '#')

    def test_walls_with_targets(self):
        warehouse = Warehouse()
        warehouse.targets = []
        warehouse.walls = [(0, 0), (0, 1), (0, 2)]
        result = taboo_cells(warehouse)
        self.assertEqual(result, '#\n#\n#')

    def test_complex_scenario_1(self):
        warehouse = Warehouse()
        warehouse.walls = [(0, 0), (1, 0), (2, 0),
                            (0, 1),(2, 1), 
                            (0, 2), (1, 2), (2, 2)]
        warehouse.targets = [(1, 1)]
        result = taboo_cells(warehouse)
        expected = '###\n# #\n###'
        self.assertEqual(result, expected)

    def test_complex_scenario_2(self):
        warehouse = Warehouse()
        warehouse.walls = [(0, 0), (1, 0), (2, 0),
                            (0, 1),(2, 1), 
                            (0, 2), (1, 2), (2, 2)]
        warehouse.targets = []

        result = taboo_cells(warehouse)
        expected = '###\n#X#\n###'
        self.assertEqual(result, expected)
        
    def test_complex_scenario_3(self):
        warehouse = Warehouse()
        warehouse.walls = [(0, 0), (1, 0),(2,0),(3,0),(4,0),
                            (0, 1),(4,1) ,
                            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]
        warehouse.targets = [(1,1)]

        result = taboo_cells(warehouse)
        expected = '#####\n#  X#\n#####'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
