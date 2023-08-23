"""
https://leetcode.com/problems/arranging-coins/
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l+r) // 2
            total = (m * (m+1))/2
            if total == n:
                return m
            elif total > n:
                r = m - 1
            else:
                ans = m
                l = m + 1
        return ans