from typing import Dict
from src.domain.entities.robot import Robot
from src.domain.exceptions import OutOfBoardError, RobotNotFoundError
from src.domain.value_objects.position import Position


class Board:
    def __init__(self, width: int, height: int):
        self.width = width + 1
        self.height = height + 1
        self.robots: Dict[str,Robot] = {}
        
    def add_robot(self, robot: Robot):
        if not self.is_inside(robot.position):
            raise OutOfBoardError("Robot outside of the board")

        self.robots[robot.id] = robot
        
    def is_inside(self, position: Position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height
    
    def is_occupied(self, position: Position):
        return not any(r.position == position for r in self.robots.values())
    
    def move_robot_forward(self, robot_id: str):
        robot = self.robots.get(robot_id)
        if not robot:
            raise RobotNotFoundError("Robot not found")
        new_position = robot.position.next(robot.direction)
        if self.is_inside(new_position):
           robot.move_forward()            

    def rotate_robot_left(self, robot_id: str):
        robot = self.robots.get(robot_id)
        if not robot:
            raise RobotNotFoundError("Robot not found")
        robot.rotate_left()

    def rotate_robot_right(self, robot_id: str):
        robot = self.robots.get(robot_id)
        if not robot:
            raise RobotNotFoundError("Robot not found")
        robot.rotate_right()