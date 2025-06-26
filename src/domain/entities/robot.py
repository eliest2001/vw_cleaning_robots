from dataclasses import dataclass, field
from uuid import uuid4
from src.domain.value_objects.direction import Direction
from src.domain.value_objects.position import Position


@dataclass
class Robot:
    """
    Represents a robot with a position and direction on the board.

    Attributes:
        position (Position): The current position of the robot.
        direction (Direction): The current facing direction of the robot.
        id (str): Unique identifier for the robot.
    """

    position: Position
    direction: Direction
    id: str = field(default_factory=lambda: str(uuid4()))
    
    def move_forward(self):
        """
        Moves the robot forward one unit in its current direction.
        """
        self.position = self.position.next(self.direction)
    
    def rotate_left(self):
        """
        Rotates the robot to the left.
        """
        self.direction = self.direction.left()
    
    def rotate_right(self):
        """
        Rotates the robot to the right.
        """
        self.direction = self.direction.right()
        
    def format(self, length: int):
        """
        Returns a formatted string representing the robot's position and direction.

        Args:
            length (int): The zero-padding length for coordinates.

        Returns:
            str: The formatted string, e.g., "0203 N".
        """
        x_str = str(self.position.x).zfill(length)
        y_str = str(self.position.y).zfill(length)
        return f"{x_str}{y_str} {self.direction}"