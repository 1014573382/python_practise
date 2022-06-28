import yaml

from VSPN.sufubi.api.baseapi import BaseApi


class Room(BaseApi):
    def create(self, players=6, game_mode=1, game_loan=1):
        """创建房间，game_mode：1为拍卖艺术，2为决战苏富比，game_loan：1贷款，0不贷"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/room/create",
            "json": {
                "players": players,
                "game_mode": game_mode,
                "game_loan": game_loan,
                "name": "上号，开一把",
                "password": ""
            },
            "headers": self.header
        }
        result = self.send(data).json()
        self._room_id = result["room_id"]
        # return self
        return result

    def join(self, room_id=None):
        """加入房间"""
        if room_id is None:
            room_id = self._room_id
        data = {
            "method": "post",
            "url": self.test_env + "/api/room/join",
            "json": {
                "room_id": room_id,
	            "password": ""
            },
            "headers": self.header
        }
        self.send(data)
        return self

    def detail(self, room_id):
        """房间详情"""
        data = {
            "method": "get",
            "url": self.test_env + "/api/room/detail",
            "params": {
                "room_id": room_id,
                "seq": 0
            },
            "headers": self.header
        }
        result = self.send(data).json()
        print("获取房间详情结果：", result)
        return result

    def exit(self, room_id=None):
        """退出房间，返回结果为空"""
        if room_id is None:
            room_id = self._room_id
        data = {
            "method": "post",
            "url": self.test_env + "/api/room/exit",
            "json": {
                "room_id": room_id,
                "is_collapse": False
            },
            "headers": self.header
        }
        return self.send(data)

    def room_list(self):
        """获取房间列表"""
        data = {
            "method": "get",
            "url": self.test_env + "/api/room/list",
            "params": {
                "page": 1,
                "limit": 10,
                "game_mode": 1
            },
            "headers": self.header
        }
        return self.send(data).json()

    def quick_join(self, game_moe=1):
        """快速加入房间"""
        data ={
            "method": "post",
            "url": self.test_env + "/api/room/quick-join",
            "json": {
                "game_moe": game_moe
            },
            "headers": self.header
        }
        return self.send(data).json()

    def ready(self, room_id=None):
        """房间内准备，返回body为空"""
        if room_id is None:
            room_id = self._room_id
        data = {
            "method": "post",
            "url": self.test_env + "/api/room/ready",
            "json": {
                "room_id": room_id
            },
            "headers": self.header
        }
        return self.send(data)

    def cancel_ready(self, room_id=None):
        """取消准备"""
        if room_id is None:
            room_id = self._room_id
        data = {
            "method": "post",
            "url": self.test_env + "/api/room/unready",
            "json": {
                "room_id": room_id
            },
            "headers": self.header
        }
        return self.send(data)

    def room_search(self, room_id):
        """搜索房间"""
        # if room_id is None:
        #     room_id = self._room_id
        data = {
            "method": "get",
            "url": self.test_env + "/api/room/search",
            "params": {
                "room_id": room_id
            },
            "headers": self.header
        }
        return self.send(data).json()

    def kick_people(self, room_id, user_id):
        """踢人出房间"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/room/kick",
            "json": {
                "room_id": room_id,
                "user_id": user_id
            },
            "headers": self.header
        }
        return self.send(data)

    def update_room(self, room_id,  players, game_loan=1, password=None, name=None):
        """更新房间信息，返回body为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/room/update",
            "json": {
                "room_id": room_id,
                "name": name,
                "players": players,
                "password": password,
                "game_loan": game_loan
            },
            "headers": self.header
        }
        return self.send(data)


