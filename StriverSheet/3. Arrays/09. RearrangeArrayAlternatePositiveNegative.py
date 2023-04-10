"""
https://leetcode.com/problems/rearrange-array-elements-by-sign/

Approach

tc
sc
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        p = 0
        n = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(pos[p])
                p += 1
            else:
                res.append(neg[n])
                n += 1
        
        return res