from maze.cell import Cell
from maze.robot_map import RobotMap

def edge(a, b):
    return frozenset((a, b))


def tremaux(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)

    current = start
    visited_cells = {start}
    stack = [start]  

    edge_marks = {} 

    robot_map.set_free(start)
    yield current, visited_cells.copy(), robot_map

    while stack:
        current = stack[-1]

        if current == goal:
            return

        neighbors = list(maze.get_neighbors(current))

        next_cell = None
        for n in neighbors:
            e = edge(current, n)
            if edge_marks.get(e, 0) == 0:
                next_cell = n
                break

        if next_cell:
            e = edge(current, next_cell)
            edge_marks[e] = 1

            robot_map.set_free(next_cell)
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
