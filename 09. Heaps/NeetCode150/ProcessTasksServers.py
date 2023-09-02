"""
https://leetcode.com/problems/process-tasks-using-servers/

using two heaps because in the waiting as well we want to get the min server. 
and, there can be two servers getting ready at the same time.

"""

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = []
        waiting = []
        for i in range(len(servers)):
            heapq.heappush(available, (servers[i], i))
        time = 0
        res = []
        
        for i in range(len(tasks)):
            while (waiting and waiting[0][0] == time):
                t, s, ind = heapq.heappop(waiting)
                heapq.heappush(available, (s, ind))
            
            if available:    
                availS, availI = heapq.heappop(available)
                res.append(availI)
                heapq.heappush(waiting, (time + tasks[i], availS, availI))
            else:
                t, s, ind = heapq.heappop(waiting)
                res.append(ind)
                heapq.heappush(waiting, (t+tasks[i], s, ind))
            time += 1
        return res