import copy
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QTableWidget, QTableWidgetItem,
    QFileDialog, QMessageBox
)

from maze.maze import Maze
from maze.cell import Cell
from maze.generator import generate_maze_prim
from maze.export import maze_to_text
from algorithms import ALGORITHMS
from simulation.simulator import simulate
from analysis.results import AlgorithmResult
from analysis.plots import plot_results


class TestTab(QWidget):
    def __init__(self):
        super().__init__()
        self.results = []
        self.grid = None
        self.start = None
        self.goal = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.maze_view = QTextEdit()
        self.maze_view.setReadOnly(True)
        self.maze_view.setFontFamily("Courier")
        layout.addWidget(self.maze_view)

        self.run_btn = QPushButton("Rozpocznij testy")
        self.run_btn.clicked.connect(self.run_tests)
        layout.addWidget(self.run_btn)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Algorytm", "Kroki", "Czas [s]"])
        layout.addWidget(self.table)

        self.save_btn = QPushButton("Zapisz wyniki do pliku")
        self.save_btn.clicked.connect(self.save_results)
        layout.addWidget(self.save_btn)

        self.plot_btn = QPushButton("Zobacz wykres")
        self.plot_btn.clicked.connect(self.show_plot)
        layout.addWidget(self.plot_btn)

        self.setLayout(layout)

    def run_tests(self):
        self.grid = generate_maze_prim(21, 21)
        self.start = (1, 1)
        self.goal = (19, 19)

        maze_text = maze_to_text(self.grid, self.start, self.goal)
        self.maze_view.setText(maze_text)

        self.results.clear()
        self.table.setRowCount(0)

        for name, algorithm in ALGORITHMS.items():
            maze = Maze(copy.deepcopy(self.grid))
            start_cell = Cell(*self.start)
            goal_cell = Cell(*self.goal)

            explorer = algorithm(maze, start_cell, goal_cell)
            steps = simulate(explorer)

            if not steps:
                continue

            result = AlgorithmResult(
                name=name,
                steps=len(steps),
                time=steps[-1].time_sec,
                path=[s.cell for s in steps]
            )
            self.results.append(result)

            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(result.steps)))
            self.table.setItem(row, 2, QTableWidgetItem(f"{result.time:.2f}"))

        QMessageBox.information(self, "Gotowe", "Testy zakończone")

    def save_results(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Zapisz wyniki", "", "Plik tekstowy (*.txt)"
        )
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            f.write("LABIRYNT:\n")
            f.write(self.maze_view.toPlainText())
            f.write("\n\nWYNIKI:\n")

            for r in self.results:
                f.write(
                    f"{r.name}: {r.steps} kroków, {r.time:.2f} s\n"
                )

        QMessageBox.information(self, "Zapisano", "Plik zapisany")

    def show_plot(self):
        if not self.results:
            return
        goal_cell = Cell(*self.goal)
        plot_results(self.results, goal_cell)
