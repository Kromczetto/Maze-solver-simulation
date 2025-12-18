from maze.cell import Cell
from maze.robot_map import RobotMap
from maze.robot_map import CellState
from simulation.robot_sensors import sense

# Kierunki: N, E, S, W
DIRS = [
    (-1, 0),  # N
    (0, 1),   # E
    (1, 0),   # S
    (0, -1),  # W
]

def turn_right(d): return (d + 1) % 4
def turn_left(d): return (d - 1) % 4
def turn_back(d): return (d + 2) % 4


def micromouse_explore(real_maze, start: Cell, goal: Cell):
    robot_map = RobotMap(real_maze.height, real_maze.width)

    current = start
    direction = 1  # start: patrzy na EAST
    visited = {current}

    while True:
        # ===== SENSOR =====
        sensed = sense(real_maze, current)
        robot_map.set_free(current)

        for cell, state in sensed.items():
            if state == "WALL":
                robot_map.set_wall(cell)
            else:
                robot_map.set_free(cell)

        # ===== YIELD (animacja) =====
        yield current, visited.copy(), robot_map

        if current == goal:
            return

        moved = False

        # ===== WALL FOLLOWING (prawa ręka) =====
        for new_dir in [
            turn_right(direction),
            direction,
            turn_left(direction),
            turn_back(direction),
        ]:
            dr, dc = DIRS[new_dir]
            next_cell = Cell(current.row + dr, current.col + dc)

            if not real_maze.in_bounds(next_cell.row, next_cell.col):
                continue

            if real_maze.is_wall(next_cell.row, next_cell.col):
                continue

            # RUCH FIZYCZNY
            direction = new_dir
            current = next_cell
            visited.add(current)
            moved = True
            break

        if not moved:
            return
