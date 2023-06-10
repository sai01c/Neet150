"""
https://leetcode.com/problems/house-robber-ii/

Approach: this is similar to house robber but circular. 
so we can either take 0 to n-2 or 1 to n-1 to avoid adjacency. nice cool trick

Tc: O(n)
Sc: O(n)

"""

class Solution():
    def houseRobber2(self, nums):
        return max(
            nums[0], 
            self.houseRobber1(nums[0:len(nums)-1]), 
            self.houseRobber1(nums[1:])
        )
    
    def houseRobber1(self, nums):
        a = 0
        b = 0
        curr = 0 #define curr first because if input is [0] for loop won't be executed
        for num in nums:
            c = max(c, a+b)
            a = b
            b = c
        return c



 