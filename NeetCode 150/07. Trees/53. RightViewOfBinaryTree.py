"""
Explanation: First, we create a queue and add all the elements to it.
Now we iterate through the queue. And pop one item each iteration.
Now, we add the val to the level array and add left and right values back to the queue.
Each iteration we set the level to empty array.
We will have a result array and then add the level array.

Tc: O(n) traverse all the nodes at once. 
Sc: O(n) queue 

for left view - we should first do level order traversal 
then, for each iteration take the first element 
"""

import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        result = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if node and i == 0:
                    result.append(node.val)

        return result


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        result = []

        while q:
            right = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right = node
            if right:
                result.append(right.val)

        return result


"""
for right view- do level order traversal 
and then after every iteration take the last node and add it to the result
"""
