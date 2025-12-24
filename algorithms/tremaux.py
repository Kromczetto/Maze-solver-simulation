from maze.cell import Cell
from maze.robot_map import RobotMap

DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def edge(a, b):
    return frozenset((a, b))


def tremaux(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)

    stack = [start]
    visited_cells = {start}
    edge_marks = {} 

    robot_map.set_free(start)
    yield start, visited_cells.copy(), robot_map

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
            e = edge(current, n)
            if edge_marks.get(e, 0) == 0:
                next_cell = n
                break

        if next_cell:
            e = edge(current, next_cell)
            edge_marks[e] = 1

            visited_cells.add(next_cell)
            stack.append(next_cell)
            yield next_cell, visited_cells.copy(), robot_map
        else:
            stack.pop()
            if not stack:
                return

            back = stack[-1]
            e = edge(current, back)
            edge_marks[e] = 2
            yield back, visited_cells.copy(), robot_map
