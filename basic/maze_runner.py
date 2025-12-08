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
                

