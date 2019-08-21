# -*- coding: utf-8 -*- 
# @Author : yunze
"""
题目：最短路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 获取行
        m = len(grid)
        # 获取列
        n = len(grid[0])
        # 建立多少维数组,m行n列
        res = [[0]*n]*m
        # 循环行
        for i in range(m):
            # 循环列
            for j in range(n):
                if 0 <= i-1 < m and 0 <= j-1 < n:
                    res[i][j] = min(res[i][j-1],res[i-1][j])+grid[i][j]
                # 第一行中,第一个除外
                elif 0 <= i-1 < m:
                    res[i][j] = res[i-1][j] + grid[i][j]
                # 第一列中，第一个除外
                #
                elif 0 <= j-1 < n:
                    res[i][j] = res[i][j-1] + grid[i][j]
                else:
                    res[i][j] = grid[i][j]
        return res[m-1][n-1]
