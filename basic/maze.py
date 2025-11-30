def create_maze(width: int = 5, height: int = 5):
    """
        add function definition
    """
    maze_width = width * 2 + 1
    maze_height = height * 2 + 1

    maze = [["."] * maze_width for _ in range(maze_height)]

    for i in range(maze_width):
        maze[0][i] = "#"
        maze[maze_height - 1][i] = "#"
    
    for i in range(maze_height):
        maze[i][0] = "#"
        maze[i][maze_width - 1] = "#"

    return maze

#print(create_maze())

def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    """
        add function definition
    """
    maze[2 * horizontal_line][2 * x_coordinate + 1] = "_"
    return maze

def add_vertical_wall(maze, y_coordinate, vertical_line):
    """
        add function definition
    """
    maze[2 * y_coordinate + 1][2 * vertical_line] = "|"
    return maze

def get_dimensions(maze) -> tuple[int, int]:
    """
        add function definition
    """
    maze_width = (len(maze[0]) - 1) / 2
    maze_length = (len(maze) - 1) / 2
    return maze_width, maze_length

def get_walls(maze: list[list[str]], x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
    """
        add function definition
    """
    n_wall, e_wall, s_wall, w_wall = False, False, False, False

    # convert given coordinates to array indices
    array_x = x_coordinate * 2 + 1
    array_y = y_coordinate * 2 + 1

    if maze[array_y + 1][array_x] == "_":
        n_wall = True
    
    if maze[array_y][array_x + 1] == "|":
        e_wall = True

    if maze[array_y - 1][array_x] == "_":
        s_wall = True

    if maze[array_y][array_x - 1] == "|":
        w_wall = True
    
    return (n_wall, e_wall, s_wall, w_wall)

def output_maze(maze):
    """
    to print the maze for testing purposes, since indexing is backwards in the vertical direction
    
    :param maze: Description
    """
    for row in reversed(maze):
        print(row)
