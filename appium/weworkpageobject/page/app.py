#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/12 17:47

'''
存放app应用常用的一些方法：比如启动app,关闭app,重启app,进入首页
'''
from appium import webdriver
from weworkpageobject.page.basepage import BasePage
from weworkpageobject.page.mainpage import MainPage


class App(BasePage):
    def startapp(self):
        '''启动app'''
        if self.driver == None:
            # 第一次调用start()方法的时候 driver 为None
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["skipServerInstallation"] = "true"  # 跳过uiautomator2 server 的安装
            caps["skipDeviceInitialization"] = "true"  # 跳过设备初始化
            caps["dontStopAppOnReset"] = "true"  # 启动之前不停止app
            # caps["settings[waitForIdleTimeout]"] = 0  # 等待页面idle的时间设置为0（打卡页面时间一直在动，会被当做页面未加载完成）

            # 与server建立连接，初始化一个driver，创建session,返回一个sessionid
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

        else:
            self.driver.launch_app()
            # self.driver.start_activity() 可以启动其他应用的页面
        self.driver.implicitly_wait(14)
        return self   # 依然能够调用本类的其他方法，即：返回当前页，继续调用goto_main

    def stopapp(self):
        self.driver.quit()

    def restartapp(self):
        self.driver.close()  # 关闭app
        self.driver.launch_app()  # 再次打开app
        return self

    def goto_main(self):
        return MainPage(self.driver)


