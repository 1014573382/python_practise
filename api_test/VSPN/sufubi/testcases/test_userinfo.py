import pytest

from VSPN.sufubi.api.userinfo import UserInfo


class TestUserInfo:
    def setup(self):
        self.userinfo = UserInfo()

    @pytest.mark.parametrize("user_id", (10122465,10122434))
    def test_get_user_info(self, user_id):
        re = self.userinfo.get_user_info(user_id)
        assert re["user_id"] == user_id

    @pytest.mark.parametrize("nickname, gender, avatar",
                             [("郭郭_auto1", 1, "https://img.wxcha.com/m00/db/aa/0cceccc0647267bb4ee24c1ea08eaac5.jpg"),
                              ("郭郭_auto", 2, "")])
    def test_set_user_info(self, nickname, gender, avatar):
        self.userinfo.set_user_info(nickname, gender, avatar)
        self.userinfo.get_user_info(10122465)

    def test_get_user_status(self):
        re = self.userinfo.get_user_status()


