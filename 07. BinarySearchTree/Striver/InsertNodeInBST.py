"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Approach - use BST property to iterate over the nodes

Tc
Sc

"""

def func(root, val):
    if not root:
        return TreeNode(val)
    
    curr = root
    while curr:
        if val < curr.val:
            #val should be in this subtree but we don't have curr.left so create a 
            #node here and attach it 
            if not curr.left: 
                curr.left = TreeNode(val)
                return root
            curr = curr.left
        else:
            #val should be in this right subtree but we don't have right subtree so
            #create a right subtree and attach it.
            if not curr.right:
                curr.right = TreeNode(val)
                return root
            curr = curr.right

    