import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QRadioButton, QPushButton, QGroupBox,
    QMessageBox, QTabWidget, QFrame
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
        self.setFixedSize(460, 520)

        self.selected_algorithm = "wall_follower"

        # zapisany labirynt (opcjonalny)
        self.custom_grid = None
        self.custom_start = None
        self.custom_goal = None

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # =====================================================
        # TAB 1: ALGORYTMY
        # =====================================================
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

        run_button = QPushButton("Uruchom labirynt")
        run_button.setFixedHeight(32)
        run_button.clicked.connect(self.run_maze)
        algo_layout.addWidget(run_button)

        algo_tab.setLayout(algo_layout)
        self.tabs.addTab(algo_tab, "Algorytmy")

        # =====================================================
        # TAB 2: EDYTOR LABIRYNTU
        # =====================================================
        editor_tab = QWidget()
        editor_layout = QVBoxLayout()
        editor_layout.setSpacing(8)
        editor_layout.setContentsMargins(8, 8, 8, 8)

        # --- RAMKA Z SIATKĄ ---
        grid_frame = QFrame()
        grid_frame.setFrameShape(QFrame.StyledPanel)
        grid_layout = QVBoxLayout()
        grid_layout.setContentsMargins(4, 4, 4, 4)

        self.editor = MazeEditorWidget(rows=20, cols=20, cell_size=20)
        grid_layout.addWidget(self.editor)
        grid_frame.setLayout(grid_layout)

        editor_layout.addWidget(grid_frame)

        # --- PANEL STEROWANIA ---
        controls_frame = QFrame()
        controls_layout = QVBoxLayout()
        controls_layout.setSpacing(6)

        save_button = QPushButton("Zapisz labirynt")
        save_button.setFixedHeight(32)
        save_button.clicked.connect(self.save_drawn_maze)

        info = QLabel(
            "LPM: ściana | PPM: usuń\n"
            "SHIFT + LPM: START | CTRL + LPM: GOAL"
        )

        controls_layout.addWidget(save_button)
        controls_layout.addWidget(info)
        controls_frame.setLayout(controls_layout)

        editor_layout.addWidget(controls_frame)

        editor_tab.setLayout(editor_layout)
        self.tabs.addTab(editor_tab, "Edytor labiryntu")

        self.setLayout(main_layout)

    def set_algorithm(self, key):
        self.selected_algorithm = key

    # =====================================================
    # LOGIKA ZAPISU / URUCHAMIANIA
    # =====================================================

    def save_drawn_maze(self):
        self.custom_grid = [row[:] for row in self.editor.grid]
        self.custom_start = self.editor.start
        self.custom_goal = self.editor.goal

        QMessageBox.information(
            self,
            "Zapisano labirynt",
            "Labirynt został zapisany.\n"
            "Zostanie użyty przy kolejnym uruchomieniu."
        )

    def run_maze(self):
        algorithm = ALGORITHMS[self.selected_algorithm]

        # jeśli zapisano własny labirynt – używamy go
        if self.custom_grid is not None:
            grid = self.custom_grid
            sr, sc = self.custom_start
            gr, gc = self.custom_goal
        else:
            # domyślny labirynt
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
            sr, sc = 0, 0
            gr, gc = 18, 17

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
