"""
https://leetcode.com/problems/leaf-similar-trees/

"""
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = self.dfs(root1)
        leaf2 = self.dfs(root2)

        return leaf1 == leaf2
        
    def dfs(self, root):
        res = []
        if not root:
            return
        curr = root
        if not curr.left and not curr.right:
            res.append(curr.val)
        if curr.left:
            res.extend(self.dfs(curr.left))
        if curr.right:
            res.extend(self.dfs(curr.right))
        
        return res
        