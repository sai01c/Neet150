"""
https://leetcode.com/problems/longest-happy-string/

"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        reserve = []
        if a:
            heapq.heappush(heap, (-a, "a"))
        if b:
            heapq.heappush(heap, (-b, "b"))
        if c:
            heapq.heappush(heap, (-c, "c"))

        res = ""
        while heap:
            fre, char = heapq.heappop(heap)
            if len(res) >= 2 and char == res[-1] and char == res[-2]:
                reserve.append((fre, char))
                continue
            res += char
            fre += 1
            if fre < 0:
                heapq.heappush(heap, (fre, char))

            for f, c in reserve:
                if res[-1] != c:
                    reserve.remove((f, c))
                    heapq.heappush(heap, (f, c))
        
        return res