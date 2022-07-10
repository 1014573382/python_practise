#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2022/07/10 16:21
from selenium import webdriver


class TestPerformance:
    def test_performance(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3.org/TR/navigation-timing/")
        # JSON.stringify 进行json格式化
        per = driver.execute_script("return JSON.stringify(window.performance.timing)")
        print("所有性能数据：", per)
        responsetime = "return JSON.stringify(window.performance.timing.responseEnd - window.performance.timing.responseStart)"
        print("服务器响应所花时间:", driver.execute_script(responsetime))
