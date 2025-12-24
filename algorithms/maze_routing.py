from enum import Enum
from maze.cell import Cell
from maze.robot_map import RobotMap


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def left(self):
        return Direction((self.value - 1) % 4)

    def right(self):
        return Direction((self.value + 1) % 4)

    def back(self):
        return Direction((self.value + 2) % 4)

DIR_MOVE = {
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (1, 0),
    Direction.WEST: (0, -1),
}

def manhattan(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)

def maze_routing(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)

    current = start
    heading = Direction.EAST

    visited_states = set()        
    move_stack = []               

    robot_map.set_free(start)
    visited_states.add((current, heading))
    yield current, set(c for c, _ in visited_states), robot_map

    while True:

        if current == goal:
            return
        
        free_dirs = []

        for d, (dr, dc) in DIR_MOVE.items():
            nr, nc = current.row + dr, current.col + dc
            neighbor = Cell(nr, nc)

            if not maze.in_bounds(nr, nc):
                continue

            if maze.is_wall(nr, nc):
                robot_map.set_wall(neighbor)
            else:
                robot_map.set_free(neighbor)
                free_dirs.append((d, neighbor))

        candidates = []

        for d, cell in free_dirs:
            state = (cell, d)
            if state not in visited_states:
                md = manhattan(cell, goal)
                candidates.append((md, d, cell))

        if candidates:
            candidates.sort(key=lambda x: x[0])
            _, d, cell = candidates[0]

            move_stack.append((current, heading))
            heading = d
            current = cell
            visited_states.add((current, heading))
            yield current, set(c for c, _ in visited_states), robot_map
            continue

        if move_stack:
            current, heading = move_stack.pop()
            yield current, set(c for c, _ in visited_states), robot_map
            continue

        return
