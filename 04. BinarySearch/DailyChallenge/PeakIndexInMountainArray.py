"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/

"""

class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m
        
        
            
