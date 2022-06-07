from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Hogwarts_practise.test_wework_login_po.pages.base_page import BasePage
from Hogwarts_practise.test_wework_login_po.pages.register_page import RegisterPage


class LoginPage(BasePage):
    """登录页面"""

    def scan_wechat_login(self):
        """
        扫描二维码登录
        :return:
        """
        pass

    def goto_register(self):
        """点击企业注册，进入到注册页面"""
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self._driver)
