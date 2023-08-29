"""
https://leetcode.com/problems/largest-bst-subtree/

"""

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            count = 0
            if not root:
                return 0
            count += 1
            count += dfs(root.left)
            count += dfs(root.right)
            
            return count
            
        def validate(root, l, r):
            if not root:
                return True
            if not (root.val > l and root.val < r):
                return False
            return validate(root.left, l, root.val) and validate(root.right, root.val, r)
            
        ans = 0
        if not root:
            return ans
        if validate(root, float('-inf'), float('inf')):
            ans = max(ans, dfs(root))
        
        ans = max(ans, self.largestBSTSubtree(root.left))
        ans = max(ans, self.largestBSTSubtree(root.right))
            
        return ans