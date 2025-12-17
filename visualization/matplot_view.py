import matplotlib.pyplot as plt
import matplotlib.animation as animation
from maze.robot_map import CellState


def animate_exploration(maze, steps, start, goal):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")

    for r in range(maze.height):
        for c in range(maze.width):
            ax.add_patch(
                plt.Rectangle(
                    (c, maze.height - r - 1),
                    1, 1,
                    edgecolor="gray",
                    fill=False
                )
            )

    ax.text(
        start.col + 0.5,
        maze.height - start.row - 0.5,
        "S",
        ha="center",
        va="center",
        color="green",
        fontsize=12,
        weight="bold"
    )

    ax.text(
        goal.col + 0.5,
        maze.height - goal.row - 0.5,
        "G",
        ha="center",
        va="center",
        color="red",
        fontsize=12,
        weight="bold"
    )

    robot_patch = None
    memory_patches = {}

    def update(i):
        nonlocal robot_patch
        cell, visited, robot_map = steps[i]

        for r in range(robot_map.height):
            for c in range(robot_map.width):
                state = robot_map.map[r][c]
                if state == CellState.UNKNOWN:
                    continue

                key = (r, c)
                if key in memory_patches:
                    continue

                if state == CellState.WALL:
                    color = "black"
                    alpha = 1.0
                else:
                    color = "lightblue"
                    alpha = 0.4

                rect = plt.Rectangle(
                    (c, maze.height - r - 1),
                    1, 1,
                    color=color,
                    alpha=alpha
                )
                ax.add_patch(rect)
                memory_patches[key] = rect

        if robot_patch:
            robot_patch.remove()

        robot_patch = plt.Rectangle(
            (cell.col, maze.height - cell.row - 1),
            1, 1,
            color="yellow",
            alpha=0.7
        )
        ax.add_patch(robot_patch)

        return []

    ax.set_xlim(0, maze.width)
    ax.set_ylim(0, maze.height)
    ax.set_xticks([])
    ax.set_yticks([])

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=len(steps),
        interval=300,
        repeat=False
    )

    plt.show()
