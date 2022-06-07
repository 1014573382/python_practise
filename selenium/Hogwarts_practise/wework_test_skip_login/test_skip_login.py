import shelve

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWework:
    def setup_method(self):
        option = Options()
        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 chrome -remote-debugging-port=7333 开启调试
        option.debugger_address="127.0.0.1:7333"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(6)

    @pytest.mark.skip
    def test_skip_login(self):
        # self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        # 获取cookie
        # print(self.driver.get_cookies())
        self.driver.get("https://work.weixin.qq.com/")
        # 把cookie 存储在shelve 中。 shelve是对象持久化保存方法，将对象保存到文件里面，默认的数据存储文件是二进制的，就是一个简单的数据存储方案
        # 创建或打开一个数据库
        db = shelve.open("cookies")
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '-OccjvZ2yr7RbAiw5vf-A8h7ha0eXVjFoV2WX-jV-NIRx9Obui31SR0vwD_HRkPbHlOZ4iDcn8UE2HC9XBCXiim0ArdR9YRvQ039Di8jVhi7gZOF63oMKo2vSvvQWRCOgvwj4LQl4FCk01PlZWVeCedGX3cNiADl4u9cCsC1_RXYAO63WyRbGtFFdWetTCX5e1_oGqhQyG49rzqjqvRYWSegNWWa1C2K74RgtAT36lt_57FN-GYMax1WR-2_ZhN49E0xQF9ehntRm-QXz_Wjlg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688854284316806'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970326212982084'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688854284316806'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True, 'value': '368645372627196'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': 'a73e8e0a0113dc077b6e392cb3e68d92e38519ba2361f0b3f450db464e9ca91b'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1250164'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'JZ0N8UpwRY'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True, 'value': 'direct'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': True, 'value': 'q1f6y3U7j556O3N2B9p261w126'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': True, 'value': 'a2e99cf27f2ff77c'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'u4YAMImbBA0_VM1QktMjg4We7OQW1P7abEWjpuH9y_SOIcZbddbemEspGXRebLFU'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': True, 'value': ''}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s5899838943'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True, 'value': '0_89d125b157d17'}, {'domain': '.work.weixin.qq.com', 'expiry': 1656671256, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1636703527,1636703542'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4368392512'}, {'domain': '.qq.com', 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': True, 'value': 'GA1.2.616229761.1636703823'}]
        # 将数据存储在 shelve 中
        # db["cookies"] = cookies
        # 取出数据
        cookies = db["cookies"]
        for cookie in cookies:
            # 去掉过期时间（是小数时可能会报错，一般不用特意去掉expiry）
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 把字典加入到driver 的 cookie 中
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        db.close()

    def test_skip_login_yaml(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 保存 cookies 到 cookies.yml 文件中
        # with open("./config/cookies.yml", 'w', encoding='utf-8') as f:
        #     yaml.dump(cookies, f, allow_unicode=True, encoding='utf-8')
        self.driver.get("https://work.weixin.qq.com/")
        # 读取yml 文件中的 cookies， 然后添加到 driver 的 cookie 中
        with open("./config/cookies.yml", 'r', encoding='utf-8')as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
