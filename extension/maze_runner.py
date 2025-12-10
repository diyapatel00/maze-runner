"""Module for finding the shortest path between the runner start and goal."""

import argparse
import csv

from runner import *
from maze import *


def shortest_path(maze: list[list[str]],
                  starting: tuple[int, int] = None,
                  goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
    """Return the sequence of moves of shortest path between start and goal.

    :param maze: Current version of the maze to find path from
    :type maze: list[list[str]]
    :param starting: Starting position to find shortest path from
    :type starting: tuple[int, int]
    :param goal: Ending position to find shortest path to
    :type goal: tuple[int, int]
    :return: List of movements to get from start to goal in minimal steps
    :rtype: list[tuple[int, int, str]]
    """
    if starting is not None:
        starting = convert_to_tuple(starting)
    else:
        starting = (0, 0)

    if goal is not None:
        goal = convert_to_tuple(goal)
    ## else goal will be converted in explore

    start_position = (starting[0], starting[1], "N")
    minimal_path_found = False

    while not minimal_path_found:
        orientations = find_orientation(maze, starting, goal)
        movements = explore(start_position, maze, goal)
        visited = set()

        for i, move in enumerate(movements):
            minimal_path_found = True
            if move[2] == "B" or (move[0], move[1]) in visited:
                curr_orient = orientations[i]
                if curr_orient == "N":
                    add_horizontal_wall(maze, move[0], move[1] + 1)
                elif curr_orient == "S":
                    add_horizontal_wall(maze, move[0], move[1])
                elif curr_orient == "E":
                    add_vertical_wall(maze, move[1], move[0] + 1)
                else:
                    add_vertical_wall(maze, move[1], move[0])
                minimal_path_found = False
                break

            visited.add((move[0], move[1]))

    return explore(start_position, maze, goal)


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


def actual_shortest_path(maze: list[list[str]], start: tuple[int, int] = None, goal: tuple[int, int] = None) -> list[list[str]]:
    if start is None:
        start = (0, 0)
    else:
        start = convert_to_tuple(start)
    
    if goal is None:
        goal = (int((len(maze[0]) - 2) / 2), int((len(maze) - 2) / 2))
    else:
        goal = convert_to_tuple(goal)
    
    maze[2 * goal[1] + 1][2 * goal[0] + 1] = "X"
    visiting_queue = [start]
    visited = {start}
    adjacent = {}

    (x, y) = visiting_queue.pop()
    maze[2 * y + 1][2 * x + 1] = "@"
    output_maze(maze)
    is_walls = get_walls(maze, x, y)
    print(is_walls)

    if (x, y) == goal:
        return return_actual_shortest_path(adjacent, start, goal)

    for i, (nx, ny) in enumerate([(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]):
        if (nx, ny) not in visited and not is_walls[i] and (nx, ny) != "#":
            visited.add((nx, ny))
            adjacent[(nx, ny)] = (x, y)
            visiting_queue.append((nx, ny))

    return -1

def return_actual_shortest_path(adjacent, start, goal):
    path = [goal]
    position = goal

    while position != start:
        path.append(adjacent[position])
        position = [n for n, c in adjacent.items() if c == position]

    return path.reverse()

    

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

    print(actual_shortest_path(maze, args.starting, args.goal))

    #exploration = explore((start_x, start_y, "N"),
    #                      maze,
    #                      convert_to_tuple(args.goal))
    #path = shortest_path(maze, args.starting, args.goal)

    #output_shortest_path_maze(path, maze)

    """# Storing log of exploration into "exploration.csv"
    with open("exploration.csv", "w") as e:
        exploration_writer = csv.writer(e)
        exploration_writer.writerow(["Step",
                                     "x-coordinate",
                                     "y-coordinate",
                                     "Actions"])
        for step, move in enumerate(exploration):
            exploration_writer.writerow([step + 1, move[0], move[1], move[2]])

    # Storing statistics into "statistics.txt"
    with open("statistics.txt", "w") as s:
        s.write(f"Maze: {args.maze}\n")
        s.write(f"Score: {len(exploration) / 4 + len(path)}\n")
        s.write(f"No. of steps for exploration: {len(exploration)}\n")
        s.write(f"Shortest path: {path}\n")
        s.write(f"Length of shortest path: {len(path)}\n")"""
