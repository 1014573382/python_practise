#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2022/06/03 20:21
from selenium.webdriver.common.by import By

from Hogwarts_practise.wework_test_po.pages.base_page import BasePage


class AddMember(BasePage):
    def add_member(self, name, account, mobile):
        self.find(By.CSS_SELECTOR, '#username')
        self.find_and_send(By.CSS_SELECTOR, '#username', name)
        self.find_and_send(By.CSS_SELECTOR, '#memberAdd_acctid', account)
        self.find_and_send(By.CSS_SELECTOR, '#memberAdd_phone', mobile)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()


    def cancel_add(self):
        pass