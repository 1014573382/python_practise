from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, loactor, value):
        return self._driver.find_element(loactor, value)