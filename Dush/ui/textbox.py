from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class RichTextBox(QTextEdit):
    def __init__(self, parent, width, height, bg: str = '#17AEFF', fg: str = 'white', border: str = '2px',
                 border_radius: str = '2px'):
        super().__init__(parent)
        self.resize(width, height)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0.4, 0.5)
        self.effect.setBlurRadius(0.5)
        self.effect.setColor(QColor(Qt.gray))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet(f"""background-color: {bg}; color: {fg}; border: {border}; border-radius: {border_radius}""")

    def display(self, x, y):
        self.move(x, y)