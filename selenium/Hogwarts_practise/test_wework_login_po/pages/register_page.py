from selenium.webdriver.common.by import By
from Hogwarts_practise.test_wework_login_po.pages.base_page import BasePage


class RegisterPage(BasePage):
    """
    注册页面
    """
    def register(self):
        self._driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys("郭郭的企业")
        self._driver.find_element(By.CSS_SELECTOR, '#corp_industry>a>span:nth-child(1)').click()
        self._driver.find_element(By.XPATH, '//*[@data-name="IT服务"]').click()
        self._driver.find_element(By.XPATH, '//*[@data-name="互联网和相关服务"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '#manager_name').send_keys("guoguo")
        return True
