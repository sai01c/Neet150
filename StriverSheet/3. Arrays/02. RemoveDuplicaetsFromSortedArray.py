"""

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        prev = -101
        for i in range(len(nums)):
            if nums[i] != prev:
                nums[j] = nums[i]
                prev = nums[j]
                j += 1
                
            
        return j
        
        