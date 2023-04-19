"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

Approach - 

tc
sc
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = l + ((r-l) // 2)
            if (
                (m - 1 < 0 or nums[m] != nums[m-1]) 
                and
                (m+1 == len(nums) or nums[m] != nums[m+1])
                ):
                return nums[m]
            
            if nums[m] == nums[m-1]:
                leftSize = m-1
            else:
                leftSize = m
            
            if leftSize % 2 == 0:
                l = m + 1
            else:
                r = m - 1
            
            
            