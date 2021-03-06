# -*- coding: utf-8 -*-
# @Time : 2021/4/16 15:05
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_calc.py
# @Software: PyCharm

# 测试文件
import pytest

from pythoncode.calc import Calculator


# 模块级别
def setup_module():
    print("模块级别 setup")


def teardown_module():
    print("模块级别 teardown")


# 方法级别 类外面使用def 定义的叫做函数，在类里面使用def 定义的叫方法
def setup_function():
    print("函数级别 setup")


def teardown_function():
    print("函数级别 teardown")


def testcase1():
    print("testcase1")


class TestCalc:
    # 类级别 setup_class和teardown_class分别在每个类的前后分别执行
    def setup_class(self):
        self.cal = Calculator()
        print("类级别 setup")

    def teardown_class(self):
        print("类级别 teardown")

    # 函数级别
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 2),
        (2, 3, 5),
        (2, 2, 4),
        (100, 100, 200),
        (0.1, 0.1, 0.2),
        (-1, -1, -2)
    ],
                             ids=['int1',
                                  'int2',
                                  'int3',
                                  'bignum',
                                  'float',
                                  'negative'
                                  ]
                             )
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.div
    def test_div(self):
        # guo = Calculator()
        assert 2 == self.cal.div(6, 3)

    @pytest.mark.div
    def test_div1(self):
        # guo = Calculator()
        assert 50 == self.cal.div(100, 2)
