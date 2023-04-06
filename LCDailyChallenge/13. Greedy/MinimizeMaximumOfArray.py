"""
https://leetcode.com/problems/minimize-maximum-of-array/

Approach - this is very tricky problem. 
we can do our operations from 1st index that means 0th index element can only increase.
it can't be decreased. so in the worst case also our maximum will be 0th index element
so we iterate from 1st index element and we will find the average because if we increase 
element by 1 and decrease element by 1 - average will remain same. 

Tc - O(n)
Sc - O(1)
"""

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        #worst case - it won't go below this
        #we only increase this 
        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            temp = math.ceil(total / (i+1)) 
            #i+1 because we added 0th index element to our total
            #ceiling because we wanted maximum of the array
            res = max(res, temp)
            
        return res