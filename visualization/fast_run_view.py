import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_fast_run(maze, path, title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_aspect("equal")

    for r in range(maze.height):
        for c in range(maze.width):
            color = "black" if maze.is_wall(r, c) else "white"
            ax.add_patch(
                plt.Rectangle(
                    (c, maze.height - r - 1),
                    1, 1,
                    edgecolor="gray",
                    facecolor=color
                )
            )

    robot = plt.Rectangle(
        (path[0].col, maze.height - path[0].row - 1),
        1, 1,
        color="red"
    )
    ax.add_patch(robot)

    def update(i):
        cell = path[i]
        robot.set_xy((cell.col, maze.height - cell.row - 1))
        return robot,

    ax.set_xlim(0, maze.width)
    ax.set_ylim(0, maze.height)
    ax.set_xticks([])
    ax.set_yticks([])

    animation.FuncAnimation(
        fig,
        update,
        frames=len(path),
        interval=100,
        repeat=False
    )

    plt.show()
