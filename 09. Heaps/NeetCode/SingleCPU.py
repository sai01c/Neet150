"""
https://leetcode.com/problems/single-threaded-cpu/

"""

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        startTime, processTime = [], []
        for i in range(len(tasks)):
            s, p = tasks[i]
            heapq.heappush(startTime, (s, p, i))
        res = []
        currTime = 1
        while startTime or processTime:
            while startTime and currTime >= startTime[0][0]:
                s, p, ind = heapq.heappop(startTime)
                heapq.heappush(processTime, (p, ind))
            
            if processTime:
                p, ind = heapq.heappop(processTime)
                res.append(ind)
                currTime += p
            else:
                currTime = startTime[0][0]
        return res