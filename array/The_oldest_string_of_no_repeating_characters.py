# -*- coding: utf-8 -*- 
# @Author : yunze


# str = 'abcdeeeeee'
# a = []
# for i in str:
#     if i not in a:
#        a.append(i)
# print(a)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        st = ''
        num = []
        for i in range(len(s)):
            if s[i] not in st:
                st += s[i]
                num.append(len(st))
                print(num)
            else:
                st = st[st.find(s[i]) + 1:] + s[i]
        return max(num)


a = Solution()
print(a.lengthOfLongestSubstring('abcabc'))

# str = "abcdeab"
# s = ""
# b = []
# for i in range(len(str)):
#     if str[i] not in s:
#         s+=str[i]
#         b.append(len(s))
#         print(b)
