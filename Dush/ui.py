from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys, os
from gradients import *

TOP = 'top'


class DushWindow(QMainWindow):
    def __init__(self, title: str = 'Dush App', icon: str = 'default',
                 x: int = None, y: int = None, width: int = 850, height: int = 600, fullscreen: bool = False,
                 bg: str = '#381772', border: str = '0px',
                 border_radius: str = '5px'):
        super().__init__()
        self.setWindowTitle(title)
        self.navbar = ''
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
        # self.layout().setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(f"""background-color: {bg};""")
        self.frame = QFrame()
        self.frame.setStyleSheet(f"""background-color: {bg}; border: {border}; border-radius: {border_radius};""")
        self.screen = QtWidgets.QDesktopWidget()
        self.setCentralWidget(self.frame)
        # self.frame.setLayout(self.layout())

    def addNavBar(self, navbar, align=TOP):
        navbar.move(0, 0)
        # navbar.setStyleSheet("""background-color: #381772;""")
        navbar.resize(self.width(), 45)
        self.navbar = navbar

    def over_all(self, b: bool = False):
        if b == True:
            self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def under_all(self, b: bool = False):
        if b == True:
            self.setWindowFlags(Qt.WindowStaysOnBottomHint)

    def remove_border(self):
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint)

    def move_right(self):
        self.move(int(self.screen.width() - self.width() / 2), 150)

    def scale_up_animation(self, x, y, sw, sh, ew, eh, duration):
        self.anim = QPropertyAnimation(self, b'geometry')
        self.anim.setDuration(duration)
        self.anim.setStartValue(QRect(x, y, sw, sh))
        self.anim.setEndValue(QRect(x, y, ew, eh))
        self.anim.start()
    def addPanel(self, area, widget):
        self.addDockWidget(area, widget)


class Image(QLabel):
    def __init__(self, parent, file, width, height, fixed_size: bool = False, fullScale: bool = False):
        super().__init__(parent)
        self.parent = parent
        self.resize(width, height)
        if fixed_size == True:
            self.pix = QPixmap(file)
        else:
            self.pix = QPixmap(file).scaled(width, height, Qt.KeepAspectRatio)
        if fullScale == True:
            self.move(0, 0)
            self.resize(430, 540)
            self.pix = QPixmap(file).scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.setPixmap(self.pix)
        self.setAlignment(Qt.AlignCenter)
    def selectable(self):
        self.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)

    def display(self, x, y):
        self.move(x, y)


class Text(QLabel):
    def __init__(self, parent, text, font: tuple = (), width: int = 50,
                 height: int = 50, x: int = 0, y: int = 0,
                 bg: str = 'none', color: str = 'white',
                 border: int = 0,
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

    def selectable(self):
        self.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)

    def editable(self):
        self.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)


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


class Button(QPushButton):
    def __init__(self, parent: QWidget, text: str = ..., color: str = 'white', bg: str = ...,
                 selectbackground: str = ..., selectforeground: str = ..., border: str = 'none',
                 border_radius: str = 'none', hoverbackground: str = ..., hoverforeground: str = ..., font: tuple = (),
                 command: any = ...):
        super().__init__(parent)
        style = []
        select = []
        overall = []
        hover = []
        if font == ():
            self.setFont(QFont('Arial Rounded MT Bold', 11, 24, False))
        if command != ...:
            self.clicked.connect(command)
        if text != ...:
            self.setText(text)
        if color != 'white':
            style.append(f'color: {color};')
        else:
            style.append(f'color: white;')
        if bg != ...:
            style.append(f'background-color: {bg};')
        if border != 'none':
            style.append(f'border: {border};')
        if border_radius != 'none':
            style.append(f'border-radius: {border_radius};')
        if selectbackground != ...:
            select.append(f'background-color: {selectbackground};')
        if selectforeground != ...:
            select.append(f'color: {selectforeground};')
        if hoverbackground != ...:
            hover.append(f'background-color: {hoverbackground};')
        if hoverforeground != ...:
            hover.append(f'color: {hoverforeground};')
        if len(hover) >= 1:
            style_hover = 'QPushButton::hover{\n\t' + '\n\t'.join(hover)
            overall.append(style_hover)
            print(overall)
        if len(style) >= 1:
            style_norm = 'QPushButton{\n\t' + '\n\t'.join(style)
            overall.append(style_norm)
        if len(select) >= 1:
            style_select = 'QPushButton::pressed{\n\t' + '\n\t'.join(select)
            overall.append(style_select)
        overall_style = '\n}\n\n'.join(overall) + '\n}'
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(0.2)
        self.effect.setOffset(0.3, 1)
        self.effect.setColor(QColor('#333334'))
        self.setGraphicsEffect(self.effect)
        self.setStyleSheet(overall_style)

    def display(self, x, y):
        self.move(x, y)

class Box(QWidget):
    def __init__(self):
        super().__init__()

class SidePanel(QDockWidget):
    def __init_(self, parent):
        super().__init__(parent)
    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setBrush(QColor(Qt.white))
        self.painter.drawRect(self.rect())
        self.painter.end()

class Link(QLabel):
    def __init__(self, parent, text, cursor=Qt.PointingHandCursor, fg: str = '#5949D2', bg: str = ..., ):
        super().__init__(parent)
        self.t = text
        self.setText(self.t)
        self.setStyleSheet("""
        QLabel{
            color: #5949D2;
            text-decoration: underline;
        }
        
        QLabel::hover{
            color: #3E69BA;
        }
        
            """)
        self.setFont(QFont('Helvetica', 9, 40, False))
        self.setCursor(cursor)
        self.adjustSize()
    def display(self, x, y):
        self.move(x, y)
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        import webbrowser
        webbrowser.open(self.text(), 1, True)

class ComboBox(QComboBox):
    def __init__(self, parent, width, height, fg= 'white', bg= '#4A91FF', handle_bg: str = '#59F56D'):
        super().__init__(parent)
        self.fg = fg
        self.bg = bg
        self.handle_bg = handle_bg
        self.resize(width, height)
    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setBrush(QBrush(QColor(self.bg)))
        self.painter.drawRect(self.rect())
        self.painter.end()
    def display(self, x, y):
        self.move(x, y)

class NavBar(QFrame):
    def __init__(self, parent, color: str = 'none'):
        super().__init__(parent)
        self.hbox = QHBoxLayout()
        self.setStyleSheet(f"""background-color: {color}""")
        # self.hbox.setContentsMargins(int(self.width() * 1 / 2), 0, int(self.height() * 1 / 2), 0)
        self.setLayout(self.hbox)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.resize(self.parent().width(), 50)


    def addItem(self, widget: QWidget):
        self.hbox.addWidget(widget)
        widget.setStyleSheet("""background-color: #381772; color: white;""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DushWindow(fullscreen=False, border= '5px', border_radius= '5px')
    box = Box()
    combo = ComboBox(widget, 100, 35)
    combo.display(10, 10)
    widget.setCentralWidget(box)
    widget.show()
    sys.exit(app.exec_())
