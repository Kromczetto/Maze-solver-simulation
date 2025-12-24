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

    visited_cells = set()
    visited_states = set()   

    max_steps = maze.height * maze.width * 4
    steps = 0

    robot_map.set_free(current)
    visited_cells.add(current)
    visited_states.add((current, direction))

    yield current, visited_cells.copy(), robot_map

    while current != goal:
        steps += 1
        if steps > max_steps:
            print("[WallFollower] Przerwano: wykryto pętlę lub brak wyjścia")
            return

        moved = False

        for d in [direction.left(), direction, direction.right(), direction.back()]:
            dr, dc = DIR_MOVE[d]
            nr, nc = current.row + dr, current.col + dc

            if not maze.in_bounds(nr, nc):
                continue

            next_cell = Cell(nr, nc)

            if maze.is_wall(nr, nc):
                robot_map.set_wall(next_cell)
                continue

            next_state = (next_cell, d)
            if next_state in visited_states:
                continue

            robot_map.set_free(next_cell)
            current = next_cell
            direction = d

            visited_cells.add(current)
            visited_states.add((current, direction))

            moved = True
            break

        if not moved:
            print("[WallFollower] Brak możliwego ruchu — zakończenie")
            return

        yield current, visited_cells.copy(), robot_map
