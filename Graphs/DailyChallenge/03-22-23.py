"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

Approach: it is connected graph. we need to traverse all edges and find the minimum edge. 
we need to find the min edge from 1 to n. 
although if our min edge is not in the path from 1 to n. we can go to the min edge path and comeback to n
we can go from 1 to 2 and come back from 2 to 1.
Basically, find the min edge among all the connected nodes.

tc - O(v + e)
sc - o(n)

"""

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        q = collections.deque()
        dic = defaultdict(list)
        for s, e, l in roads:
            dic[s].append((e, l))
            dic[e].append((s, l))

        visit = set()
        res = float('inf')
        q.append((1, res))
        while q:
            node, length = q.popleft()
            visit.add(node) # we want to add to visit here after visiting all edges from this node
            #this way we can traverse all edges. 
            #this is slight modification from generic bfs 
            #generic we visit all nodes only once but here we may have to visit more than once.
            res = min(res, length)
            for conn, connLen in dic[node]:
                if conn not in visit:
                    q.append((conn, min(connLen, length))) #we are not adding conn to visit here

        return res



