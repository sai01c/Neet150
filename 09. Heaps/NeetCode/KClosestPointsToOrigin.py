"""
https://leetcode.com/problems/k-closest-points-to-origin/

APPROACH: First, we find the distance of each cordinate point, 
then store in a heap. Interesting point is that we can create heap of arrays. 
and heap gets sorted based on the first index in each array. 
so we store [dist, x, y]
we use a loop to return the first k points. 

TC: nlogn
Sc: O(n)

"""

from ast import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points: #nlogn operation 
            dist = (x*x + y*y)
            heapq.heappush(heap, (dist, x, y)) #logn
        
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap) #logn
            res.append([x, y])
            k -= 1
            
        return res