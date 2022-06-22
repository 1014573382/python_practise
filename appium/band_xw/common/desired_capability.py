from appium import webdriver

class Capabilities():
    def setup(self):
        des_caps = {}
        des_caps["platformName"] = "Android"
        des_caps["deviceName"] = "Galaxy A71"
        des_caps["udid"] = "R5CR30D00QP"
        des_caps["browserName"] = "Chrome"
        # des_caps["appPackage"] = "com.sec.android.app.sbrowser"
        # des_caps["appActivity"] = "com.sec.android.app.sbrowser.SBrowserMainActivity"
        # des_caps["noReset"] = "True"
        des_caps['unicodeKeyboard'] = True
        des_caps['resetKeyboard'] = True
        des_caps["skipServerInstallation"] = True  # 跳过uiautomator2 server 的安装
        des_caps["skipDeviceInitialization"] = True  # 跳过设备初始化
        des_caps["dontStopAppOnReset"] = True  # 启动之前不停止app
        # 修改chromedriver的路径
        des_caps["chromedriverExecutable"] = "D:\\Program\\appium_chromedriver\\78.0.3904.105\\chromedriver.exe"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()


