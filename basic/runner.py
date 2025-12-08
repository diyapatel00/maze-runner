"""Module for creating and updating the runner, alongside allowin the runner to move and explore the maze."""
from maze import * # REMOVE AFTER TESTING

def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> tuple[int, int, str]:
    """Return a runner given multiple input values relating to co-ordinates and starting orientation.
    
    :param x: Starting x-coordinate of the runner, defaults to 0
    :type x: int
    :param y: Starting y-coordinate of the runner, defaults to 0
    :type y: int
    :param orientation: DescripStarting orientation (North, East, South, West) of the runner, defaults to 'N'tion
    :type orientation: str
    :return: Starting position of the runner
    :rtype: tuple[int, int, str]
    """
    return (x, y, orientation)


def get_x(runner: tuple[int, int, str]) -> int:
    """Return the current x-coordinate of the actual maze list of the runner.
    
    :param runner: DescripCurrent position of the runnertion
    :type runner: tuple[int, int, str]
    :return: Current x-coordinate of the runner
    :rtype: int
    """
    return runner[0]


def get_y(runner: tuple[int, int, str]) -> int:
    """Return the current y-coordinate of the actual maze list of the runner.
    
    :param runner: Current position of the runner
    :type runner: tuple[int, int, str]
    :return: Current y-coordinate of the runner
    :rtype: int
    """
    return runner[1]


def get_orientation(runner: tuple[int, int, str]) -> str:
    """Return the current orientation of the runner, either North, East, South, West.
    
    :param runner: Current position of the runner
    :type runner: tuple[int, int, str]
    :return: Current orientation of the runner, either "N", "E", "S", "W"
    :rtype: str
    """
    return runner[2]


def turn(runner: tuple[int, int, str], direction: str) -> tuple[int, int, str]:
    """Return updated runner after turning in the given direction
    
    :param runner: Current position and orientation of the runner
    :type runner: tuple[int, int, str]
    :param direction: Direction for runner to turn in
    :type direction: str
    :return: Updated runner after turning
    :rtype: tuple[int, int, str]
    """
    left_orientation = {"N": "W", "E": "N", "S": "E", "W": "S"}
    right_orientation = {"N": "E", "E": "S", "S": "W", "W": "N"}

    if direction == "Left":
        return (runner[0], runner[1], left_orientation[runner[2]])
    else:
        return (runner[0], runner[1], right_orientation[runner[2]])


def forward(runner: tuple[int, int, str]) -> tuple[int, int, str]:
    """Return the updated runner after moving forward by 1 index.
    
    :param runner: Current position of the runner
    :type runner: tuple[int, int, str]
    :return: Updated version of runner, after moving forward
    :rtype: tuple[int, int, str]
    """
    if runner[2] == "N":
        return (runner[0], runner[1] + 1, runner[2])
    elif runner[2] == "E":
        return (runner[0] + 1, runner[1], runner[2])
    elif runner[2] == "S":
        return (runner[0], runner[1] - 1, runner[2])
    else:
        return (runner[0] - 1, runner[1], runner[2])


def sense_walls(runner: tuple[int, int, str], maze: list[list[str]]) -> tuple[bool, bool, bool]:
    """Return whether there are walls to the left, right and in front of the current runner.
    
    :param runner: Current position and orientation of runner
    :type runner: tuple[int, int, str]
    :param maze: Current version of maze
    :type maze: list[list[str]]
    :return: If there are walls around the runner 
    :rtype: tuple[bool, bool, bool]
    """
    x = 2 * get_x(runner) + 1
    y = 2 * get_y(runner) + 1
    orientation = get_orientation(runner)
    left_wall, front_wall, right_wall = False, False, False

    if orientation == "N":
        if maze[y][x-1] == "|" or maze[y][x-1] == "#":
            left_wall = True
        if maze[y+1][x] == "_" or maze[y+1][x] == "#":
            front_wall = True
        if maze[y][x+1] == "|" or maze[y][x+1] == "#":
            right_wall = True
    elif orientation == "E":
        if maze[y+1][x] == "_" or maze[y+1][x] == "#":
            left_wall = True
        if maze[y][x+1] == "|" or maze[y][x+1] == "#":
            front_wall = True
        if maze[y-1][x] == "_" or maze[y-1][x] == "#":
            right_wall = True
    elif orientation == "S":
        if maze[y][x+1] == "|" or maze[y][x+1] == "#":
            left_wall = True
        if maze[y-1][x] == "_" or maze[y-1][x] == "#":
            front_wall = True
        if maze[y][x-1] == "|" or maze[y][x-1] == "#":
            right_wall = True
    else: # orientation == "W"
        if maze[y-1][x] == "_" or maze[y-1][x] == "#":
            left_wall = True
        if maze[y][x-1] == "|" or maze[y][x-1] == "#":
            front_wall = True
        if maze[y+1][x] == "_" or maze[y+1][x] == "#":
            right_wall = True
    return (left_wall, front_wall, right_wall)

def go_straight(runner: tuple[int, int, str], maze: list[list[str]]) -> tuple[int, int, str]:
    """Return a function call to forward() to return updated runner, to return the updated runner after checking if there is a wall in front of runner.
    
    :param runner: Current position and orientation of runner 
    :type runner: tuple[int, int, str]
    :param maze: Current version of maze
    :type maze: list[list[str]]
    :raises: :class: `ValueError`: Wall in front of runner
    :return: Updating runner after moving straight, from function forward()
    :rtype: tuple[int, int, str]
    """
    if sense_walls(runner, maze)[1]:
        raise ValueError("There is a wall")
    else:
        return forward(runner)


def move(runner: tuple[int, int, str], maze: list[list[str]]) -> tuple[tuple[int, int, str], str]:
    """Return updated runner and sequence of movements made.
    
    :param runner: Current position and orientation of runner
    :type runner: tuple[int, int, str]
    :param maze: Current version of maze
    :type maze: list[list[str]]
    :return: Updating runner and sequence of movements
    :rtype: tuple[tuple[int, int, str], str]
    """
    walls = sense_walls(runner, maze)
    
    if not walls[0]:
        return (forward(turn(runner, "Left")), "LF")
    elif not walls[1]:
        return (forward(runner), "F")
    elif not walls[2]:
        return (forward(turn(runner, "Right")), "RF")
    else:
        return (turn(turn(runner, "Right"), "Right"), "B")


def explore(runner: tuple[int, int, str], maze: list[list[str]], goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
    """Return sequence of movements made for the runner to reach goal given.
    
    :param runner: Starting position and orientation of runner
    :type runner: tuple[int, int, str]
    :param maze: Maze for runner to move through
    :type maze: list[list[str]]
    :param goal: Co-ordinates for the runner to 'find', default to None
    :type goal: tuple[int, int]
    :return: List of movements made from start of runner to reaching goal
    :rtype: list[tuple[int, int, str]]
    """
    movements = []
    found_goal = False

    #print(goal_index)
    #print((get_y(runner), get_x(runner)))
    
    while not found_goal:
        runner_position = (runner[0], runner[1])
        movement = move(runner, maze)
        #print(movement)
        movements.append((runner_position[0], runner_position[1], movement[1]))
        runner = movement[0]

        # check if goal has been reached
        if (get_x(runner), get_y(runner)) == goal:
            found_goal = True

        #maze[get_y(runner)][get_x(runner)] = "Y"
        
        #print(runner)

    return movements


def find_orientation(start: tuple[int, int], index: tuple[int, int], maze: list[list[str]]) -> list[str]:
    """Return list of orientations of runner when moving through the move.
    
    :param start: Start position of the runner
    :type start: tuple[int, int]
    :param index: End position of the runner, a.k.a. goal
    :type index: tuple[int, int]
    :param maze: Maze for runner to move through
    :type maze: list[list[str]]
    :return: List of orientations at each position of the runner when exploring maze
    :rtype: list[str]
    """
    orientations = []
    at_index = False
    position = (start[0], start[1], "N")

    while not at_index:
        movement = move(position, maze)
        position = movement[0]
        orientations.append(position[2])
        maze[2 * position[1] + 1][2 * position[0] + 1] = "Y"

        if (get_x(position), get_y(position)) == index:
            at_index = True


    return orientations
