from VSPN.sufubi.api.game import Game


class TestGame:
    def setup(self):
        self.game = Game()
        self.room_id = 100507

    def test_game_detail(self):
        self.game.game_detail(self.room_id)

    def test_loan(self):
        self.game.loan(self.room_id)

    def test_play_cards(self):
        """出牌，卡牌命名：色系编号｜拍卖方式编号｜星数｜序号"""
        self.game.play_cards(self.room_id, ["4141"])

    def test_offer_price(self):
        self.game.offer_price(self.room_id, 5)

    def test_giveup(self):
        self.game.giveup(self.room_id)

    def test_confirm(self):
        self.game.confirm(self.room_id)

    def test_cancel_deposit(self):
        self.game.cancel_deposit(self.room_id)
