"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/


"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        nums = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root)
            inorder(root.right)
        inorder(root)
        
        for i in range(len(nums)):
            j = i+1
            if i+1 >= len(nums):
                j = 0
            nums[i].right = nums[j]
            nums[j].left = nums[i]
        
        return nums[0]