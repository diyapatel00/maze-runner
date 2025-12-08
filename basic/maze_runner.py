"""Module for finding the shortest path between the runner start and the end goal"""

# can only use the explore function to gain information about the maze
from runner import explore


def shortest_path(maze: list[list[str]], starting: tuple[int, int] = None, goal: tuple[int, int] = None) -> list[tuple[int, int, str]]:
    """Return the sequence of runner co-ordinates and movements for the shortest path between given starting position and goal
    
    :param maze: Description
    :type maze: list[list[str]]
    :param starting: Description
    :type starting: tuple[int, int]
    :param goal: Description
    :type goal: tuple[int, int]
    :return: Description
    :rtype: list[tuple[int, int, str]]
    """
    if starting == None:
        start_index = (0, 0)
    else:
        start_index = (2 * starting[0] + 1, 2 * starting[1] + 1)

    start_position = (start_index[0], start_index[1], "N")
    #print(start_position)

    #print(goal)
    #print(goal_index)

    visited = set()
    minimal_path = []
    minimal_path_found = False
    
    #while not minimal_path_found:
        #movements = explore(start_position, maze, goal)
    movements = explore(start_position, maze, goal) 
    for move in movements:
        minimal_path_found = True
        if move[2] == "B":
            print(get_orientation(runner))
            #if runner[2] == ""
            #minimal_path_found = False
            #break
            # if no "B" in movements then for loop stops, minimal path found

    #return explore(start_position, maze, goal)
                


# for testing shortest path
from maze import *
from runner import *
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
maze[7][15] = "X"
runner = create_runner(0, 0, "N")
maze[get_y(runner)][get_x(runner)] = "^"
output_maze(maze)
print(shortest_path(maze, goal = (7, 3)))