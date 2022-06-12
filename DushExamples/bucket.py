from PyQt5 import QtCore

from Games.Flexer.Dush.ui import *


class Card(Rectangle):
    def __init__(self, parent, box_width, box_height, rotate: float = ..., bg: str = '#6883FF', border_x: int = 1,
                 border_y: int = 1, pen_color: str = ..., clicked: any = ...):
        super().__init__(parent, box_width, box_height, rotate, bg, border_x, border_y, pen_color)
        self.clicked = clicked
        self.border_x = border_x

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.clicked != ...:
            self.clicked()

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(f"""background-color: QLinearGradient(x1:0 y1:0, x2:0 y2:1, stop:0 white, stop:1 grey); border: 5px; border-radius: {self.border_x};""")

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet("""background-color: transparent;""")

class ExampleApp(DushWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DushUi Examples')
        self.setWindowIcon(QIcon('bucket-images/DushUi.png'))
        self.screen = Screen(self)
        self.resize(850, 600)
        self.setFixedSize(850, 600)
        self.slayout = QVBoxLayout()
        self.setStyleSheet("""background-color: white;""")
        self.frame = QFrame(self)
        self.frame.setLayout(self.slayout)
        self.frame.setStyleSheet("""background-color: white;""")
        self.image = RealImage(self.frame, 'C:/Users/adara/Desktop/ui_arrow.png', 150, 287)
        self.slayout.addWidget(self.image)
        self.bottom_frame = QFrame(self)
        self.bottom_frame.setFixedHeight(70)

        self.button = Button(self.bottom_frame, 'close', 100, 50, 'black', 'white', hoverbackground='#3763EA'
                             , border='5px', border_radius='5px', underground_glow_color='#4A7EDA'
                             , command=self.close_app, tooltip='Close the Application')
        self.button.display(self.width() - self.button.width() - 25,
                            self.bottom_frame.height() - self.button.height() - 5)

        self.toggle = Button(self.bottom_frame, 'Light', 100, 50, 'black', 'white', hoverbackground='#3763EA'
                             , border='5px', border_radius='5px', underground_glow_color='#4A7EDA'
                             , command=self.toggler, tooltip='Toggle on or off between modes')
        self.toggle.display(self.width() - self.button.width() - self.toggle.width() - 32,
                            self.bottom_frame.height() - self.button.height() - 5)

        self.slayout.addWidget(self.bottom_frame)
        self.timer = QTimer(self)
        # self.timer.setInterval(100)
        self.timer.start(6000)
        self.timer.timeout.connect(self.switch_frame)

        self.selection_frame = QFrame(self)

        self.selection_layout = QGridLayout()
        self.selection_layout.setContentsMargins(30, 10, 30, 20)
        self.selection_frame.setLayout(self.selection_layout)
        self.f1 = Card(self.selection_frame, 350, 420, border_x=7, border_y=7, pen_color='grey', bg='white',
                       clicked=self.open_settings)
        self.label = RealImage(self.f1, 'C:/Users/adara/Desktop/settings.png', 200, 200)
        self.f1.addWidget(self.label)
        self.f1.setFixedSize(280, 220)
        self.f1_widget = QFrame(self.screen)

        self.f2 = Card(self.selection_frame, 350, 420, border_x=7, border_y=7, pen_color='grey', bg='white',
                       clicked=self.open_widget_selection)
        self.label2 = RealImage(self.f1, 'C:/Users/adara/Desktop/interface_select.png', 200, 200)
        self.f2.addWidget(self.label2)
        self.f2.setFixedSize(280, 220)
        self.f2_widget = QFrame(self.screen)

        self.selection_layout.addWidget(self.f1, 0, 0)
        self.selection_layout.addWidget(self.f2, 0, 1)

        self.f3 = Card(self.selection_frame, 350, 420, border_x=7, border_y=7, pen_color='grey', bg='white',
                       clicked=self.open_effect_panel)
        self.label3 = RealImage(self.f1, 'C:/Users/adara/Desktop/interface_effects.png', 200, 200)
        self.f3.addWidget(self.label3)
        self.f3_widget = QFrame(self.screen)

        self.f3.setFixedSize(280, 220)

        self.selection_layout.addWidget(self.f3, 1, 0)

        self.f4 = Card(self.selection_frame, 350, 420, border_x=7, border_y=7, pen_color='grey', bg='white',
                       clicked=self.open_lnr_panel)
        self.label4 = RealImage(self.f1, 'C:/Users/adara/Desktop/dush_license.png', 200, 200)
        self.f4.addWidget(self.label4)

        self.f4_widget = QFrame(self.screen)
        self.f4_layout = QVBoxLayout()
        self.f4_layout.setContentsMargins(18, 0, 0, 0)
        self.text = Text(self.f4_widget, 'README & License', font=('Calibri', 17, 70, False), color='white',
                         bg='#3763EA', border=5, border_radius=5)
        self.text.setFixedHeight(50)
        self.text.setAlignment(Qt.AlignLeft)

        self.readme = Rectangle(self.f4_widget, 100, 350, border_x=5, border_y=5, pen_color='grey', bg='white')
        self.readme.setFixedSize(self.width() - 35, 550)

        self.f = open('../README.md', 'r+')
        self.write_up = self.f.read()
        self.readme_text = Text(self.readme, self.write_up, color='black')
        self.readme.addWidget(self.readme_text)

        self.back_button = Button(self.f4_widget, 'Back', 100, 50, 'white', bg='orange', hoverbackground='#3763EA',
                                  underground_glow_color='grey', border='5px', border_radius='7px',
                                  command=self.selection_go_back)
        self.back_button.display(50, self.height() - self.back_button.height() - 40)

        self.f4_layout.addWidget(self.text)
        self.f4_layout.addWidget(self.readme)
        self.f4_widget.setLayout(self.f4_layout)

        self.view_frame = Rectangle(self.selection_frame, 50, 170, border_x=10, border_y=10, bg='white',
                                    pen_color='grey', underglow_color='grey')
        self.view_frame.display(35,
                                40)

        self.expand_button = Button(self.view_frame, icon_file='C:/Users/adara/Desktop/dropdown.png',
                                  icon_size=(32, 32), border='5px', border_radius='10px',
                                  use_underground_glow_color=False, command=self.expand, tooltip='Expand the panel')
        self.expand_button.hide()

        self.drop_button = Button(self.view_frame, icon_file='C:/Users/adara/Desktop/dropup.png',
                                  icon_size=(32, 32), border='5px', border_radius='10px',
                                  use_underground_glow_color=False, command=self.collapse, tooltip='Collapse the panel')

        self.view_frame.addWidget(self.drop_button)

        self.view_button = Button(self.view_frame, icon_file='C:/Users/adara/Desktop/5_level_grid.png',
                                  icon_size=(32, 32), border='5px', border_radius='10px',
                                  use_underground_glow_color=False, hoverbackground='#3763EA',
                                  tooltip='Switch to a gridview')

        self.view_frame.addWidget(self.view_button)
        self.view_button.setFixedSize(32, 50)


        self.view_button_2 = Button(self.view_frame, icon_file='C:/Users/adara/Desktop/3_down_list.png',
                                  icon_size=(32, 32), border='5px', border_radius='10px',
                                  use_underground_glow_color=False, hoverbackground='#3763EA',
                                  tooltip='Switch to a listview')
        self.view_frame.addWidget(self.view_button_2)

        self.view_button_2.setFixedSize(32, 50)




        self.f4.setFixedSize(280, 220)

        self.selection_layout.addWidget(self.f4, 1, 1)

        self.selection_frame.setStyleSheet("""background-color: white;""")

        self.screen.add(self.frame)
        self.screen.add(self.selection_frame)
        self.screen.add(self.f1_widget)
        self.screen.add(self.f2_widget)
        self.screen.add(self.f3_widget)
        self.screen.add(self.f4_widget)
        self.setCentralWidget(self.screen)

    def collapse(self):
        self.view_frame.setFixedSize(50, 45)
        self.view_frame.addWidget(self.expand_button)
        self.expand_button.show()
        self.view_button.hide()
        self.view_button_2.hide()
        self.drop_button.hide()

    def expand(self):
        self.view_frame.setFixedSize(50, 170)
        self.expand_button.hide()
        self.view_button.show()
        self.view_button_2.show()
        self.drop_button.show()


    def open_settings(self):
        self.screen.switch(2)

    def open_widget_selection(self):
        self.screen.switch(3)

    def open_effect_panel(self):
        self.screen.switch(4)

    def selection_go_back(self):
        self.screen.switch(1)

    def open_lnr_panel(self):
        self.screen.switch(5)

    def close_app(self):
        self.close()

    def switch_frame(self):
        self.screen.switch(1)
        self.timer.stop()

    def toggler(self):
        if self.toggle.text() == 'Light':
            self.toggle.setText('Dark')
            self.frame.setStyleSheet("""background-color: #04030B""")
        elif self.toggle.text() == 'Dark':
            self.toggle.setText('Light')
            self.frame.setStyleSheet("""background-color: white;""")


app = QApplication(sys.argv)
example = ExampleApp()
example.show()
sys.exit(app.exec())
