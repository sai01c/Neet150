"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

APPROACH: 
we know bst, node > left and node < right
we are given p and q, so for every node we check if node is greater than p and q. 
if val is lesser we need to move right
greater move to left

Tc: O(n)
Sc: O(1)

"""


def function(root, p, q):
    curr = root
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr
