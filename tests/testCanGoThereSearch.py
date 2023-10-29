import unittest
from canGoThereSearch import can_go_there, CanGoThereSearch
from sokoban import Warehouse

class TestCanGoThereSearch(unittest.TestCase):

    def setUp(self):
        self.warehouse = Warehouse()  # Assume Warehouse is defined elsewhere

        # Walls to make a warehouse with a 3x1 open space
        self.warehouse.walls = (
            (0, 0), (1, 0), (2, 0), (3, 0),(4,0),
            (0, 1),                        (4, 1),
            (0, 2), (1, 2), (2, 2), (3, 2),(4,2)
        )

        # Worker's position
        self.warehouse.worker = (1, 1)

        # Box position
        self.warehouse.boxes = ((2, 1),)

        # Target position
        self.target_position = (3, 1)

    def test_can_go_there(self):
        self.warehouse.boxes = ((3, 1),)
        self.target_position = (2, 1)

        result = can_go_there(self.warehouse, self.target_position)

        # Assuming that the worker can actually go there
        self.assertTrue(result)

    def test_cannot_go_there(self):
        # Initialize an unreachable target_position

        result = can_go_there(self.warehouse, self.target_position)

        self.assertFalse(result)  # Assuming that the worker cannot go there  

if __name__ == '__main__':
    unittest.main()
