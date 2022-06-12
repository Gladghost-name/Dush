from Games.Flexer.Dush.ui import *

app = QtApp('Platform App', bg='white', border='5px', border_radius='6px')
app.remove_border()


def Onpress(e):
    e.setText('You Clicked Me')
    e.setFixedSize(350, 85)
    print(e.text())


button = TitleBar(app.window, 'Settings', '#418CFF', 'white', border=5, border_radius=6, font_size=17)

app.addNavBar(button)

card = DSCard(app.window, 500, 500, bg='white', pen_color='white')
button = Button(card, 'Click Me!', width=100, height=35,  color='white', bg='#418CFF', hoverbackground='orange')
card.addWidget(button)
app.addWidget(card)
app.loop()
