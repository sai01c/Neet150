"""
https://leetcode.com/problems/longest-increasing-subsequence/

Approach: we are going in reverse direction, we initiate the dp
array with 1 because each one is itself subsequence. 
for every number we add another for loop and check every number
if the number is greater then we take the max of itself and 1+ that number

Tc: O(n^2)
Sc: O(n)

follow - up: nlogn using binary search
even Neetcode said it is next level

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1+dp[i])
        return max(dp)