from selenium.webdriver.common.by import By

from BigbankXW.page.basepage import BasePage
from BigbankXW.page.loginpage import LoginPage


class LandingPage(BasePage):

    checkcredit_ele_gh = (By.CSS_SELECTOR, "#app .generalize-zmd-new_btn")
    checkcredit_ele_gdpf = (By.CSS_SELECTOR, ".generalize-zh_content button")

    def checkcredit(self):
        try:
            # 光大和浦发的落地页
            self.webdriver_wait(self.checkcredit_ele_gdpf).click()
        except:
            # 助梦贷和工新借落地页
            self.webdriver_wait(self.checkcredit_ele_gh).click()
        return LoginPage(self.driver)
