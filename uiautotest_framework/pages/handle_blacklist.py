import logging

import allure
from selenium.webdriver.common.by import By


def handle_blacklist(func):
    logging.basicConfig(level=logging.INFO)
    """对黑名单元素进行处理的装饰器"""
    # _blacklist = [
    #     (By.ID, "tv_skip"),  # 首页的广告弹框
    #     (By.ID, "iv_action_back")  # 跳转到登录页后点击叉叉关掉
    # ]
    # _max_err_num = 3
    # _error_num = 0
    def wrapper(*args, **kwargs):
        # 通过 *args, **kwargs 接收find() 中的参数并传给func()
        from pages.base_page import BasePage
        # 指定instance 为传入的第一个参数，实际就是find() 传过来的self
        instance: BasePage = args[0]
        try:
            # 调用传入的方法，其实就是find(), 如果元素找到，就清空 error 计数
            element = func(*args, **kwargs)
            _error_num = 0
            instance.set_implicitly_wait(3)
            return element
        except Exception as e:
            # 发生异常后截图 并把截图保存到allure报告中，然后打印日志
            instance.screenshot("../screenshot/error.png")
            with open("../screenshot/error.png", 'rb')as f:
                content = f.read()
            allure.attach(content, "弹框截图", attachment_type=allure.attachment_type.PNG)
            logging.error("element not found, handle blacklist")
            instance.set_implicitly_wait(2)
            # 如果元素没找到，就进行黑名单处理
            if instance._error_num > instance._max_err_num:
                # 如果error 次数大于指定数，就重置 error 次数并抛出异常
                instance._error_num = 0
                raise e
            instance._error_num += 1
            for ele in instance._blacklist:
                # 对黑名单中的元素进行点击
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名单中")
    return wrapper