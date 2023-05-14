"""
https://leetcode.com/problems/convert-bst-to-greater-tree/

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []
        def inorder(root):
            total = 0
            if not root:
                return 0
            total += inorder(root.left)
            nums.append(root)
            total += root.val
            total += inorder(root.right)
            
            return total
            
        total = inorder(root)
        prefix = 0
        for node in nums:
            temp = node.val
            node.val = total - prefix
            prefix += temp
            
        
        return root
        
        
