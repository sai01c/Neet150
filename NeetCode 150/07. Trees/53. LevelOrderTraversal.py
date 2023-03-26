"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Explanation: First, we create a queue and add all the elements to it.
Now we iterate through the queue. And pop one item each iteration.
Now, we add the val to the level array and add left and right values back to the queue.
Each iteration we set the level to empty array.
We will have a result array and then add the level array.

Tc: O(n) traverse all the nodes at once. 
Sc: O(n) queue 
"""

import collections


def levelOrder(root):
    q = collections.deque()
    q.append(root)
    result = []

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            result.append(level)
    return result
