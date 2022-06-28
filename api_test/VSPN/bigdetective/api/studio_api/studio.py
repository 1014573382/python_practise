import yaml

from VSPN.bigdetective.api.baseapi import BaseApi
from VSPN.bigdetective.api.studio_api.util import Util


class Studio(BaseApi):

    def __init__(self):
        self.token = Util().get_token()
        with open("./config/env.yaml", encoding='utf-8') as f:
            self.test_url = yaml.safe_load(f)
        with open("./config/studio.yaml", encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def add_studio(self, studio_name, mobile, idcard):
        # req_data = {
        #     "studio_name": "郭郭的第二工作室",
        #     "contact": "郭郭gita",
        #     "mobile": "15222181123",
        #     "idcard": "622428199608053511"
        # }
        # res = requests.post(self.test_url["test_env"] + '/mgr/studio/add', json=req_data)
        self.params["test_url"] = self.test_url
        self.params["studio_name"] = studio_name
        self.params["mobile"] = mobile
        self.params["idcard"] = idcard
        return self.send(self.data["add"])
