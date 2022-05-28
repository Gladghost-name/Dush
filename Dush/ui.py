from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys, os
from gradients import *


class DushWindow(QMainWindow):
    def __init__(self, title: str = 'Dush App', icon: str = 'default',
                 x: int = None, y: int = None, width: int = 850, height: int = 600, fullscreen: bool = False,
                 bg: str = LinearGradient('0', '0', '1', '0', '#381772', '#481E90')):
        super().__init__()
        self.setWindowTitle(title)
        if x != None and y != None:
            self.move(x, y)
        if fullscreen is not True:
            self.resize(width, height)
        else:
            self.showMaximized()
        if icon != 'default':
            self.setWindowIcon(QIcon(icon))
        else:
            self.setWindowIcon(QIcon('window-icon.png'))
        self.setStyleSheet(f"""background-color: {bg}""")


class DLabel(QLabel):
    def __init__(self, parent, text, font: tuple = (), width: int = 50,
                 height: int = 50, x: int = 0, y: int = 0, bg: str = LinearGradient('0', '0', '1', '0', '#381772', '#481E90'), color: str = 'white', border: int = 0,
                 border_radius: int = 0, type: str = 'none'):
        super().__init__(parent)
        self.move(x, y)
        self.text = text

        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0, 0.3)
        self.effect.setColor(QColor('grey'))
        self.effect.setBlurRadius(0.5)
        self.setGraphicsEffect(self.effect)

        self.pl = parent
        self.setText(self.text)
        self.resize(width, height)
        # self.resize(width, height)
        self.setAlignment(Qt.AlignCenter)
        if font != ():
            self.setFont(QFont(font[0], font[1], font[2], font[3]))
        else:
            self.setFont(QFont('Arial Rounded MT Bold', 11, 24, False))
        self.setStyleSheet(
            f"""background-color: {bg}; color: {color}; border: {str(border)}px; border-radius: {str(border_radius)}px;""")

    def display(self):
        self.pl.setCentralWidget(self)

    def place(self, x, y):
        self.move(x, y)

LINK = 'link'

class IconCircularButton(QPushButton):
    def __init__(self, parent, text, x, y):
        super().__init__(parent)
        self.t = text
        self.painter = ''
        self.move(x, y)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setBrush(QColor('#332EC3'))
        self.painter.setPen(QPen(Qt.NoPen))
        image = QImage(r"C:\Users\adara\Downloads\layers.png")
        self.painter.setRenderHints(
            QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.Antialiasing)
        self.painter.drawEllipse(self.rect().x(), self.rect().y(), image.size().width(), image.size().height())
        self.painter.drawImage(self.rect().x(), self.rect().y(), image, 0, 0, image.rect().width() + 10,
                               image.rect().height() + 10)
        self.painter.setPen(QPen(QColor(Qt.white)))
        self.resize(image.size().width() + 70, image.size().height() + 70)
        self.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vbox = QVBoxLayout()
    widget = DushWindow(fullscreen=False)
    widget.setLayout(vbox)
    label = DLabel(widget,
                   'Start Developing!',
                   x=100,
                   y=100,
                   width=500,
                   border = 5,
                   border_radius=5
                   )
    label.display()
    widget.show()
    sys.exit(app.exec_())
