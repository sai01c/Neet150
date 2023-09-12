"""
https://leetcode.com/problems/is-graph-bipartite/

approach - divide the nodes into two sets.
if the edge b/w two vertices are in same set then it is false

"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        even = set()
        odd = set()
        
        def bfs(node):
            if node in odd: return True #why adding this condition
            #this is bit tricky write down on paper to understand
            q.append((node, even))
            even.add(node)
            
            while q:
                node, sett = q.popleft()
                for nei in graph[node]:
                    if nei in sett: return False
                    if sett == even:
                        if nei not in odd:
                            q.append((nei, odd))
                            odd.add(nei)
                    elif sett == odd:
                        if nei not in even:
                            q.append((nei, even))
                            even.add(nei)
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True