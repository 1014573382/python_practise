#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/07/31 18:01
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from WeworkTest.common.desired_caps import Connection


class TestWeWork(Connection):
    def test_daka(self):
        # 点击工作台（Workspace）
        workspace_ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='Workspace']")
        workspace_ele.click()
        # 滚动查找 打卡 并点击
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable' 
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("Attendance (Punch)").instance(0));').click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Attendance (Punch)").instance(0));')
        # 点击外出打卡（Offsite Punch）
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ic6").click()
        # 点击打卡区域进行打卡
        time.sleep(4)
        # 验证是否进入外出打卡页面
        element_offsite_punch = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b2t").text
        assert "Punch (2nd)" in element_offsite_punch

        # 点击外出打卡
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b2n").click()


        



