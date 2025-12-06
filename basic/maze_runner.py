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
    
    
    if goal == None:
        goal_index = (len(maze[0]) - 2, len(maze) - 2)
    else:
        goal_index = (2 * goal[0] + 1, 2 * goal[1] + 1)

    #print(goal)
    #print(goal_index)

    movements = explore(start_position, maze, goal)
    print(movements)

    visited = set()
    shortest_path = []
    
    
    while goal not in visited:
        for i, move in enumerate(movements):
            index_at = (move[0], move[1])
            if move[2] == "B":
                start_index = (movements[i-1][0], movements[i-1][1])
                shortest_path.extend(movements[:i+1])
                movements = explore((start_index[0], start_index[1], "N"), maze, goal)
                break
        print(movements)

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