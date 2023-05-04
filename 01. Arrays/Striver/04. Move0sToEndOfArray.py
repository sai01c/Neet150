"""
https://leetcode.com/problems/move-zeroes/

approach - if we see non-zero element just swap it to the left and increase left pointer by 1

tc - O(n)
sc - O(1)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0: #element is valid so swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 #increase the pointer by 1