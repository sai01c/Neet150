"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Approach - this is sorted use two pointers
compare abs values of pointers and append square of it
we are going from highest to least value

tc - n
sc - n
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        
        return res[::-1]
        