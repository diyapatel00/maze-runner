"""Module for finding the shortest path between the runner start and the end goal"""

# can only use the explore function to gain information about the maze
from runner import *
from maze import *

def shortest_path(maze: list[list[str]], starting: tuple[int, int] = None, goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
    """Return the sequence of runner co-ordinates and movements for the shortest path between given starting position and goal
    
    :param maze: Current version of the maze to find path from
    :type maze: list[list[str]]
    :param starting: Starting position to find shortest path from
    :type starting: tuple[int, int]
    :param goal: Ending position to find shortest path to
    :type goal: tuple[int, int]
    :return: List of movements to get from start to goal in minimal steps
    :rtype: list[tuple[int, int, str]]
    """
    if starting == None:
        starting = (0, 0)
        start_index = (0, 0)
    else:
        start_index = (2 * starting[0] + 1, 2 * starting[1] + 1)

    start_position = (start_index[0], start_index[1], "N")
    minimal_path_found = False

    count = 0
    
    while not minimal_path_found:
        orientations = find_orientation(starting, goal, maze)
        movements = explore(start_position, maze, goal)

        #print(movements)
        #print(f"while Iteration: {count + 1}")

        for i, move in enumerate(movements):
            minimal_path_found = True
            if move[2] == "B":
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

    return explore(start_position, maze, goal)
                

def maze_reader(maze_file: str) -> list[list[str]]:
    file_maze = []
    maze = []

    try:
        with open(maze_file, "r") as f:
            for line in f.readlines():
                file_maze.append(line.strip())
    except Exception:
        raise IOError("Problem reading from input file")
    
    # Check external walls fully enclose maze
    if len(maze_file[0]) != len(maze_file[len(maze_file) - 1]):
        raise ValueError("Content of file does not form proper maze")


    # Create basic structure of maze (before adding any internal walls)
    maze = [["."] * len(file_maze[0]) for _ in range(len(file_maze))]
    for i in range(len(file_maze[0])):
        maze[0][i] = "#"
        maze[len(file_maze) - 1][i] = "#"

    for i in range(len(file_maze)):
        maze[i][0] = "#"
        maze[i][len(file_maze[0]) - 1] = "#"

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
                    
                # check if index at is a wall
                if file_maze[i][j] == "#":
                    if (j % 2 == 0) and (i % 2 == 1):
                        # is a vertical wall
                        maze[i][j] = "|"
                    else:
                        # is a horizontal wall
                        maze[i][j] = "_"
    except Exception:
        raise ValueError("Content of file does not form proper maze")

    return list(reversed(maze))

output_maze(maze_reader("test-maze-reader.mz"))

