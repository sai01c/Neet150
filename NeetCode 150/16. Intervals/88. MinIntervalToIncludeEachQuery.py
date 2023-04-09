"""
https://leetcode.com/problems/minimum-interval-to-include-each-query/

Optimal Approach:

Tc: O(nlogn + qlogq)
sc - 
"""

import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        dic = {}
        heap = []
        intervals.sort() #sort the intervals
        i = 0 #notice i is outside for loop
        for q in sorted(queries): #sorting the queries 
            if q in dic: #this value is already computed so continue
                continue 
            
            #instead of iterating through all intervals select only ones where q >= start
            #both intervals and queries are sorted so this will work
            while (i < len(intervals) and q >= intervals[i][0]):
                s, e = intervals[i]
                size = e - s + 1
                heapq.heappush(heap, (size, e)) #append all of them into heap
                i += 1 
                #for next query we don't want to start from i = 0
                
            while heap and q > heap[0][1]: #remove the ones which doesn't satisfy q <= end
                heapq.heappop(heap)
                
            if heap: #add to dic so that we can use later
                dic[q] = heap[0][0]  #this is the minimum size
            else:
                dic[q] = -1 
            
        for q in queries:
            res.append(dic[q])
            
        return res