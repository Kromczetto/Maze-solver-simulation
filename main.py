from maze.maze import Maze
from maze.cell import Cell
from visualization.matplot_view import animate_exploration
from algorithms import ALGORITHMS

def run(explorer):
    steps = []
    try:
        while True:
            steps.append(next(explorer))
    except StopIteration:
        pass
    return steps


def choose_algorithm():
    print("Wybierz algorytm eksploracji:")
    print("1. Wall Follower")
    print("2. DFS")

    choice = input("Podaj numer (1–2): ").strip()

    if choice == "1":
        return ALGORITHMS["wall"]
    elif choice == "2":
        return ALGORITHMS["dfs"]
    else:
        raise ValueError("Nieprawidłowy wybór algorytmu")


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

    algorithm = choose_algorithm()
    explorer = algorithm(maze, start, goal)

    steps = run(explorer)
    animate_exploration(maze, steps, start, goal)


if __name__ == "__main__":
    main()
