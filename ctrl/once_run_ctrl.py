from PyQt5.QtWidgets import QTableWidgetItem, QDialog
from view.once_run_view import *
from model.Model import Model
from ctrl.once_help_control import Oncehelp

class OnceRunCtrl(Ui_once_run):
    def __init__(self, num, max_num, min_num, probabilities):
        super().__init__()
        self.num = num
        self.max = max_num
        self.min = min_num
        self.probabilities = probabilities

    def setupUi(self, once_run):
        '''
        重构setupUi函数，并将button与相应的函数相连
        :param once_run:
        :return:
        '''
        self.oncedialog = once_run
        Ui_once_run.setupUi(self, once_run)
        self.clr_cache_btn.clicked.connect(self.clr_cache)
        self.finish_btn.clicked.connect(self.finish)
        self.once_run_btn.clicked.connect(self.once_run)
        self.help_btn.clicked.connect(self.help)

    def clr_cache(self):
        '''
        将显示窗口的所有数据清空
        :return:
        '''
        while self.once_run_table.rowCount() != 0:
            self.once_run_table.removeRow(0)
        self.once_run_table.insertRow(0)
        item = QTableWidgetItem()
        item.setText("**")
        self.once_run_table.setVerticalHeaderItem(0, item)
        self.sys_use_txt.clear()
        self.avg_txt.clear()

    def finish(self):
        '''
        完成并退出此界面
        :return:
        '''
        self.oncedialog.close()

    def once_run(self):
        '''
        一次运行函数，将结果显示在界面上
        :return:
        '''
        self.clr_cache()
        m = Model()
        m.data_gen(int(self.num), int(self.max), int(self.min), self.probabilities)
        m.result_cal(int(self.num))
        r = m.data_pool()
        col_count = self.once_run_table.columnCount()
        self.once_run_table.removeRow(0)
        for j in range(len(r[0])):
            self.once_run_table.insertRow(j)
            self.once_run_table.setVerticalHeaderItem(j, QTableWidgetItem(str(j + 1)))
            self.once_run_table.setItem(j, 0, QTableWidgetItem(str(j + 1)))
            for i in range(1, col_count):
                self.once_run_table.setItem(j, i, QTableWidgetItem(str(r[i - 1][j])))
        self.avg_txt.setText(str(r[8]))
        self.sys_use_txt.setText(str(r[9]))

    def help(self):
        '''
        帮助函数，会显示运行规则
        :return:
        '''
        help_dialog = QDialog()
        ui = Oncehelp()
        ui.setupUi(help_dialog)
        help_dialog.show()
        help_dialog.exec()
