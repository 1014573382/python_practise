from appium import webdriver


class Connection():
    def setup(self):
        caps = {
            "platformName": "Android",
            "deviceName": "Honor V10",  # 可随意写，不起实际作用
            # "avd": "PixelXL_API_30",  #指定模拟器名称，脚本执行时会自动启动模拟器
            "udid": "RKK0217C15000011",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",  # 不会停止app、清除数据和卸载app
            "skipServerInstallation": "true",   # 跳过uiautomator2 server 的安装
            "skipDeviceInitialization": "true", # 跳过设备初始化
            "dontStopAppOnReset": "true",  #启动之前不停止app
            "autoGrantPermissions": "true",  # 自动点掉弹框，但如果noReset 是true的话此参数就不会生效
            "newCommandTimeout": 120   # 上一个命令与下一个命令之间的间隔时间，默认60秒
            # "browserName": "Chrome",  # 测试webview时，需要指定浏览器名称和下面的driver地址，系统自带的浏览器就写 "Browser"
            # 方案一，直接指定具体的某一个与浏览器对应的 driver
            # "chromedriverExecutable": "D:/python/pythonappium/chromedriver/chromedriver.exe",
            # 方案二：指定存放chromedriver的文件夹，然后在mapping文件中指定不同版本浏览器和driver的对应关系
            # "chromedriverExecutableDir": r"D:\Python\PythonAppium\chromedriver",
            # "chromedriverChromeMappingFile": r"D:\github_code\appium\webview_test\mapping.json"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)