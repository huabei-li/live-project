# -*- coding: utf-8 -*-
import sys
import sqlite3
import random
import http.client
import urllib
import hashlib
import datetime
import re
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from create import Ui_MainWindow


class Create_activ(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.pushButton.clicked.connect(lambda: self.ok())
        self.pushButton_2.clicked.connect(lambda: self.cancel())

    def ok(self):
        self.name = self.lineEdit.text()  # 活动名称
        self.text = self.textEdit.toPlainText()  # 文案
        self.keyword = self.lineEdit_2.text()  # 关键词
        self.starttime = self.dateTimeEdit.date()  # 开始时间
        self.stoptime = self.dateTimeEdit_2.date()  # 结束时间
        self.rule1 = self.radioButton.isChecked()
        self.rule2 = self.radioButton_2.isChecked()
        self.rule3 = self.radioButton_3.isChecked()
        self.first_prize = self.spinBox.Value()
        self.second_prize = self.spinBox_2.text()
        self.third_prize = self.spinBox_3.text()
        self.publishtime = self.dateTimeEdit_3.date()  # 公布时间

        print(self.name)
        pass

    def cancel(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Create_activ()
    ui.show()
    sys.exit(app.exec_())
