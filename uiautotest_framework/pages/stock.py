from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.search import Search


class Stock(BasePage):
    def goto_search(self):
        # self.find(By.ID, 'action_search').click()
        self.steps("../yaml_config/stock.yml", "goto_search")
        return Search(self._driver)