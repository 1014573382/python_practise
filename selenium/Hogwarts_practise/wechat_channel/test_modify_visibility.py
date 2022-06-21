from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestVisiblePermissions():
    def setup(self):
        chrome_option = Options()
        chrome_option.debugger_address = "127.0.0.1:8888"
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.implicitly_wait(6)

    def each_page_click(self):
        """实现每一页所有视频可见权限的修改"""
        # 获取本页视频的数量
        vedio_num = len(self.driver.find_elements(By.CSS_SELECTOR, '.center-info'))
        print(vedio_num)
        for num in range(1, (vedio_num + 1)):
            # 移动到可见权限位置并点击，下面是 所有人可见状态 下的可见权限元素（锁上状态）
            # permission_element = self.driver.find_element(By.CSS_SELECTOR, '.post-list-body .post-list-item:nth-child(1) .opr .opr-item-wrap:nth-child(3)')
            # permission_element = self.driver.find_element(By.CSS_SELECTOR,
            #                                               f".post-list-body .post-list-item:nth-child({num}) .weui-icon-outlined-lock")
            # 仅自己可见状态 下的可见权限元素（开锁状态）
            permission_element = self.driver.find_element \
                (By.CSS_SELECTOR,
                 f".post-list-body .post-list-item:nth-child({num}) .opr .opr-item-wrap:nth-child(3) .opr-item")

            ActionChains(self.driver).move_to_element(permission_element).click(permission_element).perform()
            # 点击确定，最后一个改为 nth-child(1) 即点击取消
            sleep(0.5)
            self.driver.find_element(By.CSS_SELECTOR, '.app-body>div:nth-child(3) .footer div:nth-child(1)').click()

    def test_visible_permissions(self):

        self.each_page_click()
        for i in range(1):
            # 只有两页的情况下下一页箭头定位
            # next_page_ele = self.driver.find_element(By.CSS_SELECTOR, '.weui-desktop-pagination a')
            try:
                # 在中间页时，下一页元素定位方式
                next_page_ele = self.driver.find_element(By.CSS_SELECTOR, '.weui-desktop-pagination a:nth-child(3)')
                ActionChains(self.driver).move_to_element(next_page_ele).click(next_page_ele).perform()
            except:
                # 在第一页时，下一页元素定位方式(如果在中间页，就会定位到’跳转‘)
                next_page_ele = self.driver.find_element(By.CSS_SELECTOR, '.weui-desktop-pagination a:nth-child(2)')
                ActionChains(self.driver).move_to_element(next_page_ele).click(next_page_ele).perform()

            sleep(2)
            self.each_page_click()


