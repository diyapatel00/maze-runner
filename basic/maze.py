def create_maze(width: int = 5, height: int = 5) -> list[list[str]]:
    """Return a maze created with given dimensions.

    :param width: The horizontal dimension of the maze (int)
    :param height: The vertical dimension of the maze (int)
    :return: Maze with given dimensions (2D list)
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

def add_horizontal_wall(maze: list[list[str]], x_coordinate: int, horizontal_line: int) -> list[list[str]]:
    """Return updated maze after adding horizontal wall to co-ordinates given

    :param maze: Current version of the maze (2D list)
    :param x_coordinate: Horizontal co-ordinate of where wall is to be placed (int)
    :param horizontal_line: Vertical axis co-ordinate of where wall is to be placed (int)
    :param return: Updated maze with wall added (2D list)
    """
    maze[2 * horizontal_line][2 * x_coordinate + 1] = "_"
    return maze

def add_vertical_wall(maze: list[list[str]], y_coordinate: int, vertical_line: int) -> list[list[str]]:
    """Return updated maze after adding vertical wall to co-ordinates given

    :param maze: Current version of the maze (2D list)
    :param y_coordinate: Vertical co-ordinate of where wall is to be placed (int)
    :param vertical_line: Horizontal axis co-ordinate of where wall is to be placed (int)
    :param return: Updated maze with wall added (2D list) 
    """
    maze[2 * y_coordinate + 1][2 * vertical_line] = "|"
    return maze

def get_dimensions(maze: list[list[str]]) -> tuple[int, int]:
    """Return the dimensions of the maze

    :param maze: Current version of the maze (2D list)
    :param return: Current maze width and current maze length (tuple of int)
    """
    maze_width = (len(maze[0]) - 1) / 2
    maze_length = (len(maze) - 1) / 2
    return maze_width, maze_length

def get_walls(maze: list[list[str]], x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
    """Returns whether there are walls North, East, South, West of the given co-ordinates

    :param maze: Current version of the maze (2D list)
    :param x_coordinate: Horizontal co-ordinate of point to be assessed (int)
    :param y_coordinate: Vertical axis co-ordinate of point to be assessed (int)
    :param return: True or False depending on whether wall is present in each direction (tuple of bool)
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

def output_maze(maze: list[list[str]]) -> None:
    """Prints the maze for better viewing of appearance of walls
    
    :param maze: Current version of the maze (2D list)
    """
    for row in reversed(maze):
        print(row)
