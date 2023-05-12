"""
https://leetcode.com/problems/path-sum-ii/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return None
        q = collections.deque()
        q.append((root, root.val, [root.val]))
        res = []
        while q:
            for i in range(len(q)):
                node, curr, nums = q.popleft()
                if node:
                    if not node.left and not node.right and curr== targetSum:
                        res.append(nums)
                    if node.left:
                        q.append((node.left, curr+node.left.val, nums + [node.left.val]))
                    if node.right:
                        q.append((node.right, curr+node.right.val, nums + [node.right.val]))
        
        return res
