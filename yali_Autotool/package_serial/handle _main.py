#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 处理串口
import datetime
import threading
import time

import serial

from yali_Autotool.run import program


class handle_serial():
    # 复选主功能
    def main_func(self, dbs, timeout):
        try:
            com = program.ui.serialEdit.text()  # 串口
            self.ser = serial.Serial(com,
                                     # self.ser = serial.Serial('com8',
                                     self.dbs,
                                     timeout=self.timeout)
            program.ui.resultBrowser.append("*********连接串口成功*********")
            program.ui.mucButton.setEnabled(False)
            program.ui.appButton.setEnabled(False)
        except Exception:
            program.ui.resultBrowser.append("*********端口号错误或者未填写端口号*********")
            program.ui.resultBrowser.append("*********需要重新打开程序*********")
            # self.ui.mcuBox.setEnabled(True)
            self.err = -1
        if program.ui.mcuBox.isChecked():
            program.ui.mcuBox.setEnabled(False)
            program.ui.pushButton.clicked.connect(self.thread_recv)

    # 复选app添加设备
    def add_device_func(self, dbs, timeout):
        self.dbs = dbs
        self.timeout = timeout
        try:
            com = program.ui.serialEdit.text()  # 串口
            self.ser = serial.Serial(com,
                                     # self.ser = serial.Serial('com8',
                                     self.dbs,
                                     timeout=self.timeout)
            program.ui.resultBrowser.append("*********连接串口成功*********")
        except Exception:
            program.ui.resultBrowser.append("*********端口号错误或者未填写端口号*********")
            program.ui.resultBrowser.append("*********需要重新打开程序*********")
            # self.ui.mcuBox.setEnabled(True)
            program.err = -1
        if program.ui.add_deviceBox.isChecked():
            program.ui.pushButton.clicked.connect(self.thread_recv)  # 断言判断
            program.ui.pushButton.clicked.connect(self.thread_add_devices)  # appium启动配置

    # 复选app绑定温湿度计
    def add_temp_func(self, dbs, timeout):
        self.dbs = dbs
        self.timeout = timeout
        try:
            com = program.ui.serialEdit.text()  # 串口
            self.ser = serial.Serial(com,
                                     # self.ser = serial.Serial('com8',
                                     self.dbs,
                                     timeout=self.timeout)
            program.ui.resultBrowser.append("*********连接串口成功*********")
        except Exception:
            program.ui.resultBrowser.append("*********端口号错误或者未填写端口号*********")
            program.ui.resultBrowser.append("*********需要重新打开程序*********")
            # self.ui.mcuBox.setEnabled(True)
            program.err = -1
        if program.ui.add_tempBox.isChecked():
            program.ui.pushButton.clicked.connect(self.thread_recv)  # 断言判断
            program.ui.pushButton.clicked.connect(self.thread_add_temp)  # appium启动配置

    # 处理串口数据，接收串口返回数据
    def read_date(self):
        check_edit = program.ui.assertTextEdit.toPlainText().split(",")
        check_dates = {}  # 断言数据
        while True:
            now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S----->")
            is_success_date = ''  # 判断是否执行成功的临时数据
            try:
                date_line = self.ser.readline().decode()
                time.sleep(0.1)
                is_success_date += date_line
                program.txt_date += str(date_line)  # 所有写入到txt文档
                program.write_txt(program.txt_date)
                for i in range(len(check_edit)):
                    # 开机:55 11 01 00 01 01 69, 关机:55 11 01 00 01 00 68
                    check_dates[check_edit[i].split(":")[0]] = check_edit[i].split(":")[1]  # 将每个输入的键值对加入到字典里
                    check_list = []
                    for j in check_dates:
                        check_list.append(j)
                    if check_dates[check_list[i]] in date_line:
                        success_date = str(now_time + check_list[i]) + "."
                        program.err_date += success_date
                        program.txt_date += success_date
                        program.ui.resultBrowser.append(success_date)
            except Exception:
                break

        """
        线程控制app
        """

    # app添加设备
    def thread_add_devices(self):
        try:
            self.add_devices_thread = threading.Thread(target=self.add_devices)
            self.add_devices_thread.start()
        except Exception as e:
            print("无法启动线程:{}".format(e))

    # app绑定温湿度计
    def thread_add_temp(self):
        try:
            self.add_temp_thread = threading.Thread(target=self.add_temp)
            self.add_temp_thread.start()
        except Exception as e:
            print("无法启动线程:{}".format(e))

    # 线程读取数据
    def thread_recv(self):
        try:
            self.recv_thread = threading.Thread(target=self.read_date)
            self.recv_thread.start()
        except Exception as e:
            print("无法启动线程:{}".format(e))