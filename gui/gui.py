import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QRadioButton, QPushButton, QGroupBox, QMessageBox
)

from maze.maze import Maze
from maze.cell import Cell
from visualization.matplot_view import animate_exploration
from algorithms import ALGORITHMS
from main import run   


class MazeExplorerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maze Explorer")
        self.setFixedSize(320, 260)

        self.selected_algorithm = "wall_follower"

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Wybierz algorytm eksploracji")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)

        algo_group = QGroupBox("Algorytmy")
        algo_layout = QVBoxLayout()

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
            algo_layout.addWidget(rb)
            self.radio_buttons[key] = rb

        self.radio_buttons["wall_follower"].setChecked(True)

        algo_group.setLayout(algo_layout)
        layout.addWidget(algo_group)

        run_button = QPushButton("Uruchom symulację")
        run_button.clicked.connect(self.run_simulation)
        layout.addWidget(run_button)

        self.setLayout(layout)

    def set_algorithm(self, key):
        self.selected_algorithm = key

    def run_simulation(self):
        if self.selected_algorithm not in ALGORITHMS:
            QMessageBox.critical(self, "Błąd", "Nieznany algorytm")
            return

        algorithm = ALGORITHMS[self.selected_algorithm]

        grid = [
            [0,0,0,1,0],
            [1,1,0,1,0],
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,0],
        ]

        maze = Maze(grid)
        start = Cell(0, 0)
        goal = Cell(4, 4)

        try:
            explorer = algorithm(maze, start, goal)
            steps = run(explorer)
            animate_exploration(maze, steps, start, goal)
        except Exception as e:
            QMessageBox.critical(self, "Błąd uruchomienia", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MazeExplorerGUI()
    window.show()
    sys.exit(app.exec_())
