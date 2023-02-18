"""
https://leetcode.com/problems/invert-binary-tree/

Approach: we reverse left and right using temp pointer technique just as in arrays
now after reversing left and right, we also need to reverse their child so we apply
recurive function now

Tc: since we are visiting all nodes once it is O(n)
Sc: recursive stack is used here so it is height of binary tree which is O(n) in worst case
"""

def inverTree(root):
    if not root:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp

    inverTree(root.left)
    inverTree(root.right)

    return root