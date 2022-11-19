#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : https://blog.csdn.net/zhouzhiwengang/article/details/119735750
# @File    : https://blog.csdn.net/zhouzhiwengang/article/details/119735750
# @Description : 主程序111
import threading

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtUiTools import QUiLoader

import sys


class Auto_main(QWidget):
    def __init__(self):
        super().__init__()
        # self.err = 0
        # self.dbs = dbs
        # self.timeout = timeout
        # self.err_date = ''  # 做是否有错误判断的数据
        # self.txt_date = ''  # 写入TXT的数据
        # self.err_count = 0  # 记录错误次数

        self.ui = QUiLoader().load('./config/Skutest.ui')
        self.ui.setMinimumSize(600, 700)
        self.ui.setMaximumSize(600, 700)
        self.ui.main_funBox.clicked.connect(self.main_func)  # 复选助主功能功能
        self.ui.add_deviceBox.clicked.connect(self.add_device_func)  # 复选添加设备功能
        self.ui.add_tempBox.clicked.connect(self.add_temp_func)  # 复选绑定温湿度计功能
        self.ui.quitButton.clicked.connect(self.quit_app)  # 退出

        self.ui.skuBox.addItems(['H7130', 'H7131', 'H7143'])  # 下拉选择

        # 默认设置
        self.ui.main_funBox.setChecked(True)  # 默认设置为主功能

    # 退出
    @staticmethod
    def quit_app():
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    program = Auto_main()
    app.setWindowIcon(QIcon("../config/touxiang.ico"))
    program.ui.show()
    app.exec_()
