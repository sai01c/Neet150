"""
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

"""

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append((root, -1, -1))
        res = 0
        while q:
            for i in range(len(q)):
                node, p, gp = q.popleft()
                if node:
                    if gp % 2 == 0:
                        res += node.val
                    q.append((node.left, node.val, p))
                    q.append((node.right, node.val, p))
        return res
        