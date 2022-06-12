from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class SidePanel(QDockWidget):
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


