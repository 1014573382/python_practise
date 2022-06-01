from selenium import webdriver

class TestStart():
     def setup(self):
         self.driver = webdriver.Chrome()

     def test_open(self):
         self.driver.get("https://www.baidu.com")



if __name__ == '__main__':
    TestStart().test_open()