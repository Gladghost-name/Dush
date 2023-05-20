from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class ActionButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
        QPushButton{
            background-color: white; 
            border: 2px; 
            border-radius: 5px;
            padding: 10px;
        }
        
        QPushButton::hover{
            background-color: #EBEBEB;
            border: 1px solid grey;
        }
        """)

class ColorCircle(QLabel):
    def __init__(self):
        super().__init__()
        self.default_color = 'black'
        self.setFixedSize(20, 20)
        self.selected_color = None
        self.setStyleSheet("""background-color: transparent;""")
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHints(QPainter.Antialiasing)
        self.painter.setPen(QPen(QColor('black'), .5))
        self.painter.setBrush(QColor(self.default_color))
        self.painter.drawEllipse(1, 1, self.rect().width()-2, self.rect().height()-2)
        self.painter.end()
    def set_color(self, color):
        self.default_color = color
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            self.default_color = self.default_color
            print(self.default_color)

class ColorBox(QLabel):
    def __init__(self):
        super().__init__()
        self.default_color = 'black'
        self.setFixedSize(50, 50)
        self.selected_color = None
        self.setStyleSheet("""background-color: transparent;""")
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)
        self.painter.setRenderHints(QPainter.Antialiasing)
        self.painter.setPen(QPen(Qt.NoPen))
        self.painter.setBrush(QColor(self.default_color))
        self.painter.drawRect(1, 1, self.rect().width()-2, self.rect().height()-2)
        self.painter.end()
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            self.color_picker = QColorDialog()
            self.color_picker.exec()
            self.default_color = self.color_picker.selectedColor().name()
            self.update()
class PaintToolBar(QToolBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""background-color: white;""")

        self.label = ActionWidget()
        self.label.setTitle("Tools")

        self.tool_frame = QFrame()
        self.tool_grid = QGridLayout()

        self.tool_frame.setLayout(self.tool_grid)

        self.pen_tools = ActionButton()
        self.pen_tools.setIcon(QIcon('office-material.png'))
        self.pen_tools.setToolTip("""Pencil""")

        self.eraser = ActionButton()
        self.eraser.setIcon(QIcon('eraser.png'))
        self.eraser.setToolTip("""Eraser""")

        self.fill = ActionButton()
        self.fill.setIcon(QIcon('fill.png'))
        self.fill.setToolTip("""Bucket Fill""")

        self.dropper = ActionButton()
        self.dropper.setIcon(QIcon('eye-dropper.png'))
        self.dropper.setToolTip("""Color picker""")

        self.text = ActionButton()
        self.text.setIcon(QIcon('font.png'))
        self.text.setToolTip("""Add Text""")

        self.tool_grid.setContentsMargins(0, 0, 0, 0)
        self.tool_grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.tool_grid.addWidget(self.pen_tools, 1, 1)
        self.tool_grid.addWidget(self.eraser, 1, 2)
        self.tool_grid.addWidget(self.fill, 1, 3)
        self.tool_grid.addWidget(self.dropper, 2, 1)
        self.tool_grid.addWidget(self.text, 2, 2)

        self.label.setTopWidget(self.tool_frame)
        self.addWidget(self.label)



        self.color_palette = ActionWidget()
        self.color_palette.setTitle("Palette")

        self.color_frame = QFrame()
        self.color_grid = QGridLayout()
        self.color_frame.setLayout(self.color_grid)

        self.row = 1
        self.col = 1

        color_list = ['#000000', '#FF9D9D', "#9DFFD0", '#A4BDFF', '#FFFFFF', "#FF0404", '#14FF00', '#00B2FF', '#C172FF', '#FF57A8', '#FAFF00', '#FFFFFF', '#EBEBEB', '#CFCFCF', '#A7A7A7', '#898989', '#717171', '#000000']
        for color in color_list:
            self.color_circle = ColorCircle()
            self.color_circle.set_color(color)
            self.color_grid.addWidget(self.color_circle, self.row, self.col)
            if self.col == 7:
                self.col = 1
                self.row += 1
            else:
                self.col += 1

        self.color_palette.setTopWidget(self.color_frame)

        self.addWidget(self.color_palette)


        self.color_picker = ActionWidget()
        self.color_picker.setTitle("Color")

        self.picker_frame = QFrame()
        self.picker_layout = QVBoxLayout()
        self.picker_frame.setStyleSheet("""background-color: transparent; padding: 10px;""")
        self.picker_layout.setContentsMargins(0, 0, 0, 0)
        self.picker_layout.setAlignment(Qt.AlignCenter)
        self.picker_frame.setLayout(self.picker_layout)

        self.color_box = ColorBox()
        self.picker_layout.addWidget(self.color_box)

        self.color_picker.setTopWidget(self.picker_frame)

        self.addWidget(self.color_picker)


        self.shapes = ActionWidget()
        self.shapes.setTitle("Shapes")

        self.shapes_frame = QFrame()
        self.shapes_layout = QGridLayout()
        self.shapes_frame.setStyleSheet("""background-color: transparent; padding: 10px; border: 1px solid grey; border-radius: 10px;""")
        self.shapes_layout.setContentsMargins(0, 0, 0, 0)
        self.shapes_layout.setAlignment(Qt.AlignCenter)
        self.shapes_frame.setLayout(self.shapes_layout)

        row = 1
        col = 1

        for i in range(12):
            self.button = ActionButton()
            self.button.setText(str(i))
            self.shapes_layout.addWidget(self.button, row, col)
            if col == 6:
                col = 1
                row += 1
            else:
                col += 1

        self.shapes.setTopWidget(self.shapes_frame)

        self.addWidget(self.shapes)



        self.size_picker = ActionWidget()
        self.size_picker.setTitle("Size&Position")

        self.size_frame = QFrame()
        self.size_layout = QFormLayout()
        self.size_frame.setStyleSheet("""background-color: transparent; padding: 10px;""")
        self.size_layout.setContentsMargins(0, 0, 0, 0)
        self.size_layout.setAlignment(Qt.AlignCenter)
        self.size_frame.setLayout(self.size_layout)

        self.width = QSpinBox()
        self.size_layout.setSpacing(5)
        self.size_layout.addRow("Width: ", self.width)
        self.size_layout.setAlignment(Qt.AlignCenter)

        self.height = QSpinBox()
        self.size_layout.addRow("Height: ", self.height)

        self.size_picker.setTopWidget(self.size_frame)

        self.addWidget(self.size_picker)


        self.setMovable(False)


class ActionWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("actionwidget")
        self.setStyleSheet(
            """#actionwidget{background-color: white; border-right: .5px solid #D9D9D9;}""")
        self.vbox = QVBoxLayout()
        self.title_widget = QLabel("Document")
        self.title_widget.setStyleSheet("""color: grey; font-size: 17px; font-family: Calibri; padding: 10px;""")
        self.title_widget.setAlignment(Qt.AlignCenter)
        self.vbox.insertWidget(1, self.title_widget, 1, Qt.AlignBottom)
        self.setLayout(self.vbox)
    def setTitle(self, title: str = 'Document'):
        self.title_widget.setText(title)
    def setTopWidget(self, widget):
        self.vbox.insertWidget(0, widget, 1, Qt.AlignTop)

class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.setWindowTitle("Simple Interface Design!")
        self.resize(980, 700)

        self.tools = ['Clipboard', 'Image', 'Tools', 'Brushes', 'Shapes', 'Size', "Colors"]

        self.toolbar = PaintToolBar()

        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.menubar = QMenuBar()
        self.menubar.setStyleSheet("""
        QMenuBar{
            background-color: white; 
            padding: 10px;
        }
        
        QMenuBar::item::hover{
            background-color: grey;
        }
        """)
        self.setMenuBar(self.menubar)

        self.file_menu = QMenu("File")
        # self.file_menu.setAttribute(Qt.WA_NoSystemBackground, True)
        # self.file_menu.setAttribute(Qt.WA_TranslucentBackground, True)
        self.file_menu.setStyleSheet(
            """
            QMenu{
                border: 1px solid #d9d9d9;
                background-color: white;
                padding: 5px;
                border-radius: 8px;
            }
            
            QMenu::item:selected {
                padding: 10px;
                background: #d9d9d9;
            }
            
            QMenu::item{
                height: 5px;
                width: 200px;
                border: 5px solid white;
                border-radius: 10px;
                padding: 10px;
            }
            
           QMenu::separator{
                height: .5px;
                border: 2px;
                margin: 1px;
                background: #d9d9d9;
            }
            """
        )
        self.file_menu.addAction(QIcon('folder.png'), "Open", self.sample, 'ctrl+o')
        self.file_menu.addSeparator()
        self.file_menu.addAction(QIcon('file.png'), "New Document", self.sample, 'ctrl+n')
        self.file_menu.addAction(QIcon('export.png'), "Export As", self.sample, 'ctrl+e')
        # self.file_menu.addAction(QIcon('export.png'), "Export As", self.sample, 'ctrl+e')
        self.menubar.addMenu(self.file_menu)
    def sample(self):
        pass


class MainApp(QApplication):
    def __init__(self):
        super(MainApp, self).__init__(sys.argv)
        self.window = Interface()

    def run(self):
        self.window.show()
        sys.exit(self.exec())


app = MainApp()
app.run()
