from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys

from PySide6.QtCore import Property


class TextFlatButton(QPushButton):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.text = text
        self.resize(88, 39)
        self.clicked = False

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setBrush(QColor(5, 5, 5, 2))
        if self.clicked == True:
            self.painter.setBrush(QColor('#CCCCCC'))
        elif self.clicked == False:
            self.painter.setBrush(QColor(5, 5, 5, 2))
        self.painter.setFont(QFont('Helvetica', 8, 60, False))
        self.painter.setRenderHints(
            QPainter.TextAntialiasing | QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.drawRoundedRect(self.rect(), 1, 1)
        self.painter.setPen(QColor('#36987E'))
        self.painter.drawText(self.rect(), Qt.AlignCenter, 'CANCEL')
        self.painter.end()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.clicked = True

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.clicked = False

    def display(self, x, y):
        self.move(x, y)
        self.update()


class RaisedButton(QPushButton):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.text = text
        self.resize(88, 39)
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0, 0.7)
        self.effect.setColor(QColor('#B6B6B6'))
        self.effect.setBlurRadius(5)
        self.setGraphicsEffect(self.effect)
        self.value = 0
        self.x = self.rect().x()
        self.y = self.rect().y()
        self.clicked = False
        self.value_change = False
        self.start_animation = False
        self.c1 = QtGui.QColor(54, 152, 126)
        self.c2 = QtGui.QColor(40, 99, 84)
        self.easing = QEasingCurve()
        self.easing.setType(QEasingCurve.InOutQuad)
        self._animation = QVariantAnimation(self, valueChanged=self.value_changed)
        self._animation.setDuration(850)
        self._animation.setEasingCurve(self.easing)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setBrush(QBrush(QColor('#36987E')))
        if self.clicked == True:
            self.effect.setColor(QColor('#6D6D6D'))
            self.effect.setOffset(0, 0.9)
            self._animation.setStartValue(20)
            self._animation.setEndValue(230)
        elif self.clicked == False:
            self.effect.setColor(QColor('#B6B6B6'))
            self.effect.setOffset(0, 0.7)
        if self.value_change == True:
            self.radial = QRadialGradient(20, 18, self.value, self.x, self.y)
            self.radial.setColorAt(0.0, QColor(196, 202, 199))
            self.radial.setColorAt(0.3, QColor(196, 202, 199))
            self.radial.setColorAt(0.2, QColor(196, 202, 199))
            self.radial.setColorAt(0.4, QColor(196, 202, 199))
            self.radial.setColorAt(0.5, QColor('#36987E'))
            self.radial.setColorAt(0.9, QColor('#36987E'))
            self.painter.setOpacity(9)
            self.painter.setBrush(QBrush(self.radial))
            if self.value == self._animation.endValue():
                self.radial = QRadialGradient(32, 16, self.value, 10, 10)
                self.radial.setColorAt(0.5, QColor('#36987E'))
                self.radial.setColorAt(0.9, QColor('#36987E'))
                self.painter.setBrush(QBrush(self.radial))
                self._animation.stop()


        self.painter.setFont(QFont('Helvetica', 8, 60, False))
        self.painter.setRenderHints(
            QPainter.TextAntialiasing | QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.drawRect(self.rect())
        self.painter.setPen(QColor('#EFEFEF'))
        self.painter.drawText(self.rect(), Qt.AlignCenter, self.text)
        self.painter.end()

    def value_changed(self, value):
        self.value = value
        self.value_change = True
        self.update()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self.clicked = True
        self.x = e.pos().x()
        self.y = e.pos().y()
        self._animation.start()



    def display(self, x, y):
        self.move(x, y)
        self.update()


class RectangularButton(QPushButton):
    def __init__(self, parent, icon_file):
        super().__init__(parent)
        self.resize(100, 50)
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0.7, 0.7)
        self.effect.setColor(QColor('#8C8F8C'))
        self.effect.setBlurRadius(7)
        self.icon_file = icon_file
        self.entered = False
        self.setGraphicsEffect(self.effect)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(Qt.NoPen)
        self.painter.setBrush(QColor('#6587FF'))
        if self.entered == True:
            self.painter.setBrush(QColor('#FF6A32'))
        elif self.entered == False:
            self.painter.setBrush(QColor('#6587FF'))
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.drawRoundedRect(self.rect(), 4, 4)
        self.icon = QPixmap(self.icon_file)
        self.painter.drawPixmap(self.rect(), self.icon)
        self.resize(self.icon.width(), self.icon.height())
        self.painter.end()

    def display(self, x, y):
        self.move(x, y)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.entered = True

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.entered = False


class IconCircularButton(QPushButton):
    def __init__(self, parent, icon_file):
        super().__init__(parent)
        self.effect = QGraphicsDropShadowEffect()
        self.resize(60, 60)
        self.c = False
        self.circle_pos_x = self.rect().x()
        self.circle_pos_y = self.rect().y()
        self.effect.setOffset(0.4, 0.7)
        self.effect.setColor(QColor('grey'))
        self.effect.setBlurRadius(4)
        self.setGraphicsEffect(self.effect)
        self.setStyleSheet("""background-color: yellow;""")
        self.icon_file = icon_file
        self.entered = False

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.cone = QLinearGradient(20, 55, 27, 58)
        self.cone.setColorAt(0.0, QColor('#5360C0'))
        self.cone.setColorAt(0.5, QColor('#5360C0'))
        self.cone.setColorAt(1.0, QColor('#5A66D3'))
        self.painter.setBrush(QBrush(self.cone))
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setPen(Qt.NoPen)
        if self.entered == True:
            self.cone2 = QLinearGradient(20, 55, 27, 58)
            self.cone2.setColorAt(0.0, QColor('#EB632E'))
            self.cone2.setColorAt(0.5, QColor('#EB632E'))
            self.cone2.setColorAt(1.0, QColor('#FF6A32'))
            self.painter.setBrush(QBrush(self.cone2))
        self.painter.drawEllipse(self.rect().x(), self.rect().y(), 60, 60)
        self.icon = QPixmap(self.icon_file).scaled(32, 32, Qt.KeepAspectRatio)
        self.painter.drawPixmap(
            QRect(self.rect().left() + self.rect().width() - 46, self.rect().top() + self.rect().height() - 46,
                  self.icon.width(), self.icon.height()), self.icon)
        # self.painter.setBrush(QColor('red'))
        # self.painter.drawRoundedRect(QRect(self.rect().x()+self.rect().width()-25, self.rect().y(), 25, 15), 8, 8)
        self.painter.end()

    def display(self, x, y):
        self.move(x, y)
        self.update()

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.entered = True

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.entered = False


# app = QApplication(sys.argv)
# window = QMainWindow()
# window.resize(850, 600)
# button = RaisedButton(window, 'OK')
# button.display(50, 50)
# button1 = TextFlatButton(window, 'OK')
# button1.display(50, 100)
# button1 = RectangularButton(window,
#                             icon_file=r'C:\Users\adara\Documents\Benzel\Games\Flexer\DushExamples\bucket-images\5_level_grid.png')
# button1.display(50, 150)
# button2 = IconCircularButton(window,
#                              icon_file=r'C:\Users\adara\Documents\Benzel\Games\Flexer\DushExamples\bucket-images\5_level_grid.png')
# button2.display(50, 200)
# window.show()
# sys.exit(app.exec_())
