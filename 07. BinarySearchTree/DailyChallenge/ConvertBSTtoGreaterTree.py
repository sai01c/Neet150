"""
https://leetcode.com/problems/convert-bst-to-greater-tree/

"""

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
        
        
