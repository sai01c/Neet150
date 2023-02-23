"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Approach: 
first element in the preorder will always be the root 
find the index of this root in the inorder. Now this will be mid. 
the left elements and right elements can be formed using this mid index

Tc: O(n) traverse every node once
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructTree(preorder, inorder):
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = constructTree(preorder[1:mid+1], inorder[:mid])
    root.right = constructTree(preorder[mid+1:], inorder[mid+1:])

    return root
