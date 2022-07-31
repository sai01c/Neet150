"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

APPROACH: 
Have a helper function where you pass the nodea and the maxValue so far. 
if the node.val is greater than maxValue , we increase the output by 1
repeat for left and right nodes. 

O(n) traverse every node once
"""


def countGoodNodes(root):
    return helper(root, root.val)


def helper(node, val):
    output = 0
    if not node:
        return 0
    if node.val >= val:
        output += 1
        val = max(val, node.val)
    output += helper(node.left, val)
    output += helper(node.right, val)

    return output
