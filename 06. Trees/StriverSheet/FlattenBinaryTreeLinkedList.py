"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


"""


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = []
        stack.append(root)
        prev = None
        
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            node.left = None
            if prev:
                prev.right = node
            prev = node