"""
https://leetcode.com/problems/contains-duplicate-ii/

another example of where we need all the pair in n^2 solution 
but using dic we can do it in n
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                j = dic[nums[i]]
                if abs(i-j) <= k:
                    return True
            dic[nums[i]] = i
        return False