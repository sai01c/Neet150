"""
https://leetcode.com/problems/4sum/

Approach - this is extension of three sum. have four pointers and pattern is same

tc O(n^3)
sc - 
The space complexity of the fourSum function is O(1), which means that the amount of memory used by the function does not depend on the size of the input array nums.

The function uses only a fixed amount of extra space to store the result list res and a few integer variables for the loop indices and pointers.

The sorting step at the beginning of the function does not require any extra space beyond what is already used by the input array.

Therefore, the overall space complexity of the function is constant, and does not grow with the size of the input array.
"""

class Solution:
    def fourSum(self, nums, target):
        nums.sort() 
        res = []
        n = len(nums)
        
        # Iterate over all possible first indices i.
        for i in range(n - 3): 
            # Skip duplicates to avoid redundant computations.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Iterate over all possible second indices j.
            for j in range(i + 1, n - 2):
                # Skip duplicates to avoid redundant computations.
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                l, r = j + 1, n - 1 
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        # Move the left pointer to the next unique element.
                        l += 1 
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                            
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        
        return res
