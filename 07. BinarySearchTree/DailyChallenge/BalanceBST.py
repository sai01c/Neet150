"""
https://leetcode.com/problems/balance-a-binary-search-tree/

given is a BST so inorder will give sorted order
now create a new BST with this sorted order put root at middle so we can have balance BST
"""

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        
        def create(nums):
            if not nums:
                return
            
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = create(nums[:mid])
            root.right = create(nums[mid+1:])
            
            return root
        
        inorder(root)

        return create(nums)
