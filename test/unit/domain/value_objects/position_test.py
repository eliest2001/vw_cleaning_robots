import unittest
from src.domain.value_objects.position import Position
from src.domain.value_objects.direction import Direction

class TestPosition(unittest.TestCase):
    def setUp(self):
        self.position = Position(2, 3)

    def test_next_north(self):
        new_pos = self.position.next(Direction.NORTH)
        self.assertEqual(new_pos, Position(2, 4))

    def test_next_south(self):
        new_pos = self.position.next(Direction.SOUTH)
        self.assertEqual(new_pos, Position(2, 2))

    def test_next_east(self):
        new_pos = self.position.next(Direction.EAST)
        self.assertEqual(new_pos, Position(3, 3))

    def test_next_west(self):
        new_pos = self.position.next(Direction.WEST)
        self.assertEqual(new_pos, Position(1, 3))


if __name__ == "__main__":
    unittest.main()