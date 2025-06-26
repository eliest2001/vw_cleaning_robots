from src.infrastructure.exceptions import InputParseError


def parse_input(input_data: str):
    lines = input_data.strip().splitlines()
    if not lines:
        raise InputParseError("Input is empty")

    first_line = lines[0].strip().replace(" ", "")
    if not first_line.isdigit() or len(first_line) % 2 != 0:
        raise InputParseError(
            f"Invalid grid dimensions on first line: '{lines[0]}'. "
            "Must contain only positives digits with even length."
        )

    board_coords_len = len(first_line) // 2
    width_str = first_line[:board_coords_len]
    height_str = first_line[board_coords_len:]
    width = int(width_str)
    height = int(height_str)

    if width <= 0 or height <= 0:
        raise InputParseError(f"Grid width and height must be positive. Got width={width}, height={height}")

    robot_data = []
    i = 1

    while i < len(lines):
        if i + 1 >= len(lines):
            raise InputParseError(f"Missing instructions for the robot on line {i+1}")

        position_line = lines[i].split()
        instr_line = lines[i+1].strip()

        if len(position_line) != 2:
            raise InputParseError(f"Invalid position line at line {i+1}: '{lines[i]}'")

        robot_coords_str = position_line[0]
        robot_dir_str = position_line[1].upper()

        if not robot_coords_str.isdigit() or len(robot_coords_str) % 2 != 0:
            raise InputParseError(
                f"Invalid coordinate string on line {i+1}: '{robot_coords_str}'"
            )
                          
        robot_mid_coords = len(robot_coords_str) // 2
        if robot_mid_coords != board_coords_len:
            raise InputParseError(
                f"Board coords must have the same length as robot coords" 
            ) 
        x_str = robot_coords_str[:robot_mid_coords]
        y_str = robot_coords_str[robot_mid_coords:]
        x = int(x_str)
        y = int(y_str)

        if robot_dir_str not in ("N", "S", "E", "W"):
            raise InputParseError(
                f"Invalid direction on line {i+1}: '{robot_dir_str}'"
            )

        if any(c not in ("L", "R", "M") for c in instr_line):
            raise InputParseError(
                f"Invalid instructions on line {i+2}: '{instr_line}'"
            )

        robot_data.append((x, y, robot_dir_str, instr_line))
        i += 2

    return board_coords_len, width, height, robot_data
