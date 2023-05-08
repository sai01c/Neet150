"""
https://leetcode.com/problems/kth-missing-positive-number/

"""

class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l+r) // 2
            missing = nums[m] - m - 1
            if missing > k:
                r = m - 1
            elif missing < k:
                l = m + 1
        
        return l + k

    