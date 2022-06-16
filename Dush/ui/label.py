from PyQt5.QtWidgets import *
from PyQt5.Qt import *


LINK = 'link'  # Assigning a string to the LINK var!.

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
            self.setFont(QFont('Calibri', 8, 24, False))  # Setting a default font for the text
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

class MultilineEdit(QLabel):
    def __init__(self, parent, place_holder: str = ...):
        super().__init__(parent)
        if place_holder != ...:
            self.setText(place_holder)
        self.setStyleSheet("""border-bottom: 2px solid #6EA1FF; background-color: transparent; color: white;""")
        self.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)

    def display(self, x, y):
        self.move(x, y)

