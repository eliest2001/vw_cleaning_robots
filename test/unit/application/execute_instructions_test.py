import unittest
from unittest.mock import MagicMock, patch
from src.application.use_cases.execute_instructions import ExecuteInstructionsUseCase

class TestExecuteInstructionsUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_board_repository = MagicMock()
        self.mock_board = MagicMock()
        self.mock_board_repository.get_current.return_value = self.mock_board
        self.use_case = ExecuteInstructionsUseCase(self.mock_board_repository)
        self.robot_id = "robot1"

    def test_execute_calls_move_forward(self):
        self.use_case.execute(self.robot_id, "M")
        self.mock_board.move_robot_forward.assert_called_once_with(robot_id=self.robot_id)
        self.mock_board_repository.save.assert_called_once_with(self.mock_board)

    def test_execute_calls_rotate_left(self):
        self.use_case.execute(self.robot_id, "L")
        self.mock_board.rotate_robot_left.assert_called_once_with(robot_id=self.robot_id)
        self.mock_board_repository.save.assert_called_once_with(self.mock_board)

    def test_execute_calls_rotate_right(self):
        self.use_case.execute(self.robot_id, "R")
        self.mock_board.rotate_robot_right.assert_called_once_with(robot_id=self.robot_id)
        self.mock_board_repository.save.assert_called_once_with(self.mock_board)

    def test_execute_multiple_instructions(self):
        self.use_case.execute(self.robot_id, "MLMR")
        self.assertEqual(self.mock_board.move_robot_forward.call_count, 2)
        self.assertEqual(self.mock_board.rotate_robot_left.call_count, 1)
        self.assertEqual(self.mock_board.rotate_robot_right.call_count, 1)
        self.mock_board_repository.save.assert_called_once_with(self.mock_board)

    def test_execute_invalid_instruction_raises(self):
        with self.assertRaises(ValueError):
            self.use_case.execute(self.robot_id, "MX")
        self.mock_board.move_robot_forward.assert_called_once_with(robot_id=self.robot_id)
        self.mock_board_repository.save.assert_not_called()

    def test_execute_handles_exception_from_board(self):
        self.mock_board.move_robot_forward.side_effect = Exception("fail")
        with self.assertRaises(Exception):
            self.use_case.execute(self.robot_id, "M")
        self.mock_board_repository.save.assert_not_called()

    def test_execute_empty_instructions(self):
        self.use_case.execute(self.robot_id, "")
        self.mock_board.move_robot_forward.assert_not_called()
        self.mock_board.rotate_robot_left.assert_not_called()
        self.mock_board.rotate_robot_right.assert_not_called()
        self.mock_board_repository.save.assert_called_once_with(self.mock_board)

if __name__ == "__main__":
    unittest.main()