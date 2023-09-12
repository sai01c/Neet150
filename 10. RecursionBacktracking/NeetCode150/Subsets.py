"""
https://leetcode.com/problems/subsets/

Approach - ths is backtracking problem, so draw a state-space tree. 
array contains unique elements so our subsets will also be unique.

Tc: n * 2**len(nums)
Sc- n * 2**len(nums)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(ind):
            if ind >= len(nums):
                res.append(subset.copy())
                return
            
            #first case - add element to our subset
            subset.append(nums[ind])
            backtrack(ind+1)

            #second case - don't add element to our subset
            subset.pop()
            backtrack(ind+1)

        backtrack(0)
        return res
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def backtrack(i):
            if len(sub) == k:
                res.append(sub.copy())
                return
            for j in range(i, len(nums)):
                sub.append(nums[j])
                backtrack(j+1)
                sub.pop()
        
        for k in range(len(nums)+1):
            backtrack(0)
        return res