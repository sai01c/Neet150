"""
https://leetcode.com/problems/min-cost-to-connect-all-points/

Approach - this is minimum spanning tree algorithm
Minimum spanning tree is finding minimum cost and make sure no cycle exists.
#[[0,0],[2,2],[3,10],[5,2],[7,0]]

tc - 
sc - 

"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                dic[i].append([dist, j])
                dic[j].append([dist, i])

        heap = []
        visit = set()
        res = 0
        heapq.heappush(heap, [0,0])
        while len(visit) < len(points):
            dist, node = heapq.heappop(heap)
            if node in visit:
                continue
            res += dist
            visit.add(node)
            for heapDist, nei in dic[node]:
                if nei not in visit:
                    heapq.heappush(heap, [heapDist, nei])
            
        return res