#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2022/06/03 19:11
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        chrome_option = Options()
        chrome_option.debugger_address = "127.0.0.1:9888"
        if driver == None:
            self._driver = webdriver.Chrome(options=chrome_option)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def find_and_send(self, by, locator, value):
        return self._driver.find_element(by, locator).send_keys(value)

    def wait_for_click(self, locator):
        """等待元素可被点击"""
        return WebDriverWait(self._driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self, condition):
        """满足 condition 的显示等待"""
        return WebDriverWait(self._driver, 10).until(condition)