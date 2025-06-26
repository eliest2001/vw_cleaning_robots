from enum import Enum

class Direction(str, Enum):
    """
    Enum representing the four cardinal directions for robot orientation.

    Values:
        NORTH ("N"): Facing north (up).
        SOUTH ("S"): Facing south (down).
        EAST ("E"): Facing east (right).
        WEST ("W"): Facing west (left).
    """
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    
    def left(self) -> 'Direction':
        """
        Returns the direction to the left (counterclockwise) of the current direction.

        Returns:
            Direction: The new direction after turning left.
        """
        mapping = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH
        }
        return mapping[self]
    
    def right(self) -> 'Direction':
        """
        Returns the direction to the right (clockwise) of the current direction.

        Returns:
            Direction: The new direction after turning right.
        """
        mapping = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        return mapping[self]
    
    def __str__(self):
        """
        Returns the string representation of the direction.

        Returns:
            str: The direction as a string (e.g., "N", "S", "E", "W").
        """
        return super().__str__()    