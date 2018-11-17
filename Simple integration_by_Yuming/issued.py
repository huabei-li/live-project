# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'issued.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Issued(object):
    def setupUi(self, Issued):
        Issued.setObjectName("Issued")
        Issued.resize(620, 600)
        self.buttonBox = QtWidgets.QDialogButtonBox(Issued)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Issued)
        self.buttonBox.accepted.connect(Issued.accept)
        self.buttonBox.rejected.connect(Issued.reject)
        QtCore.QMetaObject.connectSlotsByName(Issued)

    def retranslateUi(self, Issued):
        _translate = QtCore.QCoreApplication.translate
        Issued.setWindowTitle(_translate("Issued", "抽奖助手-已发布抽奖"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Issued = QtWidgets.QDialog()
    ui = Ui_Issued()
    ui.setupUi(Issued)
    Issued.show()
    sys.exit(app.exec_())