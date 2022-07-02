import allure
import pytest

from pages.app import App

@allure.feature("测试雪球")
class TestMain:

    def setup(self):
        self.app = App()

    @pytest.mark.skip
    def test_main(self):
        # self.app.start().main().click_skip_advertise().goto_search()
        self.app.start().main().click_skip_advertise().goto_search()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("测试搜索")
    @allure.title("test search")
    @pytest.mark.parametrize("stock_name", [("阿里巴巴-SW"),("美团-W")])
    def test_search(self, stock_name):
        # self.app.start().main().click_skip_advertise().goto_stock().goto_search().search(stock_name)
        self.app.start().main().goto_stock().goto_search().search(stock_name)
