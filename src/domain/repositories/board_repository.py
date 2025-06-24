from typing import Protocol
from src.domain.entities.board import Board

class BoardRepository(Protocol):
    def get_current(self) -> Board:
        ...
    def save(self, board: Board) -> None:
        ...