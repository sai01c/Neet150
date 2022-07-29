"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Depth = depth is the maximum from root to nodes. Count nodes from root to leaf. 
Root should be depth 0. 

you can calculate height also using same code

Tc: 
Sc: 

"""


def depth(root):
    if root == None:
        return 0
    l = depth(root.left)
    r = depth(root.right)
    return (1 + max(l, r))


print(depth([3, 9, 20, None, None, 15, 7]))
