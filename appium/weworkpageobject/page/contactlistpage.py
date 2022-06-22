#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/12 17:58

from appium.webdriver.common.mobileby import MobileBy
from weworkpageobject.page.department_search import DepartmentSearch
from weworkpageobject.page.addmemberpage import AddMemberPage
from weworkpageobject.page.basepage import BasePage


class ContactListPage(BasePage):
    '''通讯录列表页'''
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_text = '添加成员'
    search_ele = (MobileBy.ID, "com.tencent.wework:id/it6")

    def add_contact(self):
        '''添加成员'''
        # 滚动查找“添加成员”元素
        self.find_by_scroll(self.addmember_text).click()
        return AddMemberPage(self.driver)

    def search_contact(self):
        '''搜索成员'''
        self.find_and_click(self.search_ele)
        return DepartmentSearch(self.driver)