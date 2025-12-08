"""Module for finding the shortest path between the runner start and the end goal"""

import argparse

# can only use the explore function to gain information about the maze
from runner import *
from maze import *

def shortest_path(maze: list[list[str]], starting: tuple[int, int] = (0, 0), goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
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
    start_position = (starting[0], starting[1], "N")
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

maze = create_maze(11, 5)
maze = add_horizontal_wall(maze, 0, 1)
maze = add_horizontal_wall(maze, 1, 1)
maze = add_horizontal_wall(maze, 2, 1)
maze = add_vertical_wall(maze, 1, 3)
maze = add_vertical_wall(maze, 2, 3)
maze = add_vertical_wall(maze, 3, 3)
maze = add_horizontal_wall(maze, 3, 4)
maze = add_vertical_wall(maze, 3, 4)
maze = add_vertical_wall(maze, 2, 4)
maze = add_horizontal_wall(maze, 4, 4)
maze = add_horizontal_wall(maze, 5, 4)
maze = add_horizontal_wall(maze, 6, 4)
maze = add_horizontal_wall(maze, 7, 4)
runner = create_runner(0, 0, "N")
maze[2 * get_y(runner) + 1][2 * get_x(runner) + 1] = "^"
output_maze(maze)
print(shortest_path(maze))

def maze_reader(maze_file: str) -> list[list[str]]:
    """
    Docstring for maze_reader
    
    :param maze_file: Description
    :type maze_file: str
    :return: Description
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
    
    # Check top and bottom walls of maze same length - other length errors will be caught when adding walls
    if len(maze_file[0]) != len(maze_file[len(maze_file) - 1]):
        raise ValueError("Content of file does not form proper maze")

    # Check surrounded walls of file enclosed with "#"
    for i in range(len(file_maze[0])):
        if (file_maze[0][i] != "#") or (file_maze[len(file_maze) - 1][i] != "#"):
            raise ValueError("Content of file does not form proper maze")
    
    for i in range(len(file_maze)):
        if (file_maze[i][0] != "#") or (file_maze[i][len(file_maze[0]) - 1]) != "#":
            raise ValueError("Content of file does not form proper maze")

    # Create basic structure of maze (before adding any internal walls)
    maze = create_maze(int((len(file_maze[0]) - 1) / 2), int((len(file_maze) - 1) / 2))

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
                        maze = add_vertical_wall(maze, int((i - 1) / 2), int(j / 2))
                    else:
                        # is a horizontal wall
                        maze = add_horizontal_wall(maze, int((j - 1) / 2), int((i / 2)))
    except Exception:
        raise ValueError("Content of file does not form proper maze")

    return list(reversed(maze))

#output_maze(maze_reader("test-maze-reader.mz"))

"""if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ECS Maze Runner")
    
    parser.add_argument("maze", type=str, help="The name of the maze file, e.g., maze1.mz")
    parser.add_argument("--starting", type=tuple[int, int], help="The starting position, e.g., \"2, 1\"")
    parser.add_argument("--goal", type=tuple[int, int], help="The goal position, e.g., \"4, 5\"")

    args = parser.parse_args()

    maze = maze_reader(args.maze)
    path = shortest_path(maze, args.starting, args.goal)
    print(path)
    """
