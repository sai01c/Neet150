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
    #do generic traversal and each iteration compare node.val with p and q.
    curr = root 
    while curr:
        #p and q are greater than node so shift right
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        #p and q less than node so shift left
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        #we can't shift left and right. this node is the output
        else:
            return curr
