import pytest

from pages.app import App


class TestMain:

    def setup(self):
        self.app = App()

    def test_main(self):
        # self.app.start().main().click_skip_advertise().goto_search()
        self.app.start().main().goto_search()

    @pytest.mark.parametrize("stock_name", ("阿里巴巴-SW", "京东"))
    def test_search(self, stock_name):
        self.app.start().main().goto_stock().goto_search().search(stock_name)
