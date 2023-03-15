"""
https://leetcode.com/problems/subtree-of-another-tree/

APPROACH: 
use the same tree function and apply it to s and t. 
if it satisfies with left or right, then it can be true

Tc: O(n) traverse every node once. 
Sc: O(n) stack recursion
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False
        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t: #slight modification from prev same tree
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False
