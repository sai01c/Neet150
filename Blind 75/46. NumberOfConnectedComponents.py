"""
https://leetcode.com/problems/number-of-provinces/

Approach - this question is like number of connected components. 
difficulty part of the question is how input is formatted

Basically, we do dfs and add nodes to visit set for all the connecting nodes. 
At the end we iterate and run dfs on nodes that are not in visit

Tc: 
Sc: 
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        res = 0
        def dfs(node):
            if node in visit:
                return 
            visit.add(node)
            for i in range(len(isConnected[node-1])): #this is tricy, write to undertand format
                if isConnected[node-1][i] == 1: #we have an edge for these nodes
                    dfs(i+1) 
        #from one node we get all the connected nodes to the set.     
        for node in range(1, len(isConnected) + 1):
            if node not in visit: #nodes not in visit means not connected
                dfs(node)
                res += 1
                
        return res
            
        