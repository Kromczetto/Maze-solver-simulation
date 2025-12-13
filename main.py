from maze.maze import Maze
from maze.cell import Cell
from visualization.matplot_view import animate_maze

grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
]

maze = Maze(grid)

path = [
    Cell(0, 0),
    Cell(1, 0),
    Cell(2, 0),
    Cell(2, 1),
    Cell(2, 2),
    Cell(3, 2),
    Cell(3, 3),
]

animate_maze(maze, path)
