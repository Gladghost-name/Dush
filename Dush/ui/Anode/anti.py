import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QImage, QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shape Fill Tool")
        self.setGeometry(100, 100, 400, 400)

        self.image = QImage(400, 400, QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.pixmap = QPixmap.fromImage(self.image)

        self.label = QLabel()
        self.label.setPixmap(self.pixmap)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.label.mousePressEvent = self.mousePressEvent

    def fillShape(self, event):
        # Get the mouse click position
        pos = event.pos()

        # Create a QPainter object
        painter = QPainter(self.image)

        # Get the color at the click position
        target_color = QColor(self.image.pixel(pos))

        # Set the fill color
        fill_color = QColor(Qt.yellow)

        # Perform the flood fill operation
        self.floodFill(pos.x(), pos.y(), target_color, fill_color, painter)

        painter.end()

        # Update the pixmap
        self.pixmap = QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmap)

    def floodFill(self, x, y, target_color, fill_color, painter):
        # Create a stack for storing pixel positions
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            # Check if the current pixel matches the target color
            if self.image.pixel(x, y) != target_color.rgb():
                continue

            # Set the fill color for the current pixel
            painter.setPen(fill_color)
            painter.drawPoint(x, y)

            # Add adjacent pixels to the stack
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.fillShape(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())