"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Approach - try to find a point where the array is not strictly increasing 
then apply reverse function here 
after reversing the point check for stricly increasing condition again if we found anything
then false. if not true 

tc O(n)
sc O(1)

"""

class Solution:
    def check(self, nums: List[int]) -> bool:
    
        k = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                k = i #try to apply reverse function at this point. 
                break 

        self.reverse(nums, 0, k)
        self.reverse(nums, k+1, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)

        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: #they are not sorted
                return False
        return True #if sorted then true
    
    def reverse(self, nums, l ,r): #generic reverse function
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
            
        return nums
            