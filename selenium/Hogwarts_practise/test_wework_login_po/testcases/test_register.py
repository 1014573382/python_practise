from Hogwarts_practise.test_wework_login_po.pages.index import IndexPage


class TestRegister():
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        self.index.goto_register().register()