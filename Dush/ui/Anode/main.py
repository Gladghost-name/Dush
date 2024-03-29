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
        self._zoom = 0
        self.fill_ended = True
        self.start_drawing_points = False

        self.pen_color = 'black'
        self.paint_fill = False
        self.drawing_disabled = False

        self.default_pen = QPen()
        self.pen_size = 4
        self.default_pen.setWidth(self.pen_size)
        self.default_pen.setColor(QColor(self.pen_color))
        self.default_pen.setCapStyle(Qt.RoundCap)

        self.start_angular = False
        self.lines = []
        self.setAcceptHoverEvents(True)

        self.polygon_list = []
        self.start_erasing = False
        self.drawing_path = False
        # self.setCursor(QCursor(QPixmap('pencil.png').scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)))

        self.setCursor(Qt.CursorShape.CrossCursor)
        self.filled = True

        self.pixel_x_iter = 0
        self.pixel_y_iter = 0

        self.cur_x = 0
        self.cur_y = 0
        self.canvas_refresh = QTimer()
        self.canvas_refresh.setInterval(int(1000 / 60))
        self.canvas_refresh.timeout.connect(self.update_canvas)
        self.canvas_refresh.start()

        self.setPixmap(self.pixmap_display)

    def update_canvas(self):
        pass

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        color_position = event.pos()
        x = int(color_position.x())
        y = int(color_position.y())
        if self.paint_fill and self.fill_ended:
            self.fill_ended = False
            self.image = self.pixmap_display.toImage()
            self.fillShape(event, self.image)
            # self.fill_ended = False
        if self.start_drawing_points:
            self.cur_x = color_position.x()
            self.cur_y = color_position.y()
            self.point = QPointF(color_position.x(), color_position.y())
            self.line = self.scene().addLine(color_position.x(), color_position.y(), color_position.x(),
                                             color_position.y())
            self.start_angular = True
            self.lines.append(self.line)
            self.polygon_list.append(self.point)
        # self.update()

    def hoverMoveEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        position = event.pos()
        if self.start_angular:
            self.line.setLine(QLineF(self.cur_x, self.cur_y, position.x(), position.y()))
            self.update()

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
        self.update()
        self.fill_ended = True

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

        if self.drawing_disabled == False:
            self.painter.setPen(self.default_pen)

            # disabled for complete bucket fill look!
            # self.painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

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
        self.update()

    def draw_eraser(self):
        self.paint_fill = False
        self.drawing_disabled = False
        self.start_erasing = True

    def set_color(self):
        self.dialog = QColorDialog()
        self.dialog.colorSelected.connect(self.select_color)
        self.dialog.show()

    def select_color(self):
        self.pen_color = self.dialog.selectedColor().name()
        self.update()

    def draw_pen(self):
        self.paint_fill = False
        self.drawing_disabled = False
        self.start_erasing = False
        self.update()

    def clear(self):
        self.pixmap_display.fill(QColor('white'))
        self.setPixmap(self.pixmap_display)
        self.update()

    def fill_pixels(self):
        # self.setCursor(
        #     QCursor(QPixmap('paint-bucket.png').scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)))
        self.drawing_disabled = True
        self.paint_fill = True
        self.update()

    def save_image(self):
        self.file_diag = QFileDialog()
        self.file_info = self.file_diag.getSaveFileName()
        if self.file_info[0]:
            self.pixmap_display.save(self.file_info[0])

    def draw_polygon(self):
        self.drawing_disabled = True
        self.start_drawing_points = True


class PaintDisplay(QGraphicsView):
    def __init__(self, scene, canvas):
        super(PaintDisplay, self).__init__(scene)
        self.canvas = canvas
        self.polygon_list = []
        self.cur_x = 0
        self.cur_y = 0
        self.start_angular = False
        self.grabKeyboard()
        self.lines = []
        self.start_drawing_points = False
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Return:
            self.canvas.drawing_disabled = False
            self.canvas.start_drawing_points = False
            for line in self.canvas.lines:
                self.scene().removeItem(line)
            self.canvas.lines = []
            self.canvas_painter = QPainter(self.canvas.pixmap_display)
            self.canvas_painter.setPen(QPen(Qt.NoPen))
            self.canvas_painter.setBrush(QBrush(QColor('black')))
            self.canvas_painter.drawPolygon(QPolygonF(self.canvas.polygon_list))
            self.canvas.polygon_list = []
            self.canvas_painter.end()
            self.canvas.setPixmap(self.canvas.pixmap_display)
            self.update()


class PaintWindow(QMainWindow):
    def __init__(self):
        super(PaintWindow, self).__init__()
        self.setWindowTitle("Simple Paint App!")

        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.scene = QGraphicsScene()
        self.canvas = PaintView()
        self.view = PaintDisplay(self.scene, self.canvas)

        self.toolbar.addAction("color", self.canvas.set_color)
        self.toolbar.addAction("eraser", self.canvas.draw_eraser)
        self.toolbar.addAction("pen", self.canvas.draw_pen)
        self.toolbar.addAction("clear", self.canvas.clear)
        self.toolbar.addAction("fill", self.canvas.fill_pixels)
        self.toolbar.addAction("save as", self.canvas.save_image)
        self.toolbar.addSeparator()
        self.toolbar.addAction("path", self.canvas.draw_polygon)
        self.toolbar.addAction("open", self.open_file)

        self.scene.addItem(self.canvas)
        self.setCentralWidget(self.view)
        self._zoom = 0

    def open_file(self):
        self.filedialog = QFileDialog()
        self.info = self.filedialog.getOpenFileName()
        if self.info[0]:
            self.canvas.pixmap_display = QPixmap(self.info[0]).scaled(1000, 500, Qt.KeepAspectRatio,
                                                                      Qt.SmoothTransformation)
            self.canvas.setPixmap(self.canvas.pixmap_display)


class MainApp(QApplication):
    def __init__(self):
        super(MainApp, self).__init__(sys.argv)
        self.window = PaintWindow()

    def run(self):
        self.window.show()
        sys.exit(self.exec())


app = MainApp()
app.run()
