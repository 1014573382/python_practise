import json

import requests
import yaml


class BaseApi:
    params = {}

    def __init__(self):
        with open("../config/env.yaml", encoding='utf-8')as f:
            self.test_env = yaml.safe_load(f)["test_env"]

        with open("../data/token.yaml", encoding='utf-8')as f:
            self.token = yaml.safe_load(f)["token"]

        self.header = {
            "authorization": self.token,
            "Client-Type": "android"
        }


    # get和post方法实际上是调用requests.request(),传入的第一个参数请求方法method：get或post等
    # 下面做一个封装，data参数作为一个整体数据，让用户传入是什么方法和参数
    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace('${' + key + '}', value)
            print(raw_data)
        data = json.loads(raw_data)
        return requests.request(**data)