import matplotlib.pyplot as plt
import matplotlib.animation as animation

CELL_SIZE = 1.0  

def animate_maze(maze, path):
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

    robot_dot, = ax.plot([], [], "ro", markersize=8)

    def cell_center(cell):
        x = cell.col + 0.5
        y = maze.height - cell.row - 0.5
        return x, y

    def update(frame):
        cell = path[min(frame, len(path) - 1)]
        x, y = cell_center(cell)
        robot_dot.set_data(x, y)
        return robot_dot,

    ax.set_xlim(0, maze.width)
    ax.set_ylim(0, maze.height)
    ax.set_xticks([])
    ax.set_yticks([])

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(path),
        interval=400,
        repeat=False
    )

    plt.show()
