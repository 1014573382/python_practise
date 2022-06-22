import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.driver.find_element(*locator).click()

    def find_and_sendkeys(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

    def find_by_scroll(self, text):
        '''滚动查找元素'''
        logging.info("find_by_scroll")
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).'
                                        'instance(0)).'
                                        'scrollIntoView('
                                        'new UiSelector().'
                                        f'text("{text}").instance(0));')

    def back(self, num=1):
        logging.info(f"back: {num}")
        for i in range(num):
            self.driver.back()

    def webdriver_wait(self, locator, timeout=10):
        logging.info(f'webdriver_wait: {locator}, timeout:{timeout}')
        return WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))