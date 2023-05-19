from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class PaintView(QGraphicsPixmapItem):
    def __init__(self):
        super(PaintView, self).__init__()

        self.pixmap_display = QPixmap(QSize(500, 500))
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
            if self.paint_fill:
                self.pixel_image = self.pixmap_display.toImage()
            pixel = self.pixel_image.pixel(int(event.pos().x()), int(event.pos().y()))
            selected_color = self.get_hex_from_pixel(pixel)
            self.filled = False
            self.pixel_x_iter = x
            self.pixel_y_iter = y
            default_pos_x = int(color_position.x())

            while self.pixel_x_iter != self.pixel_image.width():
                pixel = self.pixel_image.pixel(self.pixel_x_iter, self.pixel_y_iter)
                color = self.get_hex_from_pixel(pixel)
                self.pixel_image.setPixelColor(self.pixel_x_iter, self.pixel_y_iter, QColor(self.pen_color))
                if color == selected_color:
                    self.pixel_image.setPixelColor(self.pixel_x_iter, self.pixel_y_iter, QColor(self.pen_color))
                    self.pixel_x_iter += 1
                else:
                  print('yes')

            self.pixmap_display = self.pixmap_display.fromImage(self.pixel_image)
            self.setPixmap(self.pixmap_display)
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

        if self.prev_point: self.painter.drawLine(int(self.prev_point.x()), int(self.prev_point.y()), int(position.x()), int(position.y()))
        else: self.painter.drawPoint(int(position.x()), int(position.y()))

        self.painter.end()

        self.setPixmap(self.pixmap_display)
        self.prev_point = position
    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.prev_point = None
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
