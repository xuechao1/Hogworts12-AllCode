#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/31 17:39'

import yaml
import pytest


class Test_Yaml_Demo:

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("data.yaml")))
    def test_data(self, a, b):
        c = a + b
        print(c)
