"""
https://leetcode.com/problems/symmetric-tree/

Approach - use same tree concept but exchange the left and right trees

tc - n visiting every node once
sc - n recursive stack
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return helper(p.left, q.right) and helper(p.right, q.left)
        
        return helper(root.left, root.right)
