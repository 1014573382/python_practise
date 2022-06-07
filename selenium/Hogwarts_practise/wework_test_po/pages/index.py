#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2022/06/03 20:08
from selenium.webdriver.common.by import By

from Hogwarts_practise.wework_test_po.pages.add_member import AddMember
from Hogwarts_practise.wework_test_po.pages.base_page import BasePage
from Hogwarts_practise.wework_test_po.pages.contacts import Contacts


class Index(BasePage):
    """
    企业微信首页功能
    """
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()
        return AddMember(self._driver)

    def goto_import_contact(self):
        pass

    def goto_member_join(self):
        pass

    def goto_contacts(self):
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        return Contacts(self._driver)

