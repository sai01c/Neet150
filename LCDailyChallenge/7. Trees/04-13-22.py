"""
https://leetcode.com/problems/search-in-a-binary-search-tree/

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Binary search tree means left is less than head and right is more than head
For any tree question, we'll have base case and recursive steps.
we check is the head is val and if there is no root
repeat the same for left and right
"""

#this is incomplete
# solution is correct but not executing tree in VS Code


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)

    print(searchBST([4, 2, 7, 1, 3], 2))
