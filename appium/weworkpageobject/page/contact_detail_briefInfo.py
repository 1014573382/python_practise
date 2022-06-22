#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/20 12:31
from appium.webdriver.common.mobileby import MobileBy

from weworkpageobject.page.contact_detail_setting import ContactDetailSetting
from weworkpageobject.page.basepage import BasePage


class ContactDetailBriefInfo(BasePage):

    detail_setting_ele = (MobileBy.ID, "com.tencent.wework:id/isv")

    def goto_contact_detail_setting(self):
        """点击右上角三个点，设置相关信息"""
        self.find_and_click(self.detail_setting_ele)
        return ContactDetailSetting(self.driver)

    def send_message(self):
        pass

    def invitejoin(self):
        pass