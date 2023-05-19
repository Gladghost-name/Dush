from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


class PaintView(QGraphicsPixmapItem):
    def __init__(self):
        super(PaintView, self).__init__()

        self.pixmap_display = QPixmap(QSize(1000, 500))
        self.pixmap_display.fill(QColor(255, 255, 255, 255))

        self.prev_point = None

        self.pen_color = 'black'
        self.paint_fill = False

        self.default_pen = QPen()
        self.pen_size = 1
        self.default_pen.setWidth(self.pen_size)
        self.default_pen.setColor(QColor(self.pen_color))
        self.default_pen.setCapStyle(Qt.RoundCap)

        self.start_erasing = False
        self.setCursor(Qt.CursorShape.CrossCursor)
        self.filled = True

        self.pixel_x_iter = 0
        self.pixel_y_iter = 0

        self.setPixmap(self.pixmap_display)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        color_position = event.pos()
        x = int(color_position.x())
        y = int(color_position.y())
        if self.paint_fill:
            self.image = self.pixmap_display.toImage()
            self.fillShape(event, self.image)
    def fillShape(self, event, image):
        # Get the mouse click position
        pos = event.pos()

        # Create a QPainter object
        painter = QPainter(image)

        # Get the color at the click position
        target_color = QColor(image.pixel(int(pos.x()), int(pos.y())))

        # Set the fill color
        fill_color = QColor(self.pen_color)

        # Perform the flood fill operation
        self.floodFill(int(pos.x()), int(pos.y()), target_color, fill_color, painter, image)

        painter.end()

        # Update the pixmap
        self.pixmap_display = QPixmap.fromImage(image)
        self.setPixmap(self.pixmap_display)

    def floodFill(self, x, y, target_color, fill_color, painter, image):
        # Create a stack for storing pixel positions
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            # Check if the current pixel matches the target color
            if image.pixel(x, y) != target_color.rgb():
                continue

            # Set the fill color for the current pixel
            painter.setPen(fill_color)
            painter.drawPoint(x, y)

            # Add adjacent pixels to the stack
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))
    def get_hex_from_pixel(self, pixel):
        hex_code = "#{:02x}{:02x}{:02x}".format(
            (pixel >> 16) & 0xFF, (pixel >> 8) & 0xFF, pixel & 0xFF
        )
        return hex_code

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        position = event.pos()

        self.painter = QPainter(self.pixmap_display)

        self.default_pen.setColor(QColor(self.pen_color))
        self.default_pen.setWidth(self.pen_size)

        if self.start_erasing:
            self.default_pen.setColor(QColor('white'))
            self.default_pen.setWidth(10)

        self.painter.setPen(self.default_pen)
        # painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

        if self.prev_point:
            self.painter.drawLine(int(self.prev_point.x()), int(self.prev_point.y()), int(position.x()),
                                  int(position.y()))
        else:
            self.painter.drawPoint(int(position.x()), int(position.y()))

        self.painter.end()

        self.setPixmap(self.pixmap_display)
        self.prev_point = position

    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.prev_point = None
        self.paint_fill = False
        self.update()

    def draw_eraser(self):
        self.start_erasing = True

    def set_color(self):
        self.dialog = QColorDialog()
        self.dialog.colorSelected.connect(self.select_color)
        self.dialog.show()

    def select_color(self):
        self.pen_color = self.dialog.selectedColor().name()
        self.update()

    def draw_pen(self):
        self.start_erasing = False
        self.update()

    def clear(self):
        self.pixmap_display.fill(QColor('white'))
        self.setPixmap(self.pixmap_display)
        self.update()

    def fill_pixels(self):
        self.paint_fill = True
        self.update()
    def save_image(self):
        self.file_diag = QFileDialog()
        self.file_info = self.file_diag.getSaveFileName()
        if self.file_info[0]:
            self.pixmap_display.save(self.file_info[0])


class PaintWindow(QMainWindow):
    def __init__(self):
        super(PaintWindow, self).__init__()
        self.setWindowTitle("Simple Paint App!")

        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.scene = QGraphicsScene()
        self.canvas = PaintView()

        self.toolbar.addAction("color", self.canvas.set_color)
        self.toolbar.addAction("eraser", self.canvas.draw_eraser)
        self.toolbar.addAction("pen", self.canvas.draw_pen)
        self.toolbar.addAction("clear", self.canvas.clear)
        self.toolbar.addAction("fill", self.canvas.fill_pixels)
        self.toolbar.addAction("save as", self.canvas.save_image)

        self.scene.addItem(self.canvas)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)


class MainApp(QApplication):
    def __init__(self):
        super(MainApp, self).__init__(sys.argv)
        self.window = PaintWindow()

    def run(self):
        self.window.show()
        sys.exit(self.exec())


app = MainApp()
app.run()
