from pages.app import App


class TestMain:

    def setup(self):
        self.app = App()

    def test_main(self):
        # self.app.start().main().click_skip_advertise().goto_search()
        self.app.start().main().goto_search()

    def test_search(self):
        self.app.start().main().goto_stock().goto_search().search("阿里巴巴-SW")