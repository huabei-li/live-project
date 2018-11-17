from random import randint
import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore 
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout,QListWidgetItem, QLabel,QApplication
#from Gui import dialog

class LeftTabWidget(QWidget):
    
    def __init__(self, *args, **kwargs):

        super(LeftTabWidget, self).__init__(*args, **kwargs)

        self.resize(1000, 800)

        #左右布局(左边一个QListWidget + 右边QStackedWidget)

        layout = QHBoxLayout(self, spacing=0)

        layout.setContentsMargins(0, 0, 0, 0)

        # 左侧列表

        self.listWidget = QListWidget(self)

        layout.addWidget(self.listWidget)

        # 右侧层叠窗口

        widget1 = Ui_Form()

        layout.addWidget(widget1)

        self.initUi()

    def initUi(self):

        #self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setFixedWidth(180)
        # 这里就用一般的文本配合图标模式了(也可以直接用Icon模式,setViewMode)
        item1 = QListWidgetItem(str('创建'), self.listWidget)
        item1.setSizeHint(QSize(200,100))
        item1.setTextAlignment(Qt.AlignCenter)

        item1 = QListWidgetItem(str('发布'), self.listWidget)
        item1.setSizeHint(QSize(200,100))
        item1.setTextAlignment(Qt.AlignCenter)

        item2 = QListWidgetItem(str('结束'), self.listWidget)
        item2.setSizeHint(QSize(200,100))
        item2.setTextAlignment(Qt.AlignCenter)

        item3 = QListWidgetItem(str('开奖'), self.listWidget)
        item3.setSizeHint(QSize(200,100))
        item3.setTextAlignment(Qt.AlignCenter)

    #def click(self):
    #    yuming = QtWidgets.QDialog()
    #    cre_dia = yuming.Ui_Dialog()
    #    cre_dia.setupUi(Dialog)
    #    Dialog.show
    #   Dialog .     

if __name__ == '__main__':

    
    style = open(r"C:\Users\wangq\Documents\课件\docu.18-01\软工实践\MetroUI.qss","r",encoding='utf-8')
    style_str = style.read()
    #style_str = style_str.decode('utf-8')
    app = QApplication(sys.argv)
    #app.setStyleSheet(style_str)

    #MainWindow = QtWidgets.QMainWindow()
    r_widget = Ui_Form()
    r_widget.show
    l_widget = LeftTabWidget()
    l_widget.show()
    #MainWindow.show()

    sys.exit(app.exec_())