"""
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

tc - n! or n**n 
sc

"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = []
        sub = []
        def backtrack(i):
            if i >= len(s):
                res.append(len(sub.copy()))
                return
            for j in range(i, len(s)):
                if s[i:j+1] not in sub:
                    sub.append(s[i:j+1])
                    backtrack(j+1)
                    sub.pop()
        backtrack(0)
        return max(res)
