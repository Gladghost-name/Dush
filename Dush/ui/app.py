from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys

TOP = 'top'
DARK = 200
LIGHT = 300
HORIZONTAL = 330
VERTICAL = 430
GRIDED = 530


class QtApp(QApplication):
    """Modified from QApplication which makes window development easier"""

    def __init__(self, title: str = 'Dush App', icon: str = 'default',
                 x: int = None, y: int = None, width: int = 850, height: int = 600, fullscreen: bool = False,
                 bg: str = 'white', border: str = '0px',
                 border_radius: str = '5px', name='QtApp'):
        super().__init__(sys.argv)
        self.window = QMainWindow()  # Creating the main window
        self.window.setWindowTitle(title)  # Setting the title
        self.navbar = ''
        self.setObjectName(name)
        if x != None and y != None:
            self.window.move(x, y)  # window should move by the x and y coords
        if fullscreen is not True:
            self.window.resize(width, height)  # window should resize with the width and height vars
        else:
            self.window.showMaximized()  # Show the window maximized
        if icon != 'default':
            self.window.setWindowIcon(QIcon(icon))  # Set the window icon if the icon is not the default
        else:
            self.window.setWindowIcon(QIcon('../Dush/window-icon.png'))  # Set the default icon
        self.window.setStyleSheet(f"""background-color: {bg};""")  # Set the default background color for the window
        self.status = QStatusBar()  # making the status bar instance
        icon = QLabel()  # Creating the label instance
        icon.setPixmap(QPixmap('../images/Dush.png').scaled(28, 28, Qt.KeepAspectRatio))  # Setting a image to the label
        self.bhbox = QHBoxLayout()
        self.back = QFrame()
        self.back.setLayout(self.bhbox)
        self.bhbox.setContentsMargins(0, 0, 0, 0)
        self.box = QFrame()
        self.bhbox.addWidget(self.box)
        self.hbox = QVBoxLayout()
        self.box.setLayout(self.hbox)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.app_box = []
        # self.frame = QFrame()  # Creating the frame instance
        # self.hbox.addWidget(self.frame)
        # self.vbox = QVBoxLayout()  # Creating the vbox instance
        self.bg = bg  # assigning self.bg to bg
        # self.frame.setLayout(self.vbox)  # setting the frame layout to self.vbox
        # self.frame.setStyleSheet(
        #     f"""background-color: {bg}; border: {border}; border-radius: {border_radius};""")  # setting a stylesheet for the widget
        self.screen = QtWidgets.QDesktopWidget()  # Getting the widget for the actual screen
        self.window.setCentralWidget(self.back)  # setting the central widget for the screen



    def setOrientType(self, type):
        """Setting the Orientation of the widgets in the frame"""
        if type == HORIZONTAL:
            self.hbox = QHBoxLayout()  # Creating a QHBoxLayout which is horizontal
            self.frame.setLayout(self.hbox)  # setting the layout of the frame to be self.hbox
        elif type == VERTICAL:
            self.vbox = QVBoxLayout()  # Creating a QVBoxLayout which is vertical
            self.frame.setLayout(self.vbox)  # setting the frame layout to be self.vbox
        elif type == GRIDED:
            self.gridbox = QGridLayout()  # Creating a QGridLayout which which needs a grid
            self.frame.setLayout(self.grid)  # setting the layout of the frame to be self.gridbox

    def addNavBar(self, navbar, align=TOP):
        """Adding a navbar to the top of the screen"""
        navbar.move(0, 0)  # Moving the navbar to the top of the window
        navbar.resize(self.window.width(), 45)  # resizing the navbar to fit the window width
        self.navbar = navbar  # setting the navbar to be a instance of self

    def over_all(self, b: bool = False):
        """Window should stay over al the other windows opened on the screen"""
        if b == True:
            self.window.setWindowFlag(Qt.WindowStaysOnTopHint)  # Placing the window o over the other windows

    def setMode(self, mode):
        """Switching between light or dark
        """
        if mode == DARK:
            self.frame.setStyleSheet(f"""background-color: #000311;""")  # Setting the window color to be dark
        elif mode == LIGHT:
            self.frame.setStyleSheet(f"""background-color: {self.bg};""")  # setting the window to be it's default

    def under_all(self, b: bool = False):
        """Placing the window below the other windows in the screen"""
        if b == True:
            self.window.setWindowFlags(  # Setting a window flag
                Qt.WindowStaysOnBottomHint)  # Window should only stay in the bottom of the other widgets

    def remove_border(self):
        """Removing the border of the windows"""
        self.window.setAttribute(Qt.WA_NoSystemBackground, True)  # removing the system background
        self.window.setAttribute(Qt.WA_TranslucentBackground, True)  # Creating a translucent window
        self.window.setWindowFlags(
            Qt.FramelessWindowHint | Qt.CustomizeWindowHint)  # Creating both a frameless window and customizable window

    def move_right(self):
        """simply moving the window to the right; from a test made!; It is an experiment!"""
        self.window.move(int(self.screen.width() - self.width() / 2),
                         150)  # trying to move the window on your screen to the left

    def scale_up_animation(self, x, y, sw, sh, ew, eh, duration):
        """Creating a simple experimented scroll-up animation"""
        self.anim = QPropertyAnimation(self, b'geometry')  # Creating a QPropertyAnimation
        self.anim.setDuration(duration)  # setting the duration for the animation
        self.anim.setStartValue(QRect(x, y, sw, sh))  # setting the start value of the scale and location
        self.anim.setEndValue(QRect(x, y, ew, eh))  # Setting the End Value
        self.anim.start()  # Starting the animation

    def title(self, text: str = 'PyQt Application'):
        """Creating a title for the window"""
        self.window.setWindowTitle(text)  # Setting the window title

    def size(self, width, height):
        """setting the size of the window"""
        self.window.setFixedSize(width, height)  # resizing the window

    def display(self, x, y):
        """moving the window to the x and y coordinate"""
        self.window.move(x, y)  # moving the window

    def loop(self):
        """Handles the drawing, looping and close event"""
        self.window.show()  # showing the window on the screen
        sys.exit(self.exec_())  # setting the close event

    def addPanel(self, area, widget):
        """Adding a panel on the window"""
        self.window.addDockWidget(area, widget)  # Adding the panel in the area specified

    def icon(self, file):
        icon = QIcon(file)
        self.window.setWindowIcon(icon)

    def addSideBar(self, widget):
        self.box.addWidget(widget)

    def addToolbar(self, toolbar):
        self.box.layout().addWidget(toolbar)

    def addAppBox(self, appBox):
        self.app_box.append(appBox)
        self.box.layout().addWidget(appBox)

    def addSideBar(self, sidebar):
        self.bhbox.addWidget(sidebar)

class DushWindow(QMainWindow):
    """A Much more complicated method of creating a window using the normal method of using pyqt5"""

    def __init__(self, title: str = 'Dush App', icon: str = 'default',
                 x: int = None, y: int = None, width: int = 850, height: int = 600, fullscreen: bool = False,
                 bg: str = 'white', border: str = '0px',
                 border_radius: str = '5px'):
        super().__init__()
        self.setWindowTitle(title)  # Setting the window Title
        self.navbar = ''  # setting a navbar instance
        if x != None and y != None:
            self.move(x, y)  # moving the window on the x and y coords
        if fullscreen is not True:
            self.resize(width, height)  # resize the window to be full screen
        else:
            self.showMaximized()  # show the window being maximized
        if icon != 'default':
            self.setWindowIcon(QIcon(icon))  # Setting the window icon
        else:
            self.setWindowIcon(QIcon(r'C:\Users\adara\Documents\Benzel\Games\Flexer\Dush\window_images\window-icon.png'))  # Setting the window icon as default
        self.setStyleSheet(f"""background-color: {bg};""")  # Setting the background color of the window
        self.status = QStatusBar()  # Creating a status bar
        icon = QLabel()  # Creating the label
        icon.setPixmap(
            QPixmap('../images/Dush.png').scaled(28, 28, Qt.KeepAspectRatio))  # Creating the pixmap of the label
        self.frame = QFrame()  # Creating the frame instance
        self.vbox = QVBoxLayout()  # Creating a vbox layout which is vertical
        # setting the alignment for the layout
        self.vbox.setAlignment(Qt.AlignCenter)
        self.bg = bg  # setting the background color to be self.bg
        self.frame.setLayout(self.vbox)  # setting the layout to be the self.vbox
        self.frame.setStyleSheet(
            f"""background-color: {bg}; border: {border}; border-radius: {border_radius};""")  # Setting a style sheet to the window frame
        self.screen = QtWidgets.QDesktopWidget()  # Getting the actual screen widgets which encompasses the window
        self.setCentralWidget(self.frame)  # setting the central widget to be the frame created above

    def addWidget(self, widget):
        """ Adding a widget to the layout of the frame"""
        self.frame.layout().addWidget(widget)  # Adding the widget to the layout

    def setSpacing(self, level):
        """setting the spacing of the layout"""
        self.frame.layout().setSpacing(level)

    def setOrientType(self, type):
        """Setting the Orientation of the widgets in the frame"""
        if type == HORIZONTAL:
            self.hbox = QHBoxLayout()  # Creating a QHBoxLayout which is horizontal
            self.frame.setLayout(self.hbox)  # setting the layout of the frame to be self.hbox
        elif type == VERTICAL:
            self.vbox = QVBoxLayout()  # Creating a QVBoxLayout which is vertical
            self.frame.setLayout(self.vbox)  # setting the layout of the frame to be self.vbox
        elif type == GRIDED:
            self.gridbox = QGridLayout()  # Creating a QGridLayout which which needs a grid
            self.frame.setLayout(self.gridbox)  # setting the layout of the frame to be self.gridbox

    def addNavBar(self, navbar, align=TOP):
        """Adding a navbar to the top of the screen"""
        navbar.move(0, 0)  # Moving the navbar to the top of the window
        navbar.resize(self.width(), 45)  # resizing the navbar to fit the window width
        self.navbar = navbar  # setting the navbar to be a instance of self

    def over_all(self, b: bool = False):
        """Window should stay over al the other windows opened on the screen"""
        if b == True:
            self.setWindowFlag(Qt.WindowStaysOnTopHint)  # Placing the window o over the other windows

    def setMode(self, mode):
        """Switching between light or dark
        """
        if mode == DARK:
            self.frame.setStyleSheet(f"""background-color: #000311;""")  # Setting the window color to be dark
        elif mode == LIGHT:
            self.frame.setStyleSheet(f"""background-color: {self.bg};""")  # setting the window to be it's default

    def under_all(self, b: bool = False):
        """Placing the window below the other windows in the screen"""
        if b == True:
            self.setWindowFlags(  # Setting a window flag
                Qt.WindowStaysOnBottomHint)  # Window should only stay in the bottom of the other widgets

    def remove_border(self):
        """Removing the border of the windows"""
        self.setAttribute(Qt.WA_NoSystemBackground, True)  # removing the system background
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # Creating a translucent window
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.CustomizeWindowHint)  # Creating both a frameless window and customizable window

    def move_right(self):
        """simply moving the window to the right; from a test made!; It is an experiment!"""
        self.move(int(self.screen.width() - self.width() / 2),
                  150)  # trying to move the window on your screen to the left

    def scale_up_animation(self, x, y, sw, sh, ew, eh, duration):
        """Creating a simple experimented scroll-up animation"""
        self.anim = QPropertyAnimation(self, b'geometry')  # Creating a QPropertyAnimation
        self.anim.setDuration(duration)  # setting the duration for the animation
        self.anim.setStartValue(QRect(x, y, sw, sh))  # setting the start value of the scale and location
        self.anim.setEndValue(QRect(x, y, ew, eh))  # Setting the End Value
        self.anim.start()  # Starting the animation

    def addPanel(self, area, widget):
        """Adding a panel on the window"""
        self.addDockWidget(area, widget)  # Adding the panel in the area specified

class AppBox(QFrame):
    """ A AppBox Placed after the Toolbar"""
    def __init__(self, app_window):
        super().__init__(app_window)
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vbox)
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setBrush(QColor('white'))
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.drawRect(self.rect())
        self.painter.end()
    def addWidget(self, widget):
        """ Adding a widget to the layout of the frame"""
        self.layout().addWidget(widget)
        self.layout().setAlignment(Qt.AlignCenter)