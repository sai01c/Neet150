"""
https://leetcode.com/problems/same-tree/

Approach: 
identify the base cases - if p,q both none that means they are equal
if one of them is none they are not equal
if val is not equal they are not equal
if val is equal then left and right must be equal 

Tc: O(n) as you are travesing every node. 
Sc: O(n) recursion stack

"""

def sameBinaryTree(p, q):
    if not p and not q: #
    #AND condition should be checked first as OR condition can also satisfy and condition
        return True
    if not p or not q: 
        return False  
    if p.val != q.val: #that means values are not equal
        return False

    #now check recursively for children
    return (sameBinaryTree(p.left, q.left) and sameBinaryTree(p.right, q.right))
