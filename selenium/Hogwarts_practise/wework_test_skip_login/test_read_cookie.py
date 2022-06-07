
def test_read_cookie():
    # cookies 中包含两个列表，读的时候一个列表 一个列表的读
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '-OccjvZ2yr7RbAiw5vf-A8h'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}]
    for cookie in cookies:
        a = cookie
        print("a = ", a)