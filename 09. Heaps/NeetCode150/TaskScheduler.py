"""
https://leetcode.com/problems/task-scheduler/

Approach - first iterate over the input and create a frequency dic with letter and count. 
Now create a max with these counts.
Every iteration pop the max frequency from the heap. decrease the frequency by 1. 


"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        free = []
        for k, v in count.items():
            heapq.heappush(free, (-v, k))
        q = collections.deque()
        time = 0
        
        while free or q:
            if q and time == q[0][0]: #n is constant so using queue.
                t, f, c = q.popleft()
                heapq.heappush(free, (f, c))
            
            if free:
                fre, char = heapq.heappop(free)
                fre += 1
                if fre < 0:
                    q.append((time + n + 1, fre, char))
            
            time += 1
        return time