import unittest
import pytest
from src.application.use_cases.execute_instructions import ExecuteInstructionsUseCase
from src.domain.exceptions import OutOfBoardError, RobotNotFoundError
from src.infrastructure.persistence.in_memory_board_repository import InMemoryBoardRepository
from src.domain.entities.robot import Robot
from src.domain.value_objects.position import Position
from src.domain.value_objects.direction import Direction

def setup_board(width, height):
    repo = InMemoryBoardRepository(width, height)
    return repo

def add_robot_to_board(repo, x, y, dir_str):
    robot = Robot(
        position=Position(x, y),
        direction=Direction(dir_str)
    )
    tablero = repo.get_current()
    tablero.add_robot(robot)
    repo.save(tablero)
    return robot

class TestExecuteInstructionsUseCase(unittest.TestCase):
    def test_robot_stop_if_going_out_of_bounds(self):
        repo = setup_board(2, 2)
        r = add_robot_to_board(repo, 2, 2, "N") 
        use_case = ExecuteInstructionsUseCase(repo)
        
        use_case.execute(r.id, "M")
        self.assertEqual(r.position, Position(2,2))
    
    def test_robot_long_execution(self):
        repo = setup_board(5, 5)
        r = add_robot_to_board(repo, 1, 2, "N") 
        r2 = add_robot_to_board(repo, 3, 3, "E") 
        use_case = ExecuteInstructionsUseCase(repo)
        
        use_case.execute(r.id, "LMLMLMLMM")
        use_case.execute(r2.id, "MMRMMRMRRM")
        
        self.assertEqual(r.position, Position(1,3))
        self.assertEqual(r.direction, Direction.NORTH)
        
        self.assertEqual(r2.position, Position(5,1))
        self.assertEqual(r2.direction, Direction.EAST)
        
    def test_robot_not_found(self):
        repo = setup_board(2, 2)
        use_case = ExecuteInstructionsUseCase(repo)
        
        with self.assertRaises(RobotNotFoundError):
            use_case.execute("1", "M")

    def test_robot_out_of_board(self):
        repo = setup_board(2, 2)  
        with self.assertRaises(OutOfBoardError):
            add_robot_to_board(repo, 3, 3, "N") 
            
        