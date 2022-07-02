from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.stock import Stock


class Main(BasePage):
    def click_skip_advertise(self):
        try:
            self.find(By.ID, "tv_skip").click()
            return self
        except:
            return self

    def goto_search(self):
        # self.find(By.ID, "home_search").click()
        # self.find(By.ID, "search_input_text").send_keys("歌尔股份")
        self.steps("../yaml_config/main.yml", "goto_search")

    def goto_stock(self):
        """进入股票页"""
        self.set_implicitly_wait(3)
        # self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@index="1"and @clickable="true"]').click()
        # self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="股票"]').click()
        self.steps("../yaml_config/main.yml", "goto_stock")
        return Stock(self._driver)