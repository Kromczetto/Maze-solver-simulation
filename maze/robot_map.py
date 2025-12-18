from enum import Enum

class CellState(Enum):
    UNKNOWN = 0
    FREE = 1
    WALL = 2
    
class RobotMap:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = [
            [CellState.UNKNOWN for _ in range(width)]
            for _ in range(height)
        ]

    def set_free(self, cell):
        self.map[cell.row][cell.col] = CellState.FREE

    def set_wall(self, cell):
        self.map[cell.row][cell.col] = CellState.WALL

    def is_free(self, cell):
        return self.map[cell.row][cell.col] == CellState.FREE
