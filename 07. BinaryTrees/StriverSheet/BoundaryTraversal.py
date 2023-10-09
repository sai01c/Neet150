"""
TODO
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        def leftDFS(node):
            if node:
                if not node.left and not node.right:
                    return []
                else:
                    if node.left:
                        return [node.val] + leftDFS(node.left)
                    else:
                        return [node.val] + leftDFS(node.right)
            else:
                return []
            
        def rightDFS(node):
            if node:
                if not node.left and not node.right:
                    return []
                else:
                    if node.right:
                        return rightDFS(node.right) + [node.val]
                    else:
                        return rightDFS(node.left) + [node.val]
            else:
                return []
        
        def leaves(node):
            if node:
                if not node.left and not node.right:
                    return [node.val]
                else:
                    return leaves(node.left) + leaves(node.right)
            else:
                return []
        
        return [root.val] + leftDFS(root.left) + leaves(root.left) + leaves(root.right) + rightDFS(root.right)