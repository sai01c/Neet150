"""
https://leetcode.com/problems/subsets/

Approach - ths is backtracking problem, so draw a state-space tree. 
array contains unique elements so our subsets will also be unique.

Tc: (2^ len(nums)) * n 
Sc- 
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