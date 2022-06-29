from VSPN.sufubi.api.baseapi import BaseApi


class Rank(BaseApi):
    def rank(self, types, date=None):
        """排行榜，type: 1 总榜 2 日榜 3 周榜 4 历史榜单（date字段需要赋值）"""
        data = {
            "method": "get",
            "url": self.test_env + "/api/rank/user",
            "params": {
                "types": types,
                "date": date
            },
            "headers": self.header
        }
        return self.send(data).json()