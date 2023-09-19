"""
https://leetcode.com/problems/evaluate-division/

"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(list)
        for i in range(len(equations)):
            s, t = equations[i]
            val = values[i]
            dic[s].append((t, val))
            dic[t].append((s, 1/val))

        def bfs(s, t):
            if s not in dic or t not in dic: return -1
            q = collections.deque()
            visit = set()
            q.append((s, 1))
            visit.add(s)
            while q:
                node, currVal = q.popleft()
                if node == t:
                    return currVal
                for nei, neiVal in dic[node]:
                    if nei not in visit:
                        q.append((nei, currVal * neiVal))
                        visit.add(nei)
            return -1
        
        res = []
        for s, t in queries:
            res.append(bfs(s, t))
        return res