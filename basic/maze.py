"""Module for creating and updating the maze."""


def create_maze(width: int = 5, height: int = 5) -> list[list[str]]:
    """Return a maze created with given dimensions.

    :param width: Horizontal length of the maze
    :type width: int
    :param height: Vertical length of the maze
    :type height: int
    :return: Maze with given dimensions
    :rtype: list[list[str]]
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


def add_horizontal_wall(maze: list[list[str]], x_coordinate: int, horizontal_line: int) -> list[list[str]]:
    """Return updated maze after adding horizontal wall to coordinates given.

    :param maze: Current version of maze
    :type maze: list[list[str]]
    :param x_coordinate: Horizontal coordinate of where wall is to be placed
    :type x_coordinate: int
    :param horizontal_line: Vertical coordinate of where wall is to be placed
    :type horizontal_line: int
    :return: Updated maze with wall added
    :rtype: list[list[str]]
    """
    maze[2 * horizontal_line][2 * x_coordinate + 1] = "_"
    return maze


def add_vertical_wall(maze: list[list[str]], y_coordinate: int, vertical_line: int) -> list[list[str]]:
    """Return updated maze after adding vertical wall to coordinates given.

    :param maze: Current version of the maze
    :type maze: list[list[str]]
    :param y_coordinate: Vertical coordinate where wall is to be placed
    :type y_coordinate: int
    :param vertical_line: Horizontal coordinate where wall is to be placed
    :type vertical_line: int
    :return: Updated maze with wall added
    :rtype: list[list[str]]
    """
    maze[2 * y_coordinate + 1][2 * vertical_line] = "|"
    return maze


def get_dimensions(maze: list[list[str]]) -> tuple[int, int]:
    """Return the dimensions of the maze.

    :param maze: Current version of the maze (2D list: str)
    :return: Current maze width and current maze length (tuple: int, int)
    """
    maze_width = (len(maze[0]) - 1) / 2
    maze_length = (len(maze) - 1) / 2
    return int(maze_width), int(maze_length)


def get_walls(maze: list[list[str]], x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
    """Return whether there are walls around a given coordinate.

    :param maze: Current version of the maze
    :type maze: list[list[str]]
    :param x_coordinate: Horizontal coordinate to be assessed
    :type x_coordinate: int
    :param y_coordinate: Vertical axis coordinate to be assessed
    :type y_coordinate: int
    :return: Tuples with whether wall in either direction
    :rtype: tuple[bool, bool, bool, bool]
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
    """Print the maze for easier viewing of appearance of walls.

    :param maze: Current version of the maze
    :type maze: list[list[str]]
    """
    for row in reversed(maze):
        print(row)
