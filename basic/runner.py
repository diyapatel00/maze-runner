"""Module for creating and updating the runner, alongside allowin the runner to move and explore the maze."""


def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> tuple[int, int, str]:
    """Return a runner given multiple input values relating to co-ordinates and starting orientation.

    :param x: Starting x-coordinate of the runner, defaults to 0 (int)
    :param y: Starting y-coordinate of the runner, defaults to 0 (int)
    :param orientation: Starting orientation (North, East, South, West) of the runner, defaults to 'N' (str)
    :return: Starting position of the runner (tuple: int, int, str)
    """
    return (x, y, orientation)


def get_x(runner: tuple[int, int, str]) -> int:
    """Return the current x-coordinate of the actual maze list of the runner.

    :param runner: Current position of the runner (tuple: int, int, str)
    :return: Current x-coordinate of the runner (int)
    """
    return 2 * runner[0] + 1


def get_y(runner: tuple[int, int, str]) -> int:
    """Return the current y-coordinate of the actual maze list of the runner.

    :param runner: Current position of the runner (tuple: int, int, str)
    :return: Current y-coordinate of the runner (int)
    """
    return 2 * runner[1] + 1


def get_orientation(runner: tuple[int, int, str]) -> str:
    """Return the current orientation of the runner, either North, East, South, West.

    :param runner: Current position of the runner (tuple: int, int, str)
    :return: Current orientation of the runner, either "N", "E", "S", "W" (str)
    """
    return runner[2]


def turn(runner: tuple[int, int, str], direction: str) -> tuple[int, int, str]:
    """Return the updated runner after 'turning' in a given direction.

    :param runner: Current position of the runner (tuple: int, int, str)
    :param direction: Direction to turn in, "Left" or "Right" (str)
    :return: Runner with updated orientation (tuple: int, int, str)
    """
    left_orientation = {"N": "W", "E": "N", "S": "E", "W": "S"}
    right_orientation = {"N": "E", "E": "S", "S": "W", "W": "N"}

    if direction == "Left":
        return (runner[0], runner[1], left_orientation[runner[2]])
    else:
        return (runner[0], runner[1], right_orientation[runner[2]])


def forward(runner: tuple[int, int, str]) -> tuple[int, int, str]:
    """Return the updated runner after moving forward by 1 index.

    :param runner: Current position of the runner (tuple: int, int, str)
    :return: Updated version of runner, after moving forward (tuple: int, int, str)
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

    :param runner: Current position and orientation of runner (tuple: int, int, str)
    :param maze: Current version of maze (2D list)
    :return: If there are walls around the runner (tuple: bool, bool, bool)
    """
    x = get_x(runner)
    y = get_y(runner)
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
            front_wall == True
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
    """Return a function call to forward(), to return the updated runner after checking if there is a wall in front of runner.

    :param runner: Current position and orientation of runner (tuple: int, int, str)
    :param maze: Current version of maze (2D array)
    :raises: :class:`ValueError`: Wall in front of runner
    :return: Function call to forward()
    """
    if sense_walls(runner, maze)[1]:
        raise ValueError("There is a wall")
    else:
        return forward(runner)


def move(runner: tuple[int, int, str], maze: list[list[str]]) -> tuple[tuple[int, int, str], str]:
    """Return updated runner and sequence of movements made.

    :param runner: Current position and orientation of runner (tuple: int, int, str)
    :param maze: Current version of maze (2D list)
    :return: Updating runner and sequence of movements (tuple: tuple: int, int, str; str)
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

    :param runner: Starting position and orientation of runner (tuple: int, int, str)
    :param maze: Maze for runner to move through (2D list)
    :param goal: Co-ordinates for the runner to 'find', default to None (tuple: int, int)
    """
    movements = []
    found_goal = False

    if goal == None:
        goal_index = (len(maze[0])-2, len(maze)-2)
    else:
        goal_index = (2 * goal[1] + 1, 2 * goal[0] + 1)

    print(goal_index)
    #print((get_y(runner), get_x(runner)))
    
    while not found_goal:
        movement = move(runner, maze)
        runner = movement[0]
        movements.append((runner[0], runner[1], movement[1]))

        # check if goal has been reached
        if (get_x(runner), get_y(runner)) == goal_index:
            found_goal = True

        maze[get_y(runner)][get_x(runner)] = "Y"
        output_maze(maze)
        #print(runner)

    return movements


# testing explore function
from maze import *
maze = create_maze(11, 5)
maze = add_horizontal_wall(maze, 0, 1)
maze = add_horizontal_wall(maze, 1, 1)
maze = add_horizontal_wall(maze, 2, 1)
maze = add_horizontal_wall(maze, 1, 2)
maze = add_vertical_wall(maze, 1, 1)
maze[3][3] = "X"
#print(maze)
#output_maze(maze)
runner = create_runner(0, 0, "N")
maze[get_y(runner)][get_x(runner)] = "^"
output_maze(maze)
#print(sense_walls(runner, maze))
print(explore(runner, maze, goal = (1,1)))
#print(runner)
#new_runner = move(runner, maze)[0]
#print(get_x(new_runner), get_y(new_runner))