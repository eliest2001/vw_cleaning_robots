from dataclasses import dataclass
from src.domain.value_objects.direction import Direction

@dataclass(frozen=True)
class Position:
    x: int
    y: int
    
    def next(self, direction: Direction) -> 'Position':
        if direction == Direction.NORTH:
            return Position(self.x, self.y + 1)
        elif direction == Direction.SOUTH:
            return Position(self.x, self.y - 1)
        elif direction == Direction.EAST:
            return Position(self.x + 1, self.y)
        elif direction == Direction.WEST:
            return Position(self.x - 1, self.y)