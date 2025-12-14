from typing import List
from maze.cell import Cell

CELL_LENGTH_M = 0.30
WALL_THICKNESS_M = 0.005
ROBOT_SPEED_MPS = 1.0

def estimate_travel_time(path: List[Cell]) -> float:
    if len(path) < 2:
        return 0.0

    steps = len(path) - 1
    distance = steps * CELL_LENGTH_M
    return distance / ROBOT_SPEED_MPS
