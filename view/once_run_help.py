# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'once_run_help.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 311)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 391, 131))
        self.label.setObjectName("label")
        self.verifty = QtWidgets.QPushButton(Dialog)
        self.verifty.setGeometry(QtCore.QRect(160, 200, 93, 28))
        self.verifty.setObjectName("verifty")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "帮助"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>点击“运行一次”开始运行，并在显示框中显示相应的数据</p><p>点击“清除数据缓存”，所有数据清空</p><p><br/></p></body></html>"))
        self.verifty.setText(_translate("Dialog", "确定"))

