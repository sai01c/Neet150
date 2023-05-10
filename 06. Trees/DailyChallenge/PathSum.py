"""
https://leetcode.com/problems/path-sum/

"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        q = collections.deque()
        q.append((root, root.val))
        
        while q:
            for i in range(len(q)):
                node, val = q.popleft()
                if node:
                    if not node.left and not node.right and val == targetSum:
                        return True
                    if node.left:
                        q.append((node.left, val + node.left.val))
                    if node.right:
                        q.append((node.right, val + node.right.val))
            
        return False
                    
