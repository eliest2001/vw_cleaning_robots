from typing import Dict
from src.domain.entities.robot import Robot
from src.domain.exceptions import OutOfBoardError, RobotNotFoundError
from src.domain.value_objects.position import Position


class Board:
    """
    Represents the board where robots can be placed and moved.

    The board manages robot placement, movement, and rotation, ensuring that all robot actions
    are within the board's boundaries. It also provides utility methods to check positions and
    occupancy.

    Attributes:
        width (int): The width of the board (inclusive, board goes from 0 to width).
        height (int): The height of the board (inclusive, board goes from 0 to height).
        robots (Dict[str, Robot]): Dictionary of robots on the board, keyed by robot ID.
    """

    def __init__(self, width: int, height: int):
        """
        Initializes the board with the given width and height.

        Args:
            width (int): The width of the board (max x coordinate).
            height (int): The height of the board (max y coordinate).
        """
        self.width = width + 1
        self.height = height + 1
        self.robots: Dict[str,Robot] = {}
        
    def add_robot(self, robot: Robot):
        """
        Adds a robot to the board at its current position.

        Args:
            robot (Robot): The robot to add.

        Raises:
            OutOfBoardError: If the robot's position is outside the board.
        """
        if not self.is_inside(robot.position):
            raise OutOfBoardError("Robot outside of the board")

        self.robots[robot.id] = robot
        
    def is_inside(self, position: Position):
        """
        Checks if a given position is inside the board boundaries.

        Args:
            position (Position): The position to check.

        Returns:
            bool: True if inside the board, False otherwise.
        """
        return 0 <= position.x < self.width and 0 <= position.y < self.height
    
    def is_occupied(self, position: Position):
        """
        Checks if a given position is occupied by any robot.

        Args:
            position (Position): The position to check.

        Returns:
            bool: True if the position is occupied, False otherwise.
        """
        return not any(r.position == position for r in self.robots.values())
    
    def move_robot_forward(self, robot_id: str):
        """
        Moves the specified robot forward in its current direction if possible.

        Args:
            robot_id (str): The ID of the robot to move.

        Raises:
            RobotNotFoundError: If the robot with the given ID does not exist.
        """
        robot = self.robots.get(robot_id)
        if not robot:
            raise RobotNotFoundError("Robot not found")
        new_position = robot.position.next(robot.direction)
        if self.is_inside(new_position):
           robot.move_forward()            

    def rotate_robot_left(self, robot_id: str):
        """
        Rotates the specified robot to the left.

        Args:
            robot_id (str): The ID of the robot to rotate.

        Raises:
            RobotNotFoundError: If the robot with the given ID does not exist.
        """
        robot = self.robots.get(robot_id)
        if not robot:
            raise RobotNotFoundError("Robot not found")
        robot.rotate_left()

    def rotate_robot_right(self, robot_id: str):
        """
        Rotates the specified robot to the right.

        Args:
            robot_id (str): The ID of the robot to rotate.

        Raises:
            RobotNotFoundError: If the robot with the given ID does not exist.
        """
        robot = self.robots.get(robot_id)
        if not robot:
            raise RobotNotFoundError("Robot not found")
        robot.rotate_right()