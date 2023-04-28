"""
https://leetcode.com/problems/redundant-connection/

Approach - this is my own algorithm. 
we maintain a dic and set. we iterate through the edges and keep adding them to the dic. 
Now, if we find a cycle, we append this to our res and remove these edges. 

Tc - 
Sc - 
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        res = []
        
        for s, e in edges:
            dic[s].append(e) #undirected graph - so always add both s->e and e->s
            dic[e].append(s)
            #initite new set because we want to check for cycle fresh after appending this edge to dic
            cycle = set() 
            
            if self.dfs(s, e, dic, cycle) == False and [e, s] in edges: 
                #if cycle exists and this edge in our input
                res.append([e, s])
                #we want to remove this edge from dic because even though if next edges 
                #don't form a cycle - they will result in cycle because of this edge
                dic[s].remove(e) 
                dic[e].remove(s)
            
            if self.dfs(e, s, dic, cycle) == False and [s, e] in edges: 
                res.append([s, e])
                dic[s].remove(e)
                dic[e].remove(s)
        
        return res[-1] #we need the last corrupted edge
    
    #regular cycle check dfs - refer to course prerequisites problem
    def dfs(self, node, parent, dic, cycle):
        if node in cycle: return False
        if node not in dic or dic[node] == []: return True
        
        cycle.add(node)
        for nei in dic[node]:
            if nei == parent: continue #undirected graph
            if not self.dfs(nei, node, dic, cycle): return False
        
        cycle.remove(node)
        #dic[node] = [] #not sure why this is throwing error
        return True
            
        
        