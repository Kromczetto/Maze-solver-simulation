from maze.maze import Maze
from maze.cell import Cell
from algorithms.bfs import bfs
from algorithms.dfs import dfs_explore
from visualization.matplot_view import animate_maze, animate_exploration
from config import SimulationConfig

def show_menu() -> SimulationConfig:
    print("=== MAZE SOLVER SIMULATION ===")
    print("Wybierz algorytm:")
    print("1 - BFS (planowanie, bez cofania)")
    print("2 - DFS (eksploracja z cofaniem)")

    while True:
        choice = input("Twój wybór [1/2]: ").strip()
        if choice in ("1", "2"):
            break
        print("Niepoprawny wybór.")

    print("\nPodaj grubość ścian (mm) – parametr eksperymentalny")
    while True:
        try:
            wall_thickness = float(input("Grubość ścian [np. 5]: "))
            break
        except ValueError:
            print("Podaj liczbę.")

    algorithm = "bfs" if choice == "1" else "dfs"

    return SimulationConfig(
        algorithm=algorithm,
        wall_thickness=wall_thickness
    )


def main():
    config = show_menu()

    print(f"\nWybrany algorytm: {config.algorithm.upper()}")
    print(f"Grubość ścian: {config.wall_thickness} mm\n")

    grid = [
        [0,0,0,1,0,0,0],
        [1,1,0,1,0,1,0],
        [0,0,0,0,0,1,0],
        [0,1,1,1,0,1,0],
        [0,1,0,0,0,0,0],
    ]

    maze = Maze(grid)
    start = Cell(0, 0)
    goal = Cell(4, 6)

    if config.algorithm == "bfs":
        path, visited = bfs(maze, start, goal)
        animate_maze(maze, path, visited, start, goal)

    elif config.algorithm == "dfs":
        explorer = dfs_explore(maze, start, goal)
        animate_exploration(maze, explorer, start, goal)


if __name__ == "__main__":
    main()
