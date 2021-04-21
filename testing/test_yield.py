# -*- coding: utf-8 -*-
# @Time : 2021/4/20 11:30
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_yield.py
# @Software: PyCharm

# yield 生成器

def fun():
    for i in range(3):
        print(f"i = {i}")
        yield  # return  同时相当于暂停并且记住 上一次的执行位置


f = fun()
next(f)
next(f)
next(f)
