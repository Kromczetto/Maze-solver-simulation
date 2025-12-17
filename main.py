from maze.maze import Maze
from maze.cell import Cell
from algorithms.micromouse import micromouse_explore
from algorithms.astar_memory import astar_on_memory
from algorithms.dijkstra import dijkstra
from visualization.matplot_view import animate_exploration
from visualization.fast_run_view import animate_fast_run


def run(explorer):
    steps = []
    try:
        while True:
            steps.append(next(explorer))
    except StopIteration as e:
        robot_map = e.value
    return steps, robot_map


def main():
    grid = [
        [0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0],
        [1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1],
        [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
        [1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0],
        [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
        [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0],
        [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],
        [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
    ]

    maze = Maze(grid)
    start = Cell(0, 0)
    goal = Cell(4, 6)

    # FAZA 1 – EKSPLORACJA
    steps, robot_map = run(micromouse_explore(maze, start, goal))
    animate_exploration(maze, steps, start, goal)

    # FAZA 2 – PLANOWANIE
    path_astar = astar_on_memory(robot_map, start, goal)
    path_dijkstra = dijkstra(robot_map, start, goal)

    # FAZA 3 – FAST RUN (2 OKNA)
    animate_fast_run(maze, path_astar, "FAST RUN – A*")
    animate_fast_run(maze, path_dijkstra, "FAST RUN – DIJKSTRA")


if __name__ == "__main__":
    main()
