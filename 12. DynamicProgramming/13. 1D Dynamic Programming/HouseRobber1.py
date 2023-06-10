"""
https://leetcode.com/problems/house-robber/

Approach: we can't rob adjacent houses. let us say nums is [1,2,3,4].
Now imagine this0,that0,this1,that2,3,4 - we can rob first either this(1+0) or that 0
new iteration we can rob that (2+0) or 1
next iteration we can rob (3+1) or 2

Tc: O(n)
Sc: O(1)
"""
class HouseRobber():
    def houseRobber1(self, nums):
        a = 0
        b = 0
        for num in nums:
            c = max(c, a+b)
            a = b
            b = c
        return c

        
