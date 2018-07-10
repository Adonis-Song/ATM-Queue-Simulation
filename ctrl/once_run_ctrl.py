from PyQt5.QtWidgets import QTableWidgetItem, QDialog
from view.once_run_view import Ui_OnceRun
from model.Model import Model
from ctrl.once_help_control import Oncehelp


class OnceRunCtrl(Ui_OnceRun):
    def __init__(self, num, max_num, min_num, probabilities):
        super().__init__()
        self.num = num
        self.max = max_num
        self.min = min_num
        self.probabilities = probabilities

    def setupUi(self, once_run):
        Ui_OnceRun.setupUi(self, once_run)
        self.clr_cache_btn.clicked.connect(self.clr_cache)
        self.finish_btn.clicked.connect(self.finish)
        self.once_run_btn.clicked.connect(self.once_run)
        self.help_btn.clicked.connect(self.help)

    def clr_cache(self):
        while self.once_run_table.rowCount() != 0:
            self.once_run_table.removeRow(0)
        self.once_run_table.insertRow(0)
        item = QTableWidgetItem()
        item.setText("**")
        self.once_run_table.setVerticalHeaderItem(0, item)
        self.sys_use_txt.clear()
        self.avg_txt.clear()

    def finish(self):
        exit(0)

    def once_run(self):
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
        help_dialog = QDialog()
        ui = Oncehelp()
        ui.setupUi(help_dialog)
        help_dialog.show()
        help_dialog.exec()
