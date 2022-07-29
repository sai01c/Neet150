"""
https://leetcode.com/problems/invert-binary-tree/

Approach: each iteration we look at the head and invert its children

In general, they use recursive dfs or iterative bfs for tree. 

Tc: 
Sc: 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invert(self, root):
        if not root:
            return None

        temp = root.left
        root.left = self.invert(root.right)
        root.right = self.invert(temp)

        return root
