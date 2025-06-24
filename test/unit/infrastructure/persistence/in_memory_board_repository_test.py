import unittest
from unittest.mock import MagicMock, patch
from src.infrastructure.persistence.in_memory_board_repository import InMemoryBoardRepository

class TestInMemoryBoardRepository(unittest.TestCase):
    @patch("src.infrastructure.persistence.in_memory_board_repository.Board")
    def test_init_creates_board(self, MockBoard):
        repo = InMemoryBoardRepository(5, 6)
        MockBoard.assert_called_once_with(5, 6)
        self.assertIsNotNone(repo._board)

    @patch("src.infrastructure.persistence.in_memory_board_repository.Board")
    def test_get_current_returns_board(self, MockBoard):
        mock_board_instance = MockBoard.return_value
        repo = InMemoryBoardRepository(3, 4)
        self.assertEqual(repo.get_current(), mock_board_instance)

    @patch("src.infrastructure.persistence.in_memory_board_repository.Board")
    def test_save_updates_board(self, MockBoard):
        repo = InMemoryBoardRepository(2, 2)
        mock_board = MagicMock()
        repo.save(mock_board)
        self.assertIs(repo._board, mock_board)

    @patch("src.infrastructure.persistence.in_memory_board_repository.Board")
    def test_save_and_get_current_consistency(self, MockBoard):
        repo = InMemoryBoardRepository(1, 1)
        mock_board = MagicMock()
        repo.save(mock_board)
        self.assertIs(repo.get_current(), mock_board)
    
if __name__ == "__main__":
    unittest.main()