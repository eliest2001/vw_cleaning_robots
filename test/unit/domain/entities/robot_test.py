import unittest
from unittest.mock import MagicMock
from src.domain.entities.robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.mock_position = MagicMock()
        self.mock_direction = MagicMock()
        self.robot = Robot(id="robot1", position=self.mock_position, direction=self.mock_direction)

    def test_move_forward_updates_position(self):
        new_position = MagicMock()
        self.mock_position.next.return_value = new_position
        self.robot.move_forward()
        self.mock_position.next.assert_called_once_with(self.mock_direction)
        self.assertEqual(self.robot.position, new_position)

    def test_rotate_left_updates_direction(self):
        new_direction = MagicMock()
        self.mock_direction.left.return_value = new_direction
        self.robot.rotate_left()
        self.mock_direction.left.assert_called_once()
        self.assertEqual(self.robot.direction, new_direction)

    def test_rotate_right_updates_direction(self):
        new_direction = MagicMock()
        self.mock_direction.right.return_value = new_direction
        self.robot.rotate_right()
        self.mock_direction.right.assert_called_once()
        self.assertEqual(self.robot.direction, new_direction)

if __name__ == "__main__":
    unittest.main()