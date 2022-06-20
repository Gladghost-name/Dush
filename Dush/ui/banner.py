from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys


class OverlapBanner(QFrame):
    def __init__(self, parent, bg='#18181C', imagef: str = ..., header: str = ..., body: str = ...):
        super().__init__(parent)
        self.bg = bg
        self.header = header
        self.body = body
        self.parent = parent
        self.move(25, 5)
        self.file = imagef
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0, 0.7)
        self.effect.setBlurRadius(0.5)
        self.effect.setColor(QColor('#3A3D3A'))
        self.setGraphicsEffect(self.effect)
        self.setStyleSheet("""background-color: transparent;""")
        self.resize(self.parent.width() - 50, 65)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHint(QPainter.HighQualityAntialiasing)
        self.painter.setPen(QPen(Qt.NoPen))
        if self.file != ...:
            self.painter.drawPixmap(self.rect, QPixmap(self.file))
        self.painter.setBrush(QBrush(QColor(self.bg)))
        self.painter.drawRoundedRect(self.rect(), 9, 9)
        self.painter.setBrush(QBrush(QColor('red')))
        self.painter.drawRoundedRect(self.rect().width() - 85, self.rect().y(), 85,
                                     self.rect().height(), 9, 9)
        self.painter.setPen(QPen(QColor(Qt.white)))
        if self.header != ...:
            self.painter.drawText(self.rect().x() + 10, self.rect().y() + 20, self.header)
        self.painter.setFont(QFont('Helvetica', 12, 120, False))
        if self.body != ...:
            self.painter.drawText(self.rect().x() + 10, self.rect().y() + 45, self.body)
        self.painter.drawText(self.rect().width() - 68, 20, 85,
                              self.rect().height(), 0, "Close")
        self.painter.end()


class InfoBanner(QFrame):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.w = width
        self.parent = parent
        self.h = height
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0.4, 0.7)
        self.effect.setBlurRadius(8)
        self.setGraphicsEffect(self.effect)
        self.resize(width, height)
    def display(self, x, y):
        self.move(x, y)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.resize(self.parent.width()-86, self.parent.height()-130)
        print(self.w, self.h)
        self.painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setBrush(QBrush(QColor('#0081E7')))
        self.painter.drawPolygon(QPolygon([QPoint(self.width()-140, 10), QPoint(self.width()+35, 10), QPoint(self.width()-int(self.width()/2), self.height())]))
        self.painter.drawRoundedRect(self.rect().x(), self.rect().y(), self.rect().width(), self.rect().height()-45, 5, 5)
        self.painter.end()

class Banner(QFrame):
    """Helping to create a custom banner widget"""
    def __init__(self, parent: any = ..., height: int = ..., bg: str = '#2686FF', color: str = 'black'):
        super().__init__(parent)
        self.parent = parent
        self.w = self.parent.parent().width()
        self.h = height
        # self.setFixedSize(self.w, self.h)
        # Assigning all the variables
        self.text = ...
        self.draw_text = False
        self.icf = ...
        self.size = ()
        self.bg = bg
        self.color  = color
        self.ix = self.rect().x()
        self.iy = self.rect().y()
        self.tx = self.rect().x()
        self.iy = self.rect().y()
        self.draw_icon = False
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """Drawing some elements on the widgets"""
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setBrush(QColor(self.bg))
        self.painter.drawRoundedRect(self.rect(), 1, 1)
        if self.draw_text == True:
            self.painter.setFont(QFont('Calibri', 12, 115, False))
            self.painter.setPen(QColor(self.color))
            self.painter.drawText(self.rect(), 0, self.text)
        if self.draw_icon == True:
            self.pix = QPixmap(self.icf)
            self.painter.drawPixmap(self.ix, self.iy, self.pix)
        self.setFixedSize(self.parent.parent().width(), self.h)
        self.painter.end()
    def setText(self, s: str = ..., x: int = ..., y: int = ...):
        """ Setting the text of the button"""
        self.text = s
        self.tx = x
        self.ty = y
        # setting the draw text var to be true
        self.draw_text = True
    def drawIcon(self, icon_file, x, y):
        """Drawing an icon on the screen"""
        self.ix = x
        self.iy = y
        self.icf = icon_file
        # setting the draw_icon var to be true
        self.draw_icon = True

    def setSize(self, width: int = ..., height: int = ...):
        """"Setting the fixed size of the widget"""
        # setting the fixed width and height
        self.w = width
        self.h = height
        self.setFixedSize(width, height)


class TopBanner(Banner):
    def __init__(self, parent, height, bg, color):
        super().__init__(parent, height, bg, color)
        self.parent = parent
        self.move(0, 0)
    def display(self, x, y):
        self.move(x, y)
        self.update()

# app = QApplication(sys.argv)
# window = QMainWindow()
# window.resize(850, 600)
# banner = InfoBanner(window, window.width()-75, window.height()-150)
# banner.display(38, window.height()-banner.height()-20)
# window.show()
# sys.exit(app.exec_())