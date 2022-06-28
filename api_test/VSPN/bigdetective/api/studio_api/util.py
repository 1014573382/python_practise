import requests


class Util():
    _username = 'test2'
    _password = 'e10adc3949ba59abbe56e057f20f883e'

    def get_token(self):
        requests_data = {
            "user_name": self._username,
            "password": self._password
        }

        res = requests.post("http://42.192.15.124:50055/mgr/user/login", json=requests_data)
        # print(res)
        # print(res.json()['token'])
        global token
        token =  res.json()['token']
        return token