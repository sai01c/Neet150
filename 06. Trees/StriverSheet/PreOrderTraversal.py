"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

approach - have stack and insert right first and left second so we can pop left first

tc - n
sc - n
"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return ans
        