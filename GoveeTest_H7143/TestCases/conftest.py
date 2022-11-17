#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 实现的是setup、teardown功能。使用pytest框架提供的能力fixture的功能。


import pytest, time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="class")
def access_web():
    # 前置：打开浏览器
    # 修改页面加载策略
    desired_capabilities = DesiredCapabilities.CHROME
    # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    desired_capabilities["pageLoadStrategy"] = "none"
    # 实例化对象
    driver = webdriver.Chrome()
    # 访问网址
    driver.get("www.baidu.com")
    # 窗口最大化
    driver.maximize_window()
    # 等待
    time.sleep(4)
    # 返回对象
    yield driver
    # 后置：关闭浏览器
    driver.quit()


@pytest.fixture
def refresh(access_web):
    yield access_web
    # 刷新页面
    access_web.refresh()
    # 操作1
    # access_web.find_element(*LP.s).click()
    # 操作2
    # access_web.find_element(*LP.che).click()
    time.sleep(1)


def pytest_configure(config):
    config.addinivalue_line("markers", 'smoke')
    config.addinivalue_line("markers", 'P0')
    config.addinivalue_line("markers", 'P1')

