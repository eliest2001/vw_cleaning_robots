from typing import Protocol
from src.domain.entities.board import Board

class BoardRepository(Protocol):
    """
    Protocol for board persistence operations.

    Defines the interface for retrieving and saving the current board state.
    Implementations may persist the board in memory, a database, or other storage.

    Methods:
        get_current() -> Board:
            Returns the current board instance.

        save(board: Board) -> None:
            Persists the given board instance.
    """
    def get_current(self) -> Board:
        ...
    def save(self, board: Board) -> None:
        ...