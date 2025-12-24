from dataclasses import dataclass
from maze.cell import Cell

@dataclass
class AlgorithmResult:
    name: str
    steps: int
    time: float
    path: list[Cell]
