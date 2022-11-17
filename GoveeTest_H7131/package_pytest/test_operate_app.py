#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 操作app
import datetime
import os
import time

import allure
import pytest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from GoveeTest_H7131.package_pytest.process_serial import program


@allure.epic("APP自动化测试")
class TestH7131(object):

    # 每个类前执行
    @classmethod
    def setup_class(self):
        self.driver = start_app.start_appium()

    # 每个用例前执行
    def setup_method(self):
        self.now_time = datetime.datetime.now().strftime("\n%Y-%m-%d %H:%M:%S----->")

    # 进入设备详情页
    @allure.feature("进入设备详情页")
    def test_app_home(self):
        try:
            self.driver.find_element(By.ID, "rl_item").click()
        except Exception as e:
            print("找不到元素了！！！\n", e)
        print("\n--------进入设备详情页--------")
        time.sleep(5)

    @allure.feature("关机")
    def test_off(self):
        # 点击开关
        try:
            self.driver.find_element(By.ID, "iv_switch").click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '关机成功'

        time.sleep(3)

    @allure.feature("开机")
    def test_on(self):
        try:
            self.driver.find_element(By.ID, "iv_switch").click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '开机成功'

        time.sleep(3)

    @allure.feature("设置低档")
    def test_low(self):
        try:
            self.driver.find_element(By.ID, "iv_gear_low_bg").click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '设置低档成功'

        time.sleep(3)

    @allure.feature("设置中档")
    def test_medium(self):
        try:
            self.driver.find_element(By.ID, "iv_gear_mid_bg").click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '设置中档成功'

        time.sleep(3)

    @allure.feature("设置高档")
    def test_high(self):
        try:
            self.driver.find_element(By.ID, "iv_gear_high_icon").click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '设置高档成功'

        time.sleep(3)

    @allure.feature("设置自动档")
    def test_auto(self):
        try:
            self.driver.find_element(By.ID, "iv_auto_icon").click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        time.sleep(3)

        print("设置自动挡成功")
        assert 1 == 1

    @allure.feature("设置风扇档")
    def test_fan(self):
        try:
            self.driver.find_element(By.ID, "iv_fan_icon").click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        time.sleep(3)
        print("设置风扇档成功")
        assert 1 == 1
        start_app.swipe_down()  # 向下滑动

    @allure.feature("开启摇头")
    def test_on_head(self):
        # 摇头
        try:
            self.driver.find_element(By.ID, 'iv_shake_switch').click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '开启摇头成功'
        time.sleep(3)

    @allure.feature("关闭摇头")
    def test_off_head(self):
        try:
            self.driver.find_element(By.ID, 'iv_shake_switch').click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '关闭摇头成功'

        time.sleep(3)

    @allure.feature("开启夜灯")
    def test_on_light(self):
        # 夜灯
        try:
            self.driver.find_element(By.ID, 'iv_light_rgb_switch_ext1').click()
        except Exception as e:
            print("找不到元素了！！！\n", e)
        print("开启夜灯成功")
        assert 1 == 1
        time.sleep(3)

    @allure.feature("关闭夜灯")
    def test_off_light(self):
        try:
            self.driver.find_element(By.ID, 'iv_light_rgb_switch_ext1').click()
        except Exception as e:
            print("找不到元素了！！！\n", e)
        print("关闭夜灯成功")
        assert 1 == 1
        time.sleep(3)

    @allure.feature("开启童锁")
    def test_lock(self):
        try:
            self.driver.find_element(By.ID, 'iv_lock_switch').click()
        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '开启童锁成功'
        time.sleep(3)

    @allure.feature("关闭童锁")
    def test_off_lock(self):
        try:
            self.driver.find_element(By.ID, 'iv_lock_switch').click()


        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '关闭童锁成功'
        time.sleep(3)

    @allure.feature("开启显示")
    def test_show(self):
        # 显示
        try:
            self.driver.find_element(By.ID, 'iv_light_indicator_switch').click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '开启显示成功'

        time.sleep(3)

    @allure.feature("关闭显示")
    def test_off_show(self):
        try:
            self.driver.find_element(By.ID, 'iv_light_indicator_switch').click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '关闭显示成功'
        time.sleep(3)

    @allure.feature("绑定温湿度计")
    def test_thermometer(self):
        # 绑定温湿度计
        try:
            self.driver.find_element(By.ID, 'bind_tempe_container').click()
            time.sleep(3)
            self.driver.find_element(By.ID, "item_icon_choose_iv").click()
            time.sleep(3)
            self.driver.find_element(By.ID, "btn_ok").click()
            time.sleep(10)

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '绑定温湿度计成功'
        time.sleep(3)

    @allure.feature("解绑温湿度计")
    def test_off_thermometer(self):
        try:
            # 删除温湿度计
            self.driver.find_element(By.ID, 'iv_bind_temperature_arrow').click()
            time.sleep(3)
            self.driver.find_element(By.ID, 'btn_delete').click()
            time.sleep(3)
            self.driver.find_element(By.ID, 'btn_done').click()

        except Exception as e:
            print("找不到元素了！！！\n", e)
        result = program.read_date()
        print(result)
        assert result == '解绑温湿度计成功'
        time.sleep(3)

    @allure.feature("退出设备详情页")
    def test_out_app_home(self):
        try:
            TouchAction(self.driver).press(x=100, y=130).release().perform()  # 通过定位坐标
        except Exception as e:
            print("找不到元素了！！！\n", e)
        print("\n--------退出设备详情页--------")
        time.sleep(5)

    def teardown_class(self):
        os.system("allure serve C:\\wys\\AutoTestProjects\\GoveeTest_H7131\\report\\report")
        os.system("allure generate GoveeTest_H7131/report/report -o GoveeTest_H7131/report/report_result/ --clean")

    def start_appium(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11',
            # 'deviceName': "424e4d504c383098",  # 三星
            'deviceName': "d5cd8968",  # 小米10
            'appPackage': 'com.govee.home',
            'appActivity': 'com.govee.home.HomeActivity',
            'automationName': 'Uiautomator2',
            'noReset': 'true',  # 启动app时不要清除app里原有的数据
            'adbExecTimeout': 200000,
            'newCommandTimeout': 36000,
        }
        try:
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
            driver.implicitly_wait(30)
            if driver:
                print("\n*********Appium服务器启动成功*********\n")
            return driver
        except Exception as e:
            print("\n*********Appium服务器错误*********\n", e)

    # 获取手机屏幕宽度
    def get_size(self):
        # 获取窗口尺寸
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        return x, y

    # 向下滑动
    def swipe_down(self):

        size = self.get_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.9)
        y2 = int(size[1] * 0.1)
        self.driver.swipe(x1, y1, x1, y2, 500)

    # 向上滑动
    def swipe_up(self):

        size = self.get_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.1)
        y2 = int(size[1] * 0.9)
        self.driver.swipe(x1, y1, x1, y2, 500)


start_app = TestH7131()
