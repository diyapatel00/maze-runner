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

    if direction == "Left":
        return (runner[0], runner[1], left_orientation[runner[2]])
    else:
        return (runner[0], runner[1], right_orientation[runner[2]])

def forward(runner: tuple[int, int, str]) -> tuple[int, int, str]:
    """
        need to write function definition
    """
    if runner[2] == "N":
        return (runner[0] + 1, runner[1], runner[2])
    elif runner[2] == "E":
        return (runner[0], runner[1] + 1, runner[2])
    elif runner[2] == "S":
        return (runner[0], runner[1] - 1, runner[2])
    else:
        return (runner[0] - 1, runner[1], runner[2])

def sense_walls(runner, maze) -> tuple[bool, bool, bool]:
    """
        need to write function definition
    """
    x = 2 * get_x(runner) + 1
    y = 2 * get_y(runner) + 1
    orientation = get_orientation(runner)
    left_wall, front_wall, right_wall = False, False, False

    if orientation == "N":
        if maze[y][x-1] == "|":
            left_wall = True
        if maze[y+1][x] == "_":
            front_wall = True
        if maze[y][x+1] == "|":
            right_wall = True
    elif orientation == "E":
        if maze[y+1][x] == "_":
            left_wall = True
        if maze[y][x+1] == "|":
            front_wall = True
        if maze[y-1][x] == "_":
            right_wall = True
    elif orientation == "S":
        if maze[y][x+1] == "|":
            left_wall = True
        if maze[y-1][x] == "_":
            front_wall == True
        if maze[y][x-1] == "|":
            right_wall = True
    else: # orientation == "W"
        if maze[y-1][x] == "_":
            left_wall = True
        if maze[y][x-1] == "|":
            front_wall = True
        if maze[y+1][x] == "_":
            right_wall = True
    return (left_wall, front_wall, right_wall)
 
def go_straight(runner, maze):
    """
        need to write function definition
    """
    if sense_walls(runner, maze)[1]:
        raise ValueError("There is a wall")
    else:
        return forward(runner)

def move(runner, maze) -> tuple[tuple[int, int, str], list[str]]:
    """
        need to write function definition
    """
    walls = sense_walls(runner, maze)
    
    if runner[2] == "N":
        if not walls[0]:
            runner[0] -= 1
            return (runner, "LF")
        elif not walls[1]:
            runner[1] += 1
            return (runner, "F")
        elif not walls[2]:
            runner[0] += 1
            return (runner, "RF")
        else:
            runner [1] -= 1
            return (runner, "B")
    elif runner[2] == "E":
        if not walls[0]:
            runner[1] += 1
            return (runner, "LF")
        elif not walls[1]:
            runner[0] += 1
            return (runner, "F")
        elif not walls[2]:
            runner[1] -= 1
            return (runner, "RF")
        else:
            runner[0] -= 1
            return (runner, "B")
    elif runner[2] == "S":
        if not walls[0]:
            runner[0] += 1
            return (runner, "LF")
        elif not walls[1]:
            runner[1] -= 1
            return (runner, "F")
        elif not walls[2]:
            runner[0] -= 1
            return (runner, "RF")
        else:
            runner[1] += 1
            return (runner, "B")
    else:
        if not walls[0]:
            runner[1] -= 1
            return (runner, "LF")
        elif not walls[1]:
            runner[0] -= 1
            return (runner, "F")
        elif not walls[2]:
            runner[1] += 1
            return (runner, "RF")
        else:
            runner[0] += 1
            return (runner, "B")

def explore(runner, maze, goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
    """
        need to write function definition
    """
    movements = []
    if goal == None:
        goal = (len(maze)-1, len(maze[0])-1)
    pass