import sys

from src.application.use_cases.execute_instructions import ExecuteInstructionsUseCase
from src.domain.entities.robot import Robot
from src.domain.value_objects.direction import Direction
from src.domain.value_objects.position import Position
from src.infrastructure.input_parser import parse_input
from src.infrastructure.persistence.in_memory_board_repository import InMemoryBoardRepository


def cli():
    """
    Command-line interface for running the cleaning robots simulation.

    Reads input from stdin, parses the board and robot data, initializes the board and robots,
    executes the movement instructions for each robot, and prints the final positions.

    Steps:
        1. Reads the entire input from stdin.
        2. Parses the input to extract board dimensions and robot data.
        3. Initializes the in-memory board repository and board.
        4. Adds each robot to the board and stores their instructions.
        5. Executes the instructions for each robot using the use case.
        6. Prints the final formatted position of each robot.

    Exceptions:
        Prints any exception message to stdout if an error occurs during execution.
    """
    try:
        raw_input = sys.stdin.read() 
        coords_len, width, height, robot_data = parse_input(raw_input)

        repo = InMemoryBoardRepository(width, height)

        board = repo.get_current()
        robots_ids_and_instruction = []
        for x, y, dir_str, instr_line in robot_data:
            robot = Robot(
                position=Position(int(x),int(y)),
                direction=Direction(dir_str)
            )
            board.add_robot(robot)
            robots_ids_and_instruction.append((robot.id, instr_line))
            
        repo.save(board)

        use_case = ExecuteInstructionsUseCase(repo)
        for robot_id, instructions in robots_ids_and_instruction:
            use_case.execute(robot_id, instructions)

        for robot in repo.get_current().robots.values():
            print(robot.format(coords_len))
    except Exception as e:
        print(e)
if __name__ == "__main__":
    cli()