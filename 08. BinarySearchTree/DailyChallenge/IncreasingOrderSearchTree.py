"""
https://leetcode.com/problems/increasing-order-search-tree/

"""

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return
        nums = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root)
        curr = TreeNode()
        prev = curr
        for i in range(len(nums)):
            node = TreeNode(nums[i])
            curr.right = node
            curr = curr.right
        
        return prev.right