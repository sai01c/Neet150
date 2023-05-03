"""
https://leetcode.com/problems/binary-subarrays-with-sum/

Approach - this is similar to subarray sum equal to k
we store the prefix sum and its count in a dic

tc
sc

"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        dic = defaultdict(int)
        res = 0
        prefix = 0
        dic[prefix] = 1
        for r in range(len(nums)):
            prefix += nums[r]
            diff = prefix - goal
            res += dic[diff]
            dic[prefix] += 1
        
        return res