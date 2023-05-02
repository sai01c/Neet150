"""
https://leetcode.com/problems/kth-missing-positive-number/

approach: if nums[m] - m - 1 == 0 then there are no missing points so far

Tc: O(n)
Sc: O(n)
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l+r) // 2
            val = arr[m] -m -1
            if k > val:
                l = m + 1
            else:
                r = m - 1
        
        return l + k