"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(nums)):
            dic[nums[r]] += 1
            while dic[0] > 1:
                dic[nums[l]] -= 1
                l += 1
            if dic[0] == 1:
                ans = max(ans, dic[1])
            else:
                ans = max(ans, dic[1] - 1)
        return ans
