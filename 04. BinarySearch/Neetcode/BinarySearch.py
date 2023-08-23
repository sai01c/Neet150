"""
https://leetcode.com/problems/binary-search/

Approach: approach is to divide the number of elements into half each iteration. 
use left and right pointers
calculate mid each iteration 
and shift the pointers based on left, right, mid

Tc: O(logn)
Sc: O(1) constant 
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
        
        