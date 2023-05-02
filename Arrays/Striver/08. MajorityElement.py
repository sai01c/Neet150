"""
https://leetcode.com/problems/majority-element/

Approach - this is very tricky algorithm. learn this algorithm Boyer-Moore Algorithm.

tc - O(N)
sc - O(1)

TODO
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                res = num
                count += 1
            
            elif res == num:
                count += 1
            
            else:
                count -= 1
     
        return res