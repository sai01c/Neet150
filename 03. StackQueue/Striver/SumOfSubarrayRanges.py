"""
https://leetcode.com/problems/sum-of-subarray-ranges/

approach

tc - n**2
sc - 1
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            mini = float(inf)
            maxi = float(-inf)
            
            for j in range(i, len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                
                res += (maxi - mini)
                
        return res