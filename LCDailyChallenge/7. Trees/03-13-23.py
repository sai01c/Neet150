"""
https://leetcode.com/problems/symmetric-tree/

Approach: this is similar to sametree, subtree problem. but here we are comparing opposite children.
Tc: O(n) for visiting every node once
Sc: O(n) recursion call stack

"""

def symmetricTree(root):

    def helper(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and helper(left.left, right.right) and 
        (left.right, right.left))
    
    return helper(root.left, root.right)
