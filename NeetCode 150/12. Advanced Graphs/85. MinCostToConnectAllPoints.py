"""
https://leetcode.com/problems/min-cost-to-connect-all-points/

Approach - this is minimum spanning tree algorithm
Minimum spanning tree is finding minimum cost and make sure no cycle exists.
#[[0,0],[2,2],[3,10],[5,2],[7,0]]

tc - 
sc - 

"""

def minCostConnectPoints(points):
    #think of this points as nodes and connect 1 node to all other nodes and add distance
    dic = defaultdict(list)
    
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i+1, len(points)):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            dic[i].append(dist, i)
            dic[j].append(dist, j)

    