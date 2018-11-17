# -*- coding: utf-8 -*-
import sys
import sqlite3
import random
import http.client
import urllib
import hashlib
import datetime
import re
import createdtable
import Created
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate, QDateTime , QTime



class Create_activ(QDialog,createdtable.Ui_Created):

    def __init__(self, parent=None):
        super(Create_activ, self).__init__(parent)
        # 这两句坑死人
        self.setupUi(self)
        self.retranslateUi(self)


        # qt的信号槽机制，连接按钮的点击事件和相应的方法
        self.pushButton.clicked.connect(lambda : self.create_button())
        self.pushButton_2.clicked.connect(lambda : self.delete_button())
        self.pushButton_3.clicked.connect(lambda : self.publish_button())


    def create_button(self):
        Create_Dialog = QtWidgets.QDialog()
        ui = Created.Create_activ()
        ui.setupUi(Create_Dialog)
        ui.pushButton.clicked.connect(lambda: ui.ok())
        Create_Dialog.show()
        Create_Dialog.exec_()





    def delete_button(self):
        print("delete")


    def publish_button(self):
        print("publish")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Create_activ()
    ui.show()
    sys.exit(app.exec_())
