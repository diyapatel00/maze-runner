"""Module for finding the shortest path between the runner start and goal."""

import argparse
import csv

from runner import *
from maze import *


def maze_reader(maze_file: str) -> list[list[str]]:
    """Return usable maze from given file.

    :param maze_file: File name of maze to be read
    :type maze_file: str
    :return: Maze created from the entered document
    :rtype: list[list[str]]
    """
    file_maze = []
    maze = []

    try:
        with open(maze_file, "r") as f:
            for line in f.readlines():
                file_maze.append(line.strip())
    except Exception:
        raise IOError("Problem reading from input file")

    # Check top and bottom walls of maze same length
    if len(maze_file[0]) != len(maze_file[len(maze_file) - 1]):
        raise ValueError("Content of file does not form proper maze")

    # Check surrounded walls of file enclosed with "#"
    for i in range(len(file_maze[0])):
        if ((file_maze[0][i] != "#") or
           (file_maze[len(file_maze) - 1][i] != "#")):
            raise ValueError("Content of file does not form proper maze")

    for i in range(len(file_maze)):
        if ((file_maze[i][0] != "#") or
           ((file_maze[i][len(file_maze[0]) - 1]) != "#")):
            raise ValueError("Content of file does not form proper maze")

    # Create basic structure of maze (before adding any internal walls)
    maze = create_maze(int((len(file_maze[0]) - 1) / 2),
                       int((len(file_maze) - 1) / 2))

    try:
        # Add walls where '#' are
        for i in range(1, len(file_maze) - 1):
            for j in range(1, len(file_maze[0]) - 1):
                if (i % 2 == 0) and (j % 2 == 0):
                    # Check that intersection has "#"
                    if file_maze[i][j] != "#":
                        raise Exception
                    else:
                        # Can ignore this index if "#" present
                        continue

                # Check if index at is a wall
                if file_maze[i][j] == "#":
                    if (j % 2 == 0) and (i % 2 == 1):
                        # Is a vertical wall
                        maze = add_vertical_wall(maze, int((i - 1) / 2),
                                                 int(j / 2))
                    else:
                        # Is a horizontal wall
                        maze = add_horizontal_wall(maze, int((j - 1) / 2),
                                                   int((i / 2)))
    except Exception:
        raise ValueError("Content of file does not form proper maze")

    return list(reversed(maze))


def convert_to_tuple(values: str = None) -> tuple[int, int]:
    """Return tuple from given string.

    :param values: Values to be converted into tuple form
    :type values: str
    :return: Tuple created from entered values
    :rtype: tuple[int, int]
    """
    split = values.split(",")
    return (int(split[0]), int(split[1]))


def output_shortest_path_maze(path: list[tuple[int, int, str]],
                              maze: list[list[str]]):
    """Return display of maze with shortest path shown.

    Runner represented with "@"

    :param path: Shortest path found
    :param maze: Maze path is found from
    """
    for move in path:
        maze[2 * move[1] + 1][2 * move[0] + 1] = "@"
    return output_maze(maze)


def shortest_path(maze: list[list[str]],
                  start: tuple[int, int],
                  goal: tuple[int, int] = None) -> list[list[str]]:
    """Return the shortest path using BFS.

    Breadth-First Search used to visit all nodes in maze, noting neighbours

    :param maze: Maze for runner to find path in
    :type maze: list[list[str]]
    :param start: Start coordinates of runner
    :type start: tuple[int, int]
    :param goal: Aim of runner
    :type goal: tuple[int, int]
    :return: Shortest path
    :rtype: list[list[str]]
    """
    if goal is None:
        goal = (int((len(maze[0]) - 2) / 2), int((len(maze) - 2) / 2))

    # Create queue to view connections from
    visiting_queue = [start]
    # Set to prevent visiting coordinates multiple times
    visited = {start}
    # Dictionary to store adjacent coordinates as pairs
    adjacent = {}

    # Keep finding connections until goal reached, or queue empty
    while len(visiting_queue) > 0:
        # Visit next coordinate pair in queue
        (x, y) = visiting_queue.pop()
        is_walls = get_walls(maze, x, y)

        if (x, y) == goal:
            return return_actual_shortest_path(adjacent, start, goal)

        # Iterate through 4 neighbours of current coordinates
        for i, (nx, ny) in enumerate([(x, y + 1),
                                      (x + 1, y),
                                      (x, y - 1),
                                      (x - 1, y)]):
            # Check neighbouring node not visited and not blocked by wall
            if (nx, ny) not in visited and not is_walls[i]:
                visited.add((nx, ny))
                adjacent[(nx, ny)] = (x, y)
                visiting_queue.append((nx, ny))

    # Return -1 if program fails to find goal
    return -1


def return_actual_shortest_path(adjacent: dict,
                                start: tuple[int, int],
                                maze,
                                goal: tuple[int, int]) -> list[tuple[int,
                                                                     int,
                                                                     str]]:
    """Return the shortest path from start to goal.

    :param adjacent: All adjacent coordinates
    :type adjacent: dict
    :param start: Start position of runner
    :type start: tuple[int, int]
    :param goal: Goal for runner
    :type goal: tuple[int, int]
    :return: List of movements made along path
    :rtype: list[tuple[int, int, str]]
    """
    if goal is None:
        goal = (int((len(maze[0]) - 2) / 2), int((len(maze) - 2) / 2))

    # Start from goal and work backwards to find start
    path = [goal]
    position = goal
    runner = (start[0], start[1], "N")

    while position != start:
        path.append(adjacent[position])
        position = adjacent[position]

    # Reverse path found, to find from start to goal
    shortest_path = list(reversed(path))
    movements = []

    # Add movements to path, e.g. "LF"
    for i in range(len(shortest_path) - 1):
        move, runner = movement(runner, shortest_path[i], shortest_path[i + 1])
        movements.append(move)

    return movements


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ECS Maze Runner")

    parser.add_argument("maze",
                        type=str,
                        help="The name of the maze file, e.g., maze1.mz")
    parser.add_argument("--starting",
                        type=str,
                        help="The starting position, e.g., \"2, 1\"")
    parser.add_argument("--goal",
                        type=str,
                        help="The goal position, e.g., \"4, 5\"")

    args = parser.parse_args()

    maze = maze_reader(args.maze)

    if args.starting is not None:
        starting = convert_to_tuple(args.starting)
    else:
        starting = (0, 0)

    if args.goal is not None:
        goal = convert_to_tuple(args.goal)
    else:
        goal = args.goal

    exploration, adjacent = explore(maze,
                                    (starting[0], starting[1], "N"),
                                    goal)
    path = return_actual_shortest_path(adjacent, starting, maze, goal)

    output_shortest_path_maze(path, maze)

    explore_moves = []
    runner = (starting[0], starting[1], "N")

    # Storing log of exploration into "exploration.csv"
    with open("exploration.csv", "w") as e:
        exploration_writer = csv.writer(e)
        exploration_writer.writerow(["Step",
                                     "x-coordinate",
                                     "y-coordinate",
                                     "Actions"])
        runner = (starting[0], starting[1], "N")
        for step, move_made in enumerate(exploration):
            exploration_writer.writerow([step + 1,
                                         move_made[0],
                                         move_made[1],
                                         move_made[2]])

    # Storing statistics into "statistics.txt"
    with open("statistics.txt", "w") as s:
        s.write(f"Maze: {args.maze}\n")
        s.write(f"Score: {len(exploration) / 4 + len(path)}\n")
        s.write(f"No. of steps for exploration: {len(exploration)}\n")
        s.write(f"Shortest path: {path}\n")
        s.write(f"Length of shortest path: {len(path)}\n")
