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
            
            if self.dfs(s, e, dic, cycle) == False and [s, e] in edges: 
                #if cycle exists and this edge in our input
                #we want to remove this edge from dic because even though if next edges 
                #don't form a cycle - they will result in cycle because of this edge
                res.append([s, e])
                dic[s].remove(e)
                dic[e].remove(s)
                
            
            if self.dfs(e, s, dic, cycle) == False and [e, s] in edges: 
                res.append([e, s])
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
            
        
"""
union find algorithm - not sure why this one works 

TODO

"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * (len(edges) + 1)
        for n in range(1, len(edges)+1):
            parent[n] = n
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
            
        for s, e in edges:
            if union(s, e) == False:
                return [s,e]