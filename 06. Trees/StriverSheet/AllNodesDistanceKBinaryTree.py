"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

TODO
"""

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def helper(node):
            if not node:
                return
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        dic = adj
        visit = set()
        
        def dfs(node, curr):
            res = []
            if node in visit:
                return []
            if node not in dic:
                return []
            visit.add(node)
            if curr == k:
                res.append(node)
            for conn in dic[node]:
                res += (dfs(conn, curr+1))
            return res
        return dfs(target.val, 0)

                
