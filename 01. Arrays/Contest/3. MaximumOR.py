"""
https://leetcode.com/problems/maximum-or/

Approach - this is prefix and suffix problem. for every number we have to calculate prefix and
suffic OR. now iterate through the array multiply ith element by k times and do OR with prefix and suffix

TODO

prefix sum is very important pattern. Do this problem again
"""

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        prefix = []
        suffix = []
        curr = 0
        for i in range(len(nums)):
            curr = nums[i] | curr 
            prefix.append(curr)
        
        curr = 0 
        for i in range(len(nums)-1, -1, -1):
            curr = nums[i] | curr
            suffix.append(curr)
        
        suffix = suffix[::-1]
        res = 0
        for i in range(len(nums)):
            j = 0
            temp = nums[i]
            while j < k:
                temp *= 2
                j += 1
            
            if (i - 1 >= 0 and i + 1 < len(nums)):
                val = prefix[i-1] | temp | suffix[i+1]
            
            elif (i - 1 < 0 and i + 1 >= len(nums)):
                val = temp
            
            elif i-1 < 0:
                val = 0 | temp | suffix[i+1]
            
            else:
                val = prefix[i-1] | temp | 0
            
            res = max(res, val)
        
        return res
            
        