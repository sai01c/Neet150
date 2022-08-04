"""
https://leetcode.com/problems/k-closest-points-to-origin/

APPROACH: First, we find the distance of each cordinate point, 
then store in a heap. Interesting point is that we can create heap of arrays. 
and heap gets sorted based on the first index in each array. 
so we store [dist, x, y]
we use a loop to return the first k points. 

TC: 
Sc: O(n)

"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distxy = []
        for x, y in points:
            dist = sqrt((x**2) + (y**2))
            distxy.append([dist, x, y])
        print(distxy)

        heapq.heapify(distxy)
        res = []
        i = 0
        while i < k:
            dist, x, y = heapq.heappop(distxy)
            i += 1
            res.append([x, y])
        return res
