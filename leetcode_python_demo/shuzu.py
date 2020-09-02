#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/1 21:52'

from typing import List

"""
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
"""


class Solution_old:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums
