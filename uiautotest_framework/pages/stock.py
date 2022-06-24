from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.search import Search


class Stock(BasePage):
    def goto_search(self):
        self.find(By.ID, 'action_search').click()
        return Search(self._driver)