"""
https://leetcode.com/problems/find-eventual-safe-states/

approach - terminal nodes means they have outgoing edges for safe state every node
should end up with terminal nodes. 
so that means there should not be any cycle.
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cycle = set()
        visit = set()
        res =[]
        def dfs(node):
            if node in visit:
                return True
            if node in cycle:
                return False
            cycle.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res