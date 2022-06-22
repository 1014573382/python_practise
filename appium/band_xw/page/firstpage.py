from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.select import Select

from BigbankXW.page.basepage import BasePage
from BigbankXW.page.landingpage import LandingPage


class FirstPage(BasePage):

    channelid_ele =  (MobileBy.CSS_SELECTOR, "[name='channelId']")
    channelValue = 'XWGDYHAPP'
    mobile_ele = (MobileBy.CSS_SELECTOR, "#phone")
    jump_ele = (MobileBy.CSS_SELECTOR, "#send")

    # with open("../config/channelId.yaml", encoding='utf-8')as f:
    #     channelValue = yaml.safe_load(f)

    def selectchannel(self):
        # 根据Select类进行定位
        select = Select(self.find(self.channelid_ele))
        select.select_by_value(self.channelValue)
        # sleep(1)
        return self

    def setmobile(self, mobile):
        # 输入手机号
        self.find_and_sendkeys(self.mobile_ele, mobile)
        return self

    def click_jump(self):
        self.find_and_click(self.jump_ele)
        sleep(1)
        # 确定弹框
        self.driver.switch_to.alert.accept()
        return LandingPage(self.driver)
