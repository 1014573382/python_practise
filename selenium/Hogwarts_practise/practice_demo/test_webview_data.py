from selenium import webdriver


class TestData:
    def test_data(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://home.testing-studio.com")
        # 获取chrome 加载服务的时间，和在chrome console 中执行 window.performance.timing 返回结果一致
        # 可以在console中执行 window.performance.timing.domContentLoadedEventEnd - window.performance.timing.domContentLoadedEventStart 计算dom开始加载到结束的时间
        print(self.driver.execute_script("return JSON.stringify(window.performance.timing)"))