#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/20 12:38
from appium.webdriver.common.mobileby import MobileBy

from weworkpageobject.page.contact_edit import ContactEdit
from weworkpageobject.page.basepage import BasePage


class ContactDetailSetting(BasePage):
    """个人信息设置页"""

    editmember_ele = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def click_contactedit(self):
        """编辑成员信息"""
        # 点击编辑成员
        self.find_and_click(self.editmember_ele)
        return ContactEdit(self.driver)