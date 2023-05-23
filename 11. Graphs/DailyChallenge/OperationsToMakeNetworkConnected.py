"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

Approach - basically, we have to calculate number of connected componenets. And to make these connected 
you need number of connected components - 1. draw this on paper to understand

Tc - O(n) visit all nodes once.
sc - O(n) dic
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if connections < n-1: return -1 
        #for n node we must have n-1 edges if there are less than that 
        #it is not possible to make connected component so return -1
        
        dic = defaultdict(list)
        for s, e in connections:
            dic[s].append(e)
            dic[e].append(s)

        visit = set()
        res = 0

        def dfs(node):
            if node in visit: return
            visit.add(node)
            for conn in dic[node]:
                dfs(conn) 
            #we are not removing after visiting because we are finding connected components.

        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1

        return res-1 