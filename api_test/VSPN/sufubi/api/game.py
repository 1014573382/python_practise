from VSPN.sufubi.api.baseapi import BaseApi


class Game(BaseApi):
    def game_detail(self, room_id):
        """游戏详情"""
        data = {
            "method": "get",
            "url": self.test_env + "/api/game/sothebys/detail",
            "params": {
                "room_id": room_id
            },
            "headers": self.header
        }
        return self.send(data).json()

    def loan(self, room_id, funds=0):
        """贷款，返回body为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/game/sothebys/loan",
            "json": {
                "room_id": room_id,
                "funds": funds
            },
            "headers": self.header
        }
        return self.send(data)

    def play_cards(self, room_id, brand_keys, mode=1, price=None):
        """出牌，返回body为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/game/sothebys/loan",
            "json": {
                "room_id": room_id,
                "mode": mode,
                "brand_keys": brand_keys,
                "price": price
            },
            "headers": self.header
        }
        return self.send(data)

    def offer_price(self, room_id, price):
        """出价，返回body为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/game/sothebys/offer-price",
            "json": {
                "room_id": room_id,
                "price": price
            },
            "headers": self.header
        }
        return self.send(data)

    def giveup(self, room_id):
        """放弃（过），返回body为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/game/sothebys/pass",
            "json": {
                "room_id": room_id
            },
            "headers": self.header
        }
        return self.send(data)

    def confirm(self, room_id):
        """确认(结算、贷款、结束)，返回body为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/game/sothebys/confirm",
            "json": {
                "room_id": room_id
            },
            "headers": self.header
        }
        return self.send(data)

    def cancel_deposit(self, room_id):
        """取消托管，返回body为空"""
        data = {
            "method": "post",
            "url": self.test_env + "/api/game/sothebys/un-deposit",
            "json": {
                "room_id": room_id
            },
            "headers": self.header
        }
        return self.send(data)