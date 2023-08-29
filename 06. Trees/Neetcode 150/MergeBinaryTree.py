"""
https://leetcode.com/problems/merge-two-binary-trees/

"""

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        dic = {}
        def helper(root):
            if not root: return
            q = collections.deque()
            q.append((root, 1))
            if 1 in dic:
                dic[1] += root.val
            else:
                dic[1] = root.val
            while q:
                for i in range(len(q)):
                    node, ind = q.popleft()
                    if node:
                        if node.left:
                            if 2*ind in dic:
                                dic[2*ind] += node.left.val
                            else:
                                dic[2*ind] = node.left.val
                            q.append((node.left, 2 * ind))
                        if node.right:
                            if 2*ind + 1 in dic:
                                dic[2*ind + 1] += node.right.val
                            else:
                                dic[2*ind + 1] = node.right.val
                            q.append((node.right, 2*ind+1))
        helper(root1)
        helper(root2)
        q = collections.deque()
        root = TreeNode(dic[1])
        q.append((root, 1))
        while q:
            for i in range(len(q)):
                node, ind = q.popleft()
                if node:
                    if 2*ind in dic:
                        node.left = TreeNode(dic[2*ind])
                        q.append((node.left, 2*ind))
                    if 2*ind+1 in dic:
                        node.right = TreeNode(dic[2*ind+1])
                        q.append((node.right, 2*ind+1))
        return root