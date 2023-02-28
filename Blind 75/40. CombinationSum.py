"""
https://leetcode.com/problems/combination-sum/

Approach: this is backtracking problem, we need to represent in state-space tree
For every tree we have two decisions - add the node, don't add the node.

Tc: 
Sc:
"""

def combinationSum(candidates, target):
    res = []
    def dfs(curr, total, ind):
        if total == target:
            res.append(curr.copy())
            return
        if total > target or ind >= len(candidates):
            return
        curr.append(candidates[ind])
        dfs(curr, total + candidates[ind], ind)
        curr.pop()
        dfs(curr, total, ind+1)

    dfs([], 0, 0)
    return res