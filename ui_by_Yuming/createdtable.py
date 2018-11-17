# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createdtable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from create_dialog import Ui_Create_Dialog

class Ui_Created(object):
    def setupUi(self, Created):
        Created.setObjectName("Created")
        Created.resize(620, 600)
        self.layoutWidget = QtWidgets.QWidget(Created)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 581, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 4, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Created)
        QtCore.QMetaObject.connectSlotsByName(Created)
        self.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        Create_Dialog = QtWidgets.QDialog()
        ui = Ui_Create_Dialog()
        ui.setupUi(Create_Dialog)
        Create_Dialog.show()
        Create_Dialog.exec_()

    def retranslateUi(self, Created):
        _translate = QtCore.QCoreApplication.translate
        Created.setWindowTitle(_translate("Created", "抽奖助手-已创建抽奖列表"))
        self.label.setText(_translate("Created", "已创建抽奖活动："))
        self.pushButton.setText(_translate("Created", "创建"))
        self.pushButton_2.setText(_translate("Created", "删除"))
        self.pushButton_3.setText(_translate("Created", "发布"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Created = QtWidgets.QMainWindow()
    ui = Ui_Created()
    ui.setupUi(Created)
    Created.show()
    sys.exit(app.exec_())