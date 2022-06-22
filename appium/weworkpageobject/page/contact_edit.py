#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/20 12:47
from appium.webdriver.common.mobileby import MobileBy

from weworkpageobject.page.basepage import BasePage
# from weworkpageobject.page.department_search import DepartmentSearch


class ContactEdit(BasePage):
    """编辑成员信息"""

    deletecontact_text = '删除成员'
    delete_confirm_ele = (MobileBy.XPATH, "//*[@text='确定']")

    def delete_contact(self):
        from weworkpageobject.page.department_search import DepartmentSearch
        # 滚动查找删除成员元素
        self.find_by_scroll(self.deletecontact_text).click()
        # 确认删除
        self.find_and_click(self.delete_confirm_ele)
        return DepartmentSearch(self.driver)

    def set_name(self):
        pass

    def set_department(self):
        pass