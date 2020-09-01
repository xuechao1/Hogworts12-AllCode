#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试文件
import sys

import pytest
import yaml

print(sys.path.append('..'))
from pythoncode.calc import Calculator


# 模块级别
# def setup_module():
#     print("模块级别setup")
#
#
# def teardown_module():
#     print("模块级别teardown")


# 函数级别 类外面的使用def 定义的叫做函数，
# 在类里面使用def 定义的叫方法
# def setup_function():
#     print("函数级别 setup")
#
#
# def teardown_function():
#     print("函数级别 teardown")


def test_case1():
    print("testcase1")


with open("datas/calc.yml") as f:
    datas = yaml.safe_load(f)
    addids = datas['add'].keys()
    adddatas = datas['add'].values()

    divids = datas['div'].keys()
    divdatas = datas['div'].values()


def get_steps():
    with open('steps/add.yml') as f:
        steps = yaml.safe_load(f)
    return steps


cal = Calculator()


def steps(a, b, result):
    steps1 = get_steps()
    for step in steps1:
        if 'add' == step:
            assert result == cal.add(a, b)
        elif 'add1' == step:
            assert result == cal.add1(a, b)
        elif 'add2' == step:
            assert result == cal.add2(a, b)


class TestCalc:
    # setup_class， teardown_class每个类里面 执行前后分别 执行
    def setup_class(self):
        self.cal = Calculator()
        print("类级别 setup")

    def teardown_class(self):
        print("类级别 teardown")

    # 函数级别 每条类里面的测试用例前和后分别 执行setup teardown
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.parametrize('a, b, result', adddatas
        , ids=addids)
    # @pytest.mark.add
    def test_add(self, a, b, result):
        steps(a, b, result)
        # cal = Calculator()
        # assert result == self.cal.add(a, b)
        # assert result == self.cal.add1(a, b)
        # assert result == self.cal.add2(a, b)

    # @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(1, 2)

    # @pytest.mark.div
    @pytest.mark.parametrize('a,b,c', divdatas, ids=divids)
    def test_div(self, a, b, c):
        # cal = Calculator()
        print("登录操作111")
        assert c == self.cal.div(a, b)
        print("登录操作222")
        assert 1 == self.cal.div(2, 1)
        print("登录操作333")
        assert 1 == self.cal.div(2, 1)

    def test_assume(self):
        print("登录操作")
        pytest.assume(1 == 2)
        print("搜索操作")
        pytest.assume(2 == 2)
        print("加购操作")
        pytest.assume(3 == 2)
