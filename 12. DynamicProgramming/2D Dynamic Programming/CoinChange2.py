"""
https://leetcode.com/problems/coin-change-ii/

"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for c in coins:
            for a in range(c, amount+1):
                remain = a - c
                dp[a] = dp[a] + dp[remain]
        return dp[amount]