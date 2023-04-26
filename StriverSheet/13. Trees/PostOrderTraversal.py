"""
https://leetcode.com/problems/binary-tree-postorder-traversal/

approach - use general stacka and add left and right subtrees. reverse the res at the end.

tc - n
sc - n
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