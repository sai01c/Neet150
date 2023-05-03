"""
https://leetcode.com/problems/count-number-of-nice-subarrays/

Approach - 

tc
sc
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        odd = 0
        ans = 0
        for r in range(len(nums)):
            #if you find new odd then count will be 0
            if nums[r] % 2 != 0:
                odd += 1
                count = 0
            
            while odd == k:
                if nums[l] % 2 != 0:
                    odd -= 1
                l += 1
                count += 1
            #until you see new odd number, keep adding count to final ans
            ans += count
        return ans