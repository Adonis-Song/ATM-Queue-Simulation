import sys
sys.path.append("..")
from view.repeat_run_help import Ui_repeathelpDialog

class Repeathelp(Ui_repeathelpDialog):
    def setupUi(self, repeathelpDialog):
        '''
        重构setupUi函数，并联系button与相应函数
        :param repeathelpDialog:
        :return:
        '''
        Ui_repeathelpDialog.setupUi(self,repeathelpDialog)
        self.Dialog = repeathelpDialog
        self.verity.clicked.connect(self.verify_f)

    def verify_f(self):
        '''
        退出此界面
        :return:
        '''
        self.Dialog.close()