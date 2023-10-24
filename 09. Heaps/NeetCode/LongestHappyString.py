"""
https://leetcode.com/problems/longest-happy-string/

"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heapq.heappush(heap, (-a, 'a'))
        if b:
            heapq.heappush(heap, (-b, 'b'))
        if c:
            heapq.heappush(heap, (-c, 'c'))
        res = ""
        prev, prev2 = -1, -1
        resting = []
        while heap or resting:
            while resting and (prev != resting[0][1] or prev2 != resting[0][1]):
                rf, rc = heapq.heappop(resting)
                heapq.heappush(heap, (rf, rc))
            
            if not heap: break
            fre, char = heapq.heappop(heap)
            if char == prev and char == prev2:
                heapq.heappush(resting, (fre, char))
            else:
                res += char
                fre += 1
                if fre < 0:
                    heapq.heappush(heap, (fre, char))
                prev2 = prev
                prev = char

        return res
                
            
        
            