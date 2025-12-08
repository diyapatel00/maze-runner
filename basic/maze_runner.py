"""Module for finding the shortest path between the runner start and the end goal"""

# can only use the explore function to gain information about the maze
from runner import *
from maze import *

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
        starting = (0, 0)
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
    #output_maze(maze)
    count = 0

    while not minimal_path_found:
        print(count)
        orientations = find_orientation(starting, goal, maze)
        movements = explore(start_position, maze, goal)

        for i, move in enumerate(movements):
            minimal_path_found = True
            print(move)
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
                print(count, move)
                break
        #print(count, move)
        count += 1
                
    #output_maze(maze)

            # if no "B" in movements then for loop stops, minimal path found

    return explore(start_position, maze, goal)
                


"""# for testing shortest path
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
maze = add_vertical_wall(maze, 3, 6)
maze = add_horizontal_wall(maze, 5, 3)
maze[7][15] = "X"
runner = create_runner(0, 0, "N")
maze[get_y(runner)][get_x(runner)] = "^"
#output_maze(maze)s
#print(find_orientation((0,0), (7,3), maze))
print(shortest_path(maze, goal = (7, 3)))"""

def test_shortest_path() -> None:
    """A Unit test for :py:func:`~maze_runner.shortest_path`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (0, 1).

    3. Add a vertical wall at (1, 1).

    4. Run short_path function to get the path (with default start and goal).

    5. Check that the result is a valid path, starting from (0,0) and end at
       (10, 4).
    """
    maze = create_maze(11, 5)
    maze = add_horizontal_wall(maze, 0, 1)
    maze = add_vertical_wall(maze, 1, 1)
    path = shortest_path(maze, goal = (10, 4))
    print(path)
    assert path[0] == (0, 0, "RF")
    assert path[-1] == (9, 4, "F")
    prefix = []
    for location in path:
        x, y, a = location
        assert (x, y) not in prefix, f"{location} is repeated"
        prefix.append((x, y))

test_shortest_path()