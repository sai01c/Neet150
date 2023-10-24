"""
https://leetcode.com/problems/last-stone-weight/

APPROACH: As it is a maximum problem, idea is to use heap. 
using heap we can get the first largest and second largest elements. 
if the first and second are different, push the difference to the heap
continue this process as long as the heap has more than 1 element

TC: O(n(logn))
Sc: O(n) heap
"""

import heapq

def lastStone(stones):
    heap = []
    for s in stones:
        heapq.heappush(heap, -1 * s) #min-heap

    while len(stones) > 1: 
        #pop two greatest elements
        y = -1 * heapq.heappop(stones) #O(logn)
        x = -1 * heapq.heappop(stones)
        
        if x != y:
            heapq.heappush(stones, -1 * (y-x)) #O(logn)
    
    if heap:   
        return (-1 * heap[0])
    else: 
        return 0

