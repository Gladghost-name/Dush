from app import *
from btn import *
from bar import *
from label import *
from banner import *
from lists import *
from panels import *


class MainApp(DushWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.panel = Panel(self, bg_color='grey')
        self.tab = QTabWidget(self.panel)
        self.label = QLabel('Hello', self.tab)
        self.tab.addTab(self.label, 'Document')
        self.panel.setWidget(self.tab)
        self.bar = QtToolBar(self)
        self.bar.place(Qt.TopToolBarArea)
        self.addPanel(Qt.LeftDockWidgetArea, self.panel)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
