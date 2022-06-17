from app import *
from box import *
from bar import *
from label import *

app = QtApp()
app.icon(r'..\window_images\window-icon.png')
# app.setMode(DARK)
title = ToolBar(app.window, 69, 'facebook', text_color='white', bg_color='#3193FF')
app.addTitleBar(title)
text = Text(app.window, width=100, text='Do You want to see something cool?', color='black',
            font=('Helvetica', 13, 17, False))
link = IterateBox(app.window)
app_box = AppBox(app.window)
app.addAppBox(app_box)
app_box.addWidget(text)
app_box.addWidget(link)
app.loop()
