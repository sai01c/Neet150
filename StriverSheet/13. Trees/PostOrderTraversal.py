"""
https://leetcode.com/problems/binary-tree-postorder-traversal/

approach - 

tc
sc
"""

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        stack.append(root)
        res = []
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        return res[::-1]