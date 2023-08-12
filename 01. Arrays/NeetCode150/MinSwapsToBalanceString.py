"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        close = 0
        for i in range(len(s)):
            if s[i] == "[":
                close -= 1
            else:
                close += 1
            res = max(res, close)
        return math.ceil(res/2)
