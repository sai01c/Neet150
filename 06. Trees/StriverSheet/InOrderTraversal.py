"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

Approach - this is a bit tricky. first you assign a curr node and move to its left as much as you can
now, pop from the stack and move the curr to right

tc - n
sc - n
"""

def postOrder(root):
    stack = []
    curr = root
    res = []
    while stack or curr:
        
        while curr:
            curr = root.left
            stack.append(curr)
        
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right

    return res