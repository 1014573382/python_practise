#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2022/06/03 20:13
from selenium.webdriver.common.by import By

from Hogwarts_practise.wework_test_po.pages.add_member import AddMember
from Hogwarts_practise.wework_test_po.pages.base_page import BasePage


class Contacts(BasePage):

    def goto_add_member(self):

        def add_member_condition(x):
            """
            查找 添加成员页 的 姓名 元素是否出现，如果没出现，则一直点击通讯录页的 添加成员 按钮
            添加成员 按钮 刚出现时，虽然可点击，但是点击并不会跳转，所以根据点击后的元素是否出现来判断点击是否成功
            """
            name_element_len = len(self.finds(By.CSS_SELECTOR, '#username'))
            if name_element_len < 1:
                # 添加成员 按钮
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            else:
                return name_element_len > 0

        # self.wait_for_click((By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)'))
        self.wait_for_condition(add_member_condition)
        return AddMember(self._driver)

    def delete_member(self):
        pass