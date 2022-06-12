from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

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