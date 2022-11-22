"""
https://leetcode.com/problems/k-closest-points-to-origin/

APPROACH: First, we find the distance of each cordinate point, 
then store in a heap. Interesting point is that we can create heap of arrays. 
and heap gets sorted based on the first index in each array. 
so we store [dist, x, y]
we use a loop to return the first k points. 

TC: k logn if using heap. Regular sorting, n logn
Sc: O(n)

"""


from ast import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x**2 + y**2 
            heapq.heappush(heap, [dist, [x,y]])
        res = []   
        for i in range(k): #doing k times
            d, point = heapq.heappop(heap) #logn
            res.append(point)
        return res