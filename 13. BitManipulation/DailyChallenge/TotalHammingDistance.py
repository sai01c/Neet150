"""
https://leetcode.com/problems/total-hamming-distance/
"""

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            zero = one = 0
            mask = 1 << i
          #every time we create a mask with 1 at that digit starting from right. We can do AND to know if that particular digit in num is 1 or 0
            for num in nums:
                if mask & num: 
                    one += 1
                else: 
                    zero += 1    
            ans += one * zero        
        return ans    
