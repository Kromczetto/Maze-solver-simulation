import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QRadioButton, QPushButton, QGroupBox,
    QMessageBox, QTabWidget
)

from maze.maze import Maze
from maze.cell import Cell
from visualization.matplot_view import animate_exploration
from algorithms import ALGORITHMS
from main import run

from gui.maze_editor import MazeEditorWidget


class MazeExplorerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maze Explorer")
        self.setFixedSize(460, 420)

        self.selected_algorithm = "wall_follower"

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # ===== TAB 1: ALGORYTMY =====
        algo_tab = QWidget()
        algo_layout = QVBoxLayout()

        title = QLabel("Wybierz algorytm eksploracji")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        algo_layout.addWidget(title)

        algo_group = QGroupBox("Algorytmy")
        group_layout = QVBoxLayout()
        self.radio_buttons = {}

        algorithms = [
            ("Wall Follower", "wall_follower"),
            ("DFS", "dfs"),
            ("Trémaux", "tremaux"),
            ("Maze Routing", "routing"),
        ]

        for name, key in algorithms:
            rb = QRadioButton(name)
            rb.toggled.connect(
                lambda checked, k=key: self.set_algorithm(k) if checked else None
            )
            group_layout.addWidget(rb)
            self.radio_buttons[key] = rb

        self.radio_buttons["wall_follower"].setChecked(True)

        algo_group.setLayout(group_layout)
        algo_layout.addWidget(algo_group)

        run_button = QPushButton("Uruchom (gotowy labirynt)")
        run_button.clicked.connect(self.run_default_maze)
        algo_layout.addWidget(run_button)

        algo_tab.setLayout(algo_layout)
        self.tabs.addTab(algo_tab, "Algorytmy")

        # ===== TAB 2: EDYTOR =====
        editor_tab = QWidget()
        editor_layout = QVBoxLayout()

        self.editor = MazeEditorWidget(rows=20, cols=20, cell_size=20)
        editor_layout.addWidget(self.editor)

        run_drawn = QPushButton("Uruchom na narysowanym labiryncie")
        run_drawn.clicked.connect(self.run_drawn_maze)
        editor_layout.addWidget(run_drawn)

        info = QLabel("LPM: ściana | PPM: usuń\nSHIFT+LPM: START | CTRL+LPM: GOAL")
        editor_layout.addWidget(info)

        editor_tab.setLayout(editor_layout)
        self.tabs.addTab(editor_tab, "Edytor labiryntu")

        self.setLayout(layout)

    def set_algorithm(self, key):
        self.selected_algorithm = key

    def run_default_maze(self):
        algorithm = ALGORITHMS[self.selected_algorithm]

        grid = [
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

        maze = Maze(grid)
        start = Cell(0, 0)
        goal = Cell(18, 17)

        explorer = algorithm(maze, start, goal)
        steps = run(explorer)
        animate_exploration(maze, steps, start, goal)

    def run_drawn_maze(self):
        algorithm = ALGORITHMS[self.selected_algorithm]

        grid = self.editor.grid
        sr, sc = self.editor.start
        gr, gc = self.editor.goal

        maze = Maze(grid)
        start = Cell(sr, sc)
        goal = Cell(gr, gc)

        explorer = algorithm(maze, start, goal)
        steps = run(explorer)
        animate_exploration(maze, steps, start, goal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MazeExplorerGUI()
    window.show()
    sys.exit(app.exec_())
