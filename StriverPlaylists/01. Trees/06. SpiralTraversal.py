"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Approach: 
this is similar to level order traversal
but, here they are in opposite direction each time
use the same technique from level order but modify 

Tc: O(n) traverse all nodes. 

"""

import collections


def level(root):
    res = []
    if not root:
        return res

    q = collections.deque()
    q.append(root)
    flag = True  # left to right
    while q:
        for i in range(len(q)):
            level = []
            node = q.popleft()
            if node:
                level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if flag:
            res.append(level)
            flag = False

        else:
            res.append(level[::-1])
            flag = True

    return res
