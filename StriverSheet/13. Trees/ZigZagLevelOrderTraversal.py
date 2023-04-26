"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Approach - do usual level order traversal but append level in reverse direction by having a boolean

tc
sc

"""

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return res

        q = collections.deque()
        q.append(root)
        flag = True  # left to right
        while q:
            level = []
            for i in range(len(q)):
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

        