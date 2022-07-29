"""
https://leetcode.com/problems/diameter-of-binary-tree/

Approach: 
find the height of a node. 
diameter will be the left height + right height

practice tree problems on paper. 

Tc: O(n) no idea why
Sc: 
"""


def diameter(root):
    ans = 0
    height(root)
    return ans


def height(root):
    if root == None:
        return 0

    l = height(root.left)
    r = height(root.right)
    ans = max(ans, l + r)
    return 1 + max(l, r)
