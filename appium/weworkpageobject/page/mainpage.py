#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/12 17:53

'''主页面'''
from appium.webdriver.common.mobileby import MobileBy
from weworkpageobject.page.basepage import BasePage
from weworkpageobject.page.contactlistpage import ContactListPage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    contact_ele = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        '''进入到通讯录'''
        # 点击通讯录
        self.find_and_click(self.contact_ele)
        return ContactListPage(self.driver)

    def goto_workbench(self):
        '''进入工作台'''
        pass

