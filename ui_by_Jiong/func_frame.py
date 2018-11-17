
import sys
from PyQt5.QtCore import QUrl
#from GUI import dialog
#import create_dialog.py
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QListWidget,QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget,QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore    import QSize, Qt



class LeftTabWidget(QWidget):
    '''左侧选项栏'''
    def __init__(self):
        super(LeftTabWidget, self).__init__()
        self.setObjectName('LeftTabWidget')
        self.resize(800,600)
        #self.setWindowTitle('LeftTabWidget')
    
        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)

        self.left_widget = QListWidget()     #左侧选项列表
        self.left_widget.setMaximumWidth(180)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.right_widget.resize(620,600)
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()

    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)   #list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)    #去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['创建','发布','开奖']
        
        for i in range(3):
            self.item = QListWidgetItem(list_str[i],self.left_widget)   #左侧选项的添加
            self.item.setSizeHint(QSize(30,60))
            self.item.setTextAlignment(Qt.AlignCenter)                  #居中显示

            #self.browser = QWebView()                                   #右侧用QWebView来显示html网页
            #self.browser.setUrl(QUrl.fromLocalFile('D://python//code//vision//%s' % url_list[i]))
            button = QPushButton()
            button.setFixedSize(100,60)
            button.setText("创建\n新的抽奖")
            button.setGeometry(400,100,100,60)
            
            self.right_widget.addWidget(button)
class RightStackWidget(QWidget):

    def __init__(self):
        super(RightStackWidget,self).__init__()
        self.setObjectName('RightStackWidget')
        self.resize(620,600)
        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
            
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
            
        self.right_widget = QStackedWidget (self)
        self.right_widget.addWidget (self.stack1)
        self.right_widget.addWidget (self.stack2)
        self.right_widget.addWidget (self.stack3)

        #self._setup_ui()

    def stack1UI(self):
        layout = QHBoxLayout
        label = QLabel('first')
        layout.addWidget(self,label)
        #self.setLayout(layout)
        
    def stack2UI(self):
        layout = QHBoxLayout
        label = QLabel('second')
        layout.addWidget(self,label)
        #self.setLayout(layout)

    def stack3UI(self): 
        layout = QHBoxLayout
        label = QLabel('third')
        layout.addWidget(self,label)
        #self.setLayout(layout)

    def display(self,i):
      self.Stack.setCurrentIndex(2)


def main():
    
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    right = RightStackWidget()
    right.show()

    app.exec()

if __name__ == '__main__':
    main()