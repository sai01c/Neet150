"""
https://leetcode.com/problems/combination-sum/

Approach: this is backtracking problem, we need to represent in state-space tree
For every tree we have two decisions - add the node, don't add the node.
unique elements. same number can be chosen unlimited number of times.

Tc: 2 ** len(candidates)
Sc: n + 2**n where n is for recursive call stack and 2**n is for storing in res
"""

def combinationSum(candidates, target):
    res = []
    
    def backtrack(curr, total, ind):
        if total == target: #we found the solution
            res.append(curr.copy()) #why copy? 
            #we are just using 1 variable and we continue to modify it.
            return
        #base case where we exceed the index or target
        if total > target or ind >= len(candidates):
            return
        
        #first case - add the element and do backtracking
        curr.append(candidates[ind])
        total += candidates[ind]
        backtrack(curr, total, ind) 
        #we are doing index here because we can add the same number to tree again 
        
        #second case - we don't add the element and do backtracking
        curr.pop()
        total -= candidates[ind]
        backtrack(curr, total, ind+1)

    backtrack([], 0, 0)
    return res

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        
        def backtrack(i, curr):
            if curr == target:
                res.append(sub.copy())
                return
            if curr > target:
                return
            if i >= len(nums):
                return

            for j in range(i, len(nums)):
                sub.append(nums[j])
                backtrack(j, curr+nums[j])
                sub.pop()
                
        backtrack(0, 0)
        return res
            