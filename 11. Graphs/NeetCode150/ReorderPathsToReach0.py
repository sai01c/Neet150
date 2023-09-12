"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

Approach - Think of it as undirected graph. if there is an edge from 0 -> 1 and 4 -> 0. 
Now, for 0 we go to both 1 and 4 as an undirected graph does. But, now we check if we have the edge to 0
if not we increase the count by 1. Now we check for 1. 
if all the edges are directing to 1 then they also direct to 0 because 1 is directing to 0
if you draw on paper intutuion is clearly BFS

tc - O(n)
sc - O(n)
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dic = defaultdict(list)
        edges = set()
        for s, e in connections:
            dic[s].append(e)
            dic[e].append(s)
            edges.append((s, e))
        visit = set()
        q = collections.deque()
        q.append(0)
        visit.add(0)
        res = 0
        while q:
            node = q.popleft()
            for conn in dic[node]:
                if conn not in visit:
                    q.append(conn)
                    visit.add(node)
                    if (conn, node) not in edges:
                        res += 1
        return res