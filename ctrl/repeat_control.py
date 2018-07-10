from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QWidget, QDialog

from model.Model import *
from view.repeat_run import *
import re
import sys
sys.path.append("..")
from ctrl.repeat_help_control import *

class RepeatControl(Ui_RepeatRun):
    def __init__(self, num_people, max_avg, min_avg, probabilities, parent=None):
        """
        Constructor
        :return:
        """
        super().__init__()
        self.model = Model()
        self.repeat_time = 0
        self.num_people = num_people
        self.max = max_avg
        self.min = min_avg
        self.probabilities = probabilities
        self.avg_list = []

    def setupUi(self, dialog):
        """
        connect button to function
        :return:
        """
        self.repeatdialog = dialog
        Ui_RepeatRun.setupUi(self, dialog)
        self.Verify.clicked.connect(self.verify)
        self.Reset.clicked.connect(self.reset)
        self.Finish.clicked.connect(self.finish)
        self.Help.clicked.connect(self.help)

    def verify(self):
        """
        Show all the result in the two widgets at top-left and bottom
        :return:
        """
        # 获取并判断输入框输入值的合法性
        s = self.Repetitions.text()
        flag = re.match(r"\d*$", s)
        if s is "" or flag is None or int(s) == 0:
            QMessageBox.information(self,
                                    "警告",
                                    "次数输入错误，请重新输入",
                                    QMessageBox.Cancel)
            self.Repetitions.clear()
            return
        self.repeat_time = int(s)
        # 先重置界面
        self.reset()
        # 输出平均排队时间表
        self.tableWidget_avg_wait.removeRow(0)
        for every_time in range(self.repeat_time):
            self.tableWidget_avg_wait.insertRow(every_time)
            self.tableWidget_avg_wait.setVerticalHeaderItem(every_time, QTableWidgetItem(str(every_time + 1)))
            self.tableWidget_avg_wait.setItem(every_time, 0, QTableWidgetItem(str(every_time + 1)))
            self.model.reset()
            self.model.data_gen(int(self.num_people), int(self.max), int(self.min), self.probabilities)
            self.model.result_cal(int(self.num_people))
            result = self.model.data_pool()
            self.tableWidget_avg_wait.setItem(every_time, 1, QTableWidgetItem(str(round(result[8], 1))))
            self.avg_list.append(result[8])

        # 输出n次实验最大，最小，平均排队时间及实验次数
        result = self.model.data_pool()
        self.MaxData.setText(str(round(np.max(self.avg_list), 1)))
        self.MinData.setText(str(round(np.min(self.avg_list), 1)))
        self.AverageDate.setText(str(round(float(np.mean(self.avg_list)), 1)))
        print(type(np.mean(self.avg_list)))
        self.NumOfData.setText(str(self.repeat_time))

        # 输出最后一次结果表
        self.tableWidget_last_result.removeRow(0)
        for j in range(len(result[0])):
            col_count = self.tableWidget_last_result.columnCount()
            self.tableWidget_last_result.insertRow(j)
            self.tableWidget_last_result.setVerticalHeaderItem(j, QTableWidgetItem(str(j + 1)))
            self.tableWidget_last_result.setItem(j, 0, QTableWidgetItem(str(j + 1)))
            for i in range(1, col_count):
                self.tableWidget_last_result.setItem(j, i, QTableWidgetItem(str(result[i - 1][j])))

    def reset(self):
        """
        Clear all data and back to initial status
        :return:
        """
        # 重置最后一次结果的表
        while self.tableWidget_last_result.rowCount() != 0:
            self.tableWidget_last_result.removeRow(0)
        self.tableWidget_last_result.insertRow(0)
        self.tableWidget_last_result.setVerticalHeaderItem(0, QTableWidgetItem("**"))

        # 重置平均排队时间表
        while self.tableWidget_avg_wait.rowCount() != 0:
            self.tableWidget_avg_wait.removeRow(0)
        self.tableWidget_avg_wait.insertRow(0)
        self.tableWidget_avg_wait.setVerticalHeaderItem(0, QTableWidgetItem("**"))

        # 重置其他组件
        self.NumOfData.clear()
        self.Repetitions.clear()
        self.MaxData.clear()
        self.MinData.clear()
        self.AverageDate.clear()

        # 重置平均排队时间缓存列表
        self.avg_list = []

    def finish(self):
        """
        Close the window and turn off
        :return:
        """
        # 直接退出程序
        self.repeatdialog.close()

    def help(self):
        """
        Show the manual help
        :return:
        """
        rehelpdialog = QDialog()
        ui = Repeathelp()
        ui.setupUi(rehelpdialog)
        rehelpdialog.show()
        rehelpdialog.exec()
