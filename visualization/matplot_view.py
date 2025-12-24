import matplotlib.pyplot as plt
import matplotlib.animation as animation
from maze.robot_map import CellState

def animate_exploration(maze, steps, start, goal):
    fig, ax = plt.subplots(figsize=(8, 6))

    fig.subplots_adjust(right=0.75)

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
    known_cells = {}

    info_text = fig.text(
        0.78, 0.85, "",
        ha="left",
        va="top",
        fontsize=11
    )

    def update(i):
        nonlocal robot_patch
        step = steps[i]

        for r in range(step.robot_map.height):
            for c in range(step.robot_map.width):
                state = step.robot_map.map[r][c]
                if state == CellState.UNKNOWN:
                    continue
                if (r, c) in known_cells:
                    continue

                color = "black" if state == CellState.WALL else "lightblue"
                alpha = 1.0 if state == CellState.WALL else 0.4

                rect = plt.Rectangle(
                    (c, maze.height - r - 1),
                    1, 1,
                    color=color,
                    alpha=alpha
                )
                ax.add_patch(rect)
                known_cells[(r, c)] = rect

        if robot_patch:
            robot_patch.remove()

        robot_patch = plt.Rectangle(
            (step.cell.col, maze.height - step.cell.row - 1),
            1, 1,
            color="yellow",
            alpha=0.7
        )
        ax.add_patch(robot_patch)

        info_text.set_text(
            "STATYSTYKI SYMULACJI\n"
            "------------------\n"
            f"Krok: {step.step_index}\n"
            f"Czas: {step.time_sec:.2f} s\n"
        )

        return []

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=len(steps),
        interval=300,
        repeat=False
    )

    fig._anim = anim  

    ax.set_xlim(0, maze.width)
    ax.set_ylim(0, maze.height)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show(block=False)
