"""
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

"""

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return
            if root.val == target.val:
                return root
            l = dfs(root.left) 
            r = dfs(root.right)
            if l:
                return l
            if r:
                return r
            
            return None
            
        return dfs(cloned)
                    
                