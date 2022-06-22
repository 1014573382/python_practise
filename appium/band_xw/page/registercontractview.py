from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from BigbankXW.page.basepage import BasePage
from BigbankXW.page.idcarduploadpage import IdcardUploadPage


class RegisterContractView(BasePage):

    # 向下的箭头
    gobottom_ele = (MobileBy.CSS_SELECTOR, ".xui-x-agree__go-bottom")
    # 同意签署合同
    agree_sign_ele = (MobileBy.CSS_SELECTOR, ".xui-x-agree__btn button")

    def reg_contract_view(self):
        self.find_and_click(self.gobottom_ele)
        sleep(3)
        self.webdriver_wait(self.agree_sign_ele).click()
        sleep(1)
        return IdcardUploadPage(self.driver)

