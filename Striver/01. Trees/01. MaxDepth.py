"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Approach: we are going to use recurssion
if the node is Null, then obviously height is going to be zero
then apply same function left, right nodes
height is the maximum of the left and right. 

Tc: we will be visiting all the nodes so O(n)
Sc: since recurssion auxillary space will be O(n) if the tree is skewed

we can also use level order traversal to find the height/depth. This will also be 
Tc O(n) traverse every node 
Sc O(n) queue
"""


import collections


def depth(root):
    if root == None:
        # we are checking for height, so we return 0 if there's no node.
        return 0
    l = depth(root.left)
    r = depth(root.right)
    return (1 + max(l, r))


class Solution:
    def maxDepth(self, root) -> int:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            levels = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levels:
                res.append(levels)
        return len(res)
