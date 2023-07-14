"""
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 1
        for a in arr:
            prev = dp.get(a - difference, 0)
            dp[a] = 1 + prev
            res = max(res, dp[a])
        
        return res