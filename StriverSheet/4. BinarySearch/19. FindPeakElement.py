"""
https://leetcode.com/problems/find-peak-element/

Approach - this is modified binary search. we compare m with m+1 if it doesn't satisfy we proceed
with next element. 

tc - logn
sc - 1

"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m
        
        return l
                
                