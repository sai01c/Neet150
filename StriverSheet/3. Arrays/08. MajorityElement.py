"""
https://leetcode.com/problems/majority-element/

Approach - this is very tricky algorithm. learn this algorithm

tc - 
sc - 

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0
        for num in nums:
            if count == 0:
                element = num
                count += 1
            
            elif element == num:
                count += 1
            
            else:
                count -= 1
                
        count = 0
        for num in nums:
            if num == element:
                count += 1
        
        if (count > len(nums)//2):
            return element
        else:
            return -1