from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys


class LineItem(QFrame):
    def __init__(self, parent, color: str = ..., width: int = 2, x1: int = 0, y1: int=0, x2: int = 0, y2: int = 50):
        super().__init__(parent)
        self.parent = parent
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.resize(x1+x2, y1+y2)
        self.pen_width = width
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setPen(QPen(QColor(self.color), self.pen_width))
        self.painter.drawLine(self.x1, self.y1, self.x2, self.y2)
        self.painter.end()

class DrawingBoard(QFrame):
    """Still a experiment of drawing on a widget"""

    def __init__(self, parent, width, height, full_scale = False):
        super().__init__(parent)
        self.parent = parent
        self.full_scale = full_scale
        if full_scale == True:
            self.resize(self.parent.width(), self.parent.height())
        else:
            self.resize(width, height)  # resizing the widget
    def addItem(self, item, x, y):
        item.setParent(self)
        item.move(x, y)
    def display(self, x, y):
        self.move(x, y)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        if self.full_scale == True:
            self.resize(self.parent.width(), self.parent.height())
        # self.painter.setPen(QPen(Qt.NoPen))
        # self.painter.setBrush(QBrush(QColor('white')))
        # self.painter.drawRect(self.rect())
        self.painter.end()


class CircleItem(QFrame):
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


class PieItem(QFrame):
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


class LDCard(QFrame):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.add_image = False
        self.image_file = ''
        self.resize(width, height)
        # Creating the graphics effect
        self.effect = QGraphicsDropShadowEffect()
        # setting the blur radius
        self.effect.setBlurRadius(8)
        # setting the offset of the effect
        self.effect.setOffset(0.4, 0.7)
        # setting a effect for the widget
        self.setGraphicsEffect(self.effect)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        # removing the pen from the painter
        self.painter.setPen(QPen(Qt.NoPen))
        # setting the brush of the painter
        self.painter.setBrush(QBrush(QColor('white')))
        # Creating and upgrading the graphics
        self.painter.setRenderHints(
            QPainter.HighQualityAntialiasing | QPainter.Antialiasing | QPainter.TextAntialiasing)
        # Drawing the rectangle for the card
        self.painter.drawRoundedRect(self.rect(), 3, 3)
        # Creating a image logic
        if self.add_image == True:
            # Creating a QPixmap
            pix = QPixmap(self.image_file)
            # Drawing the QPixmap on the screen
            self.painter.drawPixmap(self.rect().center().x()-int(pix.width()/2), self.rect().center().y()-int(pix.height()/2), pix)
        # Ending the paint event
        self.painter.end()

    def display(self, x, y):
        # Updating and displaying the widget
        self.move(x, y)
        self.update()

    def addImage(self, file):
        self.image_file = file
        self.add_image = True


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
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0.4, 0.7)
        self.effect.setBlurRadius(8)
        self.setGraphicsEffect(self.effect)
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


class RectangleItem(QFrame):
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
            self.effect.setOffset(0.4, 0.7)
            self.effect.setBlurRadius(8)
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


# app = QApplication(sys.argv)
# window = QMainWindow()
# window.resize(850, 600)
#
# window.show()
# sys.exit(app.exec_())
