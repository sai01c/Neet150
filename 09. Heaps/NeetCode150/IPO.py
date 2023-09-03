"""
https://leetcode.com/problems/ipo/submissions/

Optimal Approach: have two heaps - one min heap for capital other max heap for profits
while iterating over the min heap check if our current profit is more than minHeap values. 
Add all those values which satisfy this condition. Now, out of all the profits available select 
maximum profit. 

Tc: k log(n)
Sc: O(n)

TODO
"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCap = []
        maxProfit = []
        for p, c in zip(profits, capital):
            heapq.heappush(minCap, (c, p))
        
        for i in range(k):
            while minCap and w >= minCap[0][0]:
                c, p = heapq.heappop(minCap)
                heapq.heappush(maxProfit, -1 * p)

            if maxProfit:
                p = -1 * heapq.heappop(maxProfit)
                w += p
            
        return w