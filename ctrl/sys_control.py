import sys
sys.path.append("..")
from view.systemdatasetting import *
from ctrl.runtime_control import *
from ctrl.sys_help_control import *

class Systemdatasetting(Ui_QDialog):
    def setupUi(self, QDialog):
        Ui_QDialog.setupUi(self, QDialog)
        self.DateInspection.clicked.connect(self.data_check_f)
        self.Reset_1.clicked.connect(self.Reset_f)
        self.Help.clicked.connect(self.Help_f)
        self.Cancel.clicked.connect(QCoreApplication.instance().quit)
        self.QDialog = QDialog
        self.Reset_f()

    def data_check_f(self):
        '''
        数据检查函数
        :return:
        '''
        # 下面是接受数据
        probability_data = [self.PCusSer1.text(), self.PCusSer2.text(), self.PCusSer3.text(),
                            self.PCusSer4.text(), self.PCusSer5.text(), self.PCusSer6.text()]
        num_people = self.NumOfPeo.text()
        time_max = self.arrive_timemax.text()
        time_min = self.arrive_timemin.text()
        # 正则表达式判断是否是浮点数
        value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
        result = True

        for i in range(0, 6):
            tmp = value.match(probability_data[i])
            if tmp == False or tmp == None:
                result = False
                break
            else:
                probability_data[i] = float(probability_data[i])

        if result != False:
            for i in [time_min, time_max, num_people]:
                tmp = value.match(i)
                if tmp == False:
                    result = False
                    break
            time_max = float(time_max)
            time_min = float(time_min)
            num_people = float(num_people)

        # 数据输入有误
        if result == False or self.model1.data_check(probability_data, time_max, time_min, num_people) == False:
            reply = QMessageBox.warning(self,  # 使用infomation信息框
                                        "警告",
                                        "数据输入有误",
                                        QMessageBox.Cancel)

        else:
            self.probailities_data = probability_data
            self.time_min = time_min
            self.time_max = time_max
            self.num_people = num_people
            # 下面是界面更新
            tmp = probability_data[0]
            tmp = round(tmp, 1)
            self.CPCusSer1.setText(str(tmp))
            tmp += probability_data[1]
            tmp = round(tmp, 1)
            self.CPCusSer2.setText(str(tmp))
            tmp += probability_data[2]
            tmp = round(tmp, 1)
            self.CPCusSer3.setText(str(tmp))
            tmp += probability_data[3]
            tmp = round(tmp, 1)
            self.CPCusSer4.setText(str(tmp))
            tmp += probability_data[4]
            tmp = round(tmp, 1)
            self.CPCusSer5.setText(str(tmp))
            tmp += probability_data[5]
            tmp = round(tmp, 1)
            self.CPCusSer6.setText(str(tmp))

            # 界面跳转
            self.jump_to_runningtimes()

    def jump_to_runningtimes(self):
        '''
        界面跳转次数函数
        :return:
        '''
        self.QDialog.hide()
        form1 = QtWidgets.QDialog()
        ui = Runningtime()
        ui.setupUi(form1)
        ui.get_data(self.num_people, self.time_max, self.time_min, self.probailities_data)
        form1.show()
        form1.exec()
        self.QDialog.show()

    def Help_f(self):
        '''
        帮助函数，跳转到帮助界面，查看对数据的要求
        :return:
        '''
        form2 = QDialog()
        ui = Sys_help()
        ui.setupUi(form2)
        form2.show()
        form2.exec()

    def Reset_f(self):
        '''
        设置界面上的默认值
        :return:
        '''
        self.PCusSer1.setText(str(0.1))
        self.PCusSer2.setText(str(0.1))
        self.PCusSer3.setText("0.2")
        self.PCusSer4.setText("0.2")
        self.PCusSer5.setText("0.2")
        self.PCusSer6.setText("0.2")
        self.CPCusSer1.setText("0.1")
        self.CPCusSer2.setText("0.2")
        self.CPCusSer3.setText("0.4")
        self.CPCusSer4.setText("0.6")
        self.CPCusSer5.setText("0.8")
        self.CPCusSer6.setText("1.0")
        self.arrive_timemax.setText("12")
        self.arrive_timemin.setText("2")
        self.NumOfPeo.setText("10")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Systemdatasetting()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
