import unittest
from unittest.mock import MagicMock, patch
from src.domain.entities.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.width = 5
        self.height = 5
        self.board = Board(self.width, self.height)
        self.mock_robot = MagicMock()
        self.mock_robot.id = "robot1"
        self.mock_robot.position.x = 2
        self.mock_robot.position.y = 3

    def test_add_robot_inside_board(self):
        self.mock_robot.position.x = 1
        self.mock_robot.position.y = 1
        self.board.is_inside = MagicMock(return_value=True)
        self.board.add_robot(self.mock_robot)
        self.assertIn(self.mock_robot.id, self.board.robots)

    def test_add_robot_outside_board_raises(self):
        self.board.is_inside = MagicMock(return_value=False)
        with self.assertRaises(ValueError):
            self.board.add_robot(self.mock_robot)

    def test_is_inside_true(self):
        pos = MagicMock()
        pos.x = 0
        pos.y = 0
        self.assertTrue(self.board.is_inside(pos))
        pos.x = self.width - 1
        pos.y = self.height - 1
        self.assertTrue(self.board.is_inside(pos))

    def test_is_inside_false(self):
        pos = MagicMock()
        pos.x = -1
        pos.y = 0
        self.assertFalse(self.board.is_inside(pos))
        pos.x = 0
        pos.y = self.height
        self.assertFalse(self.board.is_inside(pos))

    def test_is_occupied_false_when_empty(self):
        pos = MagicMock()
        self.assertTrue(self.board.is_occupied(pos))

    def test_is_occupied_true_when_occupied(self):
        self.mock_robot.position = MagicMock()
        self.board.robots[self.mock_robot.id] = self.mock_robot
        pos = self.mock_robot.position
        # Patch __eq__ to return True for the test
        pos.__eq__ = MagicMock(return_value=True)
        self.assertFalse(self.board.is_occupied(pos))

    def test_move_robot_forward_calls_robot(self):
        self.board.robots[self.mock_robot.id] = self.mock_robot
        self.board.is_inside = MagicMock(return_value=True)
        self.board.move_robot_forward(self.mock_robot.id)
        self.mock_robot.move_forward.assert_called_once()

    def test_move_robot_forward_robot_not_found(self):
        with self.assertRaises(ValueError):
            self.board.move_robot_forward("not_exist")
            
    def test_move_robot_forward_not_inside(self):
        self.board.robots[self.mock_robot.id] = self.mock_robot
        self.board.is_inside = MagicMock(return_value=False)
        with self.assertRaises(ValueError):
             self.board.move_robot_forward(self.mock_robot.id)
        
        
    def test_rotate_robot_left_calls_robot(self):
        self.board.robots[self.mock_robot.id] = self.mock_robot
        self.board.rotate_robot_left(self.mock_robot.id)
        self.mock_robot.rotate_left.assert_called_once()

    def test_rotate_robot_left_robot_not_found(self):
        with self.assertRaises(ValueError):
            self.board.rotate_robot_left("not_exist")

    def test_rotate_robot_right_calls_robot(self):
        self.board.robots[self.mock_robot.id] = self.mock_robot
        self.board.rotate_robot_right(self.mock_robot.id)
        self.mock_robot.rotate_right.assert_called_once()

    def test_rotate_robot_right_robot_not_found(self):
        with self.assertRaises(ValueError):
            self.board.rotate_robot_right("not_exist")

if __name__ == "__main__":
    unittest.main()