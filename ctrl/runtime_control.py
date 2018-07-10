import sys

sys.path.append("..")
from view.running_times import *
from ctrl.once_run_ctrl import *
from ctrl.repeat_control import *

class Runningtime(Ui_Dialog):
    def setupUi(self, Dialog):
        '''
        重构setupUi函数，并联系button与相应函数
        :param Dialog:
        :return:
        '''
        Ui_Dialog.setupUi(self, Dialog)
        self.RunOnce.clicked.connect(self.jump_to_once)
        self.RepeatedRun.clicked.connect(self.jump_to_repeat)
        self.Dialog = Dialog

    def jump_to_once(self):
        '''
        跳转到一次运行界面
        :return:
        '''
        # self.Dialog.hide()
        form = QtWidgets.QDialog()
        ui = OnceRunCtrl(self.num, self.max, self.min, self.probabilities)
        ui.setupUi(form)
        form.show()
        form.exec()

    def jump_to_repeat(self):
        '''
        跳转到多次运行界面
        :return:
        '''
        form = QtWidgets.QDialog()
        ui = RepeatControl(self.num, self.max, self.min, self.probabilities)
        ui.setupUi(form)
        form.show()
        form.exec()
        self.Dialog.show()

    def get_data(self, num, max, min, probabilities):
        '''
        接受来自初始界面的数据
        :param num: 人数
        :param max: 间隔时间最大值
        :param min: 间隔时间最小值
        :param probabilities: 到达时间的概率
        :return:
        '''
        self.num = num
        self.max = max
        self.min = min
        self.probabilities = probabilities
