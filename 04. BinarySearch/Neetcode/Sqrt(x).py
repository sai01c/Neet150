"""
https://leetcode.com/problems/sqrtx/

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = -1
        while left <= right:
            mid = (left+right) // 2
            if (mid * mid) <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return res