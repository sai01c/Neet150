"""
https://leetcode.com/problems/split-array-largest-sum/

Approach - this is similar to capacity to ship in D days question
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums) #because sum of subarrays can't go below this
        r = sum(nums) #sum of subarrays can't go above this
        
        while l <= r:
            m = (l + r) // 2
            currSum = 0
            subs = 1
            for n in nums:
                currSum += n
                if currSum > m:
                    currSum = n
                    subs += 1
            
            if subs > k:
                l = m + 1
            else:
                ans = m
                r = m - 1
        
        return ans
        
        