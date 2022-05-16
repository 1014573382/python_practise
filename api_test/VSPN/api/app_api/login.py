import requests
import yaml

from VSPN.api.baseapi import BaseApi


class Login(BaseApi):

    def __init__(self):
        with open("../config/env.yaml", encoding='utf-8')as f:
            self.test_url = yaml.safe_load(f)['test_env']
            print(self.test_url)

    def send_message(self, mobile):
        req_data = {
            "method": "post",
            "url": self.test_url + "/api/common/send-sms",
            "json":{
                "mobile": mobile,
                "ip": "192.168.10.11"
            }
        }
        requests.request(**req_data).json()
        # print(re)
        # return self

    def sms_login(self, mobile):
        req_data = {
            "method": "post",
            "url": self.test_url + "/api/login/sms-code",
            "json":{
                "mobile": mobile,
                "code": "1234",
                "device_id": "941597bf-b507-42bb-aaea-d8c1b553e25"
            },
            "headers": {
                "Client-Type": "android"
            }
        }
        result = requests.request(**req_data).json()
        print(type(result))   #  <class 'dict'>
        token = result['token']
        user_id = result['user_id']
        print(user_id)
        return token, user_id
