from appium import webdriver


class TestEmulator():
    def setup(self):
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "",
            "deviceName": "emulator-5554",
            "avd": "PixelXL_API_30",    #指定模拟器名称，脚本执行时会自动启动模拟器
            "browserName": "Chrome",
            "chromedriverExecutableDir": r"D:\python\PythonAppium\chromedriver",
            "chromedriverChromeMappingFile": r"D:\github_code\appium\webview_test\mapping.json"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(8)

    def test_auto_open_emualtor(self):
        self.driver.get("http://www.baidu.com")