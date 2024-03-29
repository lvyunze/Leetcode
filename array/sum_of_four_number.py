# -*- coding: utf-8 -*- 
# @Author : yunze
"""
题目：四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""


class Solution():
    def fourSum(self, nums,target):
        res = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j >i+1 and nums[j] == nums[j - 1]:
                    continue
                start, end = j + 1, len(nums) - 1
                while start < end:
                    all = nums[start]+nums[end]+nums[i]+nums[j]
                    # 第一种情况
                    if all > target:
                        end -= 1
                    # 第二种情况
                    elif all < target :
                        start += 1
                    else:
                        res.append((nums[i], nums[j], nums[start], nums[end]))
                        end -= 1
                        start += 1
                        # 第三种情况
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
        return res
