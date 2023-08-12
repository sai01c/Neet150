"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        pre = 0
        res = 0
        for r in range(len(arr)):
            pre += arr[r]
            length = r - l + 1
            avg = pre / length
            if length == k: 
                if avg >= threshold:
                    res += 1
                pre -= arr[l]
                l += 1
        return res
                