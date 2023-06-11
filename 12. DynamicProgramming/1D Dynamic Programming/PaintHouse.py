"""
https://leetcode.com/problems/paint-house/

"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        dp = [0, 0, 0]
        for house in range(N):
            red = costs[house][0] + min(dp[1], dp[2])
            blue = costs[house][1] + min(dp[0], dp[2])
            green = costs[house][2] + min(dp[0], dp[1])
            dp = [red, blue, green]
        return min(dp)