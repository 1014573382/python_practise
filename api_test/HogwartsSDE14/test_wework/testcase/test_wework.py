#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/12 14:08
import random
import pytest
import requests

from HogwartsSDE14.test_requests.api.util import Util
from HogwartsSDE14.test_requests.api.wework import WeWork


def test_random_data():
    """随机生成userid,mobile和name，返回结果如[('test0790', '11139395978', '云娟贵'), ('test0626', '11139394546', '周翠仁')]"""
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁"
    boyName = "伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富"
    girlName = "秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳"
    characters = "abcdefghijklmn"
    testData = [("test0" + str(random.randint(111, 999)), "1113939" + str(random.randint(1111, 9999)),
                      str(firstName[random.choice(range(len(firstName)))] + girlName[
                          random.choice(range(len(girlName)))]
                          + boyName[random.choice(range(len(boyName)))]))for i in range(2)]
    print(testData)
    return testData


class TestWework:

    def test_get(self):
        print(WeWork().test_get('GuoNian'))

    # @pytest.mark.parametrize('userid, mobile, name', [('Guoguo', '13939391001', '郭郭')])
    @pytest.mark.parametrize("userid, mobile, name", test_random_data())
    @pytest.mark.run(order=1)
    def test_create(self,userid, mobile, name):
        # print(WeWork().test_create(userid, mobile, name))
        self.result_code = WeWork().test_create(userid, mobile, name)['errcode']
        assert 0 == self.result_code

    @pytest.mark.skip()
    def test_update(self):
        self.result = WeWork().test_update('20201213aa1')['errmsg']
        assert "updated" == self.result

    @pytest.mark.run(order=2)
    def test_delete(self):
        assert "deleted" == WeWork().test_delete("test0557")['errmsg']


    # 把获取的token放在session中，就可以在发送请求时不带access_token参数
    @pytest.mark.skip()
    def test_session(self):
        s = requests.session()
        s.params = {"access_token": Util().get_token()}
        res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=20201212aa2")
        print(res.json())