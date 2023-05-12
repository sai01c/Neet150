"""
https://leetcode.com/problems/path-sum-iii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        
        def dfs(root, curr):
            res = 0
            if not root:
                return 0
            curr += root.val
            remain = curr - targetSum
            res += dic[remain]
            dic[curr] += 1
            
            res += dfs(root.left, curr)
            res += dfs(root.right, curr)
            
            dic[curr] -= 1
            
            return res
        
        return dfs(root, 0)
    
        
