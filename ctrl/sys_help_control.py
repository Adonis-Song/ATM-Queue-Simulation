import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QCloseEvent

sys.path.append("..")

from view.sys_help import *

class Sys_help(Ui_syshelp):
    def setupUi(self, syshelp):
        '''
        重构setupUi函数，并联系button与相应函数
        :param syshelp:
        :return:
        '''
        self.dialog = syshelp
        Ui_syshelp.setupUi(self,syshelp)
        self.verify.clicked.connect(self.verify_f)

    def verify_f(self):
        '''
        完成关闭此窗口
        :return:
        '''
        self.dialog.close()

