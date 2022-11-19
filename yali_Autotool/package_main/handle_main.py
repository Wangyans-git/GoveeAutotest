#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 处理串口
import datetime
import threading
import time
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtUiTools import QUiLoader
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QApplication
from appium import webdriver
import serial


from yali_Autotool.package_page.handle_page import AppTest


class HandleMian(QWidget):
    def __init__(self):
        super().__init__()
        # self.err = 0
        # self.dbs = dbs
        # self.timeout = timeout
        # self.err_date = ''  # 做是否有错误判断的数据
        # self.txt_date = ''  # 写入TXT的数据
        # self.err_count = 0  # 记录错误次数

        self.ui = QUiLoader().load('config/Skutest.ui')
        self.ui.setMinimumSize(600, 700)
        self.ui.setMaximumSize(600, 700)
        # self.ui.main_funBox.clicked.connect(self.main_func)  # 复选助主功能功能

        # self.ui.add_tempBox.clicked.connect(self.add_temp_func)  # 复选绑定温湿度计功能
        # self.ui.quitButton.clicked.connect(self.quit_app)  # 退出

        self.ui.skuBox.addItems(['H7130', 'H7131', 'H7143'])  # 下拉选择

        # 默认设置
        self.ui.main_funBox.setChecked(True)  # 默认设置为主功能

    # 复选主功能
    # def main_func(self, dbs, timeout):
    #     try:
    #         com = self.ui.serialEdit.text()  # 串口
    #         self.ser = serial.Serial(com,
    #                                  # self.ser = serial.Serial('com8',
    #                                  dbs,
    #                                  timeout=timeout)
    #         self.ui.resultBrowser.append("*********连接串口成功*********")
    #         self.ui.mucButton.setEnabled(False)
    #         self.ui.appButton.setEnabled(False)
    #     except Exception:
    #         self.ui.resultBrowser.append("*********端口号错误或者未填写端口号*********")
    #         self.ui.resultBrowser.append("*********需要重新打开程序*********")
    #         # self.ui.mcuBox.setEnabled(True)
    #         self.err = -1
    #     if self.ui.main_funBox.isChecked():
    #         self.ui.pushButton.clicked.connect(self.thread_recv)

    # 复选app添加设备
    def add_device_func(self, dbs, timeout):
        self.dbs = dbs
        self.timeout = timeout
        try:
            com = self.ui.serialEdit.text()  # 串口
            self.ser = serial.Serial(com,
                                     # self.ser = serial.Serial('com8',
                                     self.dbs,
                                     timeout=self.timeout)
            self.ui.resultBrowser.append("*********连接串口成功*********")
        except Exception:
            self.ui.resultBrowser.append("*********端口号错误或者未填写端口号*********")
            self.ui.resultBrowser.append("*********需要重新打开程序*********")
            # self.ui.mcuBox.setEnabled(True)
            self.err = -1
        if self.ui.add_deviceBox.isChecked():
            # self.ui.pushButton.clicked.connect(self.thread_recv)  # 断言判断
            self.ui.pushButton.clicked.connect(self.thread_add_devices)  # appium启动配置

    # 复选app绑定温湿度计
    def add_temp_func(self, dbs, timeout):
        self.dbs = dbs
        self.timeout = timeout
        try:
            com = self.ui.serialEdit.text()  # 串口
            self.ser = serial.Serial(com,
                                     # self.ser = serial.Serial('com8',
                                     self.dbs,
                                     timeout=self.timeout)
            self.ui.resultBrowser.append("*********连接串口成功*********")
        except Exception:
            self.ui.resultBrowser.append("*********端口号错误或者未填写端口号*********")
            self.ui.resultBrowser.append("*********需要重新打开程序*********")
            # self.ui.mcuBox.setEnabled(True)
            self.err = -1
        if self.ui.add_tempBox.isChecked():
            self.ui.pushButton.clicked.connect(self.thread_recv)  # 断言判断
            self.ui.pushButton.clicked.connect(self.thread_add_temp)  # appium启动配置

    # 处理串口数据，接收串口返回数据
    def read_date(self):
        check_edit = self.ui.assertTextEdit.toPlainText().split(",")
        check_dates = {}  # 断言数据
        while True:
            now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S----->")
            is_success_date = ''  # 判断是否执行成功的临时数据
            try:
                date_line = self.ser.readline().decode()
                time.sleep(0.1)
                is_success_date += date_line
                self.txt_date += str(date_line)  # 所有写入到txt文档
                self.write_txt(self.txt_date)
                for i in range(len(check_edit)):
                    # 开机:55 11 01 00 01 01 69, 关机:55 11 01 00 01 00 68
                    check_dates[check_edit[i].split(":")[0]] = check_edit[i].split(":")[1]  # 将每个输入的键值对加入到字典里
                    check_list = []
                    for j in check_dates:
                        check_list.append(j)
                    if check_dates[check_list[i]] in date_line:
                        success_date = str(now_time + check_list[i]) + "."
                        self.err_date += success_date
                        self.txt_date += success_date
                        self.ui.resultBrowser.append(success_date)
            except Exception:
                break

        """
        线程控制app
        """

    # app添加设备
    def thread_add_devices(self):
        try:
            self.add_devices_thread = threading.Thread(target=AppTest.add_devices)
            self.add_devices_thread.start()
        except Exception as e:
            print("无法启动线程:{}".format(e))

    # app绑定温湿度计
    def thread_add_temp(self):
        try:
            self.add_temp_thread = threading.Thread(target=add_temp)
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


app = QApplication([])
app.setWindowIcon(QIcon("config/touxiang.ico"))
program = HandleMian()
program.ui.show()
app.exec_()
