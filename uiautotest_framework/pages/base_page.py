import json

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.handle_blacklist import handle_blacklist


class BasePage:
    # _driver: WebDriver

    _blacklist = [
        (By.ID, "tv_skip"), #首页的广告弹框
        (By.ID, "iv_action_back")  #跳转到登录页后点击叉叉关掉

    ]
    _max_err_num = 3
    _error_num = 0
    params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver



    @handle_blacklist
    def find(self, loactor, value=None):
        if value is None:
            result = self._driver.find_element(*loactor)
        else:
            result = self._driver.find_element(loactor, value)
        return result

    def finds(self, locator, value=None):
        if value is None:
            return self._driver.find_elements(*locator)
        else:
            return self._driver.find_elements(locator, value)

    def set_implicitly_wait(self, second):
        return self._driver.implicitly_wait(second)

    def steps(self, path, name):
        """对yaml文件中定义的页面实现步骤进行解析，然后直接在实现页面时调用step方法并传入yaml路径即可"""
        with open(path, encoding= 'utf-8')as f:
            steps = yaml.safe_load(f)[name]
        # 将python数据类型转化为Json数据类型
        json_data = json.dumps(steps)
        # 把yaml中的变量替换为 params = {} 传入的value
        for key, value in self.params.items():
            json_data = json_data.replace('${' + key + '}', value)
        steps = json.loads(json_data)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])

    def back(self, num=1):
        for i in range(num):
            self._driver.back()

    def screenshot(self, path):
        return self._driver.save_screenshot(path)

    # def find(self, locator, value = None):
    #     try:
    #         # 如果元素找到，就清空 error 计数
    #         if value is None:
    #             element = self._driver.find_element(*locator)
    #         else:
    #             element = self._driver.find_element(locator, value)
    #         self._error_num = 0
    #         return element
    #     except Exception as e:
    #         # 如果元素没找到，就进行黑名单处理
    #         if self._error_num > self._max_err_num:
    #             # 如果error 次数大于指定数，就重置 error 次数并抛出异常
    #             self._error_num = 0
    #             raise e
    #         self._error_num += 1
    #         for ele in self._blacklist:
    #             # 对黑名单中的元素进行点击
    #             eles = self.finds(ele)
    #             if len(eles) > 0:
    #                 eles[0].click()
    #                 return self.find(locator, value)
    #         raise ValueError("元素不在黑名单中")


