"""
https://leetcode.com/problems/continuous-subarrays/
"""


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(nums)):
            dic[nums[r]] += 1
            while max(dic) - min(dic) > 2:
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1
            res += ( r - l + 1) #this is the imp part. we are not looking for maximum but adding all subarrays
        
        return res