from src.application.use_cases.execute_instructions import ExecuteInstructionsUseCase
from src.domain.entities.robot import Robot
from src.domain.value_objects.direction import Direction
from src.domain.value_objects.position import Position
from src.infrastructure.input_parser import parse_input
from src.infrastructure.persistence.in_memory_board_repository import InMemoryBoardRepository


raw_input = "55\n12 N\nLMLMLMLMMMMMMMMMMMMM\n33 E\nMMRMMRMRRM"
width, height, robot_data = parse_input(raw_input)

repo = InMemoryBoardRepository(width, height)

board = repo.get_current()
robots_ids_and_instruction = []
for x, y, dir_str, instr_line in robot_data:
    id = id=f"R{len(robots_ids_and_instruction) + 1}"
    robot = Robot(
        id=id,
        position=Position(int(x),int(y)),
        direction=Direction(dir_str)
    )
    board.add_robot(robot)
    robots_ids_and_instruction.append((id, instr_line))
    
repo.save(board)

use_case = ExecuteInstructionsUseCase(repo)
for robot_id, instructions in robots_ids_and_instruction:
    use_case.execute(robot_id, instructions)

for robot in repo.get_current().robots.values():
    print(f"{robot.position.x}{robot.position.y} {robot.direction}")