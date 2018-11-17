# -*- coding: utf-8 -*-
import sys
import datetime
import create_dialog
from DDL_database import insert_act
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate, QDateTime , QTime



class Create_activ(QDialog,create_dialog.Ui_Create_Dialog):

    def __init__(self, parent=None):
        super(Create_activ, self).__init__(parent)
        # 这两句坑死人
        self.setupUi(self)
        self.retranslateUi(self)

        # qt的信号槽机制，连接按钮的点击事件和相应的方法
        self.pushButton.clicked.connect(lambda: self.ok())

    def ok(self):
        """
        :return:
        """
        # 获取信息
        name = self.lineEdit.text()  # 活动名称
        text = self.textEdit.toPlainText()  # 文案
        keyword = self.lineEdit_2.text()  # 关键词
        start_datatime = self.dateTimeEdit.dateTime().toString("yyyyMMddhhmmss")  # 开始时间
        stopt_datatime = self.dateTimeEdit_2.dateTime().toString("yyyyMMddhhmmss")  # 结束时间
        self.rule1 = self.radioButton.isChecked()
        self.rule2 = self.radioButton_2.isChecked()
        self.rule3 = self.radioButton_3.isChecked()
        first_prize = self.spinBox.value()
        second_prize = self.spinBox_2.value()
        third_prize = self.spinBox_3.value()
        publish_datatime = self.dateTimeEdit_3.dateTime().toString("yyyyMMddhhmmss")  # 公布时间
        path=self.lineEdit_3.text() # 路径
        now_time = datetime.datetime.now()
        insert_act(now_time,name, keyword, text, 0, path, start_datatime, stopt_datatime, publish_datatime)

    def rule(self):
        """
        :return: bool值，选择过滤规则
        """
        if self.rule1:
            return self.rule1
        elif self.rule2:
            return self.rule2
        else:
            return self.rule3



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Create_activ()
    ui.show()
    sys.exit(app.exec_())
