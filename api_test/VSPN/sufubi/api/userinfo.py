from VSPN.sufubi.api.baseapi import BaseApi


class UserInfo(BaseApi):
    def get_user_info(self, user_id):
        data = {
            "method": "get",
            "url": self.test_env + "/api/user/info",
            "params": {
               "user_id": user_id
            },
            "headers": self.header
        }
        return self.send(data).json()

    def set_user_info(self, nickname, gender, avatar=None):
        """更新用户信息, 返回 body 为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/user/set-user-info",
            "json": {
               "nickname": nickname,
                "gender": gender,
                "avatar": avatar
            },
            "headers": self.header
        }
        return self.send(data)

    def get_user_status(self):
        """获取用户状态信息, 返回用户所在的房间id,不在房间内id为0"""
        data = {
            "method": "get",
            "url": self.test_env + "/api/user/status",
            "headers": self.header
        }
        result = self.send(data).json()
        if result["room_id"] != "":
            print("用户所在的房间号:", result["room_id"])
        else:
            print("用户不在房间内")
        return result