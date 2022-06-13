from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
from label import *

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


class ToolBar(QFrame):
    def __init__(self, parent, height, title, icon_file: str = ..., font=('Helvetica', 12, 60, False),
                 text_color: str = ..., bg_color: str = ...):
        super().__init__(parent)
        self.parent = parent
        self.height = height
        self.resize(self.parent.width(), height)
        self.setFrameStyle(QFrame.Raised)
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(1, 0.7)
        self.icon_w = 0
        self.text_color = text_color
        self.icon_h = 0
        self.font = font
        self.bg_color = bg_color
        self.effect.setBlurRadius(10)
        self.title = title
        self.icon_file = icon_file
        self.change_icon_size = False
        self.effect.setColor(QColor('#5e5e5e'))
        self.setGraphicsEffect(self.effect)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        if self.bg_color != ...:
            self.painter.setBrush(QColor(self.bg_color))
        else:
            self.painter.setBrush(QColor('#208FDB'))
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.drawRect(self.rect())
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.resize(self.parent.width(), self.height)
        if self.icon_file != ...:
            pix = QPixmap(self.icon_file)
        if self.change_icon_size == True:
            pix = pix.scaled(self.icon_w, self.icon_h)
        if self.icon_file != ...:
            pix = pix.scaled(pix.width(), self.rect().height(), Qt.KeepAspectRatio)
            self.painter.drawPixmap(self.rect().x(), self.rect().y(), pix.width(), self.rect().height(), pix)
        else:
            pix = QPixmap('../window_images/window-icon.png').scaled(10, 10)
        if self.text_color != ...:
            self.painter.setPen(QColor(self.text_color))
        else:
            self.painter.setPen(QPen(Qt.white))
        self.painter.setFont(QFont(self.font[0], self.font[1], self.font[2], self.font[3]))
        self.painter.drawText(self.rect().x() + 10 + pix.width(), self.rect().y(), self.rect().width(),
                              self.rect().height(),
                              Qt.AlignVCenter, self.title)

        self.painter.end()

    def setIconSize(self, w, h):
        self.icon_w = w
        self.icon_h = h
        self.change_icon_size = True

    def display(self, x, y):
        self.move(x, y)

    def addLeftItem(self, widget):
        widget.setParent(self)
        widget.move(self.width()-widget.width()+5)

class NavBarIconTextButton(QFrame):
    def __init__(self, parent, text, width, height, icon_file: str = ...):
        super().__init__(parent)
        self.resize(width, height)
        self.parent = parent
        self.vbox  = QVBoxLayout()
        self.vbox.setContentsMargins(0, 10, 0, 10)
        self.setLayout(self.vbox)
        if icon_file != ...:
            self.icon = QLabel(self)
            self.icon.setAlignment(Qt.AlignCenter)
            self.icon.setPixmap(QPixmap(icon_file).scaled(24, 24, Qt.KeepAspectRatio))
            self.vbox.addWidget(self.icon)
        self.label = QLabel(self)
        self.setStyleSheet("""background-color: transparent;""")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(text)
        self.label.setStyleSheet("""background-color: transparent; color: white;""")
        self.vbox.addWidget(self.label)


class BottomNavBar(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.resize(self.parent.width(), 67)
        self.hbox = QHBoxLayout()
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.effect = QGraphicsDropShadowEffect()
        # self.effect.setOffset(0.7, 0)
        self.effect.setColor(QColor('#5e5e5e'))
        self.setGraphicsEffect(self.effect)
        self.setLayout(self.hbox)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setBrush(QBrush(QColor('#208FDB')))
        self.painter.drawRect(self.rect())
        self.resize(self.parent.width(), 67)
        self.move(0, self.parent.height() - self.height())
        self.painter.end()
    def display(self,x, y):
        self.move(x, y)
    def setWidget(self, widget):
        self.move(0, self.parent.height()-self.height())
    def addScreen(self, label: str = '', icon_file: str = ...):
        master_frame = QFrame(self)
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        master_frame.setLayout(hbox)
        if icon_file != ...:
            self.widget = NavBarIconTextButton(self, label, 100, 100, icon_file)
        else:
            self.widget = NavBarIconTextButton(self, label, 100, 100)
        hbox.addWidget(self.widget)
        self.hbox.addWidget(master_frame)

app = QApplication(sys.argv)
window = QMainWindow()
window.resize(850, 600)
bnav = BottomNavBar(window)
bnav.addScreen('Python', icon_file='C:/Users/adara/Downloads/python.png')
bnav.setWidget(window)
toolbar = ToolBar(window, 65, 'facebook', font=('Helvetica', 13, 110, False), text_color='white', bg_color='orange')
toolbar.display(0, 0)
window.show()
sys.exit(app.exec_())
