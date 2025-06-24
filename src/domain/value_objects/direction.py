from enum import Enum

class Direction(str, Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    
    def left(self) -> 'Direction':
        mapping = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH
        }
        return mapping[self]
    
    def right(self) -> 'Direction':
        mapping = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        return mapping[self]
    
    def __str__(self):
        return super().__str__()    