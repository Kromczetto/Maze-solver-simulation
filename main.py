from maze.maze import Maze
from maze.cell import Cell
from algorithms.wall_follower import wall_follower
from visualization.matplot_view import animate_exploration

def run(explorer):
    steps = []
    try:
        while True:
            steps.append(next(explorer))
    except StopIteration:
        pass
    return steps

def main():
    grid = [
        [0,0,0,1,0,0,0,0,1,0],
        [1,1,0,1,0,1,1,0,1,0],
        [0,0,0,1,0,0,1,0,0,0],
        [0,1,1,1,1,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    maze = Maze(grid)
    start = Cell(0, 0)
    goal = Cell(4, 6)

    explorer = wall_follower(maze, start, goal)
    steps = run(explorer)

    animate_exploration(maze, steps, start, goal)

if __name__ == "__main__":
    main()
