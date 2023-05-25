"""
https://www.lintcode.com/problem/178/
https://leetcode.com/problems/graph-valid-tree/submissions/

Approach - Basically, the graph has to be connected and acyclic to be a tree. 
cyclic - we can run dfs and use parent to eliminate edge case of undirected graph.
for connected components, length of set should be equal to number of nodes. that means graph is connected.
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1: return False
        if not edges: return True
        
        dic = defaultdict(list)
        cycle = set()
        for s, e in edges:
            dic[s].append(e)
            dic[e].append(s)
            
        def dfs(node, parent):
            if node not in dic or dic[node] == []:
                return True
            if node in cycle:
                return False
            cycle.add(node)
            for nei in dic[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(cycle) == n
        