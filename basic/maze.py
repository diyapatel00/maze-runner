def create_maze(width: int = 5, length: int = 5):
    """
        add function definition
    """
    maze = [["#"] * width]

    row = ["#"]
    for i in range(1, length-1):
        row.append(".")
    row.append("#")

    for i in range(1,width-1):
        maze.append(row)

    maze.append(["#"] * width)
    return maze

# print(create_maze())

def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    """
        add function definition
    """
    maze[x_coordinate][horizontal_line] = "#"
    return maze

#print(add_horizontal_wall(maze, 1, 1))

def add_vertical_wall(maze, y_coordinate, vertical_line):
    """
        add function definition
    """
    maze[y_coordinate, vertical_line] = "#"
    return maze

def get_dimensions(maze) -> tuple[int, int]:
    """
        add function definition
    """
    maze_width = len(maze[0])
    maze_length = len(maze)
    return (maze_width, maze_length)

def get_walls(maze, x_coordinate: int, y_coordinate: int) -> tuple[bool, bool, bool, bool]:
    """
        add function definition
    """
    n_wall, e_wall, s_wall, w_wall = False

    if maze[x_coordinate][y_coordinate - 1] == "#":
        n_wall = True
    
    if maze[x_coordinate+1][y_coordinate] == "#":
        e_wall = True

    if maze[x_coordinate][y_coordinate-1] == "#":
        s_wall = True

    if maze[x_coordinate-1][y_coordinate] == "#":
        w_wall = True
    
    return (n_wall, e_wall, s_wall, w_wall)