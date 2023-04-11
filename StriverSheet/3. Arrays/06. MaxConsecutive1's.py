"""
https://leetcode.com/problems/max-consecutive-ones/

Approach - iterate through the elements and increase counter by 1 if you see 1 else make it 0

tc - O(n)
sc - O(1)

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == 1: 
                count += 1 #increment counter by 1 because we had 0
                ans = max(count, ans) #get the maximum of count and ans
            else:
                count = 0 #initiate count to zero
        
        return ans