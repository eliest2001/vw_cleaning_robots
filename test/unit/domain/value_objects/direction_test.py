import unittest
from src.domain.value_objects.direction import Direction

class TestDirection(unittest.TestCase):
    def test_left_rotation(self):
        self.assertEqual(Direction.NORTH.left(), Direction.WEST)
        self.assertEqual(Direction.WEST.left(), Direction.SOUTH)
        self.assertEqual(Direction.SOUTH.left(), Direction.EAST)
        self.assertEqual(Direction.EAST.left(), Direction.NORTH)

    def test_right_rotation(self):
        self.assertEqual(Direction.NORTH.right(), Direction.EAST)
        self.assertEqual(Direction.EAST.right(), Direction.SOUTH)
        self.assertEqual(Direction.SOUTH.right(), Direction.WEST)
        self.assertEqual(Direction.WEST.right(), Direction.NORTH)

    def test_str_returns_value(self):
        self.assertEqual(str(Direction.NORTH), "N")
        self.assertEqual(str(Direction.SOUTH), "S")

    def test_enum_values(self):
        self.assertEqual(Direction.NORTH.value, "N")
        self.assertEqual(Direction.SOUTH.value, "S")
        self.assertEqual(Direction.EAST.value, "E")
        self.assertEqual(Direction.WEST.value, "W")

if __name__ == "__main__":
    unittest.main()