from random import randint

from PyQt5.QtCore import Qt, QSize

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout,QListWidgetItem, QLabel

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

        self.stackedWidget = QStackedWidget(self)

        layout.addWidget(self.stackedWidget)

        self.initUi()



    def initUi(self):

        # 初始化界面

        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号

        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)

        # 去掉边框

        self.listWidget.setFrameShape(QListWidget.NoFrame)

        # 隐藏滚动条

        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.listWidget.setFixedWidth(180)

        # 这里就用一般的文本配合图标模式了(也可以直接用Icon模式,setViewMode)

        

        item1 = QListWidgetItem(str('已创建'), self.listWidget)
        item1.setSizeHint(QSize(200,100))
        item1.setTextAlignment(Qt.AlignCenter)

        item2 = QListWidgetItem(str('已发布'), self.listWidget)
        item2.setSizeHint(QSize(200,100))
        item2.setTextAlignment(Qt.AlignCenter)

        item3 = QListWidgetItem(str('已开奖'), self.listWidget)
        item3.setSizeHint(QSize(200,100))
        item3.setTextAlignment(Qt.AlignCenter)

        # 再模拟20个右侧的页面(就不和上面一起循环放了)

        for i in range(4):

            label = QLabel('我是页面 %d' % i, self)

            label.setAlignment(Qt.AlignCenter)

            # 设置label的背景颜色(这里随机)

            # 这里加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)

            label.setStyleSheet('background: rgb(27,111,175);')

            self.stackedWidget.addWidget(label)

if __name__ == '__main__':

    import sys

    from PyQt5.QtWidgets import QApplication

    #style = open(r"C:\Users\wangq\Documents\课件\docu.18-01\软工实践\MetroUI.qss","r",encoding='utf-8')
    #style_str = style.read()
    #style_str = style_str.decode('utf-8')
    app = QApplication(sys.argv)
    #app.setStyleSheet(style_str)

    w = LeftTabWidget()
    w.show()
    sys.exit(app.exec_())