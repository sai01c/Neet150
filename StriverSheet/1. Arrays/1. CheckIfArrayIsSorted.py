"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

"""

class Solution:
    def check(self, nums: List[int]) -> bool:
    
        k = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                k = i
                break

        self.reverse(nums, 0, k)
        self.reverse(nums, k+1, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)

        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
    
    def reverse(self, nums, l ,r):
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
            
        return nums
            