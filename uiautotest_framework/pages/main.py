from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Main(BasePage):
    def click_skip_advertise(self):
        """跳过启动页的广告"""
        try:
            self.find(By.ID, "tv_skip").click()
            return self
        except:
            return self

    def goto_search(self):
        self.find(By.ID, "home_search").click()
        self.find(By.ID, "search_input_text").send_keys("歌尔股份")