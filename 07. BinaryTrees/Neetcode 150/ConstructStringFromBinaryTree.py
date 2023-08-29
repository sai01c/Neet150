"""
https://leetcode.com/problems/construct-string-from-binary-tree/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root, parent):
            nonlocal res
            if not root:
                if parent.right:
                    res.append('()')
                return
            res.append('(')
            res.append(str(root.val))
            preorder(root.left, root)
            preorder(root.right, root)
            res.append(')')
        
        preorder(root, root)
        return "".join(res[1:-1])