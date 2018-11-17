# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'created.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from create_dialog_behind import *
class Ui_Created(object):
    def setupUi(self, Created):
        Created.setObjectName("Created")
        Created.resize(620, 600)
        self.buttonBox = QtWidgets.QDialogButtonBox(Created)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Created)
        self.pushButton.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Created)
        self.buttonBox.accepted.connect(Created.accept)
        self.buttonBox.rejected.connect(Created.reject)
        QtCore.QMetaObject.connectSlotsByName(Created)
        self.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        ui = Create_activ()
        ui.show()
        ui.exec_()

    def retranslateUi(self, Created):
        _translate = QtCore.QCoreApplication.translate
        Created.setWindowTitle(_translate("Created", "抽奖助手-已创建抽奖"))
        self.pushButton.setText(_translate("Created", "创建"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Created = QtWidgets.QDialog()
    ui = Ui_Created()
    ui.setupUi(Created)
    Created.show()
    sys.exit(app.exec_())