"""
https://leetcode.com/problems/rotate-array/

Approach - rotate the entire array first then two sections based on k

tc - O(n)
sc - O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) #get effective number of partitions
        #if k is more than length of array we can get only the remainder and rotate
        n = len(nums)
        self.reverse(nums, 0, n-1) #first reverse entire array first
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
        
    def reverse(self, nums, l, r):
        
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
            
        return nums
        