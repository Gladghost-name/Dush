from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class vertUnknown(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(QColor('#129CFF'), 4, cap=Qt.RoundCap))
        self.painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setBrush(QBrush(Qt.NoBrush))
        self.painter.drawArc(self.rect().x()+300, self.rect().y()+400, 50, 50, 50, 500)
        # self.painter.drawPie(self.rect().x()+300, self.rect().y()+400, 100, 100, 2500, 2800)
        self.painter.end()
    def display(self, x, y):
        self.move(x, y)
        self.update()
