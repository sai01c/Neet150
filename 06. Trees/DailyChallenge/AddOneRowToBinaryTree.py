"""
https://leetcode.com/problems/add-one-row-to-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        q = collections.deque()
        q.append(root)
        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if level == depth - 1:
                        l = node.left
                        r = node.right
                        node.left = TreeNode(val, l, None)
                        node.right = TreeNode(val, None, r)
                        q.append(node.left)
                        q.append(node.right)
                    else:
                        if node.left: q.append(node.left)
                        if node.right: q.append(node.right)
        
        return root
