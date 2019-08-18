# -*- coding: utf-8 -*- 
# @Author : yunze


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
