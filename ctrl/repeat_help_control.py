import sys
sys.path.append("..")
from view.repeat_run_help import Ui_repeathelpDialog

class Repeathelp(Ui_repeathelpDialog):
    def setupUi(self, repeathelpDialog):
        Ui_repeathelpDialog.setupUi(self,repeathelpDialog)
        self.Dialog = repeathelpDialog
        self.verity.clicked.connect(self.verify_f)


    def verify_f(self):
        self.Dialog.close()