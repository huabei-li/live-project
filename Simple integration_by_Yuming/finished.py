# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finished.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Finished(object):
    def setupUi(self, Finished):
        Finished.setObjectName("Finished")
        Finished.resize(620, 600)
        self.buttonBox = QtWidgets.QDialogButtonBox(Finished)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Finished)
        self.buttonBox.accepted.connect(Finished.accept)
        self.buttonBox.rejected.connect(Finished.reject)
        QtCore.QMetaObject.connectSlotsByName(Finished)

    def retranslateUi(self, Finished):
        _translate = QtCore.QCoreApplication.translate
        Finished.setWindowTitle(_translate("Finished", "抽奖助手-已结束抽奖"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Finished = QtWidgets.QDialog()
    ui = Ui_Finished()
    ui.setupUi(Finished)
    Finished.show()
    sys.exit(app.exec_())