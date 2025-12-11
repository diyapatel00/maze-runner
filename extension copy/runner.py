"""Module for creating, updating runner and exploring maze."""

import math


from maze import *


def create_runner(x: int = 0,
                  y: int = 0,
                  orientation: str = "N") -> tuple[int, int, str]:
    """Return a runner given multiple input values with given start position.

    :param x: Starting x-coordinate of runner, defaults to 0
    :type x: int
    :param y: Starting y-coordinate of runner, defaults to 0
    :type y: int
    :param orientation: Start orientation of runner, defaults to 'N'
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
    """Return the current orientation of the runner.

    :param runner: Current position of the runner
    :type runner: tuple[int, int, str]
    :return: Current orientation of the runner, either "N", "E", "S", "W"
    :rtype: str
    """
    return runner[2]


def turn(runner: tuple[int, int, str], direction: str) -> tuple[int, int, str]:
    """Return updated runner after turning in the given direction.

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


def sense_walls(runner: tuple[int, int, str],
                maze: list[list[str]]) -> tuple[bool, bool, bool]:
    """Return whether there are walls around the current runner.

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
    else:  # orientation == "W"
        if maze[y-1][x] == "_" or maze[y-1][x] == "#":
            left_wall = True
        if maze[y][x-1] == "|" or maze[y][x-1] == "#":
            front_wall = True
        if maze[y+1][x] == "_" or maze[y+1][x] == "#":
            right_wall = True
    return (left_wall, front_wall, right_wall)


def go_straight(runner: tuple[int, int, str],
                maze: list[list[str]]) -> tuple[int, int, str]:
    """Return a function call to updated runner after moving forward.

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


def move(runner: tuple[int, int, str],
         maze: list[list[str]]) -> tuple[tuple[int, int, str], str]:
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
        return (forward(turn(turn(runner, "Right"), "Right")), "B")


def explore(runner: tuple[int, int, str],
            maze: list[list[str]],
            goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
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

    if goal is None:
        goal = (int((len(maze[0]) - 2) / 2), int((len(maze) - 2) / 2))

    while not found_goal:
        runner_position = (runner[0], runner[1])
        movement = move(runner, maze)
        movements.append((runner_position[0], runner_position[1], movement[1]))
        runner = movement[0]

        # Check if goal has been reached
        if (get_x(runner), get_y(runner)) == goal:
            found_goal = True

    return movements

def explore_a_star(maze, runner, goal = None):
    output_maze(maze)
    if goal is None:
        goal = (int((len(maze[0]) - 2) / 2), int((len(maze) - 2) / 2))

    adjacent = {(get_x(runner), get_y(runner)): None}  # dict
    total_dist = {(get_x(runner), get_y(runner)): 0}  # dict
    h_add_d = {(get_x(runner), get_y(runner)): 0}

    visit_queue = {goal}
    visited = set()  # set
    count = 0

    movements = []

    while len(visit_queue) > 0:
        print(f"heuristics are: {h_add_d}")
        current = min(h_add_d)
        print(f"current node: {current}")

        x, y = current
        is_walls = get_walls(maze, x, y)

        if current == goal:
            #output_maze(maze)
            print(movements)
            return movements
        
        for i, (nx, ny) in enumerate([(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]):
            print(f"neighbour is: {(nx, ny)}")
            if (nx, ny) not in visited and not is_walls[i] and nx >= 0 and ny >= 0:
                if (nx, ny) not in h_add_d:
                    total_dist[(nx, ny)] = math.inf

                curr_dist = total_dist[current] + 1
                if (nx, ny) not in total_dist or curr_dist < total_dist[(nx, ny)]:
                    next = curr_dist + heuristic((nx, ny), goal)
                    h_add_d[(nx, ny)] = next
                    adjacent[(nx, ny)] = current
                    total_dist[(nx, ny)] = curr_dist
                    move, runner = movement(runner, (x, y), (nx, ny))
                    movements.append(move)
                visit_queue.add((nx, ny))
                visited.add((nx, ny))

            else:
                continue
        visited.add(current)
        h_add_d.pop(current)
        maze[2 * y + 1][2 * x + 1] = count
        print(f"adjacent: {adjacent}")
        count += 1

    return -1


def heuristic(start, end):
    return abs(end[1] - start[1]) + abs(end[0] - start[0])


"""maze = create_maze(3, 3)
maze = add_vertical_wall(maze, 1, 1)
maze = add_vertical_wall(maze, 1, 2)
maze = add_vertical_wall(maze, 0, 2)
output_maze(maze)
print(explore_a_star(maze, (0, 0), (1, 1)))"""


def find_orientation(maze: list[list[str]],
                     start: tuple[int, int] = (0, 0),
                     index: tuple[int, int] = None) -> list[str]:
    """Return list of orientations of runner when moving through the move.

    :param start: Start position of the runner
    :type start: tuple[int, int]
    :param index: End position of the runner, a.k.a. goal
    :type index: tuple[int, int]
    :param maze: Maze for runner to move through
    :type maze: list[list[str]]
    :return: List of orientations of runner when exploring maze
    :rtype: list[str]
    """
    if index is None:
        index = (int(len(maze[0]) - 3) / 2, int(len(maze) - 3) / 2)

    orientations = []
    at_index = False
    position = (start[0], start[1], "N")

    while not at_index:
        movement = move(position, maze)
        position = movement[0]
        orientations.append(position[2])

        if (get_x(position), get_y(position)) == index:
            at_index = True

    return orientations


def actions(runner: tuple[int, int, str], move_orient: str) -> str:
    """Return movement action made to move in given direction.

    :param runner: Current runner before move
    :type runner: tuple[int, int, str]
    :param move_orient: Direction to move in
    :type move_orient: str
    :return: Action taken to move in direction
    :rtype: str
    """
    curr_orient = get_orientation(runner)

    n_moves = {"N": "F", "E": "RF", "S": "B", "W": "LF"}
    e_moves = {"N": "LF", "E": "F", "S": "RF", "W": "B"}
    s_moves = {"N": "B", "E": "LF", "S": "F", "W": "RF"}
    w_moves = {"N": "RF", "E": "B", "S": "LF", "W": "F"}

    if curr_orient == "N":
        return n_moves[move_orient]
    elif curr_orient == "E":
        return e_moves[move_orient]
    elif curr_orient == "S":
        return s_moves[move_orient]
    else:  # curr_orient == "W"
        return w_moves[move_orient]


def movement(runner: tuple[int, int, str],
             start: tuple[int, int],
             end: tuple[int, int]) -> tuple[int, int, str]:
    """Return runner and move made between two points.

    'start' and 'end' are adjacent coordinates

    :param runner: Current runner before movement
    :type runner: tuple[int, int, str]
    :param start: Coordinate to move from
    :type start: tuple[int, int]
    :param end: Coordinate to move to
    :type end: tuple[int, int]
    :return: Move made and updated runner
    :rtype: tuple[int, int, str]
    """
    if end == (start[0], start[1] + 1):  # Moving North
        move = (start[0], start[1], actions(runner, "N"))
        runner = (end[0], end[1], "N")
    elif end == (start[0] + 1, start[1]):  # Moving East
        move = (start[0], start[1], actions(runner, "E"))
        runner = (end[0], end[1], "E")
    elif end == (start[0], start[1] - 1):  # Moving South
        move = (start[0], start[1], actions(runner, "S"))
        runner = (end[0], end[1], "S")
    else:  # Moving West
        move = (start[0], start[1], actions(runner, "W"))
        runner = (end[0], end[1], "W")

    return move, runner
