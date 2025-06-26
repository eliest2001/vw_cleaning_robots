from dataclasses import dataclass
from src.domain.value_objects.direction import Direction

@dataclass(frozen=True)
class Position:
    """
    Value object representing a position on the board.

    Attributes:
        x (int): The x-coordinate of the position.
        y (int): The y-coordinate of the position.
    """
    x: int
    y: int
    
    def next(self, direction: Direction) -> 'Position':
        """
        Returns the next position from the current one, moving in the given direction.

        Args:
            direction (Direction): The direction to move.

        Returns:
            Position: The new position after moving in the specified direction.
        """
        if direction == Direction.NORTH:
            return Position(self.x, self.y + 1)
        elif direction == Direction.SOUTH:
            return Position(self.x, self.y - 1)
        elif direction == Direction.EAST:
            return Position(self.x + 1, self.y)
        elif direction == Direction.WEST:
            return Position(self.x - 1, self.y)