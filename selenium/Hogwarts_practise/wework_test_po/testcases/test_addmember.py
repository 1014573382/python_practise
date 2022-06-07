#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2022/06/03 20:59
from Hogwarts_practise.wework_test_po.pages.index import Index


class TestAddMember():
    def setup(self):
        self.index = Index()

    def test_addmember(self):
        self.index.goto_contacts().goto_add_member().\
            add_member('zhangsan', 'zhangsan', '11100001111')