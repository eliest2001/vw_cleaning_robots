from src.domain.entities.board import Board
from src.domain.repositories.board_repository import BoardRepository


class InMemoryBoardRepository(BoardRepository):
    def __init__(self, width: int, height: int):
        self._board = Board(width, height)
    
    def get_current(self):
        return self._board

    def save(self, board: Board):
        self._board = board