"""
https://leetcode.com/problems/min-cost-climbing-stairs/

tc - n
sc - 1

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = 0
        for num in cost:
            c = min(a+num, b+num)
            a = b
            b = c
        return min(a, b)