#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/20 12:05
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from weworkpageobject.page.contact_detail_briefInfo import ContactDetailBriefInfo
from weworkpageobject.page.basepage import BasePage


class DepartmentSearch(BasePage):
    """搜索成员页面"""

    search_ele = (MobileBy.ID, "com.tencent.wework:id/hd5")

    def find_member(self, delname):
        """搜索成员"""
        self.search_result_ele = (MobileBy.XPATH, f"//*[@text='{delname}']")

        # 输入联系人姓名
        self.find_and_sendkeys(self.search_ele, delname)
        sleep(2)
        # 以元组形式传进来，这个元组会被处理成一项，要使元组中的每一个值作为一个单独的参数，调用函数时要在元组名前面加 *
        global search_result_before
        # self.search_result_before = self.driver.find_elements(*self.search_result_ele)
        search_result_before = self.driver.find_elements(*self.search_result_ele)
        # 判断搜索出来的长度列表
        if len(search_result_before) > 1:
            # 存在 联系人，点击第二个(第一个是输入的搜索内容)
            search_result_before[1].click()
            return ContactDetailBriefInfo(self.driver)
        else:
            print("没有这个联系人")
            self.back()
            return False

    def assert_result(self, delname):
        search_result_afterdel = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{delname}']")
        if len(search_result_before) -  len(search_result_afterdel) == 1:
            return True
