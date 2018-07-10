import pymysql
import random


import numpy as np


class Model:

    def __init__(self):
        self.arrive_time = []
        self.interval_time = []
        self.serve_time = []
        self.serve_start_time = []
        self.wait_time = []
        self.serve_end_time = []
        self.spend_time = []
        self.sys_free_time = []
        self.avg_wait_time = 0
        self.sys_util = 0
        pass

    def data_gen(self, num, max, min, probabilities):
        # 下面是生成到达时间的随机值
        tmp = True
        y = []
        lam = (max + min) / 2
        while tmp:
            time_list = np.random.poisson(lam, size=num).tolist()
            for i in time_list:
                if i > max or i < min:
                    time_list.remove(i)
            y = y + time_list
            if len(y) >= num:
                tmp = False

        if len(y) > num:
            y = y[:num]

        y.sort()
        self.arrive_time = y

        # 下面是生成服务时间的随机值
        seq = [1, 2, 3, 4, 5, 6]
        while len(self.serve_time) != num:
            z = random.uniform(0, 1)
            cumprob = 0.0
            for item, item_pro in zip(seq, probabilities):
                cumprob += item_pro
                if z < cumprob:
                    break
            self.serve_time.append(item)

    def result_cal(self, num):
        # 对第一次进行数据添加
        self.wait_time.append(0)
        self.serve_end_time.append(self.serve_time[0]+self.arrive_time[0])
        self.interval_time.append(0)
        self.serve_start_time.append(0)
        self.sys_free_time.append(0)
        # 对后面的进行数据添加
        for i in range(1, num):
            wait_time = self.serve_end_time[i - 1] - \
                self.arrive_time[i]  # 等待时间=上一次的结束时间-到达时间
            if wait_time < 0:
                # 等待时间如果为0，第i个顾客的系统空闲时间就不为0
                self.sys_free_time.append(wait_time)
                wait_time = 0
            else:
                self.sys_free_time.append(0)
            self.wait_time.append(wait_time)
            self.serve_end_time.append(self.arrive_time[i]+self.wait_time[i]+self
                                       .serve_time[i])  # 结束时间=等待时间+到达时间+服务时间
        wait_time = 0
        serve_time = self.serve_time[0]
        self.spend_time.append(self.wait_time[0]+self.serve_time[0])
        for i in range(1, num):
            self.serve_start_time.append(
                self.arrive_time[i] + self.wait_time[i])  # 开始时间=到达时间+等待时间
            self.spend_time.append(
                self.wait_time[i]+self.serve_time[i])  # 花费时间 = 等待时间+服务时间
            self.interval_time.append(
                self.arrive_time[i] - self.arrive_time[i-1])  # 间隔时间 = 这次到达时间-上次到达时间
            wait_time = wait_time + self.wait_time[i]
            serve_time = serve_time + self.serve_time[i]
        self.avg_wait_time = wait_time / num  # 系统平均等待时间是等待时间之和除以人数
        # 系统总运行时间 = 最后一个人的结束时间 - 第一个人的到达时间
        all_time = self.serve_end_time[num-1] - self.arrive_time[0]
        self.sys_util = serve_time / all_time  # 系统利用率 = 系统服务总时间 / 系统总运行时间

    def data_pool(self):
        return [self.interval_time, self.arrive_time,
                self.serve_time, self.serve_start_time,
                self.wait_time, self.serve_end_time,
                self.spend_time, self.sys_free_time,
                self.avg_wait_time, self.sys_util]

    def data_check(self, probabilities, max_arr_time, min_arr_time, num_people):
        """  对数据进行检查.  """
        if len(probabilities) != 6 or num_people <= 1:
            return False
        if min_arr_time < 0 or max_arr_time < min_arr_time:
            return False
        total_prob = 0.0
        for every_prob in probabilities:
            if every_prob < 0 or every_prob > 1:
                return False
            total_prob = total_prob + every_prob
        return total_prob == 1

    def reset(self):
        self.arrive_time = []
        self.interval_time = []
        self.serve_time = []
        self.serve_start_time = []
        self.wait_time = []
        self.serve_end_time = []
        self.spend_time = []
        self.sys_free_time = []
        self.avg_wait_time = 0
        self.sys_util = 0

    def connect_db(self):
        config = {'host': '127.0.0.1',
                  'port': 3306,
                  'user': 'root',
                  'password': 'Qaz520..',
                  'db': 'xxq',
                  'charset': 'utf8'
                  }
        return pymysql.connect(**config)

    def create_table(self):
        """
        arg: self
        return: none
        To create a table describes the services for each experiment
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        sql_createDB = """
                        CREATE TABLE IF NOT EXISTS serve(
                        client_id INT UNSIGNED NOT NULL AUTO_INCREMENT  PRIMARY KEY,
                        arrive_time INT UNSIGNED,
                        interval_time INT UNSIGNED,
                        serve_time INT UNSIGNED,
                        serve_start_time INT UNSIGNED,
                        wait_time INT UNSIGNED,
                        serve_end_time INT UNSIGNED,
                        spend_time INT UNSIGNED,
                        sys_free_time INT UNSIGNED,
                        avg_wait_time INT UNSIGNED,
                        sys_util INT UNSIGNED,
                        PRIMARY KEY (client_id)
                        )ENGINE=InnoDB DEFAULT CHARSET=utf8
                        """
        try:
            cursor.execute(sql_createDB)
            conn.commit()
        except:
            conn.rollback()
            print("Exception: create table failed!")
        conn.close()
        cursor.close()

    def insert_service(self, service):
        """
        arg: self
             service: a dict, the service item that will be inserted to table serve
        return: none
        Insert the item 'service' to table 'serve'
        """
        cols = ', '.join(service.keys())
        data = service.values()
        marks = ', '.join(['%s'] * len(service))

        data = list(data)
        for i in range(len(data)):
            data[i] = int(data[i])

        conn = self.connect_db()
        cursor = conn.cursor()
        sql_insert = "INSERT INTO serve (%s) VALUES (%s)" % (cols, marks)
        try:
            cursor.execute(sql_insert, data)
            conn.commit()
        except:
            # 失败回滚
            conn.rollback()
            print("Exception: insert service failed!")
        conn.close()
        cursor.close()

    def delete_service(self, client_id):
        """
        :param client_id: the primary key that to be deleted
        :return: none
        To delete a service item whose primary key is client_id
        """
        sql_delete = "DELETE FROM xxq where client_id = \"%s\"" % client_id
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(sql_delete)
            conn.commit()
        except:
            conn.rollback()
            print("Exception: delete service failed!")
        conn.close()
        cursor.close()
        pass

    def clean_database(self):
        """
        arg: self
        return: none
        Clean the table `xxq`
        """
        sql_drop_table = "DROP TABLE xxq"
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(sql_drop_table)
            conn.commit()
            self.create_table()
        except:
            conn.rollback()
            print("Exception: clean database failed!")
        conn.close()
        cursor.close()
        pass


if __name__ == '__main__':
    """
    This is test code
    """
    """
    model = Model()
    model.create_table()
    service = {
        'client_id' : 1,
        'arrive_time' : 1,
        'interval_time' : 1,
        'serve_time' : 1,
        'serve_start_time' : 1,
        'wait_time' : 1,
        'serve_end_time' : 1,
        'spend_time' : 1,
        'sys_free_time' : 1,
        'avg_wait_time' : 1,
        'sys_util' : 1
    }
    model.insert_service(service)
    """
