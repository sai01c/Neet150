"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Approach - we need first and last occurence so we do binary search twice with helper function

tc logn
sc 1
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.helper(nums, target, True)
        right = self.helper(nums, target, False)
        return [left, right] #this is still not considered for sc
    
    def helper (self, nums, target, leftBias):    
        left = 0
        right = len(nums) - 1
        res = -1
        while left<= right:
            mid = (left+right) // 2
            
            if target<nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            if nums[mid] == target:
                res = mid
                #we need to still continue doing because we have to find first and last position
                if leftBias: 
                    right = mid - 1
                else:
                    left = mid + 1
        return res