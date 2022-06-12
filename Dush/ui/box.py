from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class Box(QWidget):
    """A Box to add other widgets"""

    def __init__(self):
        super().__init__()


class ComboBox(QComboBox):
    """ Creating a stylish comboBox from QComboBox"""
    def __init__(self, parent, width, height, fg='white', bg='#4A91FF', handle_bg: str = '#59F56D',
                 icon_file: str = '../images/Dush.png'):
        super().__init__(parent)
        # Setting up all the vars
        self.fg = fg
        self.icon_file = icon_file
        self.bg = bg
        self.handle_bg = handle_bg

        # resizing the widget
        self.resize(width, height)

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        """handles drawing the widget"""
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setBrush(QBrush(QColor(self.bg)))
        self.painter.drawRoundedRect(self.rect(), 5, 5)
        self.painter.setBrush(QBrush(QColor(self.handle_bg)))
        self.painter.drawRoundedRect(QRect(self.rect().width() - 35, self.rect().y(), 35, self.rect().height()), 5, 5)
        self.painter.drawPixmap(QRect(self.rect().width() - 35, self.rect().y(), 35, self.rect().height()),
                                QPixmap(self.icon_file))
        self.painter.setPen(QPen(QColor(self.fg)))
        self.painter.setFont(QFont('Helvetica', 10, 45, False))
        # Drawing txt on the screen
        self.painter.drawText(
            QRect(self.rect().left(), int(self.y() / 2), self.rect().width(),
                  self.rect().height()), 0, self.currentText())
        self.painter.end()

    def display(self, x, y):
        # displaying and updating the widget on the screen
        self.move(x, y)
        self.update()