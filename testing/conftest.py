# -*- coding: utf-8 -*-
# @Time : 2021/4/20 16:38
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : conftest.py
# @Software: PyCharm

import pytest


@pytest.fixture()
def login():
    print("登录方法")
    # yield激活 fixture teardown方法
    yield ['username', 'password']
    print('teardown')
