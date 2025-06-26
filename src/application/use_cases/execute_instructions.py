from src.application.exceptions import InvalidCommandError
from src.domain.exceptions import OutOfBoardError
from src.domain.repositories.board_repository import BoardRepository

class ExecuteInstructionsUseCase:
    """
    Use case for executing a sequence of movement instructions for a robot on the board.

    This class retrieves the current board from the repository, applies each instruction
    to the specified robot, and saves the updated board state. Valid instructions are:
    - 'M': Move the robot forward
    - 'L': Rotate the robot left
    - 'R': Rotate the robot right

    Raises:
        InvalidCommandError: If an instruction is not recognized.
        Exception: Propagates any exception raised by board methods.
    """

    def __init__(self, board_repository: BoardRepository):
        """
        Initialize the use case with a board repository.

        Args:
            board_repository (BoardRepository): The repository to manage board state.
        """
        self.board_repository = board_repository
        
    def execute(self, robot_id: str, instructions: str):
        """
        Execute a sequence of instructions for a robot.

        Args:
            robot_id (str): The ID of the robot to move.
            instructions (str): A string of instructions (e.g., "LMLMR").

        Raises:
            InvalidCommandError: If an instruction is invalid.
            Exception: If any board operation fails.
        """
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
                    raise InvalidCommandError(f"Instruction {instr} is not an available movement")
            except Exception as e:
                raise e
        
        self.board_repository.save(board)