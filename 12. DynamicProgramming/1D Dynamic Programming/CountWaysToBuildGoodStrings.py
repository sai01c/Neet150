"""
https://leetcode.com/problems/count-ways-to-build-good-strings/
"""

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        res = 0
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range((high)+1):
            remain = i - zero
            if remain >= 0:
                dp[i] += dp[remain]
                
            remain = i - one
            if remain >= 0:
                dp[i] += dp[remain]
                
        for i in range(len(dp)):
            if i >= low and i<= high:
                res += dp[i]
        mod = 10**9 + 7
        return res % mod