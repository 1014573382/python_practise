import yaml

from VSPN.sufubi.api.baseapi import BaseApi


class Login(BaseApi):
    def send_sms(self, mobile):
        """发送验证码"""
        data = {
            "method": "POST",
            "url":  self.test_env +"/api/common/send-sms",
            "json": {
                "mobile": mobile,
                "ip": "192.168.0.64"
            }
        }
        self.send(data)
        return self

    def sms_code(self, mobile):
        """验证码登录"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/login/sms-code",
            "json": {
                "mobile": mobile,
                "device_id": "F975871C96A0A79C6EC28B2CDB5AB17BD2003B76",
                "code": "1234"
            },
            "headers": {
                "Client-Type": "android"
            }
        }
        result = self.send(data)
        token = result["token"]
        with open("../data/token.yaml", 'w')as f:
            yaml.dump({"token": token}, f, encoding='utf-8', allow_unicode=True)
        # user_id = result["user_id"]
        print("token:", token)
        return token

    def status(self):
        data = {
            "method": "get",
            "url": self.test_env + "/api/user/status"
        }
        self.send(data)