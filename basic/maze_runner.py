"""Module for finding the shortest path between the runner start and the end goal"""

# can only use the explore function to gain information about the maze
from runner import explore


def shortest_path(maze: list[list[str]], starting: tuple[int, int] = None, goal: tuple[int][int] = None) -> list[tuple[int, int, str]]:
    pass