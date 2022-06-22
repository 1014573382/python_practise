#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/12 18:20

'''添加成员-输入具体信息页'''
# from WeworkTest.usepageobject.page.addmemberpage import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from weworkpageobject.page.basepage import BasePage


class ContactAddFastMode(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver
    name_ele = (MobileBy.ID, "com.tencent.wework:id/bd9")
    mobile_ele = (MobileBy.ID, "com.tencent.wework:id/g9o")
    cancelmsg_ele = (MobileBy.ID, "com.tencent.wework:id/fwf")
    save_ele = (MobileBy.XPATH, "//*[@text='保存']")

    def set_name(self, name):
        # 输入姓名
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bd9").send_keys(name)
        self.find_and_sendkeys(self.name_ele, name)
        return self

    def set_mobile(self, mobile):
        # 输入手机号
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g9o").send_keys(mobile)
        self.find_and_sendkeys(self.mobile_ele, mobile)
        return self

    def click_cancelmsg(self):
        # 取消勾选自动发送邀请通知
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fwf").click()
        self.find_and_click(self.cancelmsg_ele)
        return self

    def click_save(self):
        # 局部导入，解决循环导入的问题
        from weworkpageobject.page.addmemberpage import AddMemberPage
        # 点击保存
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.find_and_click(self.save_ele)
        return AddMemberPage(self.driver)