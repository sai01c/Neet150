"""
https://leetcode.com/problems/coin-change/
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                remain = a-c
                if remain >= 0:
                    dp[a] = min(dp[a], 1+dp[remain])
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1