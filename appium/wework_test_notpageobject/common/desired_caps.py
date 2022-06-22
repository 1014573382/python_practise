#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/08/13 08:27

from appium import webdriver

class Connection:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["skipServerInstallation"] = "true" # 跳过uiautomator2 server 的安装
        caps["skipDeviceInitialization"] = "true" # 跳过设备初始化
        caps["dontStopAppOnReset"] = "true" #启动之前不停止app
        #caps["settings[waitForIdleTimeout]"] = 0  # 等待页面idle的时间设置为0（打卡页面时间一直在动，会被当做页面未加载完成）

        # 与server建立连接，初始化一个driver，创建session,返回一个sessionid
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(14)

    def teardown_class(self):
        self.driver.quit()
