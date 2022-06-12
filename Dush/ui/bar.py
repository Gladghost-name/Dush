from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(85)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setBrush(QColor('#0B0B0B'))
        self.painter.drawRect(self.rect().x(), self.rect().y(), self.rect().width(), 85)
        im = QPixmap('../images/Dush.png')
        self.painter.drawPixmap(self.rect().x(), self.rect().y(), im.width(), im.height(), im)
        self.painter.setPen(QPen(QColor('white')))
        self.painter.drawText(self.rect().x(), self.rect().y(), 'Pile')
        self.painter.end()


class NavBar(QFrame):
    def __init__(self, parent, title: str = ..., color: str = 'none', text_color: str = 'none',
                 underglow_color: str = 'grey', use_underglow: bool = True, border: int = 1, border_radius: int = 1):
        super().__init__(parent)
        self.hbox = QHBoxLayout()
        self.setStyleSheet(
            f"""background-color: {color}; color: {text_color}; border-top: {border}px; border-top-radius: {border_radius}px""")
        # self.hbox.setContentsMargins(int(self.width() * 1 / 2), 0, int(self.height() * 1 / 2), 0)
        self.setLayout(self.hbox)
        if title != ...:
            self.title = QLabel(title, self)
            self.hbox.addWidget(self.title)
        self.effect = QGraphicsDropShadowEffect()
        if use_underglow == True:
            self.effect.setColor(QColor(underglow_color))
            self.effect.setBlurRadius(6)
            self.effect.setOffset(0.5, 0.4)
            self.setGraphicsEffect(self.effect)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.resize(self.parent().width(), 60)

    def addItem(self, widget: QWidget):
        self.hbox.addWidget(widget)
        widget.setStyleSheet("""background-color: #381772; color: white;""")

class TitleBar(QFrame):
    def __init__(self, parent, title: str = 'Example Title', color: str = 'none', text_color: str = 'none',
                 underglow_color: str = 'grey', use_underglow: bool = True, border: int = 1, border_radius: int = 1,
                 font_size: int = 17, icon_file: str = ..., icon_size=()):
        super().__init__(parent)
        self.hbox = QHBoxLayout()
        self.setStyleSheet(
            f"""background-color: {color}; color: {text_color}; border: {border}px; border-radius: {border_radius}px; font-size: {font_size}px;""")
        # self.hbox.setContentsMargins(int(self.width() * 1 / 2), 0, int(self.height() * 1 / 2), 0)
        self.title = QLabel(title, self)
        self.setLayout(self.hbox)
        if icon_size != ():
            self.title.setIconSize(QSize(icon_size[0], icon_size[1]))
        if icon_file != ...:
            self.title.setPixmap(QPixmap(icon_file).scaled(16, 16, Qt.KeepAspectRatio))
        self.hbox.addWidget(self.title)
        self.effect = QGraphicsDropShadowEffect()
        if use_underglow == True:
            self.effect.setColor(QColor(underglow_color))
            self.effect.setBlurRadius(6)
            self.effect.setOffset(0.5, 0.4)
            self.setGraphicsEffect(self.effect)
        self.close_button = QPushButton('X', self)
        self.close_button.setFixedWidth(10)
        self.close_button.move(self.parent().width() - self.close_button.width() - 24, 0)

        self.max_button = QPushButton('[]', self)
        self.max_button.setFixedWidth(10)
        self.max_button.move(self.parent().width() - self.close_button.width() - self.max_button.width() - 43, 0)

        self.mini_button = QPushButton('-', self)
        self.mini_button.setFixedWidth(10)
        self.mini_button.move(
            self.parent().width() - self.close_button.width() - self.max_button.width() - self.mini_button.width() - 75,
            0)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.resize(self.parent().width(), 60)
