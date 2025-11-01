def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> tuple[int, int, str]:
    """
        need to write function definition
    """
    runner = (x, y, orientation)
    return runner

def get_x(runner: tuple[int, int, str]) -> int:
    """
        need to write function definition
    """
    return runner[0]

def get_y(runner: tuple[int, int, str]) -> int:
    """
        need to write function definition
    """
    return runner[1]

def get_orientation(runner: tuple[int, int, str]) -> str:
    """
        need to write function definition
    """
    return runner[2]

def turn(runner: tuple[int, int, str], direction: str) -> tuple[int, int, str]:
    """
        need to write function definition
    """
    left_orientation = {"N": "W", "E": "N", "S": "E", "W": "S"}
    right_orientation = {"N": "E", "E": "S", "S": "W", "W": "N"}

    while True: 
        if direction == "Left":
            runner[2] = left_orientation[runner[2]]
            return runner
        else:
            runner[2] = right_orientation[runner[2]]

def forward(runner: tuple[int, int, str]) -> tuple[int, int, str]:
    """
        need to write function definition
    """
    if runner[2] == "N":
        runner[0] += 1
    elif runner[2] == "E":
        runner[1] += 1
    elif runner[2] == "S":
        runner[0] -= 1
    else:
        runner[2] -= 1

def sense_walls(runner, maze) -> tuple[bool, bool, bool]:
    """
        need to write function definition
    """
    x = runner[0]
    y = runner[1]
    orientation = runner[2]
    left_wall, front_wall, right_wall = False

    if orientation == "N":
        if maze[x-1][y] == "#":
            left_wall = True
        if maze[x][y+1] == "#":
            front_wall = True
        if maze[x+1][y] == "#":
            right_wall = True
    elif orientation == "E":
        if maze[x][y+1] == "#":
            left_wall = True
        if maze[x+1][y] == "#":
            front_wall = True
        if maze[x][y-1] == "#":
            right_wall = True
    elif orientation == "S":
        if maze[x+1][y] == "#":
            left_wall = True
        if maze[x][y-1] == "#":
            front_wall == True
        if maze[x-1][y] == "#":
            right_wall = True
    else: # orientation == "W"
        if maze[x][y-1] == "#":
            left_wall = True
        if maze[x-1][y] == "#":
            front_wall = True
        if maze[x][y+1] == "#":
            right_wall = True
    return (left_wall, front_wall, right_wall)

def go_straight(runner, maze):
    """
        need to write function definition
    """
    pass

def move(runner, maze):
    """
        need to write function definition
    """
    pass

def explore(runner, maze, goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
    """
        need to write function definition
    """
    pass