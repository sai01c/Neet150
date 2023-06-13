"""
https://leetcode.com/problems/integer-break/
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(n+1):
                remain = i - j
                if remain < 0:
                    break
                dp[i] = max(dp[i], dp[j] * (remain), j * (remain))
        return dp[n]
        