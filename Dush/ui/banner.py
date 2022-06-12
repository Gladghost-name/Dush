from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


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