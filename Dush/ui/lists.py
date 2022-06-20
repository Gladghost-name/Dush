from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class CardListItem(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0.4, 0.7)
        self.effect.setBlurRadius(8)
        self.setGraphicsEffect(self.effect)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(QColor('yellow')))
        self.painter.setBrush(QBrush(QColor('white')))
        self.painter.drawRect(self.rect())
        self.painter.end()


class CardList(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.vbox_area = QVBoxLayout()
        self.vbox_area.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vbox_area)
        self.vbox = QVBoxLayout()
        # self.vbox.setContentsMargins(0, 0, 0, 0)
        self.card = QFrame()
        self.area = QScrollArea(self)
        self.vbox.addWidget(self.area)
        self.area.setStyleSheet("""background-color: blue; border: 1px;""")
        self.card.setStyleSheet("""background-color: green;""")
        self.card.setLayout(self.vbox)
        self.area.setWidget(self)
        self.vbox_area.addWidget(self.card)
    def addCard(self, CardListItem):
        self.vbox.addWidget(CardListItem)
    def display(self, x, y):
        self.move(x, y)
        self.update()
