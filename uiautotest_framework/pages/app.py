from appium import webdriver

from pages.base_page import BasePage
from pages.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver == None:
            # 如果没有driver，就初始化driver
            caps = {
                "platformName": "Android",
                "deviceName": "vivo Y70t",
                "udid": "000003f62dd699c9",
                "appPackage": self._package,
                "appActivity": self._activity,
                "noReset": "true",
                "dontStopAppOnReset": "true"
            }
            # caps["appPackage"] = self._package
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            # 如果已经初始化过driver了，就直接调用 start_activity() 方法启动应用
            # self.driver.launch_app() 这个方法不需要传入参数，会自动启动desired_cap中设置的activity
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main:
        return Main(self._driver)


