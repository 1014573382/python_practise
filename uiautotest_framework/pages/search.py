from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Search(BasePage):
    def search(self, stock_name):
        """
        self.find(By.ID, "search_input_text").send_keys(f"{name}")
        # 有时候输入后会关闭搜索到显示的结果，再点击一下输入框就能再次显示
        self.find(By.ID, "search_input_text").click()
        # self.find(By.ID, "search_input_text").send_keys(Keys.ENTER)
        self.find(By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/name'and @text='{name}']").click()
        self.find(By.ID, "add_attention").click()  #加自选
        self.find(By.ID, "add_attention").click()  #加自选
        """
        self.params["stock_name"] = stock_name
        self.steps("../yaml_config/search.yaml", "search")
