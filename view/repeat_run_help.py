# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repeat_run_help.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_repeathelpDialog(object):
    def setupUi(self, repeathelpDialog):
        repeathelpDialog.setObjectName("repeathelpDialog")
        repeathelpDialog.resize(522, 412)
        self.label = QtWidgets.QLabel(repeathelpDialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 411, 261))
        self.label.setObjectName("label")
        self.verity = QtWidgets.QPushButton(repeathelpDialog)
        self.verity.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.verity.setObjectName("verity")

        self.retranslateUi(repeathelpDialog)
        QtCore.QMetaObject.connectSlotsByName(repeathelpDialog)

    def retranslateUi(self, repeathelpDialog):
        _translate = QtCore.QCoreApplication.translate
        repeathelpDialog.setWindowTitle(_translate("repeathelpDialog", "帮助"))
        self.label.setText(_translate("repeathelpDialog", "<html><head/><body><p>规则说明</p><p>1.首先在重复次数里面输入次数，输入必须为正整数。</p><p>2.输出次数后点击“确定”，</p><p>3.之后会在左边的显示框中输出编号以及相应的排队时间</p><p>4.同时在下方的输出框中会显示最后一次的运行结果</p><p>5.点击“重置”，可重复实验</p><p>6.点击“完成”，退出软件</p></body></html>"))
        self.verity.setText(_translate("repeathelpDialog", "确定"))

