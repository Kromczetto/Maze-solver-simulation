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


DIR_MOVE = {
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (1, 0),
    Direction.WEST: (0, -1),
}


def manhattan(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def can_move(maze, cell, direction):
    dr, dc = DIR_MOVE[direction]
    nr, nc = cell.row + dr, cell.col + dc
    return maze.in_bounds(nr, nc) and not maze.is_wall(nr, nc)


def move(cell, direction):
    dr, dc = DIR_MOVE[direction]
    return Cell(cell.row + dr, cell.col + dc)


def maze_routing(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)

    current = start
    heading = Direction.EAST
    visited = {start}

    md_best = manhattan(start, goal)

    robot_map.set_free(start)
    yield current, visited.copy(), robot_map

    while current != goal:
        moved = False

        for d in Direction:
            if can_move(maze, current, d):
                next_cell = move(current, d)
                if manhattan(next_cell, goal) < md_best:
                    heading = d
                    current = next_cell
                    md_best = manhattan(current, goal)
                    visited.add(current)
                    robot_map.set_free(current)
                    yield current, visited.copy(), robot_map
                    moved = True
                    break

        if moved:
            continue

        md_best = manhattan(current, goal)

        for d in (heading.left(), heading.right()):
            if can_move(maze, current, d):
                heading = d
                current = move(current, heading)
                visited.add(current)
                robot_map.set_free(current)
                yield current, visited.copy(), robot_map
                break

        while manhattan(current, goal) != md_best:
            for d in (heading.right(), heading, heading.left()):
                if can_move(maze, current, d):
                    heading = d
                    current = move(current, heading)
                    visited.add(current)
                    robot_map.set_free(current)
                    yield current, visited.copy(), robot_map
                    break
