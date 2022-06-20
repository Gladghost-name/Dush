from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class Screen(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def add(self, widget):
        self.addWidget(widget)

    def switch(self, m: int = 0):
        self.setCurrentIndex(m)

    def go_forward(self, max_indexes):
        if self.currentIndex() < max_indexes:
            self.setCurrentIndex(self.currentIndex() + 1)

    def go_back(self):
        if self.currentIndex() != 0:
            self.setCurrentIndex(self.currentIndex() - 1)

class RoundedDisplay(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(50, 50)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(QColor(197, 197, 197), 2))
        self.painter.setBrush(QColor(45, 159, 255))
        self.painter.setOpacity(20.0)
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.drawEllipse(self.rect().x()+10, self.rect().y()+10, 20, 20)
        self.painter.end()


class InfoScreen(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.vbox = QVBoxLayout()
        self.mframe = QFrame(self)
        self.mframe.setLayout(self.vbox)
        self.top_box = QFrame(self)
        self.vbox.addWidget(self.top_box)
        self.hbox = QHBoxLayout()
        self.bottom_box = QFrame(self)
        self.bottom_box.setFixedHeight(220)
        self.bottom_box.setLayout(self.hbox)
        self.vbox.addWidget(self.bottom_box)
        self.info = RoundedDisplay(self.bottom_box)
        self.hbox.addWidget(self.info)
        # self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setAlignment(Qt.AlignCenter)
        self.addWidget(self.mframe)