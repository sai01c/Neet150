"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((root, root.val, root.val))
        ans = float('-inf')
        while q:
            for i in range(len(q)):
                node, maxi, mini = q.popleft()
                if node:
                    ans = max(ans, abs(maxi - node.val), abs(mini-node.val))
                    maxi = max(maxi, node.val)
                    mini = min(mini, node.val)
                    if node.left:
                        q.append((node.left, maxi, mini))
                    if node.right:
                        q.append((node.right, maxi, mini))
        
        return ans