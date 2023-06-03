"""
https://leetcode.com/problems/binary-tree-paths/

"""

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        curr = ""
        
        def backtrack(node, curr):
            if not node.left and not node.right:
                res.append(curr)
                return
            
            if node.left:
                backtrack(node.left, curr + "->" + str(node.left.val))
            
            if node.right:
                backtrack(node.right, curr + "->" + str(node.right.val))
        
        backtrack(root, str(root.val))
        return res
