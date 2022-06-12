from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class DrawingBoard(QFrame):
    """Still a experiment of drawing on a widget"""

    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.resize(width, height)  # resizing the widget

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """Changing the original painting of the widget"""
        self.painter = QPainter(self)  # Creating QPainter instance in a function :/
        self.painter.setBrush(QBrush(QColor('yellow')))  # setting the brush of the QPainter
        self.painter.drawRect(self.rect())  # Drawing a simple rectangle
        self.painter.end()  # Ending the paint event

    def drawRectangle(self, x: int = 0, y: int = 0, width: int = 200, height: int = 80):
        """Drawing a rectangle on the screen"""
        self.painter.drawRect(x, y, width, height)  # Drawing a rectangle in a function; bad idea!

    def stop(self):
        """plss dont try this!"""
        self.painter.end()  # Ending it
        self.update()  # Updating

class Circle(QFrame):
    """Drawing a eclipse like frame using QPainter and QFrame"""
    def __init__(self, parent, width, height, bg: str = '#6883FF', pen_width: int = 2, pen_color: str = ...):
        super().__init__(parent)
        self.resize(width, height)  # resizing the widget
        self.bg = bg
        self.pen_color = pen_color
        self.pen_width = pen_width

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """Handles the drawing of the QFrame"""

        # Creating the painter
        self.painter = QPainter(self)
        if self.pen_color != ...:
            # creating the pen of the painter
            self.painter.setPen(QPen(QColor(self.pen_color), self.pen_width))
        else:
            # setting th QPainter pen
            self.painter.setPen(QPen(Qt.NoPen))
        # making the graphics better by setting the render hint.
        self.painter.setRenderHint(QPainter.HighQualityAntialiasing)
        # creating a brush on the painter
        self.painter.setBrush(QColor(self.bg))
        # Drawing ellipse like circle
        self.painter.drawEllipse(self.rect())
        self.painter.end()  # Ending the paint event

    def display(self, x, y):
        """displaying and updating the widget"""
        self.move(x, y)
        self.update()

class PieWidget(QFrame):
    def __init__(self, parent, width, height, a, alen, color):
        super().__init__(parent)
        self.resize(width, height)
        self.alen = alen
        self.color = color
        self.a = a
        self.setStyleSheet("""background-color: transparent;""")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setBrush(QBrush(QColor(self.color)))
        self.painter.drawPie(self.rect(), self.a, self.alen)
        self.painter.end()

    def display(self, x, y):
        self.move(x, y)
        self.update()


class DSCard(QFrame):
    def __init__(self, parent, box_width, box_height, rotate: float = ..., bg: str = '#6883FF', border_x: int = 1,
                 border_y: int = 1,
                 pen_color: str = ..., pressed: any = ..., label: str = ..., label_font=('Calibri', 25, 40, False)):
        super().__init__(parent)
        self.resize(box_width, box_height)
        self.setFixedHeight(box_height)
        self.border_x = border_x
        self.border_y = border_y
        self.rotate = rotate
        self.label = label
        self.label_font = label_font
        self.pen_color = pen_color
        self.pressed = pressed
        self.bg = bg
        self.box_lay = QVBoxLayout(self)
        self.setLayout(self.box_lay)
        self.setStyleSheet("""background-color: transparent;""")

    def addWidget(self, widget):
        self.box_lay.addWidget(widget)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.pressed != ...:
            self.pressed(self)

    def translate(self, x, y):
        self.move(x, y)

    def set_background(self, color):
        self.bg = color

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        if self.pen_color != ...:
            self.painter.setPen(QPen(QColor(self.pen_color)))
        else:
            self.painter.setPen(QPen(Qt.NoPen))
        # self.painter.rotate(20.0)
        if self.rotate != ...:
            self.painter.rotate(self.rotate)
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setBrush(QColor(self.bg))
        self.painter.drawRoundedRect(self.rect().x(), self.rect().y(), self.rect().width(), self.rect().height(),
                                     self.border_x, self.border_y)
        if self.label != ...:
            self.painter.setPen(QPen(QColor('black')))
            self.painter.setBrush(QBrush(QColor('black')))
            if self.label_font != ():
                self.painter.setFont(
                    QFont(self.label_font[0], self.label_font[1], self.label_font[2], self.label_font[3]))
            else:
                self.painter.setFont(QFont('Calibri', 25, 100, False))
            label = self.painter.drawText(
                QRect(int(self.rect().top() + self.width() / 2) - 25, int(self.rect().top() + self.height() / 2 - 25),
                      self.width(), self.height()), 0, self.label)
            # self.label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
            # self.label.setAlignment(Qt.AlignCenter)
            # self.label.setText(self.label)
            # self.box_lay.addWidget(self.label)
        self.painter.end()

    def setOpacity(self, level):
        self.painter.setOpacity(level)

    def display(self, x, y):
        self.move(x, y)
        self.update()


class Rectangle(QFrame):
    def __init__(self, parent, box_width, box_height, rotate: float = ..., bg: str = '#6883FF', border_x: int = 1,
                 border_y: int = 1,
                 pen_color: str = ..., underglow_color: str = 'grey', use_underglow: bool = True):
        super().__init__(parent)
        self.resize(box_width, box_height)
        self.setFixedHeight(box_height)
        self.border_x = border_x
        self.border_y = border_y
        self.rotate = rotate
        self.pen_color = pen_color
        self.bg = bg
        self.box_lay = QVBoxLayout(self)
        self.effect = QGraphicsDropShadowEffect()

        if use_underglow == True:
            self.effect.setColor(QColor(underglow_color))
            self.effect.setBlurRadius(8)
            self.effect.setOffset(0.4, 0.3)
            self.setGraphicsEffect(self.effect)
        self.setLayout(self.box_lay)
        self.setStyleSheet("""background-color: transparent;""")

    def addWidget(self, widget):
        self.box_lay.addWidget(widget)

    def translate(self, x, y):
        self.move(x, y)

    def set_background(self, color):
        self.bg = color

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        if self.pen_color != ...:
            self.painter.setPen(QPen(QColor(self.pen_color)))
        else:
            self.painter.setPen(QPen(Qt.NoPen))
        # self.painter.rotate(20.0)
        if self.rotate != ...:
            self.painter.rotate(self.rotate)
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setBrush(QColor(self.bg))
        self.painter.drawRoundedRect(self.rect().x(), self.rect().y(), self.rect().width(), self.rect().height(),
                                     self.border_x, self.border_y)
        self.painter.end()

    def setOpacity(self, level):
        self.painter.setOpacity(level)

    def display(self, x, y):
        self.move(x, y)
        self.update()