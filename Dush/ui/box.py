from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class Box(QWidget):
    """A Box to add other widgets"""

    def __init__(self):
        super().__init__()


class ComboBox(QComboBox):
    """ Creating a stylish comboBox from QComboBox"""

    def __init__(self, parent, width, height, fg='white', bg='#4A91FF', handle_bg: str = '#59F56D',
                 icon_file: str = '../images/Dush.png'):
        super().__init__(parent)
        # Setting up all the vars
        self.fg = fg
        self.icon_file = icon_file
        self.bg = bg
        self.handle_bg = handle_bg

        # resizing the widget
        self.resize(width, height)

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        """handles drawing the widget"""
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setBrush(QBrush(QColor(self.bg)))
        self.painter.drawRoundedRect(self.rect(), 5, 5)
        self.painter.setBrush(QBrush(QColor(self.handle_bg)))
        self.painter.drawRoundedRect(QRect(self.rect().width() - 35, self.rect().y(), 35, self.rect().height()), 5, 5)
        self.painter.drawPixmap(QRect(self.rect().width() - 35, self.rect().y(), 35, self.rect().height()),
                                QPixmap(self.icon_file))
        self.painter.setPen(QPen(QColor(self.fg)))
        self.painter.setFont(QFont('Helvetica', 10, 45, False))
        # Drawing txt on the screen
        self.painter.drawText(
            QRect(self.rect().left(), int(self.y() / 2), self.rect().width(),
                  self.rect().height()), 0, self.currentText())
        self.painter.end()

    def display(self, x, y):
        # displaying and updating the widget on the screen
        self.move(x, y)
        self.update()


class TextInput(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(5)
        self.setText('Hello, Word')
        self.setStyleSheet("""
        QLineEdit{
            background-color: transparent;
            border-bottom: 2px solid orange;
        }
        
        """)
        # self.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
        self.setFixedSize(230, 23)

    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     self.painter = QPainter(self)
    #     self.painter.drawText(self.rect(), Qt.AlignLeft, 'Hello')
    #     self.painter.setPen(QColor('#0280D6'))
    #     self.painter.drawLine(0, self.height()-6, self.width(), self.height()-6)
    #     self.painter.end()
    def display(self, x, y):
        self.move(x, y)

class IterateButton(QPushButton):
    def __init__(self, parent, file):
        super().__init__(parent)
        self.file = file
        self.setStyleSheet("""background-color: transparent;""")
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setBrush(QColor('white'))
        self.painter.drawRoundedRect(self.rect(), 25, 25)
        pix = QPixmap(self.file)
        self.painter.drawPixmap(self.rect().x(), self.rect().y(), pix)
        self.painter.end()

class IterateText(QLabel):
    def __init__(self, parent, text, font=()):
        super().__init__(parent)
        self.text = str(text)
        self.setFont(QFont(font[0], font[1], font[2], font[3]))
        self.setText(self.text)
        self.parent = parent
        self.setStyleSheet("""background-color: transparent; color: grey;""")

class IterateBox(QFrame):
    def __init__(self, parent, from_: int = 0, to: int = 100):
        super().__init__(parent)
        self.parent = parent
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0.4, 0.7)
        self.effect.setBlurRadius(8)
        self.from_ = from_
        self.to = to
        self.hbox = QHBoxLayout()
        # self.hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.hbox)
        self.left_button = IterateButton(self, 'C:/Users/adara/Downloads/left-arrow.png')
        self.left_button.setFixedWidth(30)
        self.left_button.clicked.connect(self.go_back)
        self.hbox.addWidget(self.left_button)
        self.text = IterateText(self, 0, font=('Calibri', 20, 50, False))
        self.text.setAlignment(Qt.AlignCenter)
        self.t = int(self.text.text)
        self.hbox.addWidget(self.text)
        self.right_button = IterateButton(self, 'C:/Users/adara/Downloads/right-arrow.png')
        self.right_button.setFixedWidth(30)
        self.right_button.clicked.connect(self.go_forward)
        self.hbox.addWidget(self.right_button)
        self.text.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
        self.setStyleSheet("""background-color: transparent;""")
        self.setGraphicsEffect(self.effect)
        self.setFixedSize(150, 50)

    def go_back(self):
        if self.t != self.from_:
            self.t-=5
            self.text.setText(str(self.t))
            self.text.adjustSize()

    def go_forward(self):
        if self.t != self.to:
            self.t += 5
            self.text.setText(str(self.t))
            self.text.adjustSize()
            self.text.update()
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.HighQualityAntialiasing)
        self.painter.setBrush(QColor('white'))
        self.painter.drawRoundedRect(self.rect(), 25, 25)
        self.painter.end()

    def display(self, x, y):
        self.move(x, y)
