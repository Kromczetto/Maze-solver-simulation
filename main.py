from maze.maze import Maze
from maze.cell import Cell
from algorithms.bfs import bfs_explore
from algorithms.dfs import dfs_explore
from algorithms.astar import astar_explore
from visualization.matplot_view import animate_exploration, animate_drive
from simulation.time_model import estimate_travel_time
from config import SimulationConfig


def show_menu() -> SimulationConfig:
    print("=== MAZE SOLVER SIMULATION ===")
    print("Wybierz algorytm:")
    print("1 - BFS")
    print("2 - DFS")
    print("3 - A*")

    while True:
        choice = input("Twój wybór [1/3]: ").strip()
        if choice in ("1", "2", "3"):
            break
        print("Niepoprawny wybór.")

    wall_thickness = float(input("Grubość ścian [mm]: "))

    algorithm = {"1": "bfs", "2": "dfs", "3": "astar"}[choice]

    return SimulationConfig(
        algorithm=algorithm,
        wall_thickness=wall_thickness
    )


def run_explorer(explorer):
    """Obsługuje generator eksploracyjny i wyciąga path"""
    steps = []
    path = []

    try:
        while True:
            steps.append(next(explorer))
    except StopIteration as e:
        path = e.value

    return steps, path


def main():
    config = show_menu()

    grid = [
        [0,0,0,1,0,0,0],
        [1,1,0,1,0,1,0],
        [0,0,0,0,0,1,0],
        [0,1,0,1,0,1,0],
        [0,0,0,0,0,1,0],
    ]

    maze = Maze(grid)
    start = Cell(0, 0)
    goal = Cell(4, 6)

    if config.algorithm == "bfs":
        steps, _ = run_explorer(bfs_explore(maze, start, goal))
        animate_exploration(maze, steps, start, goal)

    elif config.algorithm == "dfs":
        steps, _ = run_explorer(dfs_explore(maze, start, goal))
        animate_exploration(maze, steps, start, goal)

    elif config.algorithm == "astar":
        steps, path = run_explorer(astar_explore(maze, start, goal))

        # 1. myślenie robota
        animate_exploration(maze, steps, start, goal)

        # 2. fizyczna jazda
        # animate_drive(maze, path, start, goal)

        print(f"Szacowany czas przejazdu: {estimate_travel_time(path):.2f} s")


if __name__ == "__main__":
    main()
