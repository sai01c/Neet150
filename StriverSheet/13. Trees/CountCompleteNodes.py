"""
https://leetcode.com/problems/count-complete-tree-nodes/

"""

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def leftHeight(node):
            ans = 0
            while node:
                ans += 1
                node = node.left
            return ans
        
        def rightHeight(node):
            ans = 0
            while node:
                ans += 1
                node = node.right
            return ans
        
        if not root:
            return 0
        
        l = leftHeight(root.left)
        r = rightHeight(root.right)
        
        if l == r:
            ans = (2 ** (l+1))- 1
            return ans
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        