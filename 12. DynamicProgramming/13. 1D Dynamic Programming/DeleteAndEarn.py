"""
https://leetcode.com/problems/delete-and-earn/

same as house robber but slightly different 
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a, b, c = 0, 0, 0
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        for i in range(len(nums)):
            f = nums[i] * count[nums[i]]
            if i > 0 and nums[i] - nums[i-1] == 1:
                c = max(a+f, b)
                a = b 
                b = c
            else:
                c += f
                a = b
                b = c
                
        return c
                