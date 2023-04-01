
"""
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

Approach: find binary tree level order sum using level order traversal

Tc: O(n)
Sc: O(n) queue
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root, k):
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            level = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level += node.val
                    q.append(node.left)
                    q.append(node.right)
            if level:
                heapq.heappush(res, -1 * level)
        
        if len(res) < k: return -1
        for i in range(k):
            val = -1 * heapq.heappop(res)
        return val
