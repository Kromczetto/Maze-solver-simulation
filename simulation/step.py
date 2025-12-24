from dataclasses import dataclass
from maze.cell import Cell
from maze.robot_map import RobotMap

@dataclass
class Step:
    cell: Cell
    visited: set
    robot_map: RobotMap
    step_index: int
    time_sec: float
