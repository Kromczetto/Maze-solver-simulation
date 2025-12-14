import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

FPS = 30
CELL_LENGTH_M = 0.30
ROBOT_SPEED_MPS = 1.0

def animate_exploration(maze, explorer, start, goal):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")

    for r in range(maze.height):
        for c in range(maze.width):
            if maze.is_wall(r, c):
                ax.add_patch(
                    plt.Rectangle((c, maze.height - r - 1), 1, 1, color="black")
                )
            else:
                ax.add_patch(
                    plt.Rectangle((c, maze.height - r - 1), 1, 1,
                                  edgecolor="gray", fill=False)
                )

    visited_patches = {}
    robot, = ax.plot([], [], "ro", markersize=8)

    ax.text(start.col + 0.5, maze.height - start.row - 0.5, "S",
            ha="center", va="center", color="green")
    ax.text(goal.col + 0.5, maze.height - goal.row - 0.5, "G",
            ha="center", va="center", color="red")

    def center(cell):
        return cell.col + 0.5, maze.height - cell.row - 0.5

    steps = list(explorer)

    def update(frame):
        cell, visited = steps[frame]

        for v in visited:
            if v not in visited_patches:
                rect = plt.Rectangle(
                    (v.col, maze.height - v.row - 1),
                    1, 1,
                    color="lightblue",
                    alpha=0.3
                )
                ax.add_patch(rect)
                visited_patches[v] = rect

        x, y = center(cell)
        robot.set_data([x], [y])
        return robot,

    ax.set_xlim(0, maze.width)
    ax.set_ylim(0, maze.height)
    ax.set_xticks([])
    ax.set_yticks([])

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(steps),
        interval=300,
        repeat=False
    )

    plt.show()
        
def animate_maze(maze, path, visited, start, goal):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")

    for r in range(maze.height):
        for c in range(maze.width):
            if maze.is_wall(r, c):
                ax.add_patch(
                    plt.Rectangle((c, maze.height - r - 1), 1, 1, color="black")
                )
            else:
                ax.add_patch(
                    plt.Rectangle((c, maze.height - r - 1), 1, 1,
                                edgecolor="gray", fill=False)
                )

    for cell in visited:
        ax.add_patch(
            plt.Rectangle(
                (cell.col, maze.height - cell.row - 1),
                1, 1,
                color="lightblue",
                alpha=0.3
            )
        )

    ax.text(start.col + 0.5, maze.height - start.row - 0.5, "S",
            ha="center", va="center", color="green")
    ax.text(goal.col + 0.5, maze.height - goal.row - 0.5, "G",
            ha="center", va="center", color="red")

    robot, = ax.plot([], [], "ro", markersize=8)

    def center(cell):
        return cell.col + 0.5, maze.height - cell.row - 0.5

    def update(frame):
        cell = path[min(frame, len(path) - 1)]
        x, y = center(cell)
        robot.set_data([x], [y])
        return robot,

    ax.set_xlim(0, maze.width)
    ax.set_ylim(0, maze.height)
    ax.set_xticks([])
    ax.set_yticks([])

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(path),
        interval=300,
        repeat=False
    )

    plt.show()


def animate_drive(maze, path, start, goal):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")

    for r in range(maze.height):
        for c in range(maze.width):
            if maze.is_wall(r, c):
                ax.add_patch(plt.Rectangle((c, maze.height-r-1), 1, 1, color="black"))
            else:
                ax.add_patch(plt.Rectangle((c, maze.height-r-1), 1, 1,
                                           edgecolor="gray", fill=False))

    robot, = ax.plot([], [], "ro", markersize=8)

    def center(cell):
        return cell.col + 0.5, maze.height - cell.row - 0.5

    positions = []

    for i in range(len(path) - 1):
        x1, y1 = center(path[i])
        x2, y2 = center(path[i+1])
        frames = int((CELL_LENGTH_M / ROBOT_SPEED_MPS) * FPS)
        for t in np.linspace(0, 1, frames):
            positions.append((x1 + t*(x2-x1), y1 + t*(y2-y1)))

    def update(i):
        robot.set_data(*positions[i])
        return robot,

    ax.set_xlim(0, maze.width)
    ax.set_ylim(0, maze.height)
    ax.set_xticks([])
    ax.set_yticks([])

    animation.FuncAnimation(fig, update, frames=len(positions),
                            interval=1000/FPS, repeat=False)
    plt.show()