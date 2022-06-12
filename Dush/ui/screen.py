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
