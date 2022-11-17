#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 处理逻辑


import serial
import threading
import time
import datetime

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


class SerialAuto(object):

    def __init__(self, com, dbs, timeout):
        self.err = 0
        self.com = com
        self.dbs = dbs
        self.timeout = timeout
        self.err_date = ''  # 做是否有错误判断的数据
        self.txt_date = ''  # 写入TXT的数据
        self.err_count = 0  # 记录错误次数

        self.ui = QUiLoader().load('main.ui')
        # self.ui.setMinimumSize(370, 200)
        # self.ui.setMaximumSize(370, 200)
        self.ui.scanButton.clicked.connect(self.thread_sender)  #
        self.ui.goButton.clicked.connect(self.thread_sender)  # 开始
        # self.ui.devButton.clicked.connect(self.thread_devStatus)  # 设备信息

        try:
            self.ser = serial.Serial(self.com,
                                     self.dbs,
                                     timeout=self.timeout)
            print("*********打开串口成功*********")
        except Exception as e:
            print("*********串口异常:{}*********".format(e))
            self.err = -1

    # 向串口写入数据
    def thread_sender(self):
        threading.Thread(target=self.write_date).start()
    #
    # # 查询设备信息
    # def thread_devStatus(self):
    #     thread = threading.Thread(target=self.devStatus)
    #     thread.start()
    #
    # # 运行所有程序
    # def thread_all_run(self):
    #     thread = threading.Thread(target=self.all_run)
    #     thread.start()
    #     self.ui.goButton.setEnabled(False)  # 禁止按钮



    # 向串口写入数据
    def write_date(self):
        send_list = ['iot_test 01 01\r',  # 开机
                     'iot_test 02 01\r', 'iot_test 02 02\r', 'iot_test 02 03\r',  # 手动挡/自定义档位/自动挡
                     'iot_test 04 01 01\r', 'iot_test 04 01 05\r', 'iot_test 04 01 09\r',
                     'iot_test 03 01\r', 'iot_test 03 00\r',  # 热雾
                     'iot_test 07 01\r', 'iot_test 07 00\r',  # 水箱灯
                     'iot_test 06 01\r', 'iot_test 06 00\r',  # 夜灯
                     'iot_test 05 01\r', 'iot_test 05 00\r',  # 童锁
                     'iot_test 013 00\r', 'iot_test 13 01\r',  # 显示
                     'iot_test 01 00\r']  # 关机
        m = 0
        while True:
            print("========第{}次测试开始========".format(m + 1))
            for i in range(len(send_list)):
                self.ser.write(send_list[i].encode())
                time.sleep(3)
            print("========第{}次测试完成========".format(m + 1))
            # program.date_result(send_list)
            # m += 1
            # if m == test_count:
            #     print("所有测试完成,一共测试了{}轮".format(m))
            #     print("*********出现了{}次错误*********".format(program.date_result(send_list)))
            #     break


    # 判断错误数据
    def date_result(self, n):
        date = self.err_date.split('\r')
        # print(len(date))
        if len(date) - 1 == len(n):  # 因为split分隔后会多一段数据，所以-1
            self.err_date = ''
        elif len(date) == 1:
            pass
        else:
            err_ = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S前的一次执行中有错误！！！"))
            self.txt_date += err_
            SerialAuto.write_txt(self.txt_date)
            print(err_)
            self.err_date = ''
            self.err_count += 1
        return self.err_count

    # 数据写入txt文档
    @staticmethod
    def write_txt(t):
        result = str(t)
        try:
            with open('log.txt', 'w') as file_handle:
                file_handle.write(result)
        except Exception as e:
            print("文件读写出错：", e)

    # 线程读取数据
    def thread_recv(self, d):
        try:
            thread = threading.Thread(target=self.read_date, args=(d,), daemon=True)
            thread.start()
        except Exception as e:
            print("无法启动线程:{}".format(e))

    # 读取处理数据
    def read_date(self, check_date):
        print("线程1")
        while True:
            now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S----->")
            try:
                date_line = self.ser.readline().decode()
                time.sleep(0.1)
                self.txt_date += str(date_line)  # 所有写入到txt文档

                # if 'Please input password:' in date_line:
                #     self.write_date("govee\r")
                #     self.write_date("log print 0\r")
                if check_date['开机'] in date_line:
                    success_date = str(now_time) + "开机\r"
                    self.err_date += success_date
                    self.txt_date += success_date
                    self.ui.textBrowser.append(success_date)
                    # print(success_date)
                elif check_date['关机'] in date_line:
                    success_date1 = str(now_time) + "关机\r"
                    self.err_date += success_date1
                    self.txt_date += success_date1
                    self.ui.textBrowser.append(success_date1)
                    print(success_date1)
                elif check_date['手动挡'] in date_line:
                    success_date2 = str(now_time) + '手动挡\r'
                    self.err_date += success_date2
                    self.txt_date += success_date2
                    print(success_date2)
                elif check_date['自定义挡'] in date_line:
                    success_date = str(now_time) + '自定义挡\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['自动挡'] in date_line:
                    success_date = str(now_time) + '自动挡\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['一档'] in date_line:
                    success_date = str(now_time) + '一档\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['二档'] in date_line:
                    success_date = str(now_time) + '二档\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['三档'] in date_line:
                    success_date = str(now_time) + '三档\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['开启热雾'] in date_line:
                    success_date = str(now_time) + '开启热雾\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['关闭热雾'] in date_line:
                    success_date = str(now_time) + '关闭热雾\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['开启水箱灯'] in date_line:
                    success_date = str(now_time) + '开启水箱灯\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['关闭水箱灯'] in date_line:
                    success_date = str(now_time) + '关闭水箱灯\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['开启夜灯'] in date_line:
                    success_date = str(now_time) + '开启夜灯\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['关闭夜灯'] in date_line:
                    success_date = str(now_time) + '关闭夜灯\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['开启童锁'] in date_line:
                    success_date = str(now_time) + '开启童锁\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['关闭童锁'] in date_line:
                    success_date = str(now_time) + '关闭童锁\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['开启显示'] in date_line:
                    success_date = str(now_time) + '开启显示\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                elif check_date['关闭显示'] in date_line:
                    success_date = str(now_time) + '关闭显示\r'
                    self.err_date += success_date
                    self.txt_date += success_date
                    print(success_date)
                SerialAuto.write_txt(self.txt_date)
            except Exception as e:
                print("获取数据错误!", e)
                break


if __name__ == '__main__':
    app = QApplication([])
    program = SerialAuto('com13', 115200, 3)
    program.ui.show()
    app.exec_()
    m = 0  # 统计测试次数
    check_dates = {'开机': '55 11 01 00 01 01 69', '关机': '55 11 01 00 01 00 68', '手动挡': '55 11 02 00 01 01 6A',
                   '自定义挡': '55 11 02 00 01 02 6B', '自动挡': '55 11 02 00 01 03 6C', '开启热雾': '55 11 03 00 01 01 6B',
                   '关闭热雾': '55 11 03 00 01 00 6A', '开启水箱灯': '55 11 07 00 01 01 6F', '关闭水箱灯': '55 11 07 00 01 00 6E',
                   '开启夜灯': '55 11 06 00 01 01 6E', '关闭夜灯': '55 11 06 00 01 00 6D', '开启童锁': '55 11 05 00 01 01 6D',
                   '关闭童锁': '55 11 05 00 01 00 6C', '开启显示': '55 11 13 00 01 01 7B', '关闭显示': '55 11 13 00 01 00 7A',
                   '一档': '55 11 04 00 02 01 01 6E', '二档': '55 11 04 00 02 01 05 72', '三档': '55 11 04 00 02 01 09 76'}

    # 如果
    if program.err == 0:
        # print("初始化成功...")
        # test_count = int(input("输入需要测试的次数："))  # 测试的次数
        # print("*********开启读取数据*********\r")
        program.thread_recv(check_dates)

