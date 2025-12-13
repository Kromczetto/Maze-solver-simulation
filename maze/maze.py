from typing import List, Iterable
from maze.cell import Cell

class Maze:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0]) if self.height > 0 else 0

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.height and 0 <= col < self.width

    def is_wall(self, row: int, col: int) -> bool:
        return self.grid[row][col] == 1

    def get_neighbors(self, cell: Cell):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr = cell.row + dr
            nc = cell.col + dc
            if self.in_bounds(nr, nc) and not self.is_wall(nr, nc):
                yield Cell(nr, nc)

    def display(self, start=None, goal=None, path=None):
        path = set(path) if path else set()

        for r in range(self.height):
            line = ""
            for c in range(self.width):
                cell = Cell(r, c)
                if cell == start:
                    line += "S "
                elif cell == goal:
                    line += "G "
                elif cell in path:
                    line += "* "
                elif self.is_wall(r, c):
                    line += "# "
                else:
                    line += ". "
            print(line)
