"""
https://leetcode.com/problems/next-permutation/

Approach - first check where the array in not decreasing then reverse and find 
the smallest number among the reversed numbers and swap them to find the next
permutation.

tc - O(n)
sc - O(1)

"""

class Solution:
    # A function to swap two elements in a list
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]
        
    # A function to reverse a section of a list
    def reverse(self, nums, left, right):
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1
    
    # A function to generate the next lexicographically greater permutation of a list
    def nextPermutation(self, nums):
        # Find the index of the first element that is less than its next element from the right
        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec+1]:
            dec -= 1
        
        # Reverse the section of the list to the right of the found index
        self.reverse(nums, dec+1, len(nums)-1)
        
        # If the list is already in decreasing order, return it
        if dec == -1:
            return nums
        
        # Find the smallest element in the reversed section that is greater than the found index
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        
        # Swap the found index with the smallest greater element in the reversed section
        self.swap(nums, dec, next_num)
        
        # Return the modified list
        return nums
