"""
https://leetcode.com/problems/reorganize-string/

Approach - create a dict of the frequencies
then use a heap to get the max two freq append these two continue this until we have 
only 1 char in heap
now if the fre of thi char is more than 1 then we don't return anything
else append it to res

tc
sc
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        reserve = []
        res = ""
        prev = -1
        for k, v in count.items():
            heapq.heappush(heap, (-v, k))
        while heap or reserve:
            while reserve and prev != reserve[0][1]:
                rf, rc = heapq.heappop(reserve)
                heapq.heappush(heap, (rf, rc))
            
            if not heap: return ""    
            fre, char = heapq.heappop(heap)
            if char == prev:
                heapq.heappush(reserve, (fre, char))
            else:
                res += char
                prev = char
                fre += 1
                if fre < 0:
                    heapq.heappush(heap, (fre, char))
        return res
            
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = Counter(s)
        heap = []
        res = ""
        for k, v in dic.items():
            heap.append([-v, k])
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            v1, k1 = heapq.heappop(heap)
            res += k1
            v1 += 1
            
            v2, k2 = heapq.heappop(heap)
            v2 += 1
            res += k2
            
            if v1:
                heapq.heappush(heap, [v1, k1])
            if v2:
                heapq.heappush(heap, [v2, k2])
            
        if heap:
            v, k = heapq.heappop(heap)
            if v < -1: return ""
            res += k
        
        return res
            

         