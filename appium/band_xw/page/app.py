from appium import webdriver

from BigbankXW.page.basepage import BasePage
import yaml
from BigbankXW.page.firstpage import FirstPage

with open("../config/environment.yaml", encoding='utf-8')as file:
    test_url = yaml.safe_load(file)

class App(BasePage):

    def start(self):
        if self.driver == None:
            # 第一次调用start()方法的时候 driver 为None
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = 'Galaxy A71'
            caps['udid'] = 'R5CR30D00QP'
            caps['browserName'] = 'Chrome'
            # caps['packageName'] = ''
            # caps['activityName'] = ''
            caps['noReset'] = True
            caps['dontStopAppOnReset'] = True
            caps['skipServerInstallation'] = True  # 跳过uiautomator2 server 的安装
            caps['skipDeviceInitialization'] = True # 跳过设备初始化
            # caps["dontStopAppOnReset"] = True  # 启动之前不停止app
            caps['chromedriverExecutable'] = r'D:\Program\appium_chromedriver\78.0.3904.105\chromedriver.exe'

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(12)
        return self

    def stopapp(self):
        self.driver.quit()

    def restart(self):
        self.driver.close()
        self.driver.launch_app()
        return self

    def gotofirstpage(self):
        self.driver.get(test_url['url'])
        return FirstPage(self.driver)