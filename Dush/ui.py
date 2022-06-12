from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys, os

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
                 border_radius: str = '5px'):
        super().__init__(sys.argv)
        self.window = QMainWindow()  # Creating the main window
        self.window.setWindowTitle(title)  # Setting the title
        self.navbar = ''
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
        self.frame = QFrame()  # Creating the frame instance
        self.vbox = QVBoxLayout()  # Creating the vbox instance
        self.bg = bg  # assigning self.bg to bg
        self.frame.setLayout(self.vbox)  # setting the frame layout to self.vbox
        self.frame.setStyleSheet(
            f"""background-color: {bg}; border: {border}; border-radius: {border_radius};""")  # setting a stylesheet for the widget
        self.screen = QtWidgets.QDesktopWidget()  # Getting the widget for the actual screen
        self.window.setCentralWidget(self.frame)  # setting the central widget for the screen

    def addWidget(self, widget, gx: int = 0, gy: int = 0):
        """ Adding a widget to the layout of the frame"""
        if self.frame.layout() == QGridLayout():
            self.frame.layout().addWidget(widget, gx, gy)  # add a widget to the frame with rows and columns
        else:
            self.frame.layout().addWidget(widget)  # add widget to the frame normally

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
        self.window.resize(width, height)  # resizing the window

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
            self.setWindowIcon(QIcon('window-icon.png'))  # Setting the window icon as default
        self.setStyleSheet(f"""background-color: {bg};""")  # Setting the background color of the window
        self.status = QStatusBar()  # Creating a status bar
        icon = QLabel()  # Creating the label
        icon.setPixmap(
            QPixmap('../images/Dush.png').scaled(28, 28, Qt.KeepAspectRatio))  # Creating the pixmap of the label
        self.frame = QFrame()  # Creating the frame instance
        self.vbox = QVBoxLayout()  # Creating a vbox layout which is vertical
        self.bg = bg  # setting the background color to be self.bg
        self.frame.setLayout(self.vbox)  # setting the layout to be the self.vbox
        self.frame.setStyleSheet(
            f"""background-color: {bg}; border: {border}; border-radius: {border_radius};""")  # Setting a style sheet to the window frame
        self.screen = QtWidgets.QDesktopWidget()  # Getting the actual screen widgets which encompasses the window
        self.setCentralWidget(self.frame)  # setting the central widget to be the frame created above

    def addWidget(self, widget, gx: int = 0, gy: int = 0):
        """ Adding a widget to the layout of the frame"""
        if self.frame.layout() == QGridLayout():
            self.frame.layout().addWidget(widget, gx, gy)  # add a widget to the frame with rows and columns
        else:
            self.frame.layout().addWidget(widget)  # add widget to the frame normally

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


class FakeImage(QFrame):
    """ Creating a image using only a QPainter Pixmap"""

    def __init__(self, parent, file, im_width: int = ..., im_height: int = ...):
        super().__init__(parent)
        """Setting all the useful variables"""
        self.file = file  # setting file to be a instance of self
        self.w = im_width  # setting im_width to be a instance of self
        self.h = im_height  # setting im_height to be a instance of self

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """Painting the pixmap on the widget"""
        self.painter = QPainter(self)  # initialize the painter
        self.painter.setRenderHint(
            QPainter.HighQualityAntialiasing)  # setting the render hint to improve the rough edges
        if self.w != ... and self.height != ...:
            self.painter.drawPixmap(QRect(self.rect().left(), self.rect().top(), self.w, self.h),
                                    QPixmap(self.file).scaled(self.w, self.h,
                                                              Qt.KeepAspectRatio))  # Drawing the pixmap on the screen
        else:
            self.painter.drawPixmap(self.rect(), QPixmap(self.file))  # drawing the pixmap normally
        self.painter.end()  # ending the paint event


class RealImage(QLabel):
    """Creating the RealImage from a QLabel only"""

    def __init__(self, parent, file, width, height, fixed_size: bool = False, fullScale: bool = False):
        super().__init__(parent)
        self.parent = parent
        self.resize(width, height)
        if fixed_size == True:
            self.pix = QPixmap(file)  # setting the pixmap with a file
        else:
            self.pix = QPixmap(file).scaled(width, height,
                                            Qt.KeepAspectRatio)  # setting a pixmap with a file which is scaled
        if fullScale == True:
            self.move(0, 0)  # moving the widget to coordinate (0, 0)
            self.resize(430, 540)  # resizing the widget
            self.pix = QPixmap(file).scaled(self.width(), self.height(), Qt.KeepAspectRatio)  # Creating a scaled pixmap
        self.setPixmap(self.pix)  # Setting the label pixmap to be self.pix
        self.setAlignment(Qt.AlignCenter)  # Aligning the image to the center of the widget

    def middle_fixed(self):
        """placing the widget and the image at the center of the widget's parent"""
        self.move(int(self.parent.width() * 1 / 2), int(self.parent.height() * 1 / 2))

    def selectable(self):
        """Make the image selectable with the mouse and keyboard"""
        self.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)

    def display(self, x, y):
        """moving the widget in the (x, y) coords"""
        self.move(x, y)  # moving the widget
        self.update()  # updating the widget


class DrawingBoard(QFrame):
    """Still a experiment of drawing on a widget"""

    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.resize(width, height)  # resizing the widget

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """Changing the original painting of the widget"""
        self.painter = QPainter(self)  # Creating QPainter instance in a function :/
        self.painter.setBrush(QBrush(QColor('yellow')))  # setting the brush of the QPainter
        self.painter.drawRect(self.rect())  # Drawing a simple rectangle
        self.painter.end()  # Ending the paint event

    def drawRectangle(self, x: int = 0, y: int = 0, width: int = 200, height: int = 80):
        """Drawing a rectangle on the screen"""
        self.painter.drawRect(x, y, width, height)  # Drawing a rectangle in a function; bad idea!

    def stop(self):
        """plss dont try this!"""
        self.painter.end()  # Ending it
        self.update()  # Updating


class Text(QLabel):
    """Creating a simple text on the widget"""

    def __init__(self, parent, text, font: tuple = (), width: int = ...,
                 height: int = ..., x: int = ..., y: int = ...,
                 bg: str = 'transparent', color: str = 'white',
                 border: int = 0,
                 border_radius: int = 0, text_decoration: str = 'none'):
        super().__init__(parent)
        if x != ... and y != ...:
            self.move(x, y)  # move the label
        self.text = text  # setting the text as a instance of self

        self.effect = QGraphicsDropShadowEffect()  # Creating a graphics effect
        self.effect.setOffset(0, 0.3)  # Setting the offset of the effect
        self.effect.setColor(QColor('grey'))  # setting the color of the effect
        self.effect.setBlurRadius(0.5)  # setting the blur radius of the widget
        self.setGraphicsEffect(self.effect)  # creating the graphics effect

        self.pl = parent  # setting the parent to be an instance of self
        self.setText(self.text)  # setting the txt of the label
        if width != ... and height != ...:
            self.resize(width, height)  # resizing the widget to be width and height
        self.setAlignment(Qt.AlignCenter)  # Aligning the text to the center of the widget
        if font != ():
            self.setFont(QFont(font[0], font[1], font[2], font[3]))  # Setting the font of the text
        else:
            self.setFont(QFont('Arial Rounded MT Bold', 11, 24, False))  # Setting a default font for the text
        self.setStyleSheet(
            f"""background-color: {bg}; color: {color}; border: {str(border)}px; border-radius: {str(border_radius)}px; text-decoration: {text_decoration};""")  # Creating a stylesheet for the widget

    def display(self):
        """ displaying and updating the text on the screen at a coordinate"""
        self.pl.setCentralWidget(self)  # setting the parent as a centrak widget
        self.update()

    def place(self, x, y):
        """placing the widget at a x and y coordinate"""
        self.move(x, y)  # moving the widget

    def selectable(self):
        """making the text on the widget selectable by mouse and keybaord"""
        self.setTextInteractionFlags(
            Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)  # setting a text interaction flag

    def editable(self):
        """ Making the txt to be edited on"""
        self.setTextInteractionFlags(
            Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)  # setting a text interaction flag


LINK = 'link'  # Assigning a string to the LINK var!.


class IconCircularButton(QPushButton):
    """ Icon Circular Button made with QPainter and QPushButton"""

    def __init__(self, parent, file, x, y, hoverbackground: str = 'orange', selectbackground: str = 'yellow',
                 bg: str = '#332EC3', underglow_color: str = '#808080', use_underglow: bool = True):
        super().__init__(parent)
        self.file = file
        self.bg = bg
        self.painter = ''
        self.move(x, y)  # Moving the widget to the x and y coords
        self.setStyleSheet("""background-color: transparent;""")  # Setting a stylesheet to the widgey
        if use_underglow == True:
            self.effect = QGraphicsDropShadowEffect()  # Creating a drop shadow effect
            self.effect.setColor(QColor(underglow_color))  # Setting the color of the effect to the underglow color
            self.effect.setBlurRadius(8)  # Changing the blur radius of the graphics effect
            # Setting the offset of the widget
            self.effect.setOffset(0.3, 0.5)
            # Setting the widget's graphics effect to the self.effect
            self.setGraphicsEffect(self.effect)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """Handles the drawing of the widget"""
        self.painter = QPainter(self)  # Creating the Painter
        self.painter.setBrush(QColor(self.bg))  # Setting the brush of the painter
        self.painter.setPen(QPen(Qt.NoPen))  # Setting the pen of the painter
        image = QImage(self.file)  # Creating an image
        self.painter.setRenderHints(  # Improving the graphics
            QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.Antialiasing)
        self.painter.drawEllipse(self.rect().x(), self.rect().y(), image.size().width(), image.size().height())
        self.painter.drawImage(self.rect().x(), self.rect().y(), image, 0, 0, image.rect().width() + 10,
                               image.rect().height() + 10)
        self.painter.setPen(QPen(QColor(Qt.white)))  # Changing the pen of the painter
        self.resize(image.size().width() + 70, image.size().height() + 70)  # resizing the widget
        self.painter.end()  # Ending the paint event

    def OnClicked(self, function):
        """connecting a function to the clicked event"""
        self.clicked.connect(function)


class Button(QPushButton):
    """ Creating a Material Style Button using QPushButton"""

    def __init__(self, parent: QWidget, text: str = ..., width: int = ..., height: int = ..., color: str = 'white',
                 bg: str = ...,
                 selectbackground: str = ..., selectforeground: str = ..., border: str = 'none',
                 border_radius: str = 'none', hoverbackground: str = ..., hoverforeground: str = ..., font: tuple = (),
                 command: any = ..., underground_glow_color: str = 'grey', tooltip: str = ..., icon_file: str = ...,
                 icon_size=(), use_underground_glow_color: bool = True):
        super().__init__(parent)
        self.parent = parent
        style = []  # Storing all the styles
        select = []  # Storing of the styles bonded with selecting the widget
        overall = []  # Adding all the various styles in a list
        hover = []  # Adding a the overing styles.
        if font == ():
            # Changing the font of the text
            self.setFont(QFont('Arial Rounded MT Bold', 11, 24, False))
        if command != ...:
            # Setting a command to be called when the left mouse button is clicked
            self.clicked.connect(lambda x: command(self))
        if text != ...:
            # Setting a text on the QPushButton
            self.setText(text)
        if color != 'white':
            # Adding the color to list of styles
            style.append(f'color: {color};')
        else:
            # Adding a default color to list of styles
            style.append(f'color: white;')
        if bg != ...:
            # Adding a background color to a list of styles
            style.append(f'background-color: {bg};')
        if border != 'none':
            # Adding a border to the list of styles
            style.append(f'border: {border};')
        if border_radius != 'none':
            # Setting border_radius value in the list of styles
            style.append(f'border-radius: {border_radius};')
        if selectbackground != ...:
            # adding a background color to the list select styles
            select.append(f'background-color: {selectbackground};')
        if selectforeground != ...:
            # adding a text color to the list of select styles
            select.append(f'color: {selectforeground};')
        if hoverbackground != ...:
            # Adding a hover background to the list of hover styles
            hover.append(f'background-color: {hoverbackground};')
        if hoverforeground != ...:
            # Adding a text color to the list of hover styles
            hover.append(f'color: {hoverforeground};')
        if len(hover) >= 1:
            # creating the style_hover string to be used below
            style_hover = 'QPushButton::hover{\n\t' + '\n\t'.join(hover)
            # adding all the strings to a overall list
            overall.append(style_hover)
        if len(style) >= 1:
            # creating a style_norm string to be added in the overall list
            style_norm = 'QPushButton{\n\t' + '\n\t'.join(style)
            # adding a style_norm to the overall list
            overall.append(style_norm)
        if len(select) >= 1:
            # creating a style_select string
            style_select = 'QPushButton::pressed{\n\t' + '\n\t'.join(select)
            # Adding the style_select string to the overall list
            overall.append(style_select)
        if width != ...:
            # Setting a fixed width
            self.setFixedWidth(width)
        if height != ...:
            # Setting the fixed height
            self.setFixedHeight(height)
        overall_style = '\n}\n\n'.join(overall) + '\n}'
        # Creating a drop shadow effect
        self.effect = QGraphicsDropShadowEffect()
        # adding a elevation style blur radius
        self.effect.setBlurRadius(7)
        # setting the offset of the graphics effect
        self.effect.setOffset(0.4, 0.3)
        if use_underground_glow_color == True:
            # If we are to use the graphics effect
            self.effect.setColor(QColor(underground_glow_color))
            # setting the graphics effect
            self.setGraphicsEffect(self.effect)
        else:
            pass
        self.xc = self.x()
        self.yc = self.y()
        # Creating a style sheet
        self.setStyleSheet(overall_style)
        if tooltip != ...:
            # setting the tooltip of the widget
            self.setToolTip(tooltip)
        if icon_file != ...:
            # If we are to use the icon file
            self.setIcon(QIcon(icon_file))
        if icon_size != ():
            # setting the size of the icon
            self.setIconSize(QSize(icon_size[0], icon_size[1]))

    def display(self, x, y):
        # displaying and updating the widget
        self.xc = x
        self.yc = y
        # moving the widget in the x and y coordinate
        self.move(self.xc, self.yc)
        self.update()


class Box(QWidget):
    """A Box to add other widgets"""

    def __init__(self):
        super().__init__()


class SidePanel(QDockWidget):
    """ Creating a panel at  SIDE OF THE SCREEN"""

    def __init_(self, parent):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """Handles the drawing of the widget"""
        self.painter = QPainter(self)
        self.painter.setBrush(QColor(Qt.white))
        self.painter.drawRect(self.rect())
        self.painter.end()


class Link(QPushButton):
    """Creating a clickable hypertext on the widget"""

    def __init__(self, parent, text, cursor=Qt.PointingHandCursor, fg: str = '#5949D2', bg: str = ...,
                 web_link: str = "https://www.google.com"):
        super().__init__(parent)
        self.t = text
        self.setText(self.t)  # Modifying the text
        # Creating a stylesheet for the widget
        self.setStyleSheet("""
        QPushButton{
            color: #5949D2;
            text-decoration: underline;
        }
        
        QPushButton::hover{
            color: #3E69BA;
        }
        
            """)
        # Setting the font of the text
        self.setFont(QFont('Helvetica', 9, 40, False))
        # setting the hover cursor
        self.setCursor(cursor)
        # go to the designated web address when clicked
        self.clicked.connect(self.go_to_web_address)
        # adjust the widget size to the point size
        self.adjustSize()
        # creating the web link instace
        self.web_link = web_link

    def display(self, x, y):
        """displaying and updating the widget"""
        self.move(x, y)  # moving the widget

    def go_to_web_address(self):
        # importing the web browser module
        import webbrowser
        # opening the computer's default web browser
        webbrowser.open(self.web_link, 1, True)


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


class Circle(QFrame):
    """Drawing a eclipse like frame using QPainter and QFrame"""
    def __init__(self, parent, width, height, bg: str = '#6883FF', pen_width: int = 2, pen_color: str = ...):
        super().__init__(parent)
        self.resize(width, height)  # resizing the widget
        self.bg = bg
        self.pen_color = pen_color
        self.pen_width = pen_width

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """Handles the drawing of the QFrame"""

        # Creating the painter
        self.painter = QPainter(self)
        if self.pen_color != ...:
            # creating the pen of the painter
            self.painter.setPen(QPen(QColor(self.pen_color), self.pen_width))
        else:
            # setting th QPainter pen
            self.painter.setPen(QPen(Qt.NoPen))
        # making the graphics better by setting the render hint.
        self.painter.setRenderHint(QPainter.HighQualityAntialiasing)
        # creating a brush on the painter
        self.painter.setBrush(QColor(self.bg))
        # Drawing ellipse like circle
        self.painter.drawEllipse(self.rect())
        self.painter.end()  # Ending the paint event

    def display(self, x, y):
        """displaying and updating the widget"""
        self.move(x, y)
        self.update()


class PieWidget(QFrame):
    def __init__(self, parent, width, height, a, alen, color):
        super().__init__(parent)
        self.resize(width, height)
        self.alen = alen
        self.color = color
        self.a = a
        self.setStyleSheet("""background-color: transparent;""")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setBrush(QBrush(QColor(self.color)))
        self.painter.drawPie(self.rect(), self.a, self.alen)
        self.painter.end()

    def display(self, x, y):
        self.move(x, y)
        self.update()


class DSCard(QFrame):
    def __init__(self, parent, box_width, box_height, rotate: float = ..., bg: str = '#6883FF', border_x: int = 1,
                 border_y: int = 1,
                 pen_color: str = ..., pressed: any = ..., label: str = ..., label_font=('Calibri', 25, 40, False)):
        super().__init__(parent)
        self.resize(box_width, box_height)
        self.setFixedHeight(box_height)
        self.border_x = border_x
        self.border_y = border_y
        self.rotate = rotate
        self.label = label
        self.label_font = label_font
        self.pen_color = pen_color
        self.pressed = pressed
        self.bg = bg
        self.box_lay = QVBoxLayout(self)
        self.setLayout(self.box_lay)
        self.setStyleSheet("""background-color: transparent;""")

    def addWidget(self, widget):
        self.box_lay.addWidget(widget)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.pressed != ...:
            self.pressed(self)

    def translate(self, x, y):
        self.move(x, y)

    def set_background(self, color):
        self.bg = color

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        if self.pen_color != ...:
            self.painter.setPen(QPen(QColor(self.pen_color)))
        else:
            self.painter.setPen(QPen(Qt.NoPen))
        # self.painter.rotate(20.0)
        if self.rotate != ...:
            self.painter.rotate(self.rotate)
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setBrush(QColor(self.bg))
        self.painter.drawRoundedRect(self.rect().x(), self.rect().y(), self.rect().width(), self.rect().height(),
                                     self.border_x, self.border_y)
        if self.label != ...:
            self.painter.setPen(QPen(QColor('black')))
            self.painter.setBrush(QBrush(QColor('black')))
            if self.label_font != ():
                self.painter.setFont(
                    QFont(self.label_font[0], self.label_font[1], self.label_font[2], self.label_font[3]))
            else:
                self.painter.setFont(QFont('Calibri', 25, 100, False))
            label = self.painter.drawText(
                QRect(int(self.rect().top() + self.width() / 2) - 25, int(self.rect().top() + self.height() / 2 - 25),
                      self.width(), self.height()), 0, self.label)
            # self.label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
            # self.label.setAlignment(Qt.AlignCenter)
            # self.label.setText(self.label)
            # self.box_lay.addWidget(self.label)
        self.painter.end()

    def setOpacity(self, level):
        self.painter.setOpacity(level)

    def display(self, x, y):
        self.move(x, y)
        self.update()


class Rectangle(QFrame):
    def __init__(self, parent, box_width, box_height, rotate: float = ..., bg: str = '#6883FF', border_x: int = 1,
                 border_y: int = 1,
                 pen_color: str = ..., underglow_color: str = 'grey', use_underglow: bool = True):
        super().__init__(parent)
        self.resize(box_width, box_height)
        self.setFixedHeight(box_height)
        self.border_x = border_x
        self.border_y = border_y
        self.rotate = rotate
        self.pen_color = pen_color
        self.bg = bg
        self.box_lay = QVBoxLayout(self)
        self.effect = QGraphicsDropShadowEffect()

        if use_underglow == True:
            self.effect.setColor(QColor(underglow_color))
            self.effect.setBlurRadius(8)
            self.effect.setOffset(0.4, 0.3)
            self.setGraphicsEffect(self.effect)
        self.setLayout(self.box_lay)
        self.setStyleSheet("""background-color: transparent;""")

    def addWidget(self, widget):
        self.box_lay.addWidget(widget)

    def translate(self, x, y):
        self.move(x, y)

    def set_background(self, color):
        self.bg = color

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        if self.pen_color != ...:
            self.painter.setPen(QPen(QColor(self.pen_color)))
        else:
            self.painter.setPen(QPen(Qt.NoPen))
        # self.painter.rotate(20.0)
        if self.rotate != ...:
            self.painter.rotate(self.rotate)
        self.painter.setRenderHints(QPainter.HighQualityAntialiasing | QPainter.Antialiasing)
        self.painter.setBrush(QColor(self.bg))
        self.painter.drawRoundedRect(self.rect().x(), self.rect().y(), self.rect().width(), self.rect().height(),
                                     self.border_x, self.border_y)
        self.painter.end()

    def setOpacity(self, level):
        self.painter.setOpacity(level)

    def display(self, x, y):
        self.move(x, y)
        self.update()


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


class RichTextBox(QTextEdit):
    def __init__(self, parent, width, height, bg: str = '#17AEFF', fg: str = 'white', border: str = '2px',
                 border_radius: str = '2px'):
        super().__init__(parent)
        self.resize(width, height)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setOffset(0.4, 0.5)
        self.effect.setBlurRadius(0.5)
        self.effect.setColor(QColor(Qt.gray))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet(f"""background-color: {bg}; color: {fg}; border: {border}; border-radius: {border_radius}""")

    def display(self, x, y):
        self.move(x, y)


class MultilineEdit(QLabel):
    def __init__(self, parent, place_holder: str = ...):
        super().__init__(parent)
        if place_holder != ...:
            self.setText(place_holder)
        self.setStyleSheet("""border-bottom: 2px solid #6EA1FF; background-color: transparent; color: white;""")
        self.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)

    def display(self, x, y):
        self.move(x, y)


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


class WindowPanel(QFrame):
    def __init__(self, parent, title: str = ..., color: str = '#36539D', bg: str = '#4B99FF'):
        super().__init__(parent)
        # self.resize(370, 680)
        self.move(30, 30)
        self.parent = parent
        self.color = color
        self.bg = bg
        self.title = title
        self.setStyleSheet("""background-color: transparent;""")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setBrush(QColor(self.bg))
        self.resize(370, self.parent.height() - 50)
        self.painter.drawRoundedRect(self.rect(), 7, 7)
        self.painter.setBrush(QColor(self.color))
        self.painter.setPen(QColor('grey'))
        self.painter.drawLine(self.rect().x() + self.width(), self.rect().y() + 6, self.rect().x() + self.width(),
                              self.rect().y() + self.height() - 6)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.drawRoundedRect(self.rect().x(), self.rect().y(), self.rect().width(), 35, 2, 2)
        self.painter.setPen(QPen(Qt.white))
        self.painter.setFont(QFont('Helvetica', 9, 55, False))
        self.painter.drawPixmap(self.rect().x(), self.rect().y(), 35, 35, QPixmap("../images/Dush.png"))
        if self.title != ...:
            self.painter.drawText(self.rect().x() + 39, self.rect().y() + 8, self.rect().width(), self.rect().height(),
                                  0, self.title)
        self.painter.end()


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
