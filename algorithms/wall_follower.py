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

def wall_follower(maze, start, goal, start_dir=Direction.EAST):
    robot_map = RobotMap(maze.height, maze.width)
    current = start
    direction = start_dir
    visited = set()

    robot_map.set_free(current)
    visited.add(current)
    yield current, visited.copy(), robot_map

    while current != goal:
        for d in [direction.left(), direction, direction.right(), direction.back()]:
            dr, dc = DIR_MOVE[d]
            nr, nc = current.row + dr, current.col + dc

            if not maze.in_bounds(nr, nc):
                continue

            next_cell = Cell(nr, nc)

            if maze.is_wall(nr, nc):
                robot_map.set_wall(next_cell)
                continue

            robot_map.set_free(next_cell)
            current = next_cell
            direction = d
            visited.add(current)
            break

        yield current, visited.copy(), robot_map
