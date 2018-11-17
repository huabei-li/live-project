# -*- coding: utf-8 -*-
import sys
import sqlite3
import random
import http.client
import urllib
import hashlib
import datetime
import re
import create_dialog_front
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate, QDateTime , QTime



class Create_activ(QDialog,create_dialog_front.Ui_Create_Dialog):

    def __init__(self, parent=None):
        super(Create_activ, self).__init__(parent)
        # 这两句坑死人
        self.setupUi(self)
        self.retranslateUi(self)


        # qt的信号槽机制，连接按钮的点击事件和相应的方法
        self.pushButton.clicked.connect(lambda: self.ok())
        # self.pushButton_2.clicked.connect(lambda :self.cancel())
        # self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)  # 取消键，关闭当前窗口

    def ok(self):
        # 获取信息
        name = self.lineEdit.text()  # 活动名称
        text = self.textEdit.toPlainText()  # 文案
        keyword = self.lineEdit_2.text()  # 关键词
        start_datatime = self.dateTimeEdit.dateTime().toString("yyyyMMddhhmmss")  # 开始时间
        stopt_datatime = self.dateTimeEdit_2.dateTime().toString("yyyyMMddhhmmss")  # 结束时间
        rule1 = self.radioButton.isChecked()
        rule2 = self.radioButton_2.isChecked()
        rule3 = self.radioButton_3.isChecked()
        first_prize = self.spinBox.value()
        second_prize = self.spinBox_2.value()
        third_prize = self.spinBox_3.value()
        publish_datatime = self.dateTimeEdit_3.dateTime().toString("yyyyMMddhhmmss")  # 公布时间
        print("ok")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Create_activ()
    ui.show()
    sys.exit(app.exec_())
