"""
https://leetcode.com/problems/search-in-a-binary-search-tree/

Approach - we use BST property to move b/w left and right. Else if the values are 
equal then we found our node return this entire node

tc
sc


"""

def func(root, val):
    if not root:
        return None

    curr = root
    while curr:
        if val < curr.val:
            curr = curr.left

        elif val > curr.val:
            curr = curr.right

        else:
            return curr
        
    return None #if we haven't found anything