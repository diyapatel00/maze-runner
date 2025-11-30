def create_maze(width: int = 5, height: int = 5):
    """
        add function definition
    """
    maze_width = width * 2 + 1
    maze_height = height * 2 + 1

    maze = [["#"] * (maze_width)]

    row = ["#"]
    for i in range(1, maze_width-1):
        row.append(".")
    row.append("#")

    for i in range(1,maze_height-1):
        maze.append(row)

    maze.append(["#"] * maze_width)
    return maze

print(create_maze())

def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    """
        add function definition
    """
    maze[x_coordinate][2 * horizontal_line] = "#"
    return maze

#print(add_horizontal_wall(maze, 1, 1))

def add_vertical_wall(maze, y_coordinate, vertical_line):
    """
        add function definition
    """
    maze[y_coordinate][2 * vertical_line] = "#"
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

    if maze[x_coordinate][y_coordinate-1] == "#":
        n_wall = True
    
    if maze[x_coordinate+1][y_coordinate] == "#":
        e_wall = True

    if maze[x_coordinate][y_coordinate-1] == "#":
        s_wall = True

    if maze[x_coordinate-1][y_coordinate] == "#":
        w_wall = True
    
    return (n_wall, e_wall, s_wall, w_wall)

#maze = create_maze(11, 5)
#assert get_walls(maze, 4, 2) == (False, False, False, False)