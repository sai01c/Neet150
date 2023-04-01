"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Approach: we have done similar problem with inorder and preorder, this will follow the same pattern.
root will always be the last element from postorder we find the index of this element in inorder and 
continue to slice the array.

Tc: O(n)
Sc: O(n) recursion stack

"""

def buildTree(inorder, postorder):
    if not inorder or not postorder: return

    root = TreeNode(postorder[-1])
    index = inorder.index(postorder[-1])

    root.left = buildTree(inorder[:index], postorder[:index])
    root.right = buildTree(inorder[index+1:], postorder[index:len(postorder)-1])

    return root