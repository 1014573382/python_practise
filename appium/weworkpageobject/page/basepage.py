#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/12 20:32

'''BasePage：存放一些基本的方法，比如：初始化driver,find查找元素'''
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info(f"find: {locator}")
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        logging.info("click")
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        logging.info(f"sendkeys:{text}")
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

    def webdriver_wait(self, locator, timeout=10):
        logging.info(f"webdriver_wait: {locator}, timeout: {timeout}")
        return WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))

    def back(self, num=1):
        logging.info(f'back: {num}')
        for i in range(num):
            self.driver.back()



