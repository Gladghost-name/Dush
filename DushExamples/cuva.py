from Games.Flexer.Dush.ui.app import *
from Games.Flexer.Dush.ui.label import *
from Games.Flexer.Dush.ui.btn import *
from Games.Flexer.Dush.ui.frames import *
from Games.Flexer.Dush.ui.screen import *
from Games.Flexer.Dush.Anchor.main import *
import sys


class Cuva(DushWindow):
    def __init__(self):
        super().__init__()
        self.screen = Screen(self)
        self.first_frame = DSCard(self.screen, 100, 100, bg='#0F0F0F', underglow_color='#111111', border_x=40,
                                  border_y=40)
        self.screen.add(self.first_frame)
        self.text = Text(self, 'Complete the given text', font=('Calibri', 17, 17, False), color='#CBCBCB')
        self.first_frame.addWidget(self.text)
        self.frame.setStyleSheet("""background-color: #050511;""")
        self.resize(350, 600)
        self.text.setFixedSize(230, 70)
        self.setSpacing(100)
        self.button = Button(self, 'Get Started', bg='#2B6AFF', color='white', border=7, border_radius=20,
                             font=('Calibri', 12, 120, False), highlightforeground='white', selectforeground='white',
                             command=self.getStarted)
        self.button.setFixedSize(230, 50)
        self.first_frame.addWidget(self.button)
        self.first_frame.layout().setSpacing(20)
        self.first_frame.setContentsMargins(0, 0, 0, 0)
        self.first_frame.layout().setAlignment(Qt.AlignCenter)
        self.button1 = Button(self, 'Quit', bg='red', color='white', border=7, border_radius=20,
                              highlightbackground='#C70000', highlightforeground='white',
                              font=('Calibri', 12, 120, False), command=self.stop)
        self.button1.setFixedSize(230, 50)
        self.first_frame.addWidget(self.button1)

        next_page = DSCard(self, 10, 10, bg='#000000')
        next_page.layout().setAlignment(Qt.AlignCenter)
        next_page.layout().setSpacing(130)
        self.page_text = Text(next_page, 'Exmple Txt', font=('Calibri', 18, 45, False), editable=True)
        next_page.addWidget(self.page_text)

        self.gvbox = QVBoxLayout()
        self.gvbox.setAlignment(Qt.AlignCenter)
        generate_frame = QFrame(next_page)
        generate_frame.setLayout(self.gvbox)

        next_page.addWidget(generate_frame)
        self.gbutton = Button(generate_frame, 'GENERATE', font=('Calibri', 12, 120, False), color='white', border=7,
                              border_radius=20, bg='#00F05E', command=self.generate)
        self.gbutton.setFixedSize(230, 50)
        # generate_frame.setFixedHeight(350)
        self.gvbox.addWidget(self.gbutton)

        self.screen.add(next_page)

        self.addWidget(self.screen)

    def stop(self):
        self.close()

    def getStarted(self):
        self.screen.go_forward(2)

    def generate(self):
        text = self.page_text.text()
        splitted = text.split()
        self.page_text.setText(str(splitted))
        for i in splitted:
            if is_it_a_word(i) == False:
                self.page_text.setText('A Error in word')
            else:
                self.page_text.setText('No Text to split')


app = QApplication(sys.argv)
game = Cuva()
game.show()
sys.exit(app.exec_())
