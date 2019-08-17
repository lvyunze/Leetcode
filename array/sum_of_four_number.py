# -*- coding: utf-8 -*- 
# @Author : yunze

# 第一次上传


class Solution():
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i, len(nums) - 2):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                target = 0 - nums[i] - nums[j]
                start, end = i + 1, len(nums) - 1
                while start < end:
                    # 第一种情况
                    if nums[start] + nums[end] > target:
                        end -= 1
                    # 第二种情况
                    elif nums[start] + nums[end] < target:
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
