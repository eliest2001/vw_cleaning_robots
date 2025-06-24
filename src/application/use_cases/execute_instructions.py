from src.domain.repositories.board_repository import BoardRepository

class ExecuteInstructionsUseCase:
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository
        
    def execute(self, robot_id: str, instructions: str):
        board = self.board_repository.get_current()
        
        for instr in instructions:
            try:
                if instr == "M":
                    board.move_robot_forward(robot_id=robot_id)
                elif instr == "L":
                    board.rotate_robot_left(robot_id=robot_id)
                elif instr == "R":
                    board.rotate_robot_right(robot_id=robot_id)
                else:
                    raise ValueError(f"Instruction {instr} is not an available movement")
            except Exception as e:
                print(f"Error moving robot {robot_id}: {e}")
                raise e
        
        self.board_repository.save(board)