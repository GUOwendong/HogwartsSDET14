# -*- coding: utf-8 -*-
# @Time : 2021/4/23 19:02
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_cart.py
# @Software: PyCharm
import pytest


def test_cart1(login):
    print("购物车测试1")


def test_cart2(login):
    print("购物车用力2")


@pytest.mark.parametrize('a,b', [
    (1, 2),
    (3, 4)
])
def test_cart3(a, b):
    print("购物车用例3")
