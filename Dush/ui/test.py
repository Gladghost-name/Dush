from app import *
from btn import *
from bar import *
from label import *
from banner import *
from lists import *
from widgets import *

app = QtApp()
# app.size(364, 600)
app.icon(r'..\window_images\window-icon.png')
tool = ToolBar(app.window, 50, 'facebook', bg_color='#06B6FF')
widget = Button(tool, icon_file='C:/Users/adara/Downloads/apps_icon.png')
widget.setFixedSize(100, 50)

widget2 = Button(tool, 'Edit', color='white', highlightforeground='white',
                 highlightbackground='rgba(255, 255, 255, 120)', font=('Calibri', 10, 110, False),
                 selectbackground='rgba(255, 255, 255, 180)',  selectforeground='white')
widget2.setFixedSize(100, 50)

widget3 = Button(tool, 'Image', color='white', highlightforeground='white',
                 highlightbackground='rgba(255, 255, 255, 120)', font=('Calibri', 10, 110, False),
                 selectbackground='rgba(255, 255, 255, 180)', selectforeground='white')
widget3.setFixedSize(100, 50)

tool.addLeftItem(widget)
tool.addLeftItem(widget2)
tool.addLeftItem(widget3)
app_box = AppBox(app.window)
app.addToolbar(tool)
app.addAppBox(app_box)
app.loop()
