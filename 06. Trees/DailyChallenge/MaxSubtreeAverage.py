"""
https://leetcode.com/problems/maximum-average-subtree/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        def dfs(node):
            if not node:
                return [0, 0]
            total , count = node.val, 1
            a, b = dfs(node.left)
            total += a
            count += b
            a, b = dfs(node.right)
            total += a
            count += b
            self.ans = max(self.ans, total/count)
            return [total, count]
        
        self.ans = 0
        dfs(root)
        return self.ans