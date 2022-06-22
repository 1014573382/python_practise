#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/09/12 18:25
# import sys
# sys.path.append(r"D:\Python\Python_code\Appium\WeworkTest\usepageobject\testcases")
from time import sleep

import allure
import pytest
import yaml
from weworkpageobject.page.app import App

with open("../testdata/addmember.yaml", encoding='utf-8')as file:
    addmembers = yaml.safe_load(file)

with open("../testdata/delmember.yaml",encoding='utf-8')as file:
    delmembers = yaml.safe_load(file)

@allure.feature('通讯录测试')
class TestContact():

    def setup_class(self):
        self.app = App()
        self.main = self.app.startapp().goto_main()

    def teardown_class(self):
        self.app.stopapp()

    @allure.title("添加成员")
    @allure.story("添加成员测试")
    @pytest.mark.parametrize("name, mobile", addmembers)
    def test_addcontact(self, name, mobile):
        # name = 'gita11'
        # mobile = '17222110011'
        mypage = self.main.goto_contactlist().add_contact().add_manual().\
            set_name(name).set_mobile(mobile).click_cancelmsg().click_save()
        text = mypage.get_toast()
        assert '成功' in text
        self.app.back()  # 添加成功后，返回上一页，可以找到通讯录继续下一用例

    @pytest.mark.parametrize('delname', delmembers)
    def test_delcontact(self, delname):
        mysearch = self.main.goto_contactlist().search_contact().find_member(delname)
        if mysearch:
            delpage = mysearch.goto_contact_detail_setting().click_contactedit().delete_contact()
            sleep(3)
            assert delpage.assert_result(delname)
            self.app.back()
        else:
            self.app.back()



