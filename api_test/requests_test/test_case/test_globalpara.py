import json

import yaml


class TestGlobal():
    """
    类中一个方法想调另一个方法的属性（参数），两种方法：
    1、可以使用global定义参数为全局参数。
    2、可以在另一个方法中使用 方法名1().参数 调用方法1的属性值。
    """
    _params = {}

    def test_gl(self):
        # global a
        self.a = 12
        print(self.a)
        return self

    def test_gl2(self):
        # self.test_gl()
        self.b = self.test_gl().a + 2
        print(self.b)
        print(self.a)

    def test_repr(self):
        a = 12
        b = '1234'
        print(str(a),str(b))
        print(repr(a),repr(b))

    def test_replace(self, path):
        a = {"stock_name": "阿里巴巴", "xxx": "123"}
        b = "xxxxx${stock_name}xxxxx"
        for key, value in a.items():
            b = b.replace('${' + key + '}', value)
        print(b)


        with open(path, encoding='utf-8')as f:
            steps = yaml.safe_load(f)
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps  = json.loads(raw)


