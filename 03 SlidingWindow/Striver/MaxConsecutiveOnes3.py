"""
https://leetcode.com/problems/max-consecutive-ones-iii/

Approach - subarray problem so sliding window. this is similar to character replacement
if we see 1 increase the count by 1. so here the condition is 
length of subarray - count of ones should not exceed k if it is then we increase the left
by 1.


tc
sc
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
                
            length = r - l + 1
            if length - count > k:
                if nums[l] == 1:
                    count -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        