# -*- coding: utf-8 -*- 
# @Author : yunze
"""
题目：买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # 取第一个数
        min_p = prices[0]
        # 第一初始最大值为0
        Max = 0
        for i in range(len(prices)):
            # 遍历到较小值
            min_p = min(min_p, prices[i])
            # 求最大差值，这样就算是上面的min_p的最小值是最后一个，Max也是会取最大差值
            Max = max(Max, prices[i] - min_p)
        return Max

