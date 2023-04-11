"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Approach - write this on paper to understand
we maintain an index j to insert elements
we maintain prev element to check if we got new element

Tc - O(n)
Sc - O(n)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        prev = -101 #based on question constraints
        for i in range(len(nums)):
            if nums[i] != prev: #that means we got a new element
                nums[j] = nums[i] #put this element in jth index
                prev = nums[j] #prev will be this new element
                j += 1 #increase j by 1
                
            
        return j
        
        