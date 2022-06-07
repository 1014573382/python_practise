from selenium.webdriver.common.by import By

from Hogwarts_practise.test_wework_login_po.pages.base_page import BasePage
from Hogwarts_practise.test_wework_login_po.pages.login_page import LoginPage
from Hogwarts_practise.test_wework_login_po.pages.register_page import RegisterPage


class IndexPage(BasePage):
    """
    企业微信首页面
    """
    _base_url = "https://work.weixin.qq.com/"
    def goto_register(self):
        """点击立即注册，进入到注册的PO"""
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self._driver)

    def goto_login(self):
        """点击企业登录，进入登录页面"""
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn')
        return LoginPage(self._driver)

    def goto_download(self):
        pass