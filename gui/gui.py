import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QRadioButton, QPushButton, QTabWidget,
    QMessageBox
)

from maze.maze import Maze
from maze.cell import Cell
from algorithms import ALGORITHMS
from visualization.matplot_view import animate_exploration
from simulation.simulator import simulate
from gui.maze_editor import MazeEditorWidget
from maze.generator import generate_maze_prim

class MazeExplorerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maze Explorer")
        self.setFixedSize(540, 620)

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

        run_btn = QPushButton("Uruchom algorytm")
        run_btn.clicked.connect(self.run_maze)
        algo_layout.addWidget(run_btn)

        algo_tab.setLayout(algo_layout)
        tabs.addTab(algo_tab, "Algorytmy")

        editor_tab = QWidget()
        editor_layout = QVBoxLayout()

        self.editor = MazeEditorWidget(rows=20, cols=20, cell_size=20)
        editor_layout.addWidget(self.editor)

        gen_btn = QPushButton("Generuj labirynt (Prim)")
        gen_btn.clicked.connect(self.generate_prim_maze)
        editor_layout.addWidget(gen_btn)

        save_btn = QPushButton("Zapisz labirynt")
        save_btn.clicked.connect(self.save_drawn_maze)
        editor_layout.addWidget(save_btn)

        info = QLabel(
            "LPM: ściana | PPM: usuń\n"
            "SHIFT + LPM: START | CTRL + LPM: GOAL"
        )
        editor_layout.addWidget(info)

        editor_tab.setLayout(editor_layout)
        tabs.addTab(editor_tab, "Edytor labiryntu")

        layout.addWidget(tabs)
        self.setLayout(layout)

    def generate_prim_maze(self):
        rows = self.editor.rows
        cols = self.editor.cols

        if rows % 2 == 0:
            rows -= 1
        if cols % 2 == 0:
            cols -= 1

        grid = generate_maze_prim(rows, cols)

        self.editor.set_grid(grid)
        self.editor.start = (1, 1)
        self.editor.goal = (rows - 2, cols - 2)

    def save_drawn_maze(self):
        self.custom_grid = [row[:] for row in self.editor.grid]
        self.custom_start = self.editor.start
        self.custom_goal = self.editor.goal

        QMessageBox.information(
            self,
            "Zapisano",
            "Labirynt zapisany.\n"
            "Zostanie użyty przy kolejnym uruchomieniu."
        )

    def run_maze(self):
        algorithm = ALGORITHMS[self.selected_algorithm]

        if self.custom_grid:
            grid = self.custom_grid
            sr, sc = self.custom_start
            gr, gc = self.custom_goal
        else:
            grid = self.editor.grid
            sr, sc = self.editor.start
            gr, gc = self.editor.goal

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
