# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simply.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from created import Ui_Created
from issued import Ui_Issued
from finished import Ui_Finished

class Ui_Simply(object):
    def setupUi(self, Simply):
        Simply.setObjectName("Simply")
        Simply.resize(620, 400)
        self.centralwidget = QtWidgets.QWidget(Simply)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 211, 161))
        self.label.setStyleSheet("image: url(:/新前缀/gift.png);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 200, 477, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_created = QtWidgets.QPushButton(self.widget)
        self.pushButton_created.setObjectName("pushButton_created")
        self.horizontalLayout.addWidget(self.pushButton_created)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_issued = QtWidgets.QPushButton(self.widget)
        self.pushButton_issued.setObjectName("pushButton_issued")
        self.horizontalLayout.addWidget(self.pushButton_issued)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_finished = QtWidgets.QPushButton(self.widget)
        self.pushButton_finished.setObjectName("pushButton_finished")
        self.horizontalLayout.addWidget(self.pushButton_finished)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Simply.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Simply)
        self.statusbar.setObjectName("statusbar")
        Simply.setStatusBar(self.statusbar)

        self.retranslateUi(Simply)
        QtCore.QMetaObject.connectSlotsByName(Simply)

        self.pushButton_created.clicked.connect(self.created_button)
        self.pushButton_issued.clicked.connect(self.issued_button)
        self.pushButton_finished.clicked.connect(self.finished_button)

    def created_button(self):
        Created = QtWidgets.QDialog()
        ui = Ui_Created()
        ui.setupUi(Created)
        Created.show()
        Created.exec_()

    def issued_button(self):
        Issued = QtWidgets.QDialog()
        ui = Ui_Issued()
        ui.setupUi(Issued)
        Issued.show()
        Issued.exec_()

    def finished_button(self):
        Finished = QtWidgets.QDialog()
        ui = Ui_Finished()
        ui.setupUi(Finished)
        Finished.show()
        Finished.exec_()



    def retranslateUi(self, Simply):
        _translate = QtCore.QCoreApplication.translate
        Simply.setWindowTitle(_translate("Simply", "抽奖助手-傻瓜操作版"))
        self.label_2.setText(_translate("Simply", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">点击按钮，开始安排抽奖事务吧~！</span></p></body></html>"))
        self.pushButton_created.setText(_translate("Simply", "已创建抽奖"))
        self.pushButton_issued.setText(_translate("Simply", "已发布抽奖"))
        self.pushButton_finished.setText(_translate("Simply", "已结束抽奖"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Simply = QtWidgets.QMainWindow()
    ui = Ui_Simply()
    ui.setupUi(Simply)
    Simply.show()
    sys.exit(app.exec_())
