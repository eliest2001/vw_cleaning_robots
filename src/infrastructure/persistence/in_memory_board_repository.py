from src.domain.entities.board import Board
from src.domain.repositories.board_repository import BoardRepository


class InMemoryBoardRepository(BoardRepository):
    """
    In-memory implementation of the BoardRepository protocol.

    Stores the board state in memory for the duration of the application's execution.
    """    
    def __init__(self, width: int, height: int):
        """
        Initializes the repository with a new board of the given dimensions.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
        """
        self._board = Board(width, height)
    
    def get_current(self):
        """
        Returns the current board instance stored in memory.

        Returns:
            Board: The current board.
        """
        return self._board

    def save(self, board: Board):
        """
        Replaces the current board instance with the provided one.

        Args:
            board (Board): The board instance to store.
        """
        self._board = board