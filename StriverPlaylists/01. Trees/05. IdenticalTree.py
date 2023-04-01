"""

Approach: traverse every node and check if p and q are equal
identify the base cases - if p,q both none that means they are equal
if one of them is none they are not equal
if val is not equal they are not equal
if val is equal then left and right must be equal 
Tc: O(n) as you are travesing every node. 

you can also use level order traversal for each tree and compare. 
or any other traversal technique. 
"""


def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return (sameTree(p.left, q.left) and sameTree(p.right, q.right))
