import sys
sys.path.append("..")
from view.once_run_help import *

class Oncehelp(Ui_Dialog):
    def setupUi(self, Dialog):
        Ui_Dialog.setupUi(self,Dialog)
        self.Dialog = Dialog
        self.verifty.clicked.connect(self.verifty_f)

    def verifty_f(self):
        '''
        退出此界面
        :return:
        '''
        self.Dialog.close()