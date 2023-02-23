"""
https://leetcode.com/problems/validate-binary-search-tree/

APPROACH- 
have a helper function, which takes in 3 paramenters - root, left value and right value
based on bst condition, node > left and node < right
now, check if the node.left and node.right is also true. 

Tc: O(n) traverse every node once
"""


def validate(root):
    return helper(root, float("-infinity", float("infinity")))


def helper(node, left, right):
    if not node:
        return True
    if not (node.val > left and node.val < right):
        return False
    return helper(node.left, left, node.val) and helper(node.right, node.val, right)
