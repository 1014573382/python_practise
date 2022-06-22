import random
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BigbankXW.common.desired_capability import Capabilities

test_url = "https://uatdtestwx.hopebank.com/xwbank/dms_h5/test.html"
mobile_list = [str(random.randint(17222001254,17222099999)) for x in range(1)]
verification_code = '111111'

class TestZmd(Capabilities):
    @pytest.mark.parametrize('mobile', mobile_list)
    def test_zmdcredit(self,mobile):
        # search_ele = self.driver.find_element(
        #     MobileBy.ID, "com.sec.android.app.sbrowser:id/location_bar_edit_text")
        # search_ele.send_keys(test_url)
        self.driver.get(test_url)
        # 点击选择渠道
        # self.driver.find_element(MobileBy.CSS_SELECTOR, "#quota").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='XWESZMDXCX'and@index='5']").click()
        # 输入手机号
        self.driver.find_element(MobileBy.CSS_SELECTOR, "#phone").send_keys(mobile)
        # 点击跳转
        self.driver.find_element(MobileBy.CSS_SELECTOR, "#send").click()
        sleep(1)
        # 确定弹框
        self.driver.switch_to.alert.accept()
        # 点击查看我的额度
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.element_to_be_selected((By.XPATH, "//*[@text='查看我的额度']"))).click()
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "#app .generalize-zmd-new_btn")).click()

        """登录页面"""
        # 输入手机号
        # self.driver.find_element(MobileBy.CSS_SELECTOR, ".van-field__body input").send_keys(mobile)
        # 点击获取验证码
        self.driver.find_element(MobileBy.CSS_SELECTOR, ".sendBtn").click()
        sleep(1)
        # 输入验证码
        self.driver.find_element(MobileBy.XPATH, "//*[@type='tel'and@class='van-field__control']").send_keys(verification_code)
        sleep(1)
        # 点击登录
        self.driver.find_element(MobileBy.CSS_SELECTOR, ".xw-button_box button").click()

        """预览合同页"""
        # 点击向下的箭头
        self.driver.find_element(MobileBy.CSS_SELECTOR, ".xui-x-agree__go-bottom").click()
        sleep(2)
        # 点击同意签署合同
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, ".xui-x-agree__btn button")).click()
        # self.driver.find_element(MobileBy.CSS_SELECTOR, ".xui-x-agree__btn button").click()
        sleep(3)
        # 确定弹框
        # self.driver.switch_to.alert.accept()
        # 点击确定弹窗-业务办理说明
        # self.driver.find_element(MobileBy.CSS_SELECTOR, "#app .xui-button__content").click()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "#app .xui-button__content")).click()
        sleep(1)

        webview_context = self.driver.context
        print("webview_context: ", webview_context)
        # 点击上传身份证人像面
        self.driver.find_element(MobileBy.CSS_SELECTOR, "#app .idCard-front .idCard-UI_card__camera").click()
        sleep(1)
        # 切换到原生APP，进行拍照
        self.driver.switch_to.context("NATIVE_APP")
        # 点击授权chrome拍摄照片和录制视频（仅在使用该应用时允许）
        self.driver.find_element(MobileBy.XPATH, "//*[@text='仅在使用该应用时允许'and@class='android.widget.Button']").click()
        # 选择相机
        self.driver.find_element(MobileBy.XPATH, "//*[@text='相机'and@resource-id='android:id/text1']").click()
        # 点击拍照
        self.driver.find_element(MobileBy.ID, "com.sec.android.app.camera:id/normal_center_button").click()
        sleep(2)
        # 点击确定
        WebDriverWait(self.driver,10).until(
            lambda x: x.find_element(MobileBy.ID, "com.sec.android.app.camera:id/okay")).click()
        # self.driver.find_element(MobileBy.ID, "com.sec.android.app.camera:id/okay").click()

        self.driver.switch_to.context(webview_context)
        ele_idCardFront = WebDriverWait(self.driver,12).until(
            lambda x:x.find_element(MobileBy.CSS_SELECTOR, "#app .idCard-front .idCard-UI_card__camera"))
        if ele_idCardFront:
            # 点击上传身份证国徽面
            self.driver.find_element(MobileBy.CSS_SELECTOR, "#app .idCard-back .idCard-UI_card__camera").click()







