"""
https://leetcode.com/problems/same-tree/

Approach: 
identify the base cases - if p,q both none that means they are equal
if one of them is none they are not equal
if val is not equal they are not equal
if val is equal then left and right must be equal 

Tc: O(n) as you are travesing every node. 
Sc: TODO

"""


def sameBinaryTree(p, q):
    if not p and not q: #and condition should be checked first as 
        #or condition can also satisfy and condition
        return True
    if not p or not q: # 
        return False  
    if p.val != q.val:
        return False

    return (sameBinaryTree(p.left, q.left) and sameBinaryTree(p.right, q.right))
