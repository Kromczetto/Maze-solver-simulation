from maze.cell import Cell
from maze.robot_map import RobotMap
DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def dfs(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)

    visited = set()
    stack = [start]

    visited.add(start)
    robot_map.set_free(start)

    yield start, visited.copy(), robot_map

    while stack:
        current = stack[-1]

        if current == goal:
            return

        neighbors_free = []

        for dr, dc in DIRECTIONS:
            nr, nc = current.row + dr, current.col + dc
            neighbor = Cell(nr, nc)

            if not maze.in_bounds(nr, nc):
                continue

            if maze.is_wall(nr, nc):
                robot_map.set_wall(neighbor)
            else:
                robot_map.set_free(neighbor)
                neighbors_free.append(neighbor)

        next_cell = None
        for n in neighbors_free:
            if n not in visited:
                next_cell = n
                break

        if next_cell:
            visited.add(next_cell)
            stack.append(next_cell)
            yield next_cell, visited.copy(), robot_map
        else:
            stack.pop()
            if stack:
                yield stack[-1], visited.copy(), robot_map
