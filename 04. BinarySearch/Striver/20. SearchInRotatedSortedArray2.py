"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Approach - same approach as variation 1 but here we might have duplicates so during the initial
phase where we find the least element shift the pointers if you have duplicate elements.

tc - logn
sc - 1
"""

class Solution:
    def search(self, nums, target) -> bool:
        l = 0
        r = len(nums) - 1
        
        #find the least element 
        while l < r:
            #add extra condition's when we have duplicate's
            #when we have left and right duplicate's

            #this while loop only executes when there is a duplicate value
            #so this doesn't count for tc
            while l < r and nums[l] == nums[l+1]:
                l += 1
                
            while l < r and nums[r] == nums[r-1]:
                r -= 1
                
            m = (l + r) // 2
            if nums[m] > nums[r]:   
                l = m + 1
            else:
                r = m
        
        #shift the pointers
        least = l
        l = 0
        r = len(nums) - 1

        if target >= nums[least] and target <= nums[r]:
            l = least
            r = len(nums) - 1
        else:
            l = 0
            r = least
        
        #do regular binary search
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
                
        return False
            
            