#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/1 22:14'

from typing import List

"""
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# 方法一：双重循环暴力解。
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        for index, item in enumerate(nums):
            for count in range(index + 1, len(nums)):
                if item + nums[count] == target:
                    return [index, count]


# 第二种思路：
# 用hashmap记录之前出现的数字及下标，key是数字，val是下标。

# class Solution2(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashmap = {}
#         for index, item in enumerate(nums):
#             if hashmap.has_key(target - item):
#                 return hashmap[target - item], index
#             hashmap[item] = index

# 优化方法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, item in enumerate(nums):
            if target - item in hashmap:
                return hashmap[target - item], index
            hashmap[item] = index
