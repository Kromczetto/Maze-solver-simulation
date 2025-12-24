import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QRadioButton, QPushButton, QTabWidget
)

from maze.maze import Maze
from maze.cell import Cell
from algorithms import ALGORITHMS
from visualization.matplot_view import animate_exploration
from simulation.simulator import simulate
from gui.maze_editor import MazeEditorWidget

DEFAULT_GRID = [
    [0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0],
    [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0],
    [0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0],
    [0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
    [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0],
    [0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0],
    [0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,0],
]

DEFAULT_START = (0, 0)
DEFAULT_GOAL = (18, 17)


class MazeExplorerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maze Explorer")
        self.setFixedSize(480, 520)

        self.selected_algorithm = "wall_follower"
        self.custom_grid = None
        self.custom_start = None
        self.custom_goal = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        tabs = QTabWidget()

        algo_tab = QWidget()
        algo_layout = QVBoxLayout()

        for name, key in [
            ("Wall Follower", "wall_follower"),
            ("DFS", "dfs"),
            ("Trémaux", "tremaux"),
            ("Maze Routing", "routing"),
        ]:
            rb = QRadioButton(name)
            rb.toggled.connect(
                lambda checked, k=key: checked and setattr(self, "selected_algorithm", k)
            )
            algo_layout.addWidget(rb)
            if key == "wall_follower":
                rb.setChecked(True)

        run_btn = QPushButton("Uruchom")
        run_btn.clicked.connect(self.run_maze)
        algo_layout.addWidget(run_btn)

        algo_tab.setLayout(algo_layout)
        tabs.addTab(algo_tab, "Algorytmy")

        editor_tab = QWidget()
        editor_layout = QVBoxLayout()
        self.editor = MazeEditorWidget(rows=20, cols=20, cell_size=20)
        editor_layout.addWidget(self.editor)
        editor_tab.setLayout(editor_layout)
        tabs.addTab(editor_tab, "Edytor labiryntu")

        layout.addWidget(tabs)
        self.setLayout(layout)

    def run_maze(self):
        algorithm = ALGORITHMS[self.selected_algorithm]

        if self.custom_grid is None:
            grid = DEFAULT_GRID
            sr, sc = DEFAULT_START
            gr, gc = DEFAULT_GOAL
        else:
            grid = self.custom_grid
            sr, sc = self.custom_start
            gr, gc = self.custom_goal

        maze = Maze(grid)
        start = Cell(sr, sc)
        goal = Cell(gr, gc)

        explorer = algorithm(maze, start, goal)
        steps = simulate(explorer)

        animate_exploration(maze, steps, start, goal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MazeExplorerGUI()
    window.show()
    sys.exit(app.exec_())
