from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_option = Options()
            chrome_option.debugger_address = "127.0.0.1:7333"
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(6)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
        # else:
        #     self._driver.get("https://work.weixin.qq.com/")


