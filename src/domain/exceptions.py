class OutOfBoardError(Exception):
    """
    Exception raised when a robot is placed outside the board boundaries.
    """
    pass

class RobotNotFoundError(Exception):
    """
    Exception raised when a robot with a specified ID is not found on the board.
    """
    pass