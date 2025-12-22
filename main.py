from maze.maze import Maze
from maze.cell import Cell
from visualization.matplot_view import animate_exploration
from algorithms import ALGORITHMS

def run(explorer, max_steps=20000):
    steps = []
    for _ in range(max_steps):
        try:
            steps.append(next(explorer))
        except StopIteration:
            break
    return steps


def choose_algorithm():
    print("Wybierz algorytm eksploracji:")
    print("1. Wall Follower")
    print("2. DFS")
    print("3. Tremaux")
    print("4. Maze-Routing")

    choice = input("Podaj numer (1–4): ").strip()

    if choice == "1":
        return ALGORITHMS["wall"]
    elif choice == "2":
        return ALGORITHMS["dfs"]
    elif choice == "3":
        return ALGORITHMS["tremaux"]
    elif choice == "4":
        return ALGORITHMS["routing"]
    else:
        raise ValueError("Nieprawidłowy wybór algorytmu")

def main():
    grid = [
        [0,0,0,1,0,0,0,0,1,0, 0,0,0,1,0,0,0,0,0,0],
        [0,1,0,1,0,1,1,0,1,0, 1,1,0,1,0,1,1,1,1,0],
        [0,1,0,0,0,0,1,0,0,0, 0,1,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,0, 0,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,1,0,0,0,1,0, 0,0,0,0,0,0,1,0,0,0],
        [1,1,1,0,1,1,1,0,1,1, 1,1,1,1,1,0,1,1,1,0],
        [0,0,1,0,0,0,1,0,0,0, 0,0,0,0,1,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1, 1,1,1,0,1,1,1,0,1,0],
        [0,0,0,0,1,0,0,0,0,0, 0,0,1,0,0,0,0,0,1,0],
        [1,1,1,0,1,1,1,1,1,1, 1,0,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,1,0,0,0],
        [0,1,1,1,1,1,1,1,1,0, 1,1,1,1,1,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,1,0, 0,0,0,0,1,0,0,0,0,0],
        [0,1,1,1,1,1,1,0,1,1, 1,1,1,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,1,0,0,0, 0,0,1,0,0,0,0,0,0,0],
        [1,1,1,1,1,0,1,1,1,1, 1,0,1,1,1,1,1,1,1,0],
        [0,0,0,0,1,0,0,0,0,0, 1,0,0,0,0,0,0,0,1,0],
        [0,1,1,0,1,1,1,1,1,0, 1,1,1,1,1,1,1,0,1,0],
        [0,0,1,0,0,0,0,0,1,0, 0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,1,1,0,0,0, 1,1,1,1,1,0,0,0,1,0],
    ]

    grid2 = [
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ]

    maze = Maze(grid)
    start = Cell(0, 0)
    goal  = Cell(18, 17)

    algorithm = choose_algorithm()
    explorer = algorithm(maze, start, goal)

    steps = run(explorer)
    animate_exploration(maze, steps, start, goal)


if __name__ == "__main__":
    main()
