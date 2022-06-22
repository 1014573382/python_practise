#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/12 18:12
# from WeworkTest.usepageobject.page.contactaddfastmode import ContactAddFastMode

'''添加成员页'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from weworkpageobject.page.basepage import BasePage


class AddMemberPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver
    addmanual_ele = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")


    def add_manual(self):
        '''手动输入添加'''
        from weworkpageobject.page.contactaddfastmode import ContactAddFastMode
        # 选择手动输入添加
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmanual_ele)
        return ContactAddFastMode(self.driver)

    def get_toast(self):
        '''验证toast'''
        # element = WebDriverWait(self.driver, 10).until(
        #     lambda x:x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        element = self.webdriver_wait(self.toast_ele)
        result = element.text
        return result
