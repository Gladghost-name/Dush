from app import *
from btn import *
from bar import *
from label import *

app = QtApp()
app.icon(r'..\window_images\window-icon.png')
app.setMode(DARK)
title = ToolBar(app.window, 69, 'facebook', text_color='white', bg_color='#3193FF')
text = Text(app.window, width=100, text='Hello, World')
app.addWidget(text)
app.loop()