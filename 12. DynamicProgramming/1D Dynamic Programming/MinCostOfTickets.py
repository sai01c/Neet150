"""
https://leetcode.com/problems/minimum-cost-for-tickets/

"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = max(days)
        dp = [0] * (N+1)
        dayset = set(days)
        for i in range(N+1):
            if i not in dayset:
                dp[i] = dp[i-1]
            else:
                one = dp[max(0, i-1)] + costs[0]
                seven = dp[max(0, i-7)] + costs[1]
                thirty = dp[max(0, i-30)] + costs[2]
                dp[i] = min(one, seven, thirty)
        
        return dp[N]