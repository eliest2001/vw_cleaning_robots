def parse_input(input_data: str):
    lines = input_data.strip().splitlines()
    width, height = map(int, lines[0])
    robot_data = []
    
    i=1
    while i < len(lines):
        position_line = lines[i].split()
        instr_line = lines[i+1].strip()
        x, y = map(int, position_line[0])
        dir_str =  position_line[1]
        robot_data.append((x, y, dir_str, instr_line))
        i += 2
    
    return width, height, robot_data