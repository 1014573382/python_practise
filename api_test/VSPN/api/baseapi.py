import json
import requests


class BaseApi:
    """
    存放公共的方法
    """
    params = {}

    def send(self, data):
        # get和post方法实际上是调用requests.request(),传入的第一个参数请求方法method：get或post等
        # 下面做一个封装，data参数作为一个整体数据，让用户传入是什么方法和参数
        json_data = json.dumps(data)
        for key, value in self.params.items():
            json_data = json_data.replace('${' + key + '}', value)
            print("json_data: ", json_data)
            data = json.loads(json_data)
            return requests.request(**data).json()