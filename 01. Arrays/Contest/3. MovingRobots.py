"""
https://leetcode.com/problems/movement-of-robots/

did not understand why we just take 'd' instead of considering collisions
"""

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10**9 + 7
        for i in range(len(nums)):
            if s[i] == "L":
                nums[i] = nums[i] - d
            else:
                nums[i] = nums[i] + d
        
        nums.sort()
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            ans += (i * nums[i]) - prefix
            prefix += nums[i]
        return ans % mod
 