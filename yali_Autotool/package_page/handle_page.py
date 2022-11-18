#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 定位操作
import threading

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from yali_Autotool.run import program

import time

class app_test():
    # app执行添加设备
    def add_devices(self):
        program.ui.add_deviceBox.setEnabled(False)  # 添加/删除设备灰显
        program.ui.pushButton.setEnabled(False)  # 开始测试灰显
        n = 0
        err_test_count = 0
        test_count = self.ui.countEdit.text()
        if test_count != 0 and test_count != "":
            self.ui.resultBrowser.append("===========开始测试===========")
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '11',
                # 'deviceName': "424e4d504c383098",  # 三星
                'deviceName': "d5cd8968",  # 小米10
                'appPackage': 'com.govee.home',
                'appActivity': 'com.govee.home.HomeActivity',
                'autoAcceptAlerts': 'true',  # 默认选择接受弹窗的条款
                'noReset': 'true',  # 启动app时不要清除app里原有的数据
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
            self.driver.implicitly_wait(30)
            while n < int(test_count):
                self.ui.resultBrowser.append("添加设备/删除设备自动化测试中------>第{}次".format(n + 1))
                try:
                    """添加设备"""
                    # 添加”+“
                    self.driver.find_element(By.ID, "ivDevAdd").click()
                    time.sleep(2)
                    # 输入要添加的SKU
                    self.driver.find_element(By.ID, "tv_search").click()
                    time.sleep(3)
                    self.driver.find_element(By.ID, "et_search").send_keys("H7143")
                    time.sleep(2)
                    # 点击SKU
                    self.driver.find_element(By.ID, "sku_des").click()
                    # 选择设备
                    time.sleep(8)
                    self.driver.find_elements(By.CLASS_NAME, "android.widget.RelativeLayout")[0].click()
                    time.sleep(2)
                    self.ui.resultBrowser.append("等待配对(点击设备开关按钮。)")
                    time.sleep(10)
                    # 命名设备
                    self.driver.find_element(By.ID, "done").click()
                    time.sleep(2)
                    # wifi配置
                    self.driver.find_element(By.ID, "et_pwd").clear()
                    self.driver.find_element(By.ID, "et_pwd").send_keys("20170201")
                    self.driver.find_element(By.ID, "send_wifi").click()
                    time.sleep(20)

                    """ 删除设备 """
                    # 点击设备设置按钮
                    TouchAction(self.driver).press(x=1000, y=150).release().perform()  # 通过定位坐标
                    time.sleep(2)
                    self.swipe_down()  # 下滑
                    self.driver.find_element(By.ID, "btn_delete").click()
                    time.sleep(2)
                    self.driver.find_element(By.ID, "btn_done").click()
                    time.sleep(5)
                except Exception:
                    self.ui.resultBrowser.append("找不到定位元素了..")
                    err_test_count += 1
                n += 1
                if n == test_count:
                    self.ui.resultBrowser.append("测试完成！")
                    success_count = test_count - err_test_count  # 成功次数
                    success_rate = success_count / test_count  # 成功率
                    self.ui.resultBrowser.append(
                        "测试完成！共测试{}次,成功{}次,成功率{:.2%}".format(test_count, success_count, success_rate))
                    self.ui.pushButton.setEnabled(True)  # 开始测试使能
        else:
            self.ui.resultBrowser.append("输入测试次数...")
            self.ui.pushButton.setEnabled(True)  # 开始测试使能
            self.ui.add_deviceBox.setEnabled(True)  # 添加设备使能使能


    # app执行绑定温湿度计
    def add_temp(self):
        self.ui.add_tempBox.setEnabled(False)  # 添加/删除设备灰显
        self.ui.pushButton.setEnabled(False)  # 开始按钮设备灰显
        self.ui.resultBrowser.append("\r")
        n = 0
        err_test_count = 0
        test_count = self.ui.countEdit.text()
        if test_count != 0 and test_count != "":
            self.ui.resultBrowser.append("===========开始测试app===========")
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '11',
                # 'deviceName': "424e4d504c383098",  # 三星
                'deviceName': "d5cd8968",  # 小米10
                'appPackage': 'com.govee.home',
                'appActivity': 'com.govee.home.HomeActivity',
                'autoAcceptAlerts': 'true',  # 默认选择接受弹窗的条款
                'noReset': 'true',  # 启动app时不要清除app里原有的数据
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
            self.driver.implicitly_wait(120)
            while n < int(test_count):
                self.ui.resultBrowser.append("绑定温湿度计/删除温湿度计自动化测试中------>第{}次".format(n + 1))
                try:
                    # 进入设备详情页
                    self.driver.find_element(By.ID, "com.govee.home:id/rl_item").click()
                    time.sleep(5)
                    self.swipe_down()
                    # 绑定温湿度计
                    self.driver.find_element(By.ID, 'container_top_bind').click()
                    time.sleep(3)
                    self.driver.find_element(By.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                             ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayou"
                                             "t/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.re"
                                             "cyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.w"
                                             "idget.ImageView[2]").click()
                    time.sleep(3)
                    self.driver.find_element(By.ID, "btn_ok").click()
                    time.sleep(10)
                    # 删除温湿度计
                    self.driver.find_element(By.ID, 'iv_bind_temperature_arrow').click()
                    time.sleep(3)
                    self.driver.find_element(By.ID, 'btn_delete').click()
                    time.sleep(3)
                    self.driver.find_element(By.ID, 'btn_done').click()
                    time.sleep(3)
                except Exception:
                    self.ui.resultBrowser.append("找不到定位元素了..")
                    err_test_count += 1
                n += 1
                if n == test_count:
                    self.ui.resultBrowser.append("测试完成！")
                    success_count = test_count - err_test_count  # 成功次数
                    success_rate = success_count / test_count  # 成功率
                    self.ui.resultBrowser.append(
                        "测试完成！共测试{}次,成功{}次,成功率{:.2%}".format(test_count, success_count, success_rate))
                    self.ui.pushButton.setEnabled(True)  # 添加/删除设备正常
        else:
            self.ui.resultBrowser.append("输入测试次数...")
            self.ui.pushButton.setEnabled(True)  # 开始测试使能
            self.ui.add_tempBox.setEnabled(True)  # 添加设备使能使能






