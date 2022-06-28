import pytest

from VSPN.bigdetective.api.app_api.login import Login


class TestLogin():

    @pytest.mark.parametrize('mobile', [('13838380002')])
    def test_login(self, mobile):
        Login().send_message(mobile)
        Login().sms_login(mobile)