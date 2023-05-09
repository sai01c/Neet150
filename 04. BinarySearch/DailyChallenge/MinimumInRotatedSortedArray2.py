"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            
            while l < r and nums[r] == nums[r-1]:
                r -= 1
                
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
