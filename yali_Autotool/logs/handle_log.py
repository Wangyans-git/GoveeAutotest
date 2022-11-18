#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 处理日志
import datetime

from yali_Autotool.run import program


class handle_date():
    # 判断错误数据
    def date_result(self, n):
        date = program.err_date.split('.')
        if len(date) - 1 == len(n):  # 因为split分隔后会多一段数据，所以-1
            program.err_date = ''
        elif len(date) == 1:
            pass
        else:
            err_ = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S前的一次执行中有错误！！！"))
            program.txt_date += err_
            program.write_txt(program.txt_date)
            print(err_)
            program.err_date = ''
            program.err_count += 1
        return program.err_count

    # 数据写入txt文档
    @staticmethod
    def write_txt(t):
        result = str(t)
        try:
            with open('../logs/log.txt', 'w') as file_handle:
                file_handle.write(result)
        except Exception as e:
            print("文件读写出错：", e)
