"""
https://leetcode.com/problems/two-sum-bsts/


"""

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def search(root, target):
            if not root:
                return False
            curr = root
            while curr:
                if curr.val == target:
                    return True
                elif target < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right
            return False
            
        if not root1:
            return False
        curr = root1
        remain = target - curr.val
        if search(root2, remain):
            return True
        return (self.twoSumBSTs(root1.left, root2, target) or
    self.twoSumBSTs(root1.right, root2, target))
            