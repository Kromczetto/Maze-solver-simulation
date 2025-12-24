from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint

class MazeEditorWidget(QWidget):
    def __init__(self, rows=20, cols=20, cell_size=20):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.start = (0, 0)
        self.goal = (rows - 1, cols - 1)

        self.setFixedSize(cols * cell_size, rows * cell_size)

    def paintEvent(self, event):
        painter = QPainter(self)

        for r in range(self.rows):
            for c in range(self.cols):
                x = c * self.cell_size
                y = r * self.cell_size

                if self.grid[r][c] == 1:
                    painter.fillRect(x, y, self.cell_size, self.cell_size, QColor("black"))
                else:
                    painter.fillRect(x, y, self.cell_size, self.cell_size, QColor("white"))

                painter.setPen(QPen(Qt.gray))
                painter.drawRect(x, y, self.cell_size, self.cell_size)

        sr, sc = self.start
        painter.fillRect(
            sc * self.cell_size,
            sr * self.cell_size,
            self.cell_size,
            self.cell_size,
            QColor(0, 255, 0, 150),
        )

        gr, gc = self.goal
        painter.fillRect(
            gc * self.cell_size,
            gr * self.cell_size,
            self.cell_size,
            self.cell_size,
            QColor(255, 0, 0, 150),
        )

    def mousePressEvent(self, event):
        c = event.x() // self.cell_size
        r = event.y() // self.cell_size

        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return

        if event.modifiers() & Qt.ShiftModifier:
            self.start = (r, c)
        elif event.modifiers() & Qt.ControlModifier:
            self.goal = (r, c)
        else:
            if event.button() == Qt.LeftButton:
                self.grid[r][c] = 1
            elif event.button() == Qt.RightButton:
                self.grid[r][c] = 0

        self.update()
