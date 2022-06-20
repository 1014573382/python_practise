from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By


class TestBrowser():

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "2.0.0",
            "deviceName": "Honor v10",
            "browserName": "Chrome",
            "udid": "RKK0217C15000011",
            # "udid": "emulator-5554",
            # 方案一，直接指定具体的某一个与浏览器对应的 driver
            # "chromedriverExecutable": "D:/python/pythonappium/chromedriver/chromedriver.exe",
            # 方案二：指定存放chromedriver的文件夹，然后在mapping文件中指定不同版本浏览器和driver的对应关系。不过会优先找 android webview 默认实现
            "chromedriverExecutableDir": r"D:\Python\PythonAppium\chromedriver",
            "chromedriverChromeMappingFile": r"D:\github_code\appium\webview_test\mapping.json",
            # "showChromedriverLog": "true",
            # "appPackage": "com.android.chrome",
            # "appActivity": "com.google.android.apps.chrome.Main",
            "skipDeviceInitialization": "true",
            # "unicodeKeyboard": "true",
            # "resetKeyboard": "true",
            "noReset": "true"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(7)

    @pytest.mark.skip
    def test_weread(self):
        self.driver.find_element(By.ID, 'home_tab_timeline').click()
        self.driver.find_element(By.XPATH,'//*[@class="android.view.ViewGroup"and@clickable="true"and@index="0"]').click()
        print(self.driver.current_context)
        print(self.driver.context)
        # print(self.driver.window_handles)
        # print(self.driver.current_window_handle)

    @pytest.mark.skip
    def test_mobile(self):
        # 发短信 只能用emulator模拟器
        self.driver.send_sms('15222181111', 'test appium send message2')
        self.driver.save_screenshot("./screenshots/aaa.png")
        sleep(2)
        # 打电话
        self.driver.make_gsm_call("12241222000", GsmCallActions.CALL)
        print("current_context:", self.driver.current_context)
        self.driver.save_screenshot("./screenshots/bbb.png")

    def test_openbrowser(self):
        self.driver.get("http://www.baidu.com")