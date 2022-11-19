#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : https://blog.csdn.net/zhouzhiwengang/article/details/119735750
# @File    : https://blog.csdn.net/zhouzhiwengang/article/details/119735750
# @Description : 程序入口

from yali_Autotool.package_main.handle_main import program


class AutoMain():

    def run_func(self):
        program.add_device_func()


if __name__ == '__main__':
    AutoMain = AutoMain()
    AutoMain.run_func()
