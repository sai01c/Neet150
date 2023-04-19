"""
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Approach - 

tc - 
sc - 

"""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        
        while l <= r:
            m = (l+r) // 2
            temp = 0
            for num in nums:
                temp += ((num-1) // m) + 1
                
            if temp > threshold:
                l = m + 1
            else:
                ans = m
                r = m - 1
                
        return ans