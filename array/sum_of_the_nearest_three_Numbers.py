# -*- coding: utf-8 -*- 
# @Author : yunze

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = float("inf")
        # float("inf")代表正无穷，float("-inf")代表负无穷
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, len(nums) - 1

            while start < end:
                cur = nums[start] + nums[i] + nums[end]
                if cur == target: return target
                # (正无穷-目标)的绝对值>(和-目标)绝对值-----关键点
                if abs(res - target) > abs(cur - target):
                    res = cur
                if cur < target:
                    start += 1
                elif cur > target:
                    end -= 1
        return res
