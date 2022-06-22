from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from BigbankXW.page.basepage import BasePage
from BigbankXW.page.registercontractview import RegisterContractView


class LoginPage(BasePage):

    # 输入手机号
    inputmobile_ele = (MobileBy.CSS_SELECTOR, ".van-field__body input")
    # 获取验证码
    getsms_ele = (MobileBy.CSS_SELECTOR, ".sendBtn")
    # 输入验证码
    inputsms_ele = (MobileBy.XPATH, "//*[@type='tel'and@class='van-field__control']")
    verification_code = '111111'
    clicklogin_ele = (MobileBy.CSS_SELECTOR, ".xw-button_box button")


    def input_mobile(self, mobile):
        self.find_and_sendkeys(self.inputmobile_ele, mobile)
        return self

    def getsms(self):
        self.find_and_click(self.getsms_ele)
        return self

    def inputsms(self):
        self.find_and_sendkeys(self.inputsms_ele, self.verification_code)
        return self

    def clicklogin(self):
        sleep(0.7)
        self.find_and_click(self.clicklogin_ele)
        return RegisterContractView(self.driver)

