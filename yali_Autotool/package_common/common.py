#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    :
# @Author  : https://blog.csdn.net/zhouzhiwengang/article/details/119735750
# @File    : https://blog.csdn.net/zhouzhiwengang/article/details/119735750
# @Description : 页面操作


# 获取手机屏幕宽度
def get_size(self):
    # 获取窗口尺寸
    size = self.driver.get_window_size()
    x = size['width']
    y = size['height']
    return x, y


def swipe_down(self):
    # 向下滑动
    size = self.get_size()
    x1 = int(size[0] * 0.5)
    y1 = int(size[1] * 0.9)
    y2 = int(size[1] * 0.1)
    self.driver.swipe(x1, y1, x1, y2, 500)


def swipe_up(self):
    # 向上滑动
    size = self.get_size()
    x1 = int(size[0] * 0.5)
    y1 = int(size[1] * 0.1)
    y2 = int(size[1] * 0.9)
    self.driver.swipe(x1, y1, x1, y2, 500)