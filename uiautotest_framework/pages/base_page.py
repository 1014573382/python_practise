from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver

    _blacklist = [
        (By.ID, "tv_skip"), #首页的广告弹框
        (By.ID, "iv_action_back")  #跳转到登录页后点击叉叉关掉

    ]
    _max_err_num = 3
    _error_num = 0
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value = None):
        try:
            # 如果元素找到，就清空 error 计数
            if value is None:
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            self._error_num = 0
            return element
        except Exception as e:
            # 如果元素没找到，就进行黑名单处理
            if self._error_num > self._max_err_num:
                # 如果error 次数大于指定数，就重置 error 次数并抛出异常
                self._error_num = 0
                raise e
            self._error_num += 1
            for ele in self._blacklist:
                # 对黑名单中的元素进行点击
                eles = self.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(locator, value)
            raise ValueError("元素不在黑名单中")



    def finds(self, locator, value = None):
        if value is None:
            return self._driver.find_elements(*locator)
        else:
            return self._driver.find_elements(locator, value)

    def set_implicitly_wait(self, second):
        return self._driver.implicitly_wait(second)
