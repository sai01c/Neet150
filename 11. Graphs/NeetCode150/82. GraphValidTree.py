"""
https://www.lintcode.com/problem/178/

Approach - Basically, the graph has to be connected and acyclic to be a tree. 
cyclic - we can run dfs and use parent to eliminate edge case of undirected graph.
for connected components, length of set should be equal to number of nodes. that means graph is connected.
"""

from collections import defaultdict


def graphValidTree(n, edges):
    dic = defaultdict(list)
    for k, v in edges:
        dic[k].append(v)
        dic[v].append(k)

    print(dic)
    visit = set()
    def dfs(node, parent):
        if node in visit:
            return False
        visit.add(node)
        for val in dic[node]:
            if val == parent:
                continue
            if not dfs(val, node):
                return False
        
        return True
    
    return dfs(0, -1) and len(visit) == n
    
    
print(graphValidTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(graphValidTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))