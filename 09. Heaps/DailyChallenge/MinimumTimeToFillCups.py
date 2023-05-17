"""
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

"""

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        heap = []
        for a in amount:
            if a == 0:
                continue
            heapq.heappush(heap, -a)

        while len(heap) > 1:
            maxi1 = -1 * heapq.heappop(heap)
            maxi2 = -1 * heapq.heappop(heap)
            
            maxi1 -= 1
            maxi2 -= 1
            
            if maxi1: heapq.heappush(heap, -1 * maxi1)
            if maxi2: heapq.heappush(heap, -1 * maxi2)
        
            ans += 1
        
        if not heap: return ans
        return ans + (-1 * heap[0])
        
        
            
            
            