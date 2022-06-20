from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys


class SidePanel(QSplitter):
    """ Creating a panel at  SIDE OF THE SCREEN"""

    def __init_(self, parent):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """Handles the drawing of the widget"""
        self.painter = QPainter(self)
        self.painter.setBrush(QColor(Qt.white))
        self.painter.drawRect(self.rect())
        self.painter.end()


class WindowPanel(QFrame):
    def __init__(self, parent, title: str = ..., color: str = '#36539D', bg: str = '#4B99FF'):
        super().__init__(parent)
        # self.resize(370, 680)
        self.move(30, 30)
        self.parent = parent
        self.color = color
        self.bg = bg
        self.title = title
        self.setStyleSheet("""background-color: transparent;""")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setBrush(QColor(self.bg))
        self.resize(370, self.parent.height() - 50)
        self.painter.drawRoundedRect(self.rect(), 7, 7)
        self.painter.setBrush(QColor(self.color))
        self.painter.setPen(QColor('grey'))
        self.painter.drawLine(self.rect().x() + self.width(), self.rect().y() + 6, self.rect().x() + self.width(),
                              self.rect().y() + self.height() - 6)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.drawRoundedRect(self.rect().x(), self.rect().y(), self.rect().width(), 35, 2, 2)
        self.painter.setPen(QPen(Qt.white))
        self.painter.setFont(QFont('Helvetica', 9, 55, False))
        self.painter.drawPixmap(self.rect().x(), self.rect().y(), 35, 35, QPixmap("../images/Dush.png"))
        if self.title != ...:
            self.painter.drawText(self.rect().x() + 39, self.rect().y() + 8, self.rect().width(), self.rect().height(),
                                  0, self.title)
        self.painter.end()


class DropDownPanel(QFrame):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.resize(width, height)
        self.hbox = QHBoxLayout(self)
        self.frame = QFrame(self)
        self.frame.setStyleSheet("""background-color: yellow; border: 5px; border-radius: 5px;""")
        self.frame.resize(self.width(), 12)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.hbox)
        self.hbox.addWidget(self.frame)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setBrush(QBrush(QColor('#fefefe')))
        self.painter.drawRoundedRect(self.rect(), 5, 5)
        self.painter.end()

    def display(self, x, y):
        self.move(x, y)


class Panel(QDockWidget):
    def __init__(self, parent: any = ..., bg_color: str = 'white', closable: bool = False, movable: bool = False,
                 underglow_color: str = '#CBCBCB'):
        super().__init__(parent)
        self.bg_color = bg_color
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setColor(QColor(underglow_color))
        self.effect.setOffset(0.7, 0.4)
        self.effect.setBlurRadius(5)
        self.setGraphicsEffect(self.effect)
        if closable == False and movable == True:
            self.setFeatures(QDockWidget.DockWidgetMovable)
        elif movable == False and closable == True:
            self.setFeatures(QDockWidget.DockWidgetClosable)
        elif movable == False and closable == False:
            self.setFeatures(QDockWidget.NoDockWidgetFeatures)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setBrush(QColor(self.bg_color))
        self.painter.drawRect(self.rect())
        self.painter.end()

    def display(self, x, y):
        self.move(x, y)
        self.update()