"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        res = 0
        for num in nums:
            remain = k - num
            if dic[remain] > 0:
                res += 1
                dic[remain] -= 1
            else:
                dic[num] += 1        
        return res
