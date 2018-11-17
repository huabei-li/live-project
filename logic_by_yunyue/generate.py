# -*- coding: utf-8 -*-
import sys
import scrolled
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate, QDateTime, QTime
from DDL_database import select_status2


class Generate_activ(QWidget, scrolled.Ui_Form):

    def __init__(self, parent=None):
        super(Generate_activ, self).__init__(parent)
        self.ui = scrolled.Ui_Form()
        # 这两句坑死人
        self.setupUi(self)
        self.retranslateUi(self)

        self.width=31
        self.hight=581

        self.iterator()

    def iterator(self):
        i = 0
        activity_list = select_status2()
        for name_key in activity_list:
            self.activity_name = name_key[0]
            self.activity_keyword = name_key[1]
            self.generate(i*31,self.activity_name, self.activity_keyword)
            i=i+1

    def generate(self,po, a_name, a_keyword):
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, po, self.hight, self.width))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label_11.setText("活动名称")
        self.label_12.setText("关键词")
        self.pushButton_3.setText("查看")

    def click(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Generate_activ()
    ui.show()
    sys.exit(app.exec_())
