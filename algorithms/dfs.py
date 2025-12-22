from maze.cell import Cell
from maze.robot_map import RobotMap

def dfs(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)
    stack = [start]
    visited = set()

    robot_map.set_free(start)

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        robot_map.set_free(current)

        yield current, visited.copy(), robot_map

        if current == goal:
            return
        
        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                stack.append(neighbor)