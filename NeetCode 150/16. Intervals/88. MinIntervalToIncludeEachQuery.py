"""
https://leetcode.com/problems/minimum-interval-to-include-each-query/

Brute force approach:  32/42 test cases

we use two for loops - for every query we scan through all the intervals 
then check if the range is satisfied and then add it to the minHeap
after all the intervals are completed we retreive the first value (minimum)
repeat the same process for all the queries. 

TC: O(n*n)
Sc: O(n)

Optimal Approach:

Tc: O(nlogn)
I will never be able to do this
"""


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            heap = []
            for x, y in intervals:
                if (q >= x and q <= y):
                    heapq.heappush(heap, y-x+1)
            if heap:
                mini = heapq.heappop(heap)
                res.append(mini)
            else:
                res.append(-1)
            
        return res

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
