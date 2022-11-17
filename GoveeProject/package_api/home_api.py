#!C:\wys\AutoTestProjects
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : 
# @File    : 
# @Description : 小家电API
import json
import time

import requests


class ApiTest(object):
    def __init__(self):
        self.headers = {"Govee-API-Key": "b5c21652-6e22-4ebf-99dd-531cbd52db5b", "Content-Type": "application/json"}
        self.response = requests.get(
            url='https://developer-api.govee.com/v1/appliance/devices?Govee-API-Key=a84176b2-5cea'
                '-4adb-86d8-f17a672d4a63&Content-Type=application/json', headers=self.headers)
        self.v = 0

    def all_device(self):
        date = json.loads(self.response.text)
        str_data = json.dumps(date)
        sku_count = str_data.count('model')
        for i in range(sku_count):
            self.device = date['data']['devices'][i]['device']  # 设备id
            self.model = date['data']['devices'][i]['model']  # sku
            self.mode_all = date['data']['devices'][i]['properties']['mode']['options']  # 模式
            try:
                self.gear_all = date['data']['devices'][i]['properties']['gear']['options']  # 档位
            except Exception:
                pass
            api.all_api()

    def all_api(self):
        # mode
        print("开始测试{}".format(self.model))
        time.sleep(10)
        for i in self.mode_all:
            json = {
                "device": self.device,
                "model": self.model,
                "cmd": {
                    "name": "mode",
                    "value": i['value']
                }
            }
            response = requests.put(url='https://developer-api.govee.com/v1/appliance/devices/control',
                                    headers=self.headers,
                                    json=json)
            if 'Success' in response.text:
                print(str(i['name']) + "---->成功")
            else:
                print(str(i['name']) + "---->失败")
            time.sleep(5)

        # gear
        try:
            for i in self.gear_all:
                for self.v in range(len(i['value'])):
                    self.v += 1  # value值
                    json = {
                        "device": self.device,
                        "model": self.model,
                        "cmd": {
                            "name": "gear",
                            "value": self.v
                        }
                    }
                    response = requests.put(url='https://developer-api.govee.com/v1/appliance/devices/control',
                                            headers=self.headers,
                                            json=json)
                    if 'Success' in response.text:
                        print(str(i['name'] + str(self.v)) + "---->成功")
                    else:
                        print(str(i['name'] + str(self.v)) + "---->失败")
                    time.sleep(5)
        except Exception:
            pass


if __name__ == '__main__':
    api = ApiTest()
    api.all_device()
