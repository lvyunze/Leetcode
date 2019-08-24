# -*- coding: utf-8 -*- 
# @Author : yunze


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        d = collections.defaultdict(int)      # 统计入度数
        for i, j in trust:
            d[i] -= 1
            d[j] += 1
        for i in d:
            if d[i] == N-1:
                return i
        return -1
