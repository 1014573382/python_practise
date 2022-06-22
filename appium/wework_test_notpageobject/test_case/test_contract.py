#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/08/14 10:38
import os
from time import sleep
import allure
import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from WeworkTest.common.desired_caps import Connection

with open("../testdata/addmember.yaml", encoding='utf-8')as f:
    addmembers = yaml.safe_load(f)

with open("../testdata/delmember.yaml", encoding="utf-8") as f:
    delmembers = yaml.safe_load(f)


@allure.feature("通讯录功能模块")
class TestContact(Connection):

    @allure.title("添加成员")
    @allure.story("添加成员功能")
    @pytest.mark.first
    # @pytest.mark.parametrize("name, mobile",[("gita1","15222180002"),("gita2","15222180003")])
    @pytest.mark.parametrize("name, mobile", addmembers)
    def test_addmember(self, name, mobile):
        """企业微信 添加成员"""
        # name1 = "gita1"
        # mobile1 = "15222180001"
        print("addmembers: ", addmembers)
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找“添加成员”元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).'
                                 'instance(0)).'
                                 'scrollIntoView('
                                 'new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        # 选择手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bd9").send_keys(name)
        # 输入手机号
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g9o").send_keys(mobile)
        # 取消勾选自动发送邀请通知
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fwf").click()
        # 点击保存
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        # self.driver.save_screenshot("addsuccess.png")   #保存在当前路径下
        # 判断保存截图的路径是否存在，不存在则创建
        if not os.path.exists("../test_screenshot"):
            os.makedirs("../test_screenshot")
        else:
            pass
        self.driver.get_screenshot_as_file("../test_screenshot/addsuccess.png")
        # 可在测试报告中插入指定文本，图片或视频，此处插入图片
        allure.attach.file("../test_screenshot/addsuccess.png",
                           name="添加成员截图", attachment_type=allure.attachment_type.PNG)

        # 验证toast
        # self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        element = WebDriverWait(self.driver, 10).until(lambda x:x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        result = element.text
        assert "成功" in result
        # 返回，即可找到通讯录,继续下一用例
        self.driver.back()
        sleep(1)


    @allure.title("删除成员")
    @allure.story("删除成员功能")
    @pytest.mark.order(2)
    @pytest.mark.parametrize('del_name', delmembers)
    def test_delcontact(self, del_name):
        """企业微信 删除成员"""
        # del_name = "jack1"
        print("delmembers: ", delmembers)
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/it6").click()
        # 输入联系人姓名
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hd5").send_keys(del_name)
        sleep(3)
        # find_elements 返回找到元素的列表
        contract_list = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{del_name}']")
        print("contract_list:", contract_list)
        # 判断搜索出来的长度列表
        if len(contract_list) < 2:
            self.driver.back()
            print("没有这个联系人")
            return
        else:
            # 存在 联系人，点击第二个(第一个是输入的搜索内容)
            contract_list[1].click()
            # 点击右上角三个点
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/isv").click()
            # 点击 编辑成员
            self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
            # 滚动查找删除元素
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().'
                                     'scrollable(true).instance(0)).'
                                     'scrollIntoView(new UiSelector().'
                                     'text("删除成员").instance(0));').click()
            # 点击确定
            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
            sleep(3)
            # 判断删除后的列表长度比之前的减一，即删除成功
            afterdel_ele = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{del_name}']")
            assert len(contract_list) - len(afterdel_ele) == 1
            # 返回，即可找到通讯录,继续下一用例
            self.driver.back()






