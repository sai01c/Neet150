"""
https://leetcode.com/problems/perfect-squares/
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for target in range(1, n+1):
            for square in range(1, target+1):
                square = square * square
                remain = target - square
                if (remain) < 0:
                    break
                dp[target] = min(dp[target], 1+dp[remain])
        return dp[n]