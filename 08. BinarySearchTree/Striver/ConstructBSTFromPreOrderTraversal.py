"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Approach - this pattern of questions we have done with regular binary tree where we were given
two travesal. But, here only 1 traversal is given. We will use the BST property here
first val of array will always be the root
now among the array find first element which is greater than first val, this 
will be the index now.
continue the same steps

tc
sc
"""

def func(preorder):
    if not preorder:
        return 
    node = TreeNode(preorder[0])
    ind = len(preorder) #we are giving length because if there doesn't exist any value
    #which is greater than node that means we don't have any right subtree
    #eg = [4,2]

    for i in range(len(preorder)):
        if preorder[i] > node.val:
            ind = i
            break
    
    node.left = func(preorder[1:ind])
    node.right = func(preorder[ind:])

    return node