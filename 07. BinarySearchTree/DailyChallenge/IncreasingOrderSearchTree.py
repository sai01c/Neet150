"""
https://leetcode.com/problems/increasing-order-search-tree/

"""


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        
        inorder(root)
        dummy = TreeNode()
        prev = dummy
        
        for i in range(0, len(nums), 2):
            first = TreeNode(nums[i])
            if i + 1 < len(nums):
                second = TreeNode(nums[i+1])
            else:
                second = TreeNode()
            
            prev.right = first
            if i == len(nums) - 1: return dummy.right
            
            first.right = second
            prev = second
            
        return dummy.right
            
            
            