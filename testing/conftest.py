# -*- coding: utf-8 -*-
# @Time : 2021/4/20 16:38
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : conftest.py
# @Software: PyCharm

# 数据共享文件，公共模块放在这个文件下

import pytest


@pytest.fixture(autouse=True, params=['user1', 'user2', 'user3'])  # scope执行域的大小（session，module，function）
# session整个项目只执行一次，module每个模块也就是每个.py文件，执行一次
def login(request):
    print("登录方法")
    print(request.param)
    # yield激活 fixture teardown方法
    yield ['username', 'password']
    print('teardown')
