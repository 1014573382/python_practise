import pytest

from VSPN.sufubi.api.rank import Rank


class TestRank:
    @pytest.mark.parametrize("types, date", [(1, ""),(2, ""), (3, ""), (4, 20220628), (4, 202225)])
    def test_rank(self, types, date):
        """排行榜，type: 1 总榜 2 日榜 3 周榜 4 历史榜单（date字段需要赋值），
        历史日榜（20220611-年月日）格式，历史周榜（202212-年周）格式"""
        Rank().rank(types, date)