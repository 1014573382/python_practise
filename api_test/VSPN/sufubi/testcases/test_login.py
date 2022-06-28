import pytest
import yaml

from VSPN.sufubi.api.login import Login


class TestLogin:

    @pytest.mark.parametrize("mobile", [("13900001111")])
    def test_login(self, mobile):
        login = Login()
        login.send_sms(mobile).sms_code(mobile)


    def test_env(self):
        with open("../config/env.yaml", encoding='utf-8')as f:
            test_env = yaml.safe_load(f)["test_env"]
            print(test_env)