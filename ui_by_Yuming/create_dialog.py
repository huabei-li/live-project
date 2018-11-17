# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime , QTime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create_Dialog(object):
    def setupUi(self, Create_Dialog):
        Create_Dialog.setObjectName("Create_Dialog")
        Create_Dialog.resize(620, 600)
        self.pushButton_2 = QtWidgets.QPushButton(Create_Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(491, 560, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Create_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 560, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Create_Dialog)
        self.widget.setGeometry(QtCore.QRect(160, 10, 301, 540))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        # 指定当前日期时间为控件的日期时间
        nowdatetime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(nowdatetime)
        #设置日期时间格式
        self.dateTimeEdit.setDisplayFormat("yyyy/MM/dd HH:mm:ss")

        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)

        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit")
        # 指定当前日期时间为控件的日期时间
        self.dateTimeEdit_2.setDateTime(nowdatetime)
        # 设置日期时间格式
        self.dateTimeEdit_2.setDisplayFormat("yyyy/MM/dd HH:mm:ss")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_11.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        #过滤规则提示
        self.radioButton.setToolTip("这是不过滤")

        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        # 过滤规则提示
        self.radioButton_2.setToolTip("这是轻度过滤")

        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        # 过滤规则提示
        self.radioButton_3.setToolTip("这是深度过滤")

        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_6.addWidget(self.spinBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_7.addWidget(self.spinBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)

        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_3.setObjectName("dateTimeEdit")
        # 指定当前日期时间为控件的日期时间
        self.dateTimeEdit_3.setDateTime(nowdatetime)
        # 设置日期时间格式
        self.dateTimeEdit_3.setDisplayFormat("yyyy/MM/dd HH:mm:ss")

        self.horizontalLayout_9.addWidget(self.dateTimeEdit_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Create_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Create_Dialog)

    def retranslateUi(self, Create_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Create_Dialog.setWindowTitle(_translate("Create_Dialog", "创建新抽奖"))
        self.pushButton_2.setText(_translate("Create_Dialog", "取消"))
        self.pushButton.setText(_translate("Create_Dialog", "创建"))
        self.label.setText(_translate("Create_Dialog", "活动名称"))
        self.label_7.setText(
            _translate("Create_Dialog", "<html><head/><body><p align=\"center\">活动文案</p></body></html>"))
        self.label_2.setText(_translate("Create_Dialog", "关键词"))
        self.label_3.setText(_translate("Create_Dialog", "抽奖开始时间"))
        self.label_8.setText(_translate("Create_Dialog", "抽奖结束时间"))
        self.label_12.setText(_translate("Create_Dialog", "聊天记录保存路径"))
        self.label_4.setText(_translate("Create_Dialog", "过滤规则"))
        self.radioButton.setText(_translate("Create_Dialog", "不过滤"))
        self.radioButton_2.setText(_translate("Create_Dialog", "轻度过滤"))
        self.radioButton_3.setText(_translate("Create_Dialog", "深度过滤"))
        self.label_5.setText(_translate("Create_Dialog", "奖品设置"))
        self.label_9.setText(_translate("Create_Dialog", "一等奖人数"))
        self.label_10.setText(_translate("Create_Dialog", "二等奖人数"))
        self.label_11.setText(_translate("Create_Dialog", "三等奖人数"))
        self.label_6.setText(_translate("Create_Dialog", "结果公布时间"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Create_Dialog = QtWidgets.QDialog()
    ui = Ui_Create_Dialog()
    ui.setupUi(Create_Dialog)
    Create_Dialog.show()
    sys.exit(app.exec_())
